import datetime
import random

# database untuk pelanggan, transaksi, dan voucher
customers = {}
transactions = {}
vouchers = {}

# fungsi untuk mendaftarkan pelanggan
def register_customer(name):
    customers[name] = {'spent': 0, 'vouchers': []}

# fungsi untuk mencatat transaksi
def record_transaction(customer_name, amount):
    # update total yang dihabiskan pelanggan
    customers[customer_name]['spent'] += amount

    # generate voucher untuk setiap 1,000,000 rupiah yang dihabiskan
    while customers[customer_name]['spent'] >= 1000000:
        voucher_code = str(random.randint(100000, 999999))
        vouchers[voucher_code] = {'customer': customer_name, 'value': 10000, 'expiry': datetime.datetime.now() + datetime.timedelta(days=90)}
        customers[customer_name]['vouchers'].append(voucher_code)
        customers[customer_name]['spent'] -= 1000000


# fungsi untuk menukarkan voucher
def redeem_voucher(voucher_code):
    if voucher_code in vouchers and vouchers[voucher_code]['expiry'] > datetime.datetime.now():
        print(f"Voucher {voucher_code} redeemed for {vouchers[voucher_code]['value']} rupiah!")
        del vouchers[voucher_code]
    else:
        print("Invalid or expired voucher!")

# Test
register_customer('Ucup')
record_transaction('Ucup', 3000000)
print(customers['Ucup']['vouchers'])
for voucher_code in customers['Ucup']['vouchers']:
    redeem_voucher(voucher_code)