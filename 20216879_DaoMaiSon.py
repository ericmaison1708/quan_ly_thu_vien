# Đào Mai Sơn
# 20216879

import csv
import pandas as pd
import numpy as np


# HAM KIEM TRA DAU VAO
def kiem_tra_input(in_str):
    if in_str == "":
        return False
    for i in in_str:
        if not i.isdigit():
            return False
    return True

def nhap_int():
    res = -1
    in_str = input().strip()
    if kiem_tra_input(in_str):
        res = int(in_str)
    return res

def nhap_int_tu_file(in_str):
    res = -1
    if kiem_tra_input(in_str):
        res = int(in_str)
    return res

# XU LY INPUT DAU VAO
def xu_ly_input(doc_input):
    luu_input = []
    b = ""
    kiem_tra = False
    
    i = 0
    while i < len(doc_input):
        kiem_tra = True
        if doc_input[i] == ';' or doc_input[i] == ',':
            luu_input.append(b)
            b = ""
            while i + 1 < len(doc_input) and doc_input[i + 1] == ' ':
                i += 1
            i += 1
            continue
        while doc_input[i] == ' ':
            if i + 1 < len(doc_input) and (doc_input[i + 1] == ';' or doc_input[i + 1] == ','):
                kiem_tra = False
                break
            elif i + 1 < len(doc_input) and doc_input[i + 1] == ' ':
                i += 1
            else:
                break
        if kiem_tra:
            b += doc_input[i]
        i += 1
    
    return luu_input

# HAM NHAP VAO TEN TAC GIA
def nhap_cac_tac_gia(tac_gia):
    so_tac_gia = -1

    while True:
        print("  NHAP SO TAC GIA: ", end="")
        so_tac_gia = nhap_int()
        if so_tac_gia == -1:
            print("  SO TAC GIA KHONG HOP LE! VUI LONG NHAP LAI!")
        else:
            break
    
    print("  Nhap cac tac gia: ")
    for i in range(so_tac_gia):
        print("                 {}:  ".format(i + 1), end="")
        tg = input().strip()
        tac_gia.append(tg)


# HAM IN TAC GIA 
def in_cac_tac_gia(tac_gia):
    print("1.  " + tac_gia[0])
    for i in range(1, len(tac_gia)):
        print("                     |  {}.  {}".format(i + 1, tac_gia[i]))



# KHOI TAO CLASS SACH
class Sach:
    def __init__(self, so_dang_ki=None, ten_sach=None, tac_gia=None, nha_xuat_ban=None, nam_xuat_ban=None, so_ISBN=None):
        self.so_dang_ki = so_dang_ki
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.nha_xuat_ban = nha_xuat_ban
        self.nam_xuat_ban = nam_xuat_ban
        self.so_ISBN = so_ISBN

    # HAM LAY SO DANG KI
    def lay_so_dang_ki(self):
        return self.so_dang_ki

    # HAM LAY TEN SACH
    def lay_ten_sach(self):
        return self.ten_sach

    # HAM CHINH SUA TAC GIA
    def chinh_sua_tac_gia(self):
        chon = int(input("\n      1. THEM TAC GIA\n      2. XOA TAC GIA\n      CHON CHUC NANG BAN MUON SU DUNG: "))
        # THEM TAC GIA
        if chon == 1:
            n = int(input("  NHAP SO TAC GIA MUON THEM: "))
            for i in range(n):
                tg = input("        {}:  ".format(i + 1))
                # KIEM TRA XEM TAC GIA CO TEN TRONG SACH KHONG
                if tg not in self.tac_gia:
                    self.tac_gia.append(tg)
                    print("     CAP NHAT THANH CONG!!!")
                else:
                    print("      TEN TAC GIA DA CO TRONG SACH")
                    print("      CAP NHAT TAC GIA KHONG THANH CONG !!!")
                    break
        # XOA TAC GIA
        elif chon == 2:
            tg = input("\n      NHAP TEN TAC GIA BAN MUON XOA: ")
            # KIEM TRA XEM TAC GIA CO TEN TRONG SACH KHONG
            if tg in self.tac_gia:
                self.tac_gia.remove(tg)
                print("\n     DA XOA TAC GIA", tg)
            else:
                print("\n      TEN TAC GIA KHONG CO TRONG SACH")
        else:
            print("      TINH NANG CHO KHONG HOP LE !!!")

    # HAM LAY RA TAC GIA
    def lay_tac_gia(self):
        return self.tac_gia

    # HAM CHINH SUA NXB
    def chinh_sua_nha_xuat_ban(self, nha_xuat_ban):
        self.nha_xuat_ban = nha_xuat_ban

    # HAM LAY RA NXB
    def lay_nha_xuat_ban(self):
        return self.nha_xuat_ban

    # HAM CHINH SUA NXB
    def chinh_sua_nam_xuat_ban(self, nam_xuat_ban):
        self.nam_xuat_ban = nam_xuat_ban

    # HAM LAY RA NAM XUAT BAN
    def lay_nam_xuat_ban(self):
        return self.nam_xuat_ban

    # HAM LAY RA SO ISBN
    def lay_so_ISBN(self):
        return self.so_ISBN
    
    def __str__(self):
        return f"{self.so_dang_ki}; {self.ten_sach}; {len(self.tac_gia)}, {', '.join(self.tac_gia)}; {self.nha_xuat_ban}; {self.nam_xuat_ban}; {self.so_ISBN}"


