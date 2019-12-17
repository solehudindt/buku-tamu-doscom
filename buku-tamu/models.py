from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
# Kita harus import setiap tipe data yang ingin kita gunakan
from sqlalchemy import create_engine

# engine = create_engine('mysql+mysqlconnector://root:ge3k@localhost:3306/pygui') 
engine = create_engine('sqlite:///pinjamin.db')
Base = declarative_base()
# setiap class yang akan dipetakan harus inherit dari instance declarative_base

class Pinjam(Base): #inherit from Base
    __tablename__ = 'pinjam'    
    # tablename disini hanya sebagai metadata

    id = Column(Integer, nullable=False, primary_key=True)
    nama = Column(String(25), nullable=False)
    barang = Column(String(25), nullable=False)
    tanggal = Column(Date, nullable=False)

    tipe = Column(String(1), nullable=False, default="1")

    def __repr__(self):
    	return "<Pinjam(peminjam='{0}', barang='{1}', tanggal='{2}', tipe='{3}')>".format(
    			self.peminjam, self.barang, self.tanggal, self.tipe)

Base.metadata.create_all(engine) 
# # menjalankan perintah pemetaan/membuat database
DBSession = sessionmaker()
DBSession.configure(bind=engine)
session = DBSession()