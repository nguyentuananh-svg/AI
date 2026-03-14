import heapq

TrangThaiDich = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 0]]


def TimViTri(TrangThai, GiaTri):
    for i in range(3):
        for j in range(3):
            if TrangThai[i][j] == GiaTri:
                return i, j
    return None

# -------------------------------
# Hàm tính khoảng cách Manhattan (h)

def KhoangCachManhattan(TrangThai):
    tong = 0
    for i in range(3):
        for j in range(3):
            GiaTri = TrangThai[i][j]
            if GiaTri != 0:  # bỏ qua ô trống
                iDich, jDich = TimViTri(TrangThaiDich, GiaTri)
                tong += abs(i - iDich) + abs(j - jDich)
    return tong

# -------------------------------
# Chuyển ma trận sang tuple (để lưu trong set)

def DoiSangTuple(TrangThai):
    return tuple(tuple(hang) for hang in TrangThai)

# -------------------------------
# Sinh các trạng thái hàng xóm (neighbor)

def HangXom(TrangThai):
    KetQua = []
    x, y = TimViTri(TrangThai, 0)
    BuocDi = [(-1,0,"Lên"), (1,0,"Xuống"), (0,-1,"Trái"), (0,1,"Phải")]
    for dx, dy, Huong in BuocDi:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            Moi = [hang[:] for hang in TrangThai]
            Moi[x][y], Moi[nx][ny] = Moi[nx][ny], Moi[x][y]
            KetQua.append((Moi, Huong))
    return KetQua

# -------------------------------
# Thuật toán A*

def ASao(TrangThaiBanDau):
    HangCho = []
    heapq.heappush(HangCho, (KhoangCachManhattan(TrangThaiBanDau), 0, TrangThaiBanDau, []))
    DaXet = set()

    while HangCho:
        f, g, TrangThai, DuongDi = heapq.heappop(HangCho)
        h = KhoangCachManhattan(TrangThai)

        print("g =", g, ", h =", h, ", f =", f)
        for hang in TrangThai:
            print(hang)
        print("-"*20)

        if TrangThai == TrangThaiDich:
            print("✅ Đã tìm thấy trạng thái đích!")
            return DuongDi

        if DoiSangTuple(TrangThai) in DaXet:
            continue
        DaXet.add(DoiSangTuple(TrangThai))

        for Ke, Huong in HangXom(TrangThai):
            gMoi = g + 1
            hMoi = KhoangCachManhattan(Ke)
            fMoi = gMoi + hMoi
            heapq.heappush(HangCho, (fMoi, gMoi, Ke, DuongDi + [(Ke, Huong)]))

# -------------------------------
# Chạy thử

TrangThaiBanDau = [[1, 2, 3],
                   [4, 5, 0],
                   [7, 8, 6]]

LoiGiai = ASao(TrangThaiBanDau)

if LoiGiai:
    for i, (s, Buoc) in enumerate(LoiGiai):
        print(f"Bước {i+1}: Di chuyển {Buoc}")
        for hang in s:
            print(hang)
        print()
else:
    print("Không tìm được lời giải")


