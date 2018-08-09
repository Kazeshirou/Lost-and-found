import os, pickle
import VKTool
from PyQt5.QtWidgets import QTableWidgetItem
import PyQt5
from datetime import datetime

class Found():
    def __init__(self, **kwargs):
        self.found_id = []
        self.loss_id = None




class Engine(object):
    def __init__(self, ui_loss_table, ui_found_table):
        self.table = []
        self.raw_data = []

        self.ui_loss_table = ui_loss_table
        self.ui_found_table = ui_found_table

    def readfile(self, filename = "output.txt"):
        loss = []
        found =[]
        with open(filename,'r') as f:
            for line in f:
                l = line.split()
                loss.append(int(l[0]))
                found.append(int(l[1]))
        self.process_ids(loss,found)
        self.load_pickles(self.table)
        self.create_table()

    def process_ids(self,loss,found):
        L = set()
        result = []
        for i in range(len(loss)):
            if loss[i] not in L:
                L.add(loss[i]) 
                Obj = Found()
                Obj.loss_id = loss[i]
                Obj.found_id.append(found[i])
                result.append(Obj)
            else:
                for j in range(len(result)):
                    if loss[i] == result[j].loss_id:
                        result[j].found_id.append(found[i])
                        break
        self.table = result

    def load_pickles(self, ids_table):
        raw_data = []
        for filename in os.listdir(os.path.dirname(__file__) + "/pickles/"):
            data = []
            with open("pickles/" + filename, 'rb') as f:
                data = pickle.load(f)
            raw_data += data
    
        self.raw_data = raw_data


    def __get_pickle(self, id):
        for x in self.raw_data:
            if id == x.local_id:
                return x

    def create_table(self):
        for i in range(len(self.table)):
            self.table[i].loss_id = self.__get_pickle(self.table[i].loss_id)
            for j in range(len(self.table[i].found_id)):
                self.table[i].found_id[j] = self.__get_pickle(self.table[i].found_id[j])
        f = 9

    def update_loss_table(self):
        self.ui_loss_table.setRowCount(0)
        N = len(self.table)
        self.ui_loss_table.setRowCount(N)
        i = 0
        for tr in self.table:
            pet = tr.loss_id

            id = QTableWidgetItem(str(pet.local_id))
            text = QTableWidgetItem(str(pet.text))

            data =  datetime.fromtimestamp(pet.unixtime).strftime('%Y-%m-%d %H:%M:%S')
            data = QTableWidgetItem(str(data))
            link = QTableWidgetItem(str(None))

            self.ui_loss_table.setItem(i,0,id)
            self.ui_loss_table.setItem(i,1,text)
            self.ui_loss_table.setItem(i,2,data)
            #self.ui_loss_table.setItem(i,3,link)



            self.ui_loss_table.item(i,0).setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)
            self.ui_loss_table.item(i,1).setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)
            self.ui_loss_table.item(i,2).setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)
            #self.ui_loss_table.item(i,3).setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)


            self.ui_loss_table.setRowHeight(i,150)
            i += 1

    def update_found_table(self):
        index = self.ui_loss_table.currentIndex().row()

        self.ui_found_table.setRowCount(0)
        N = len(self.table[index].found_id)
        self.ui_found_table.setRowCount(N)
        i = 0
        for tr in self.table[index].found_id:
            pet = tr

            id = QTableWidgetItem(str(pet.local_id))
            text = QTableWidgetItem(str(pet.text))

            data =  datetime.fromtimestamp(pet.unixtime).strftime('%Y-%m-%d %H:%M:%S')
            data = QTableWidgetItem(str(data))
            link = QTableWidgetItem(str(None))


            #text.sizeHint(PyQt5.QtCore.QSize(200,200))

            self.ui_found_table.setItem(i,0,id)
            self.ui_found_table.setItem(i,1,text)
            self.ui_found_table.setItem(i,2,data)
            #self.ui_found_table.setItem(i,3,link)

            self.ui_found_table.item(i,0).setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)
            self.ui_found_table.item(i,1).setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)
            self.ui_found_table.item(i,2).setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)
            #self.ui_found_table.item(i,3).setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)

            self.ui_found_table.setRowHeight(i,150)
            i += 1



    def button_update_clicked(self):
        self.readfile()
        self.update_loss_table()


if __name__ == "__main__":
    A = Engine()
    a = A.readfile("123.txt")
    g = 9