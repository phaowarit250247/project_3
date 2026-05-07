import sys
import sqlite3
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from project_3 import Ui_MainWindow

class DatabaseManager:
    def __init__(self, db_name='project_3.db'):
        # เชื่อมต่อ และเพิ่ม timeout เพื่อป้องกัน database is locked
        self.conn = sqlite3.connect(db_name, timeout=10)
        self.cursor = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        # ใช้ IF NOT EXISTS เพื่อไม่ให้ Error เมื่อรันโปรแกรมซ้ำ
        sql = '''
        CREATE TABLE IF NOT EXISTS Patients (
            Patient_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_Card_Number TEXT NOT NULL UNIQUE,
            FirstName_TH TEXT NOT NULL,
            LastName_TH TEXT NOT NULL,
            FirstName_EN TEXT,
            LastName_EN TEXT,
            Gender TEXT,
            Religion TEXT
        );
        '''
        self.cursor.execute(sql)
        self.conn.commit()

    def add_employee(self, id_card, fname_th, lname_th, fname_en, lname_en, gender, religion):
        sql = '''
        INSERT INTO Patients (
            ID_Card_Number, FirstName_TH, LastName_TH, 
            FirstName_EN, LastName_EN, Gender, Religion
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''' 
        self.cursor.execute(sql, (id_card, fname_th, lname_th, fname_en, lname_en, gender, religion))
        self.conn.commit()
    
    def update_employee(self, patient_id, id_card, fname_th, lname_th, fname_en, lname_en, gender, religion):
        sql = '''
        UPDATE Patients 
        SET ID_Card_Number=?, FirstName_TH=?, LastName_TH=?, 
            FirstName_EN=?, LastName_EN=?, Gender=?, Religion=?
        WHERE Patient_ID=?
        '''
        self.cursor.execute(sql, (id_card, fname_th, lname_th, fname_en, lname_en, gender, religion, patient_id))
        self.conn.commit()
    
    def delete_employee(self, patient_id):
        sql = 'DELETE FROM Patients WHERE Patient_ID=?'
        self.cursor.execute(sql, (patient_id,))
        self.conn.commit()
    
    def get_all_employees(self):
        sql = 'SELECT * FROM Patients'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def get_employee_by_id(self, patient_id):
        sql = 'SELECT * FROM Patients WHERE Patient_ID=?'
        self.cursor.execute(sql, (patient_id,))
        return self.cursor.fetchone()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # สร้างตัวจัดการฐานข้อมูล
        self.db = DatabaseManager()
        
        # ตัวแปรเก็บ ID ที่กำลังแก้ไข
        self.current_patient_id = None
        
        # เชื่อมต่อปุ่มต่างๆ
        self.Add.clicked.connect(self.create_data)
        self.Delect.clicked.connect(self.delete_data)
        self.Edit.clicked.connect(self.update_data)
        
        # เชื่อมต่อการคลิกที่ตาราง - ใช้ selection model แทน itemClicked
        self.tableWidget.selectionModel().selectionChanged.connect(self.on_table_select)
        
        # โหลดข้อมูลแสดงในตาราง
        self.load_data()
        
        # ตั้งค่าให้ตารางเลือกได้ทั้งแถวและเลือกได้ครั้งละ 1 แถว
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # เลือกทั้งแถว
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)  # เลือกได้ครั้งละ 1 แถว
        
        # ทำให้สามารถคลิกเลือกได้
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # ไม่ให้แก้ไขในตารางโดยตรง
        
        # ปิดการใช้งานปุ่ม Edit และ Delete เริ่มต้น (ยังไม่ได้เลือกอะไร)
        self.Edit.setEnabled(False)
        self.Delect.setEnabled(False)
    
    def load_data(self):
        """โหลดข้อมูลจากฐานข้อมูลมาแสดงในตาราง"""
        # ล้างข้อมูลเก่าในตาราง
        self.tableWidget.setRowCount(0)
        
        # ดึงข้อมูลทั้งหมด
        employees = self.db.get_all_employees()
        
        # แสดงข้อมูลทีละแถว
        for row, emp in enumerate(employees):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(emp[0])))  # Patient_ID
            self.tableWidget.setItem(row, 1, QTableWidgetItem(emp[1]))  # ID_Card_Number
            self.tableWidget.setItem(row, 2, QTableWidgetItem(emp[2]))  # FirstName_TH
            self.tableWidget.setItem(row, 3, QTableWidgetItem(emp[3]))  # LastName_TH
            self.tableWidget.setItem(row, 4, QTableWidgetItem(emp[4] if emp[4] else ""))  # FirstName_EN
            self.tableWidget.setItem(row, 5, QTableWidgetItem(emp[5] if emp[5] else ""))  # LastName_EN
            self.tableWidget.setItem(row, 6, QTableWidgetItem(emp[6] if emp[6] else ""))  # Gender
            self.tableWidget.setItem(row, 7, QTableWidgetItem(emp[7] if emp[7] else ""))  # Religion
        
        # ปรับขนาดคอลัมน์ให้พอดีกับเนื้อหา
        self.tableWidget.resizeColumnsToContents()
    
    def clear_inputs(self):
        """ล้างข้อมูลในช่องกรอกทั้งหมด"""
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.current_patient_id = None
        
        # เปลี่ยนข้อความปุ่ม Edit กลับเป็น Edit
        self.Edit.setText("Edit")
        
        # เปิดใช้งานปุ่ม Add และปิดการใช้งาน Edit/Delete
        self.Add.setEnabled(True)
        self.Edit.setEnabled(False)
        self.Delect.setEnabled(False)
    
    def on_table_select(self, selected, deselected):
        """เมื่อมีการเลือกแถวในตาราง"""
        # ตรวจสอบว่ามีการเลือกแถวหรือไม่
        if selected.indexes():
            # ได้แถวที่ถูกเลือก (แถวแรก)
            row = selected.indexes()[0].row()
            
            # ดึงข้อมูลจากตาราง
            patient_id = self.tableWidget.item(row, 0).text()
            id_card = self.tableWidget.item(row, 1).text()
            fname_th = self.tableWidget.item(row, 2).text()
            lname_th = self.tableWidget.item(row, 3).text()
            fname_en = self.tableWidget.item(row, 4).text()
            lname_en = self.tableWidget.item(row, 5).text()
            gender = self.tableWidget.item(row, 6).text()
            religion = self.tableWidget.item(row, 7).text()
            
            # แสดงข้อมูลในช่องกรอก
            self.lineEdit_1.setText(patient_id)  # แสดง Patient_ID
            self.lineEdit_2.setText(id_card)
            self.lineEdit_3.setText(fname_th)
            self.lineEdit_4.setText(lname_th)
            self.lineEdit_5.setText(fname_en)
            self.lineEdit_6.setText(lname_en)
            self.lineEdit_7.setText(gender)
            self.lineEdit_8.setText(religion)
            
            # เก็บ ID ที่กำลังจะแก้ไข
            self.current_patient_id = int(patient_id)
            
            # เปลี่ยนปุ่ม Edit เป็น "Update" และเปิดการใช้งาน
            self.Edit.setText("Update")
            self.Edit.setEnabled(True)
            self.Delect.setEnabled(True)
            self.Add.setEnabled(False)
        else:
            # ไม่มีการเลือกแถว
            self.clear_inputs()
    
    def create_data(self):
        """เพิ่มข้อมูลใหม่"""
        # 1. ดึงข้อมูลจาก LineEdit
        id_card  = self.lineEdit_2.text()
        fname_th = self.lineEdit_3.text()
        lname_th = self.lineEdit_4.text()
        fname_en = self.lineEdit_5.text()
        lname_en = self.lineEdit_6.text()
        gender   = self.lineEdit_7.text()
        religion = self.lineEdit_8.text()
        
        # 2. ตรวจสอบเงื่อนไขการกรอกข้อมูล
        if fname_th and lname_th:
            try:
                # 3. บันทึกลง Database
                self.db.add_employee(id_card, fname_th, lname_th, fname_en, lname_en, gender, religion)
                QMessageBox.information(self, "Success", "บันทึกข้อมูลเรียบร้อย!")
                
                # 4. โหลดข้อมูลใหม่และล้างฟอร์ม
                self.load_data()
                self.clear_inputs()
            except sqlite3.IntegrityError:
                QMessageBox.warning(self, "Error", "เลขบัตรประชาชนนี้มีอยู่ในระบบแล้ว")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"เกิดข้อผิดพลาด: {e}")
        else:
            QMessageBox.warning(self, "Error", "กรุณากรอกชื่อและนามสกุลไทย")
    
    def update_data(self):
        """อัพเดทข้อมูล"""
        if self.current_patient_id is None:
            QMessageBox.warning(self, "Warning", "กรุณาเลือกข้อมูลที่ต้องการแก้ไขจากตาราง")
            return
        
        # ดึงข้อมูลจากฟอร์ม
        id_card = self.lineEdit_2.text()
        fname_th = self.lineEdit_3.text()
        lname_th = self.lineEdit_4.text()
        fname_en = self.lineEdit_5.text()
        lname_en = self.lineEdit_6.text()
        gender = self.lineEdit_7.text()
        religion = self.lineEdit_8.text()
        
        # ตรวจสอบข้อมูล
        if fname_th and lname_th:
            try:
                # อัพเดทข้อมูล
                self.db.update_employee(self.current_patient_id, id_card, fname_th, lname_th, 
                                       fname_en, lname_en, gender, religion)
                QMessageBox.information(self, "Success", "อัพเดทข้อมูลเรียบร้อย!")
                
                # โหลดข้อมูลใหม่และล้างฟอร์ม
                self.load_data()
                self.clear_inputs()
                
            except sqlite3.IntegrityError:
                QMessageBox.warning(self, "Error", "เลขบัตรประชาชนนี้มีอยู่ในระบบแล้ว")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"เกิดข้อผิดพลาด: {e}")
        else:
            QMessageBox.warning(self, "Error", "กรุณากรอกชื่อและนามสกุลไทย")
    
    def delete_data(self):
        """ลบข้อมูล"""
        # ตรวจสอบว่ามีการเลือกข้อมูลหรือไม่
        if self.current_patient_id is None:
            QMessageBox.warning(self, "Warning", "กรุณาเลือกข้อมูลที่ต้องการลบจากตาราง")
            return
        
        # ยืนยันการลบ
        reply = QMessageBox.question(self, "Confirm Delete", 
                                     "คุณต้องการลบข้อมูลนี้ใช่หรือไม่?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                # ลบข้อมูล
                self.db.delete_employee(self.current_patient_id)
                QMessageBox.information(self, "Success", "ลบข้อมูลเรียบร้อย!")
                
                # โหลดข้อมูลใหม่และล้างฟอร์ม
                self.load_data()
                self.clear_inputs()
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"เกิดข้อผิดพลาดในการลบข้อมูล: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())