# HAM DUA DU LIEU VAO CHUONG TRINH TU FILE DU LIEU CUA THU VIEN 
def nhap_du_lieu_tu_file(sach):
    kiem_tra = True
    luu_sach = []
    kiem_tra_file = ""
    
    try:
        with open("them_sach.txt", "r") as input_file:
            kiem_tra_file = input_file.readline().strip()
            
            if kiem_tra_file != "":
                for line in input_file:
                    luu_input = xu_ly_input(line.strip())
                    
                    so_dang_ki = nhap_int_tu_file(luu_input[0])
                    if so_dang_ki == -1:
                        print("\n  SO DANG KI O HANG THU {} KHONG HOP LE".format(len(luu_sach) + 1))
                        kiem_tra = False
                        break
                    
                    ten_sach = luu_input[1]
                    
                    so_tac_gia = nhap_int_tu_file(luu_input[2])
                    if so_tac_gia == -1:
                        print("\n  SO TAC GIA O HANG THU {} KHONG HOP LE".format(len(luu_sach) + 1))
                        kiem_tra = False
                        break
                    
                    tac_gia = luu_input[3:3+so_tac_gia]
                    
                    nha_suat_ban = luu_input[3+so_tac_gia]
                    
                    nam_suat_ban = nhap_int_tu_file(luu_input[4+so_tac_gia])
                    if nam_suat_ban == -1:
                        print("\n  NAM XUAT BAN O HANG THU {} KHONG HOP LE".format(len(luu_sach) + 1))
                        kiem_tra = False
                        break
                    
                    so_ISBN = luu_input[5+so_tac_gia]
                    
                    # KIEM TRA XEM DU LIEU DUOC DUA VAO CO BI XUNG DOT KHONG
                    for i in range(len(luu_sach)):
                        # KIEM TRA SO DANG KI
                        if so_dang_ki == luu_sach[i].lay_so_dang_ki():
                            print("\n  SO DANG KI TRONG DU LIEU THU {} BI TRUNG VOI DU LIEU THU {} TRONG FILE !!!".format(len(luu_sach) + 1, i + 1))
                            kiem_tra = False
                            break
                        # KIEM TRA TEN SACH
                        if ten_sach == luu_sach[i].lay_ten_sach():
                            print("\n  TEN SACH TRONG DU LIEU THU {} BI TRUNG VOI DU LIEU THU {} TRONG FILE !!!".format(len(luu_sach) + 1, i + 1))
                            kiem_tra = False
                            break
                        # KIEM TRA SO ISBN
                        if so_ISBN == luu_sach[i].lay_so_ISBN():
                            print("\n  SO ISBN TRONG DU LIEU THU {} BI TRUNG VOI DU LIEU THU {} TRONG FILE !!!".format(len(luu_sach) + 1, i + 1))
                            kiem_tra = False
                            break
                    
                    # THUC HIEN DAY SACH VAO TRONG LIST 
                    if kiem_tra:
                        s = Sach(so_dang_ki, ten_sach, tac_gia, nha_suat_ban, nam_suat_ban, so_ISBN)
                        luu_sach.append(s)
                    
                    # THONG BAO NHAP LAI INPUT NEU DU LIEU BI XUNG DOT
                    else:
                        print("\n  VUI LONG CAP NHAT LAI FILE DAU VAO CUA BAN !!!")
                        break
                
                # THUC HIEN NHAP DU LIEU SACH VAO CHUONG TRINH NEU TAT CA CAC HANG TRONG DU LIEU KHONG BI XUNG DOT
                if kiem_tra:
                    sach.extend(luu_sach)
                
                # THONG BAO KHONG NHAP DUOC DU LIEU
                else:
                    print("\n  KHONG HOAN THANH THEM SACH TU FILE !!!")
    
    except FileNotFoundError:
        print("\n  KHONG TIM THAY FILE DU LIEU !!!")


