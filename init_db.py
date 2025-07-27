from app import create_app, db
from app.models import (
    SharingGroup, PodSharingGroup, Pod, 
    Member, MemberFee, Accounting, MemberFeePayment
)

app = create_app()

def init_db():
    with app.app_context():
        db.create_all()
        
        # Create initial data if needed
        if not SharingGroup.query.first():
            groups = [
                SharingGroup(sgID=1, sgName='RueDesRomainUewn', sgNumber='00006041'),
                SharingGroup(sgID=2, sgName='RueDesRomainsEnnen', sgNumber='00006640'),
                SharingGroup(sgID=3, sgName='GroupeNational', sgNumber='00006750')
            ]
            db.session.bulk_save_objects(groups)
            
            member = Member(
                id=1, name='Marc', Firstname='Durbach',
                address='40, rue des romains-6370 Haller',
                phoneNumber='6611296114', email='mat@durbach.com',
                energyID='LUXE-MA-DU-ZPUGN'
            )
            db.session.add(member)
            
            member_fee = MemberFee(mfID=0, mfamount=5, mfYear=2025)
            db.session.add(member_fee)
            
            payment = MemberFeePayment(
                mfpID=1, memberID=1, memberFeeID=0,
                paymentDate='1/1/2025', paymentStatus='paid'
            )
            db.session.add(payment)
            
            db.session.commit()

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully!")