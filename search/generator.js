const fs = require('fs');

function random(low, high) {
	return Math.random() * (high - low) + low;
}

function randomInt (low, high) {
	return Math.floor(random(low, high));
}

function generateword(len){
	var az = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя';
	var s = '';
	for (var i = len - 1; i >= 0; i--) {
		s += az[randomInt(0,az.length)];
	}
	return s;
}

function generateps() {
	var pss =  ['существительное', 'глагол'];
	return pss[randomInt(0, pss.length)];
}


function generateknowlage(len) {
	fs.writeFile('./morphdb.pl','', (error) => {
				if(error) throw error;
			}
		);

	for (var i = len - 1; i >= 0; i--) {
		fs.appendFile('./morphdb.pl',
			'слово'+'(' + generateword(10) + ', глагол, признак, признак, признак, признак, признак, признак, признак, признак).\n',
			(error) => {
                if(error) throw error;
            }
        );
	}
}

generateknowlage(5900000);