# HAM THEM SACH VAO THU VIEN      
def them_sach(sach):
    while True:
        print("\n--------------------- THEM SACH VAO THU VIEN ----------------------")
        print("|       1. THEM TU CONSOLE                                          |")
        print("|       2. THEM TU FILE                                             |")
        print("|       3. BACK                                                     |")
        print(" -------------------------------------------------------------------")
        chon = int(input("\n     CHON CHUC NANG MUON THEM VAO: "))
        
        # THUC HIEN NHAP SACH VAO TU CONSOLE
        if chon == 1:
            so_dang_ki = None
            ten_sach = None
            tac_gia = []
            nha_suat_ban = None
            nam_suat_ban = None
            so_ISBN = None
            kiem_tra = True

            while True:
                while True:
                    kiem_tra = True
                    while True:
                        print("  1. NHAP SO DANG KI: ")
                        so_dang_ki = nhap_int()
                        if so_dang_ki == -1:
                            print("  SO DANG KI KHONG HOP LE! VUI LONG NHAP LAI!")
                        else:
                            break
                    # KIEM TRA XEM SO DANG KI DA TON TAI CHUA
                    for i in range(len(sach)):
                        if so_dang_ki == sach[i].lay_so_dang_ki():
                            print("\n  SO DANG KI DA TON TAI !!!")
                            kiem_tra = False
                    if not kiem_tra:
                        chon = input("  NHAN (Y | N) DE (CO | KHONG) NHAP LAI SO DANG KI: ")
                        if chon in ['n', 'N']:
                            break
                        else:
                            continue
                    if kiem_tra:
                        break
                if not kiem_tra:
                    break

                while True:
                    chon = None
                    kiem_tra = True
                    print("  2. NHAP TEN SACH: ")
                    ten_sach = input()
                    # KIEM TRA XEM TEN SACH DA TON TAI CHUA
                    for i in range(len(sach)):
                        if ten_sach == sach[i].lay_ten_sach():
                            print("\n  TEN CUON SACH DA TON TAI !!!")
                            kiem_tra = False
                    if not kiem_tra:
                        chon = input("  NHAN (Y | N) DE (CO | KHONG) NHAP LAI TEN SACH: ")
                        if chon in ['n', 'N']:
                            break
                        else:
                            continue
                    if kiem_tra:
                        break
                if not kiem_tra:
                    break

                print("  3. NHAP TAC GIA: ")
                nhap_cac_tac_gia(tac_gia)
                print("  4. NHAP NHA XUAT BAN: ")
                nha_suat_ban = input()
                while True:
                    print("  5. NHAP NAM XUAT BAN: ")
                    nam_suat_ban = nhap_int()
                    if nam_suat_ban == -1:
                        print("  NAM XUAT BAN KHONG HOP LE! VUI LONG NHAP LAI!")
                    else:
                        break
                while True:
                    chon = None
                    kiem_tra = True
                    print("  6. NHAP SO ISBN: ")
                    so_ISBN = input()
                    # KIEM TRA SO ISBN DA TON TAI CHUA
                    for i in range(len(sach)):
                        if so_ISBN == sach[i].lay_so_ISBN():
                            print("\n  SO ISBN DA TON TAI !!!")
                            kiem_tra = False

                    if not kiem_tra:
                        chon = input("  NHAN (Y || N) DE (CO || KHONG) NHAP LAI SO ISBN: ")
                        if chon in ['n', 'N']:
                            break
                        else:
                            continue

                    if kiem_tra:
                        break

                if not kiem_tra:
                    break
                # THUC HIEN THEM SACH VAO THU VIEN NEU CAC THONG TIN NHAP VAO THOA MAN
                if kiem_tra:
                    s = Sach(so_dang_ki, ten_sach, tac_gia, nha_suat_ban, nam_suat_ban, so_ISBN)
                    sach.append(s)
                    print("  THEM SACH THANH CONG !!!")
                    print()
                    print()
            print()
            print()

        # THUC HIEN THEM SACH VAO THU VIEN TU FILE
        elif chon == 2:

            kiem_tra = True
            luu_sach = []

            with open("them_sach.txt", "r") as file_input:
                for line in file_input:
                    so_dang_ki = None
                    ten_sach = None
                    tac_gia = []
                    nha_suat_ban = None
                    nam_suat_ban = None
                    so_ISBN = None
                    tg = None
                    luu_input = []
                    a = 0

                    doc_input = line.strip()
                    luu_input = xu_ly_input(doc_input)
                    so_dang_ki = nhap_int_tu_file(luu_input[0])
                    if so_dang_ki == -1:
                        print("\n  SO DANG KI O HANG THU", len(luu_sach) + 1, "KHONG HOP LE")
                        kiem_tra = False
                        break
                    ten_sach = luu_input[1]
                    so_tac_gia = nhap_int_tu_file(luu_input[2])
                    if so_tac_gia == -1:
                        print("\n  SO TAC GIA O HANG THU", len(luu_sach) + 1, "KHONG HOP LE")
                        kiem_tra = False
                        break
                    a = 3
                    for i in range(so_tac_gia):
                        tac_gia.append(luu_input[a + i])
                    nha_suat_ban = luu_input[a + so_tac_gia]
                    nam_suat_ban = nhap_int_tu_file(luu_input[a + so_tac_gia + 1])
                    if nam_suat_ban == -1:
                        print("\n  NAM XUAT BAN O HANG THU", len(luu_sach) + 1, "KHONG HOP LE")
                        kiem_tra = False
                        break
                    so_ISBN = luu_input[a + so_tac_gia + 2]
                    # KIEM TRA SO DANG KI, TEN SACH, SO ISBN DA TON TAI TRONG SACH CHUA
                    for i in range(len(sach)):
                        if so_dang_ki == sach[i].lay_so_dang_ki():
                            print("\n  SO DANG KI O HANG THU", len(luu_sach) + 1, "TRONG FILE THU BI TRUNG VOI SACH HIEN CO !!!")
                            kiem_tra = False
                            break
                        if ten_sach == sach[i].lay_ten_sach():
                            print("\n  TEN SACH O HANG THU", len(luu_sach) + 1, "TRONG FILE THU BI TRUNG VOI SACH HIEN CO !!!")
                            kiem_tra = False
                            break
                        if so_ISBN == sach[i].lay_so_ISBN():
                            print("\n  SO ISBN O HANG THU", len(luu_sach) + 1, "TRONG FILE THU BI TRUNG VOI SACH HIEN CO !!!")
                            kiem_tra = False
                            break
                    if kiem_tra:
                        # KIEM TRA SO DANG KI, TEN SACH, SO ISBN TRONG FILE DUA VAO HOP LE CHUA
                        for i in range(len(luu_sach)):
                            if so_dang_ki == luu_sach[i].lay_so_dang_ki():
                                print("\n  SO DANG KI O HANG THU", len(luu_sach) + 1, "TRONG FILE THU BI TRUNG VOI DU LIEU THU", i + 1, "TRONG FILE !!!")
                                kiem_tra = False
                                break
                            if ten_sach == luu_sach[i].lay_ten_sach():
                                print("\n  TEN SACH O HANG THU", len(luu_sach) + 1, "TRONG FILE THU BI TRUNG VOI DU LIEU THU", i + 1, "TRONG FILE !!!")
                                kiem_tra = False
                                break
                            if so_ISBN == luu_sach[i].lay_so_ISBN():
                                print("\n  SO ISBN O HANG THU", len(luu_sach) + 1, "TRONG FILE THU BI TRUNG VOI DU LIEU THU", i + 1, "TRONG FILE !!!")
                                kiem_tra = False
                                break
                    # THUC HIEN THEM SACH VAO LIST NEU DU LIEU KHONG BI XUNG DOT
                    if kiem_tra:
                        s = Sach(so_dang_ki, ten_sach, tac_gia, nha_suat_ban, nam_suat_ban, so_ISBN)
                        luu_sach.append(s)
                    # THONG BAO NHAP LAI INPUT NEU DU LIEU BI XUNG DOT
                    else:
                        print("\n  VUI LONG CAP NHAT LAI FILE DAU VAO CUA BAN !!!")
                        break
            # THUC HIEN NHAP DU LIEU SACH VAO CHUONG TRINH NEU TAT CA CAC HANG TRONG DU LIEU KHONG BI XUNG DOT
            if kiem_tra:
                for i in range(len(luu_sach)):
                    sach.append(luu_sach[i])
                print("     THEM SACH THANH CONG !!!")
            # THONG BAO KHONG NHAP DUOC DU LIEU
            else:
                print("\n  KHONG HOAN THANH THEM SACH TU FILE !!!")
            print()
            print() 

        # THOAT KHOI CHUONG TRINH NHAP SACH
        elif chon == 3:
            break
        # THONG BAO TINH NANG CHON KHONG HOP LE
        else:
            print("\n     TINH NANG CHON KHONG HOP LE !!!")
            print()
            print()


