from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

device_list = ['G6-200','G6-300','G7-100']

device_region_list = ['ALL','NCR','Canada']

xpath_list = [
    [2, 1, 'upc.contactlessemvl1.ver', '//*[@id="main-content"]/div[1]/table/tbody/tr[3]/td[2]/p[1]','//*[@id="main-content"]/div[1]/table/tbody/tr[3]/td[3]'],
    [2, 1, 'opt.emv.contactless.kernel.mastercard.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[4]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[4]/td[3]'],
    [2, 1, 'opt.emv.contactless.kernel.paywave.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[5]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[5]/td[3]'],
    [2, 1, 'opt.emv.contactless.kernel.dpas.ver', '//*[@id="main-content"]/div[1]/table/tbody/tr[6]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[6]/td[3]'],
    [2, 1, 'opt.emv.contactless.kernel.express.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[7]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[7]/td[3]'],
    [2, 1, 'opt.emv.contactless.kernel.jcb.ver', '//*[@id="main-content"]/div[1]/table/tbody/tr[8]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[8]/td[3]'],
    [2, 1, 'opt.emv.contactless.kernel.unionpay.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[9]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[9]/td[3]'],
    [2, 1, 'opt.emv.contactless.kernel.interac.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[10]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[10]/td[3]'],
    [2, 1, 'upc.emvkernel.ver', '//*[@id="main-content"]/div[1]/table/tbody/tr[11]/td[2]/p[1]','//*[@id="main-content"]/div[1]/table/tbody/tr[11]/td[3]'],
    [2, 1, 'upc.offlinepin.ver', '//*[@id="main-content"]/div[1]/table/tbody/tr[12]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[12]/td[3]'],
    [2, 1, 'upc.emvl1.ver', '//*[@id="main-content"]/div[1]/table/tbody/tr[13]/td[2]/span','//*[@id="main-content"]/div[1]/table/tbody/tr[13]/td[3]'],
    [2, 1, 'upc.entrypoint.ver', '//*[@id="main-content"]/div[1]/table/tbody/tr[15]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[15]/td[3]/p[2]'],
    [2, 1, 'upc.cep.ver', '//*[@id="main-content"]/div[1]/table/tbody/tr[16]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[16]/td[3]/p[2]'],

    [3, 2, 'upc.contactlessemvl1.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[3]/td[2]/p[1]','//*[@id="main-content"]/div[2]/table/tbody/tr[3]/td[4]'],
    [3, 2, 'upc.paypass.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[4]/td[2]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[4]/td[4]'],
    [3, 2, 'upc.paywave.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[5]/td[2]','//*[@id="main-content"]/div[2]/table/tbody/tr[5]/td[4]'],
    [3, 2, 'upc.dpas.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[6]/td[2]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[6]/td[4]'],
    [3, 2, 'upc.express.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[7]/td[2]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[7]/td[4]'],
    [3, 2, 'upc.interac.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[8]/td[2]','//*[@id="main-content"]/div[2]/table/tbody/tr[8]/td[4]'],
    [3, 2, 'upc.emvkernel.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[9]/td[2]/p[1]','//*[@id="main-content"]/div[2]/table/tbody/tr[9]/td[4]'],
    [3, 2, 'upc.offlinepin.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[10]/td[2]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[10]/td[4]'],
    [3, 2, 'upc.emvl1.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[11]/td[2]','//*[@id="main-content"]/div[2]/table/tbody/tr[11]/td[4]'],
    [3, 2, 'upc.entrypoint.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[13]/td[2]/p[2]','//*[@id="main-content"]/div[2]/table/tbody/tr[13]/td[4]'],
    [3, 2, 'upc.cep.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[14]/td[2]/p[2]','//*[@id="main-content"]/div[2]/table/tbody/tr[14]/td[4]'],

    [3, 3, 'upc.contactlessemvl1.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[3]/td[3]/p[1]','//*[@id="main-content"]/div[2]/table/tbody/tr[3]/td[4]'],
    [3, 3, 'upc.paypass.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[4]/td[3]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[4]/td[4]'],
    [3, 3, 'upc.paywave.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[5]/td[3]','//*[@id="main-content"]/div[2]/table/tbody/tr[5]/td[4]'],
    [3, 3, 'upc.dpas.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[6]/td[3]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[6]/td[4]'],
    [3, 3, 'upc.express.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[7]/td[3]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[7]/td[4]'],
    [3, 3, 'upc.interac.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[8]/td[3]','//*[@id="main-content"]/div[2]/table/tbody/tr[8]/td[4]'],
    [3, 3, 'upc.emvkernel.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[9]/td[3]/p[1]','//*[@id="main-content"]/div[2]/table/tbody/tr[9]/td[4]'],
    [3, 3, 'upc.offlinepin.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[10]/td[3]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[10]/td[4]'],
    [3, 3, 'upc.emvl1.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[11]/td[3]','//*[@id="main-content"]/div[2]/table/tbody/tr[11]/td[4]'],
    [3, 3, 'upc.entrypoint.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[13]/td[3]','//*[@id="main-content"]/div[2]/table/tbody/tr[13]/td[4]'],
    [3, 3, 'upc.cep.ver', '//*[@id="main-content"]/div[2]/table/tbody/tr[14]/td[3]','//*[@id="main-content"]/div[2]/table/tbody/tr[14]/td[4]'],

    [1, 1, 'pcd.ver.emvl1', '//*[@id="main-content"]/div[4]/table/tbody/tr[1]/td[2]','//*[@id="main-content"]/div[4]/table/tbody/tr[1]/td[3]'],
    [1, 1, 'pcd.ver.kernels.pp', '//*[@id="main-content"]/div[4]/table/tbody/tr[2]/td[2]/span','//*[@id="main-content"]/div[4]/table/tbody/tr[2]/td[3]'],
    [1, 1, 'pcd.ver.kernels.pw', '//*[@id="main-content"]/div[4]/table/tbody/tr[3]/td[2]','//*[@id="main-content"]/div[4]/table/tbody/tr[3]/td[3]'],
    [1, 1, 'pcd.ver.kernels.dp', '//*[@id="main-content"]/div[4]/table/tbody/tr[4]/td[2]/span','//*[@id="main-content"]/div[4]/table/tbody/tr[4]/td[3]'],
    [1, 1, 'pcd.ver.kernels.xp', '//*[@id="main-content"]/div[4]/table/tbody/tr[5]/td[2]/span','//*[@id="main-content"]/div[4]/table/tbody/tr[5]/td[3]'],
    [1, 1, 'emv.ver.emvk', '//*[@id="main-content"]/div[4]/table/tbody/tr[6]/td[2]','//*[@id="main-content"]/div[4]/table/tbody/tr[6]/td[3]/p'],
    [1, 1, 'upc.ver.emvl1', '//*[@id="main-content"]/div[4]/table/tbody/tr[8]/td[2]','//*[@id="main-content"]/div[4]/table/tbody/tr[8]/td[3]/p'],
]

