class Product :
    def __init__(self, id, name, price, quantity_sold, discount):
        self.id = id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount

        self.total_revenue = 0
        self.revenue_type = ""
        self.calculate_revenue()
        self.classify_revenue()

    def calculate_revenue(self) :
        revenue = (self.price * self.quantity_sold) - self.discount
        if revenue < 0 :
            self.total_revenue = 0
        else :
            self.total_revenue = revenue
            
    def classify_revenue(self) :
        if self.total_revenue < 5000000 :
            self.revenue_type = 'Thấp'
        elif self.total_revenue < 20000000 and self.total_revenue > 5000000:
            self.revenue_type = 'Trung bình'
        elif self.total_revenue < 50000000 and self.total_revenue > 20000000:
            self.revenue_type = 'Khá'
        elif self.total_revenue > 50000000 :
            self.revenue_type = 'Cao'


class ProductManager(Product) :
    def __init__(self):
        self.products = []

    def add_product(self):
        while True :
            add_id = input("Nhập mã SP để thêm: ").strip().upper()
            if add_id == '' :
                print("Mã sản phẩm không được rỗng")
                continue
            
            for prod in self.products :
                if add_id == prod.id :
                    print("Mã sản phẩm không được trùng")
                    break
            else :
                break

        while True :
            add_name = input("Nhập tên sản phẩm: ").strip()
            if add_name == '' :
                print("Tên sản phẩm không được rỗng")
                continue
            else :
                break

        while True :
            try :
                add_price_str = input("Nhập giá bán: ").strip()
                if add_price_str == '' :
                    print("Giá bán ko được rỗng!")
                    continue
                add_price = float(add_price_str)
                if add_price < 0:
                    print("Giá bán phải lớn hơn hoặc bằng 0")
                    continue
                break
            except ValueError :
                print("Giá bán ko hợp lệ!")
                

        while True :
            try :
                add_quantity_str = input("Nhập số lượng đã bán: ").strip()
                if add_quantity_str == '' :
                    print("Số lượng ko được rỗng!")
                    continue
                add_quantity = int(add_quantity_str)
                if add_quantity > 10000 or add_quantity < 0:
                    print("Số lượng phải là số nguyên từ 0 đến 10,000")
                    continue
                break
            except ValueError :
                print("Số lượng ko hợp lệ!")

        while True :
            try :
                add_dis_str = input("Nhập giảm giá: ").strip()
                if add_dis_str == '' :
                    print("Giảm giá ko được rỗng!")
                    continue
                add_dis = float(add_dis_str)
                if add_dis < 0:
                    print("Giảm giá phải lớn hơn hoặc bằng 0")
                    continue
                break
            except ValueError :
                print("Giảm giá không hợp lệ!")

        new_products = Product(add_id, add_name, add_price, add_quantity, add_dis)
        self.products.append(new_products)
        print("Thêm sản phẩm thành công!")


    def show_all(self):
        if not self.products :
            print("Danh sách sản phẩm đang rỗng!")
            return
        else :
            print("--- DANH SÁCH SẢN PHẨM ---")
            for prod in self.products :
                print(f"Mã SP: {prod.id} | "
                      f"Tên SP: {prod.name} | "
                      f"Giá bán: {prod.price:,} | "
                      f"Số lượng đã bán: {prod.quantity_sold} | "
                      f"Giảm giá: {prod.discount:,} | "
                      f"Tổng doanh thu: {prod.total_revenue:,} | "
                      f"Loại doanh thu: {prod.revenue_type} |")
            print("------------------------------------------------------------")

    def update_product(self):
        p_id = input("Nhập mã sản phẩm cần sửa: ").strip().upper()
        for p in self.products:
            if p.id == p_id:
                while True:
                    try:
                        new_price_str = input(f"Nhập giá mới: ").strip()
                        if new_price_str == "":
                            print("Giá ko để trống!")
                            continue
                        if new_price_str < 0:
                            print("Giá bán phải lớn hơn hoặc bằng 0")
                            continue
                        else :
                            p.price = float(new_price_str)
                            break
                    except ValueError:
                        print("Giá tiền không hợp lệ!")

                while True:
                    try:
                        new_qty_str = input(f"Nhập số lượng mới: ").strip()
                        if new_qty_str == "":
                            print("Số lượng không để trống!")
                            continue
                        if new_qty_str > 10000 or new_qty_str < 0 :
                            print("Số lượng đã bán phải là số nguyên từ 0 đến 10,000")
                            continue
                        else :
                            p.quantity_sold = int(new_qty_str)
                            break
                    except ValueError:
                        print("Số lượng không hợp lệ!")

                while True:
                    try:
                        new_disc_str = input(f"Nhập giảm giá mới: ").strip()
                        if new_disc_str == "":
                            print("Giảm giá không để trống")
                            continue
                        if new_disc_str < 0 :
                            print("Giảm giá phải lớn hơn hoặc bằng 0")
                            continue
                        else : 
                            p.discount = float(new_disc_str)
                            break
                    except ValueError:
                        print("Giảm giá không hợp lệ!")

                p.calculate_revenue()
                p.classify_revenue()
                print("Cập nhật sản phẩm thành công!")
                break
        else:
            print("Không tìm thấy sản phẩm cần cập nhật!")

    def delete_product(self):
        while True :
            confirm = False
            del_id = input("Nhập mã sản phẩm để xóa: ").strip().upper()
            for prod in self.products :
                if del_id == prod.id :
                    confirm = input("Bạn có chắc muốn xóa sản phẩm này không? (Y/N):").strip().upper()
                    
                    if confirm == 'Y' :
                        print("Xóa sản phẩm thành công!")
                        self.products.remove(prod)
                        confirm = True
                        break
                    elif confirm == 'N' :
                        print("Đã hủy thao tác xóa!")
                        confirm = True
                        break
                    else :
                        print("Lựa chọn ko hợp lệ")
                        continue
                else :
                    print("Không tìm thấy sản phẩm cần xóa!")
                    continue
            if confirm :
                break
    def search_product() :
        pass
    def statistics() :
        pass

list_product = ProductManager()

while True :
    print("""
================ MENU ================
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật sản phẩm
4. Xóa sản phẩm
5. Tìm kiếm sản phẩm
6. Thoát
=====================================
""")
    choice = input("Nhập lựa chọn của bạn: ").strip()
    if choice == '1' :
        list_product.show_all()
    elif choice == '2':
        list_product.add_product()
    elif choice == '3':
        list_product.update_product()
    elif choice == '4':
        list_product.delete_product()
    elif choice == '5':
        list_product.search_product()
    elif choice == '6':
        print("Thoát chương trình")
        break
    else :
        print("Vui lòng nhập lại!")