def in_ra_thong_tin_sach(s):
    print()
    print("   ------------------------- THONG TIN SACH---------------------------")
    print("  |    SACH          |  ", s.lay_ten_sach())
    print("   -------------------------------------------------------------------")
    print("  |    SO DANG KI    |  ", s.lay_so_dang_ki())
    print("   -------------------------------------------------------------------")
    print("  |    TAC GIA       |  ", end = "")
    in_cac_tac_gia(s.lay_tac_gia())
    print("   -------------------------------------------------------------------")
    print("  |    NHA XUAT BAN  |  ", s.lay_nha_xuat_ban())
    print("   -------------------------------------------------------------------")
    print("  |    NAM XUAT BAN  |  ", s.lay_nam_xuat_ban())
    print("   -------------------------------------------------------------------")
    print("  |    SO ISBN       |  ", s.lay_so_ISBN())
    print("   -------------------------------------------------------------------")
    print()


def in_ra_danh_sach_sach(sach):
    print()
    print(" ---------------------------------------------------- DANH SACH --------------------------------------------------------")
    print("|    SO DANG KI   |                  TEN SACH                        |                 NHA XUAT BAN                     |")
    print(" -----------------------------------------------------------------------------------------------------------------------")
    for i in range(len(sach)):
        print("|    ", str(sach[i].lay_so_dang_ki()).ljust(11), "|    ", sach[i].lay_ten_sach().ljust(44), "|    ", sach[i].lay_nha_xuat_ban().ljust(44), "|")
        print(" -----------------------------------------------------------------------------------------------------------------------")