Base = declarative_base()

class Device(Base):
    __tablename__ = 'device'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String(10), nullable=False,unique=True)

    def __repr__(self):
        return "<Device (model='%s')>" % self.model

class DeviceRegion(Base):
    __tablename__ = 'device_region'
    id = Column(Integer, primary_key=True, autoincrement=True)
    region_name = Column(String(10), nullable=False,unique=True)

    def __repr__(self):
        return "<Device Region/Customer (name='%s')>" % self.region_name

class EmvVerXpath(Base):
    __tablename__ = 'emv_ver_xpath'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('device.id'))
    device_region_id = Column(Integer, ForeignKey('device_region.id'))
    tag_name = Column(String(55))
    version_xpath = Column(String(75))
    tag_name_xpath = Column(String(75))
    device = relationship(Device)
    device_region = relationship(DeviceRegion)

    def __repr__(self):
        return "<EmvVerXpath (device_id='%d', device_region_id='%d', tag_name='%s', version_xpath='%s', tag_name_xpath='%s')>" \
               % (self.device_id, self.device_region_id,self.tag_name,self.version_xpath,self.tag_name_xpath)

engine = create_engine('sqlite:///emv_ver_xpath.db', echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

for x in device_list:
    device = Device()
    device.model = x
    session.add(device)

for x in device_region_list:
    device_region = DeviceRegion()
    device_region.region_name = x
    session.add(device_region)

for x in xpath_list:
    emv_ver_xpath = EmvVerXpath()
    emv_ver_xpath.device_id = x[0]
    emv_ver_xpath.device_region_id = x[1]
    emv_ver_xpath.tag_name = x[2]
    emv_ver_xpath.version_xpath = x[3]
    emv_ver_xpath.tag_name_xpath = x[4]
    session.add(emv_ver_xpath)

session.commit()
session.close()
