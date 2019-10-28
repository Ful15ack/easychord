'''
Created on 27 jul. 2019

@author: sebas
'''
import os
import sys #@UnusedImport
from EasyChord_1_1 import * #@UnresolvedImport @UnusedWildImport
from PyQt5.QtWidgets import * #@UnusedWildImport
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtCore import QFileInfo
from transportarNotas import * #@UnusedWildImport #@UnresolvedImport
from PyQt5.QtGui import QTextCursor
from directorio import Ui_Directorio
from PyQt5.QtWidgets import QFileSystemModel

class miFormulario(QMainWindow,QDialog):
    path=''
    enPlay2={}
    enDirectorio=[]
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.btnNuevaCancion.clicked.connect(self.nuevaCancion)
        self.ui.btnAgregarSet.clicked.connect(self.agregar_a_play)
        self.ui.listaCanciones.doubleClicked.connect(self.agregar_a_play)
        self.ui.btnQuitarSet.clicked.connect(self.borrarItemListaPlay)
        self.ui.btnPlay.clicked.connect(self.abrirCancion)
        self.ui.listaPlay.doubleClicked.connect(self.abrirCancion)
        self.ui.btnGuardarCancion.clicked.connect(self.guardarCambios)
        self.ui.btnSubir.clicked.connect(self.transportarArriba)
        self.ui.btnBajar.clicked.connect(self.transportarAbajo)
        self.ui.btnExportarPDF.clicked.connect(self.exportarPDF)
        self.ui.btnGuardarSet.clicked.connect(self.guardarSet)
        self.ui.btnCargarSet.clicked.connect(self.cargarLista)
        self.ui.btnAbrirDirectorio.clicked.connect(self.abrirBrwserCarpetas)
        self.ui.btnAbrirCancion.clicked.connect(self.abrirUnaCancion)
        
    def abrirBrwserCarpetas(self):
        self.ventana=QtWidgets.QDialog()
        self.ui2=Ui_Directorio()
        self.ui2.setupUi(self.ventana)
        self.ventana.show()
        
        homedir = os.path.expanduser("~")
        
        self.model = QFileSystemModel()
        self.model.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Dirs | QtCore.QDir.NoSymLinks)
        self.model.setRootPath(QtCore.QDir.rootPath())
        self.tree = self.ui2.vistaDirectorio
        self.tree.setModel(self.model)  
        self.tree.setRootIndex(self.model.index(homedir))
        
        self.ui2.btnAbrirCarpeta.clicked.connect(self.rutaCarpeta)
        self.ui2.btnCancelarBrowser.clicked.connect(self.cerrarBrowser)
        
    def rutaCarpeta(self):
        index=self.ui2.vistaDirectorio.currentIndex()
        self.path=self.model.filePath(index)
        self.abrirDirectorio()
    
    def cerrarBrowser(self):
        self.ventana.close()    
                
    def closeEvent(self, event):        
        respuesta = QMessageBox.question(self, 'Cerra Aplicación',
            "Está seguro que quiere cerrar la aplicación", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    def abrirDirectorio(self):
        self.enDirectorio=[] 
        self.ui.listaCanciones.clear()
        files=[]
        for r, d, f in os.walk(self.path): #@UnusedVariable
            for file in f:               
                if file[-4:]=='.cec':
                    files.append(file)
                    self.enDirectorio.append((r+'/'+file))
        for f in files:
            self.ui.listaCanciones.addItem(f.strip('.cec'))
        if files!=[]:            
            self.cerrarBrowser()
        if files==[]:
            QMessageBox.information(self, 'Error', 'Esta carpeta no contiene canciones para abrir')
            
    def abrirUnaCancion(self):
        try:
            homedir = os.path.expanduser("~")
            ruta=homedir+'\Desktop'
            path,_=QFileDialog.getOpenFileName(self, 'Seleccionar Canción', ruta)
            nombre=QFileInfo(path).fileName()
            if path[-4:]=='.cec':
                self.enDirectorio.append(path)
                self.ui.listaCanciones.addItem(nombre.strip('.cec'))
        except:
            pass
            
    def nuevaCancion(self):
        self.ui.cancionTE.clear()
        self.ui.cancionTE2.clear()
        self.ui.cancionTE.setPlaceholderText('''Escribir o pegar la cancion que desee guardar aquí 
recuerde que los reglones de las notas deben comensar con un punto (.) en el margen izquierdo 
y las tono principal deben estar en mayúscula y el resto del acorde en minúsculas.

Ej:

                TITULO  (si lo desea)
                AUTOR  (si lo desea)
                
ALGUNA OBSERVACIÓN (si lo desea)

INTRO:
.A   Dm    G#

.C                      G                   Ebm
 Mi corazón confiado está por que yo te conozco
 
.      Emaj7            F#                Gm/D
 Y en medio de la tempestad nunca estoy solo ''')   
             
    def agregar_a_play(self):
        try:
            fila=self.ui.listaCanciones.currentRow()
            lista=self.ui.listaCanciones.selectedItems()
            for l in lista: 
                self.enPlay2[l.text()]=self.enDirectorio[fila]+'\n' 
                self.ui.listaPlay.addItem(l.text())
        except:
            QMessageBox.information(self, 'Error','Error al cargar a Play List')
            
    def borrarItemListaPlay(self):
        try: 
            lista=self.ui.listaPlay.selectedItems()       
            self.ui.listaPlay.takeItem(self.ui.listaPlay.currentRow())   
            for l in lista:
                del self.enPlay2[l.text()]
        except:
            QMessageBox.information(self, 'Quitar', 'No hay nada para quitar')
        
    def abrirCancion(self):
        try:
            self.ui.cancionTE.clear()
            self.ui.cancionTE2.clear()
            lista=self.ui.listaPlay.selectedItems()
            for l in lista:
                file_text=abrirCancionSeleccionada(self.enPlay2[l.text()].strip('\n'))
            self.abrirConFormato(file_text)
            
            
        except:
            QMessageBox.information(self, 'Error', 'Verifique que la canción no se haya movido de carpeta')
            
    def guardarCambios(self):
        homedir = os.path.expanduser("~")
        ruta=homedir+'\Desktop'
        try:
            texto2 = self.ui.cancionTE.toPlainText()
            self.ui.cancionTE.clear()
            escribirCrearArchivo(texto2)
            file_text=abrirAuxiliar()

            for f in file_text:
                if f[0]=='.':                     
                    self.ui.cancionTE.setTextColor(QtGui.QColor("blue"))
                    self.ui.cancionTE.setFontWeight(QtGui.QFont.Bold)
                    self.ui.cancionTE.setFontPointSize(10)
                    self.ui.cancionTE.append(f.strip('\n'))
                if f[0]!='.':
                    if f[0]!=' ':
                        self.ui.cancionTE.setTextColor(QtGui.QColor("black"))
                        self.ui.cancionTE.setFontWeight(QtGui.QFont.Bold)
                        self.ui.cancionTE.setFontPointSize(10)                            
                        self.ui.cancionTE.append(' '+f.strip('\n'))
                    if f[0]==' ':
                        self.ui.cancionTE.setTextColor(QtGui.QColor("black"))
                        self.ui.cancionTE.setFontWeight(QtGui.QFont.Bold)
                        self.ui.cancionTE.setFontPointSize(10)                            
                        self.ui.cancionTE.append(f.strip('\n'))
            
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File', ruta)
            if filename !='':
                if QFileInfo(filename).suffix() == '':
                    filename += '.cec'
            f=open(filename, 'w')
            texto = self.ui.cancionTE.toPlainText()+'\n'+self.ui.cancionTE2.toPlainText()            
            f.write(texto)            
            f.close()            
        except:
            pass
        
    def transportarArriba(self): 
        try:       
            cancion=abrirAuxiliar()
            self.ui.cancionTE.clear()
            self.ui.cancionTE2.clear()
            nuevaCancion=transportarMedioArriba(cancion)
            self.abrirConFormato(nuevaCancion)
        except:
            QMessageBox.information(self, 'Error','Debe guardar la canción primero o No hay nada para transportar')

    def transportarAbajo(self):
        try:        
            cancion=abrirAuxiliar()
            self.ui.cancionTE.clear()
            self.ui.cancionTE2.clear()
            nuevaCancion=transportarMedioAbajo(cancion)
            self.abrirConFormato(nuevaCancion)
        except:
            QMessageBox.information(self, 'Error','Debe guardar la canción primero o No hay nada para transportar')
                    
    def exportarPDF(self):
        try:
            self.ui.cancionTE2.clear()
            file_text=abrirAuxiliar()
            for f in file_text:
                if f[0]=='.':                     
                    self.ui.cancionTE2.setTextColor(QtGui.QColor("blue"))
                    self.ui.cancionTE2.setFontWeight(QtGui.QFont.Bold)
                    self.ui.cancionTE2.setFontPointSize(10)
                    self.ui.cancionTE2.append(f.strip('\n'))
                if f[0]!='.':
                    self.ui.cancionTE2.setTextColor(QtGui.QColor("black"))
                    self.ui.cancionTE2.setFontWeight(QtGui.QFont.Bold)
                    self.ui.cancionTE2.setFontPointSize(10)                            
                    self.ui.cancionTE2.append(f.strip('\n'))
        except:
            pass
        try:
            filename, _ = QFileDialog.getSaveFileName(self, 'Exportar a PDF', None, 'PDF files (.pdf) ;; All Files()')
            if filename !='':
                if QFileInfo(filename).suffix() == '':
                    filename += '.pdf'
                printer = QPrinter(QPrinter.HighResolution)
                printer.setOutputFormat(QPrinter.PdfFormat)
                printer.setOutputFileName(filename)
                self.ui.cancionTE2.document().print_(printer)
    
            self.ui.cancionTE.clear()
            self.ui.cancionTE2.clear()
            file_text=abrirAuxiliar()
            self.abrirConFormato(file_text)
        except:
            pass
        
    def guardarSet(self):
        homedir = os.path.expanduser("~")
        ruta=homedir+'\Desktop'
        try:
            enPlay={}
            for i in range(self.ui.listaPlay.count()):
                enPlay[self.ui.listaPlay.item(i).text()]=self.enPlay2[self.ui.listaPlay.item(i).text()]
            filename, _ = QFileDialog.getSaveFileName(self, 'Guardar Lista', ruta)
            if filename !='':
                if QFileInfo(filename).suffix() == '':
                    filename += '.lec'
            f=open(filename,'w')
            f.writelines(str(enPlay))
            f.close()
            
        except:
            QMessageBox.information(self, 'Error','Error al Guardar Set') 
            
    def cargarLista(self):
        homedir = os.path.expanduser("~")
        ruta=homedir+'\Desktop'
        try:            
            self.ui.listaPlay.clear()
            self.enPlay2={}
            filename, _ = QFileDialog.getOpenFileName(self, 'Abrir Lista', ruta)
            f=open(filename, 'r')
            file_text =f.readlines()            
            for ft in file_text:
                self.enPlay2=eval(ft)
            for key in self.enPlay2.keys():
                self.ui.listaPlay.addItem(key)  
        except:
            QMessageBox.information(self, 'Error','Error al cargar Lista')
            
    def abrirConFormato(self,file_text):
        count=0
        for f in file_text:
            count+=1
            if count<40:
                if f[0]=='.':                     
                    self.ui.cancionTE.setTextColor(QtGui.QColor("blue"))
                    self.ui.cancionTE.setFontWeight(QtGui.QFont.Bold)
                    self.ui.cancionTE.setFontPointSize(10)
                    self.ui.cancionTE.append(f.strip('\n'))
                if f[0]!='.':
                    self.ui.cancionTE.setTextColor(QtGui.QColor("black"))
                    self.ui.cancionTE.setFontWeight(QtGui.QFont.Bold)
                    self.ui.cancionTE.setFontPointSize(10)                            
                    self.ui.cancionTE.append(f.strip('\n'))
            if count>=40:
                if f[0]=='.':                     
                    self.ui.cancionTE2.setTextColor(QtGui.QColor("blue"))
                    self.ui.cancionTE2.setFontWeight(QtGui.QFont.Bold)
                    self.ui.cancionTE2.setFontPointSize(10)
                    self.ui.cancionTE2.append(f.strip('\n'))
                if f[0]!='.':
                    self.ui.cancionTE2.setTextColor(QtGui.QColor("black"))
                    self.ui.cancionTE2.setFontWeight(QtGui.QFont.Bold)
                    self.ui.cancionTE2.setFontPointSize(10)                            
                    self.ui.cancionTE2.append(f.strip('\n'))
        #posicionar cursor arriba
        cursor = QTextCursor(self.ui.cancionTE2.document())
        cursor.setPosition(0)
        self.ui.cancionTE2.setTextCursor(cursor)
                       
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    miapp=miFormulario()
    miapp.show()
    sys.exit(app.exec_())