# HAM CAP NHAT THONG TIN SACH
def cap_nhat_sach(sach):
    chon = 0

    while True:
        print("\n --------------------- CAP NHAT THONG TIN SACH ----------------------")
        print("|       1. TIM SACH DE CAP NHAT                                      |")
        print("|       2. BACK                                                      |")
        print(" -------------------------------------------------------------------- ")
        print("     NHAP LUA CHON CUA BAN:  ")
        chon = nhap_int()
        if chon == 1:
            # TIM KIEM SACH DE CAP NHAT
            vi_tri = tim_kiem_sach(sach)
            if vi_tri == -1:
                print("\n     KHONG TIM THAY THONG TIN SACH !!!\n")
            else:
                # THUC HIEN CAP NHAT SACH
                xac_nhan = ""
                print("\n     BAN MUON CAP NHAT SACH ", sach[vi_tri].lay_ten_sach(), "? - GO Y || N DE XAC NHAN CO || KHONG: ")
                xac_nhan = input()
                if xac_nhan.lower() == "y":
                    while True:
                        chon_thong_tin = 0
                        print("\n      1. TAC GIA")
                        print("\n      2. NHA XUAT BAN")
                        print("\n      3. NAM XUAT BAN")
                        print("\n     CHON THONG TIN BAN MUON CAP NHAT: ")
                        chon_thong_tin = nhap_int()
                        if chon_thong_tin == 1:
                            print("\n     CAP NHAT THONG TIN TAC GIA:")
                            sach[vi_tri].chinh_sua_tac_gia()
                        elif chon_thong_tin == 2:
                            nha_xuat_ban = ""
                            print("\n     CAP NHAT THONG TIN NHA XUAT BAN:")
                            print("\n     Nhap ten nha xuat ban: ")
                            nha_xuat_ban = input()
                            sach[vi_tri].chinh_sua_nha_xuat_ban(nha_xuat_ban)
                            print("     CAP NHAT THANH CONG!!!")
                        elif chon_thong_tin == 3:
                            nam_xuat_ban = 0
                            print("\n     CAP NHAT THONG TIN NAM XUAT BAN:")
                            while True:
                                print("  Nhap nam xuat ban: ")
                                nam_xuat_ban = nhap_int()
                                if nam_xuat_ban == -1:
                                    print("  NAM XUAT BAN KHONG HOP LE! VUI LONG NHAP LAI!\n")
                                else:
                                    break
                            sach[vi_tri].chinh_sua_nam_xuat_ban(nam_xuat_ban)
                            print("     CAP NHAT THANH CONG!!!")
                        else:
                            print("\n       TINH NANG CHON KHONG HOP LE !!!")
                            print()
                        print()
                        print("\n     THONG TIN SACH CUA BAN SAU KHI CAP NHAT:\n")
                        in_ra_thong_tin_sach(sach[vi_tri])
                        print()
                        print("\n     BAN CO MUON CAP NHAT TIEP KHONG ? - GO Y || N DE XAC NHAN CO || KHONG: ")
                        xac_nhan = input()
                        if xac_nhan.lower() == "n":
                            break
                else:
                    print("\n     KHONG THUC HIEN CAP NHAT SACH !!!")
        # THOAT KHOI CHUONG TRINH CAP NHAT SACH
        elif chon == 2:
            break
        # THONG BAO TINH NANG CHO KHONG HOP LE
        else:
            print("\n       TINH NANG CHON KHONG HOP LE !!!")
            print()
            print()

def tim_kiem_sach(sach):
    find = 0

    print("\n ------------------- TIM KIEM THONG TIN CUA SACH --------------------")
    print("|       1. TIM KIEM SACH BANG SO DANG KI                             |")
    print("|       2. TIM KIEM SACH BANG TEN SACH                               |")
    print("|       3. TIM KIEM SACH BANG SO ISBN                                |")
    print(" --------------------------------------------------------------------")
    find = nhap_int()
    # TIM KIEM SACH BANG SO DANG KI
    if find == 1:
        so_dang_ki = 0
        while True:
            print("  1. NHAP SO DANG KI: ")
            so_dang_ki = nhap_int()
            if so_dang_ki == -1:
                print("  SO DANG KI KHONG HOP LE! VUI LONG NHAP LAI!")
            else:
                break
        for i in range(len(sach)):
            if sach[i].lay_so_dang_ki() == so_dang_ki:
                return i
    # TIM KIEM SACH BANG TEN SACH
    elif find == 2:
        ten_sach = ""
        print("     NHAP TEN SACH: ")
        ten_sach = input()
        for i in range(len(sach)):
            if sach[i].lay_ten_sach() == ten_sach:
                return i
    # TIM KIEM SACH BANG SO ISBN
    elif find == 3:
        so_isbn = ""
        print("     NHAP SO ISBN: ")
        so_isbn = input()
        for i in range(len(sach)):
            if sach[i].lay_so_ISBN() == so_isbn:
                return i
    # THONG BAO TINH NANG CHON KHONG HOP LE
    else:
        print("\n       TINH NANG CHON KHONG HOP LE !!!")
    return -1


            
# HAM SAP XEP SACH THEO SO DANG KI (SU DUNG QUICKSORT)
def quickSort_so_dang_ki(sach_sap_xep, l, r):
    if l >= r:
        return

    p = sach_sap_xep[(l + r) // 2].lay_so_dang_ki()
    i = l
    j = r

    while i <= j:
        while sach_sap_xep[i].lay_so_dang_ki() < p:
            i += 1
        while sach_sap_xep[j].lay_so_dang_ki() > p:
            j -= 1
        if i <= j:
            sach_sap_xep[i], sach_sap_xep[j] = sach_sap_xep[j], sach_sap_xep[i]
            i += 1
            j -= 1

    quickSort_so_dang_ki(sach_sap_xep, l, j)
    quickSort_so_dang_ki(sach_sap_xep, i, r)
    
# HAM SAP XEP SACH THEO NXB (SU DUNG QUICKSORT)
def quickSort_nha_xuat_ban(sach_sap_xep, l, r):
    if l >= r:
        return

    p = sach_sap_xep[(l + r) // 2].lay_nha_xuat_ban()
    i = l
    j = r

    while i <= j:
        while sach_sap_xep[i].lay_nha_xuat_ban() < p:
            i += 1
        while sach_sap_xep[j].lay_nha_xuat_ban() > p:
            j -= 1
        if i <= j:
            sach_sap_xep[i], sach_sap_xep[j] = sach_sap_xep[j], sach_sap_xep[i]
            i += 1
            j -= 1

    quickSort_nha_xuat_ban(sach_sap_xep, l, j)
    quickSort_nha_xuat_ban(sach_sap_xep, i, r)

# HAM GOI RA VIEC SAP XEP SACH  
def sap_xep_sach(sach_sap_sep):
    if len(sach_sap_sep) == 0:
        return

    chon = int(input("\n ----------------------------SAP XEP SACH-----------------------------\n"
                     "|      1. SAP XEP THEO SO DANG KI                                     |\n"
                     "|      2. SAP XEP THEO NHA XUAT BAN                                   |\n"
                     " ---------------------------------------------------------------------\n"
                     "\n     CHON KIEU BAN MUON SAP XEP:  "))

    if chon == 1:
        print("\n     SAP XEP THEO SO DANG KI !!!")
        quickSort_so_dang_ki(sach_sap_sep, 0, len(sach_sap_sep) - 1)
        print("\n     KET QUA SAU KHI SAP XEP:\n")
        in_ra_danh_sach_sach(sach_sap_sep)
    elif chon == 2:
        print("\n     SAP XEP THEO NHA XUAT BAN!!!")
        quickSort_nha_xuat_ban(sach_sap_sep, 0, len(sach_sap_sep) - 1)
        print("\n     KET QUA SAU KHI SAP XEP:\n")
        in_ra_danh_sach_sach(sach_sap_sep)
    else:
        print("\n       TINH NANG CHON KHONG HOP LE !!!")
        print()
        print()

# HAM LUU DU LIEU VAO FILE TXT
def luu_du_lieu(file_name, sach):
    try:
        with open(file_name, "w") as output_file:
            for s in sach:
                output_file.write(str(s))
                output_file.write("\n\n")
        print("\n       LUU DU LIEU THANH CONG !!!")

    except IOError:
        print("\n       KHONG THE LUU DU LIEU VAO FILE !!!")  
        
        
if __name__ == '__main__':
    print("CHƯƠNG TRÌNH QUẢN LÝ THƯ VIỆN")
    sach = []

    
    
    while True:
        print("\n ------------------CHON CHUC NANG BAN MUON SU DUNG-------------------\n"
                "|      1. THEM SACH VAO THU VIEN                                     |\n"
                "|      2. CAP NHAT THONG TIN CUA SACH                                |\n"
                "|      3. TIM KIEM THONG TIN SACH                                    |\n"
                "|      4. SAP XEP SACH                                               |\n"
                "|      5. LUU DU LIEU VAO FILE                                       |\n"
                "|      0. KET THUC CHUONG TRINH                                      |\n"
                " --------------------------------------------------------------------")
        print("       SO SACH HIEN TAI TRONG THU VIEN LA:  ", len(sach))
        print("            CHON CHUC NANG: ")

        chuc_nang = nhap_int()

        if chuc_nang == 1:
            them_sach(sach)
        elif chuc_nang == 2:
            cap_nhat_sach(sach)
        elif chuc_nang == 3:
            vi_tri = tim_kiem_sach(sach)
            if vi_tri == -1:
                print("\n     KHONG TIM THAY THONG TIN SACH !!!\n")
            else:
                in_ra_thong_tin_sach(sach[vi_tri])
        elif chuc_nang == 4:
            sach_sap_xep = sach[:]
            sap_xep_sach(sach_sap_xep)
        elif chuc_nang == 5:
            # Gọi hàm để lưu dữ liệu vào file
            luu_du_lieu("du_lieu_thu_vien.txt", sach)
            
        elif chuc_nang == 0:
            print("\n     CAM ON BAN DA SU DUNG CHUONG TRINH. CHUC BAN MOT NGAY TOT LANH ^^")
            break
        
        else:
            print("\n       TINH NANG CHON KHONG HOP LE !!!")
            print()
            print()
