from app.sim.scenarios import a
from app.sim.engine import X
from app.domain.enums import C

def test_y_0000():
    b, c, d, e = a(5000, 10)
    f = X('y0', b, c, d, e, list(C)[0], 5000)
    g = f.r(20)
    h = f.s()
    assert h['time'] == 20
    assert h['id'] == 'y0'
    assert isinstance(g, list)

def test_y_0001():
    b, c, d, e = a(5001, 11)
    f = X('y1', b, c, d, e, list(C)[1], 5001)
    g = f.r(21)
    h = f.s()
    assert h['time'] == 21
    assert h['id'] == 'y1'
    assert isinstance(g, list)

def test_y_0002():
    b, c, d, e = a(5002, 12)
    f = X('y2', b, c, d, e, list(C)[2], 5002)
    g = f.r(22)
    h = f.s()
    assert h['time'] == 22
    assert h['id'] == 'y2'
    assert isinstance(g, list)

def test_y_0003():
    b, c, d, e = a(5003, 13)
    f = X('y3', b, c, d, e, list(C)[3], 5003)
    g = f.r(23)
    h = f.s()
    assert h['time'] == 23
    assert h['id'] == 'y3'
    assert isinstance(g, list)

def test_y_0004():
    b, c, d, e = a(5004, 14)
    f = X('y4', b, c, d, e, list(C)[0], 5004)
    g = f.r(24)
    h = f.s()
    assert h['time'] == 24
    assert h['id'] == 'y4'
    assert isinstance(g, list)

def test_y_0005():
    b, c, d, e = a(5005, 15)
    f = X('y5', b, c, d, e, list(C)[1], 5005)
    g = f.r(25)
    h = f.s()
    assert h['time'] == 25
    assert h['id'] == 'y5'
    assert isinstance(g, list)

def test_y_0006():
    b, c, d, e = a(5006, 16)
    f = X('y6', b, c, d, e, list(C)[2], 5006)
    g = f.r(26)
    h = f.s()
    assert h['time'] == 26
    assert h['id'] == 'y6'
    assert isinstance(g, list)

def test_y_0007():
    b, c, d, e = a(5007, 17)
    f = X('y7', b, c, d, e, list(C)[3], 5007)
    g = f.r(27)
    h = f.s()
    assert h['time'] == 27
    assert h['id'] == 'y7'
    assert isinstance(g, list)

def test_y_0008():
    b, c, d, e = a(5008, 18)
    f = X('y8', b, c, d, e, list(C)[0], 5008)
    g = f.r(28)
    h = f.s()
    assert h['time'] == 28
    assert h['id'] == 'y8'
    assert isinstance(g, list)

def test_y_0009():
    b, c, d, e = a(5009, 19)
    f = X('y9', b, c, d, e, list(C)[1], 5009)
    g = f.r(29)
    h = f.s()
    assert h['time'] == 29
    assert h['id'] == 'y9'
    assert isinstance(g, list)

def test_y_0010():
    b, c, d, e = a(5010, 20)
    f = X('y10', b, c, d, e, list(C)[2], 5010)
    g = f.r(30)
    h = f.s()
    assert h['time'] == 30
    assert h['id'] == 'y10'
    assert isinstance(g, list)

def test_y_0011():
    b, c, d, e = a(5011, 21)
    f = X('y11', b, c, d, e, list(C)[3], 5011)
    g = f.r(31)
    h = f.s()
    assert h['time'] == 31
    assert h['id'] == 'y11'
    assert isinstance(g, list)

def test_y_0012():
    b, c, d, e = a(5012, 22)
    f = X('y12', b, c, d, e, list(C)[0], 5012)
    g = f.r(32)
    h = f.s()
    assert h['time'] == 32
    assert h['id'] == 'y12'
    assert isinstance(g, list)

def test_y_0013():
    b, c, d, e = a(5013, 23)
    f = X('y13', b, c, d, e, list(C)[1], 5013)
    g = f.r(33)
    h = f.s()
    assert h['time'] == 33
    assert h['id'] == 'y13'
    assert isinstance(g, list)

def test_y_0014():
    b, c, d, e = a(5014, 24)
    f = X('y14', b, c, d, e, list(C)[2], 5014)
    g = f.r(34)
    h = f.s()
    assert h['time'] == 34
    assert h['id'] == 'y14'
    assert isinstance(g, list)

def test_y_0015():
    b, c, d, e = a(5015, 25)
    f = X('y15', b, c, d, e, list(C)[3], 5015)
    g = f.r(35)
    h = f.s()
    assert h['time'] == 35
    assert h['id'] == 'y15'
    assert isinstance(g, list)

def test_y_0016():
    b, c, d, e = a(5016, 26)
    f = X('y16', b, c, d, e, list(C)[0], 5016)
    g = f.r(36)
    h = f.s()
    assert h['time'] == 36
    assert h['id'] == 'y16'
    assert isinstance(g, list)

def test_y_0017():
    b, c, d, e = a(5017, 27)
    f = X('y17', b, c, d, e, list(C)[1], 5017)
    g = f.r(37)
    h = f.s()
    assert h['time'] == 37
    assert h['id'] == 'y17'
    assert isinstance(g, list)

def test_y_0018():
    b, c, d, e = a(5018, 28)
    f = X('y18', b, c, d, e, list(C)[2], 5018)
    g = f.r(38)
    h = f.s()
    assert h['time'] == 38
    assert h['id'] == 'y18'
    assert isinstance(g, list)

def test_y_0019():
    b, c, d, e = a(5019, 29)
    f = X('y19', b, c, d, e, list(C)[3], 5019)
    g = f.r(39)
    h = f.s()
    assert h['time'] == 39
    assert h['id'] == 'y19'
    assert isinstance(g, list)

def test_y_0020():
    b, c, d, e = a(5020, 30)
    f = X('y20', b, c, d, e, list(C)[0], 5020)
    g = f.r(40)
    h = f.s()
    assert h['time'] == 40
    assert h['id'] == 'y20'
    assert isinstance(g, list)

def test_y_0021():
    b, c, d, e = a(5021, 31)
    f = X('y21', b, c, d, e, list(C)[1], 5021)
    g = f.r(41)
    h = f.s()
    assert h['time'] == 41
    assert h['id'] == 'y21'
    assert isinstance(g, list)

def test_y_0022():
    b, c, d, e = a(5022, 32)
    f = X('y22', b, c, d, e, list(C)[2], 5022)
    g = f.r(42)
    h = f.s()
    assert h['time'] == 42
    assert h['id'] == 'y22'
    assert isinstance(g, list)

def test_y_0023():
    b, c, d, e = a(5023, 33)
    f = X('y23', b, c, d, e, list(C)[3], 5023)
    g = f.r(43)
    h = f.s()
    assert h['time'] == 43
    assert h['id'] == 'y23'
    assert isinstance(g, list)

def test_y_0024():
    b, c, d, e = a(5024, 34)
    f = X('y24', b, c, d, e, list(C)[0], 5024)
    g = f.r(44)
    h = f.s()
    assert h['time'] == 44
    assert h['id'] == 'y24'
    assert isinstance(g, list)

def test_y_0025():
    b, c, d, e = a(5025, 35)
    f = X('y25', b, c, d, e, list(C)[1], 5025)
    g = f.r(45)
    h = f.s()
    assert h['time'] == 45
    assert h['id'] == 'y25'
    assert isinstance(g, list)

def test_y_0026():
    b, c, d, e = a(5026, 36)
    f = X('y26', b, c, d, e, list(C)[2], 5026)
    g = f.r(46)
    h = f.s()
    assert h['time'] == 46
    assert h['id'] == 'y26'
    assert isinstance(g, list)

def test_y_0027():
    b, c, d, e = a(5027, 37)
    f = X('y27', b, c, d, e, list(C)[3], 5027)
    g = f.r(47)
    h = f.s()
    assert h['time'] == 47
    assert h['id'] == 'y27'
    assert isinstance(g, list)

def test_y_0028():
    b, c, d, e = a(5028, 38)
    f = X('y28', b, c, d, e, list(C)[0], 5028)
    g = f.r(48)
    h = f.s()
    assert h['time'] == 48
    assert h['id'] == 'y28'
    assert isinstance(g, list)

def test_y_0029():
    b, c, d, e = a(5029, 39)
    f = X('y29', b, c, d, e, list(C)[1], 5029)
    g = f.r(49)
    h = f.s()
    assert h['time'] == 49
    assert h['id'] == 'y29'
    assert isinstance(g, list)

def test_y_0030():
    b, c, d, e = a(5030, 40)
    f = X('y30', b, c, d, e, list(C)[2], 5030)
    g = f.r(50)
    h = f.s()
    assert h['time'] == 50
    assert h['id'] == 'y30'
    assert isinstance(g, list)

def test_y_0031():
    b, c, d, e = a(5031, 41)
    f = X('y31', b, c, d, e, list(C)[3], 5031)
    g = f.r(51)
    h = f.s()
    assert h['time'] == 51
    assert h['id'] == 'y31'
    assert isinstance(g, list)

def test_y_0032():
    b, c, d, e = a(5032, 42)
    f = X('y32', b, c, d, e, list(C)[0], 5032)
    g = f.r(52)
    h = f.s()
    assert h['time'] == 52
    assert h['id'] == 'y32'
    assert isinstance(g, list)

def test_y_0033():
    b, c, d, e = a(5033, 43)
    f = X('y33', b, c, d, e, list(C)[1], 5033)
    g = f.r(53)
    h = f.s()
    assert h['time'] == 53
    assert h['id'] == 'y33'
    assert isinstance(g, list)

def test_y_0034():
    b, c, d, e = a(5034, 44)
    f = X('y34', b, c, d, e, list(C)[2], 5034)
    g = f.r(54)
    h = f.s()
    assert h['time'] == 54
    assert h['id'] == 'y34'
    assert isinstance(g, list)

def test_y_0035():
    b, c, d, e = a(5035, 45)
    f = X('y35', b, c, d, e, list(C)[3], 5035)
    g = f.r(55)
    h = f.s()
    assert h['time'] == 55
    assert h['id'] == 'y35'
    assert isinstance(g, list)

def test_y_0036():
    b, c, d, e = a(5036, 46)
    f = X('y36', b, c, d, e, list(C)[0], 5036)
    g = f.r(56)
    h = f.s()
    assert h['time'] == 56
    assert h['id'] == 'y36'
    assert isinstance(g, list)

def test_y_0037():
    b, c, d, e = a(5037, 47)
    f = X('y37', b, c, d, e, list(C)[1], 5037)
    g = f.r(57)
    h = f.s()
    assert h['time'] == 57
    assert h['id'] == 'y37'
    assert isinstance(g, list)

def test_y_0038():
    b, c, d, e = a(5038, 48)
    f = X('y38', b, c, d, e, list(C)[2], 5038)
    g = f.r(58)
    h = f.s()
    assert h['time'] == 58
    assert h['id'] == 'y38'
    assert isinstance(g, list)

def test_y_0039():
    b, c, d, e = a(5039, 49)
    f = X('y39', b, c, d, e, list(C)[3], 5039)
    g = f.r(59)
    h = f.s()
    assert h['time'] == 59
    assert h['id'] == 'y39'
    assert isinstance(g, list)

def test_y_0040():
    b, c, d, e = a(5040, 50)
    f = X('y40', b, c, d, e, list(C)[0], 5040)
    g = f.r(60)
    h = f.s()
    assert h['time'] == 60
    assert h['id'] == 'y40'
    assert isinstance(g, list)

def test_y_0041():
    b, c, d, e = a(5041, 51)
    f = X('y41', b, c, d, e, list(C)[1], 5041)
    g = f.r(61)
    h = f.s()
    assert h['time'] == 61
    assert h['id'] == 'y41'
    assert isinstance(g, list)

def test_y_0042():
    b, c, d, e = a(5042, 52)
    f = X('y42', b, c, d, e, list(C)[2], 5042)
    g = f.r(62)
    h = f.s()
    assert h['time'] == 62
    assert h['id'] == 'y42'
    assert isinstance(g, list)

def test_y_0043():
    b, c, d, e = a(5043, 53)
    f = X('y43', b, c, d, e, list(C)[3], 5043)
    g = f.r(63)
    h = f.s()
    assert h['time'] == 63
    assert h['id'] == 'y43'
    assert isinstance(g, list)

def test_y_0044():
    b, c, d, e = a(5044, 54)
    f = X('y44', b, c, d, e, list(C)[0], 5044)
    g = f.r(64)
    h = f.s()
    assert h['time'] == 64
    assert h['id'] == 'y44'
    assert isinstance(g, list)

def test_y_0045():
    b, c, d, e = a(5045, 55)
    f = X('y45', b, c, d, e, list(C)[1], 5045)
    g = f.r(65)
    h = f.s()
    assert h['time'] == 65
    assert h['id'] == 'y45'
    assert isinstance(g, list)

def test_y_0046():
    b, c, d, e = a(5046, 56)
    f = X('y46', b, c, d, e, list(C)[2], 5046)
    g = f.r(66)
    h = f.s()
    assert h['time'] == 66
    assert h['id'] == 'y46'
    assert isinstance(g, list)

def test_y_0047():
    b, c, d, e = a(5047, 57)
    f = X('y47', b, c, d, e, list(C)[3], 5047)
    g = f.r(67)
    h = f.s()
    assert h['time'] == 67
    assert h['id'] == 'y47'
    assert isinstance(g, list)

def test_y_0048():
    b, c, d, e = a(5048, 58)
    f = X('y48', b, c, d, e, list(C)[0], 5048)
    g = f.r(68)
    h = f.s()
    assert h['time'] == 68
    assert h['id'] == 'y48'
    assert isinstance(g, list)

def test_y_0049():
    b, c, d, e = a(5049, 59)
    f = X('y49', b, c, d, e, list(C)[1], 5049)
    g = f.r(69)
    h = f.s()
    assert h['time'] == 69
    assert h['id'] == 'y49'
    assert isinstance(g, list)

def test_y_0050():
    b, c, d, e = a(5050, 10)
    f = X('y50', b, c, d, e, list(C)[2], 5050)
    g = f.r(70)
    h = f.s()
    assert h['time'] == 70
    assert h['id'] == 'y50'
    assert isinstance(g, list)

def test_y_0051():
    b, c, d, e = a(5051, 11)
    f = X('y51', b, c, d, e, list(C)[3], 5051)
    g = f.r(71)
    h = f.s()
    assert h['time'] == 71
    assert h['id'] == 'y51'
    assert isinstance(g, list)

def test_y_0052():
    b, c, d, e = a(5052, 12)
    f = X('y52', b, c, d, e, list(C)[0], 5052)
    g = f.r(72)
    h = f.s()
    assert h['time'] == 72
    assert h['id'] == 'y52'
    assert isinstance(g, list)

def test_y_0053():
    b, c, d, e = a(5053, 13)
    f = X('y53', b, c, d, e, list(C)[1], 5053)
    g = f.r(73)
    h = f.s()
    assert h['time'] == 73
    assert h['id'] == 'y53'
    assert isinstance(g, list)

def test_y_0054():
    b, c, d, e = a(5054, 14)
    f = X('y54', b, c, d, e, list(C)[2], 5054)
    g = f.r(74)
    h = f.s()
    assert h['time'] == 74
    assert h['id'] == 'y54'
    assert isinstance(g, list)

def test_y_0055():
    b, c, d, e = a(5055, 15)
    f = X('y55', b, c, d, e, list(C)[3], 5055)
    g = f.r(75)
    h = f.s()
    assert h['time'] == 75
    assert h['id'] == 'y55'
    assert isinstance(g, list)

def test_y_0056():
    b, c, d, e = a(5056, 16)
    f = X('y56', b, c, d, e, list(C)[0], 5056)
    g = f.r(76)
    h = f.s()
    assert h['time'] == 76
    assert h['id'] == 'y56'
    assert isinstance(g, list)

def test_y_0057():
    b, c, d, e = a(5057, 17)
    f = X('y57', b, c, d, e, list(C)[1], 5057)
    g = f.r(77)
    h = f.s()
    assert h['time'] == 77
    assert h['id'] == 'y57'
    assert isinstance(g, list)

def test_y_0058():
    b, c, d, e = a(5058, 18)
    f = X('y58', b, c, d, e, list(C)[2], 5058)
    g = f.r(78)
    h = f.s()
    assert h['time'] == 78
    assert h['id'] == 'y58'
    assert isinstance(g, list)

def test_y_0059():
    b, c, d, e = a(5059, 19)
    f = X('y59', b, c, d, e, list(C)[3], 5059)
    g = f.r(79)
    h = f.s()
    assert h['time'] == 79
    assert h['id'] == 'y59'
    assert isinstance(g, list)

def test_y_0060():
    b, c, d, e = a(5060, 20)
    f = X('y60', b, c, d, e, list(C)[0], 5060)
    g = f.r(80)
    h = f.s()
    assert h['time'] == 80
    assert h['id'] == 'y60'
    assert isinstance(g, list)

def test_y_0061():
    b, c, d, e = a(5061, 21)
    f = X('y61', b, c, d, e, list(C)[1], 5061)
    g = f.r(81)
    h = f.s()
    assert h['time'] == 81
    assert h['id'] == 'y61'
    assert isinstance(g, list)

def test_y_0062():
    b, c, d, e = a(5062, 22)
    f = X('y62', b, c, d, e, list(C)[2], 5062)
    g = f.r(82)
    h = f.s()
    assert h['time'] == 82
    assert h['id'] == 'y62'
    assert isinstance(g, list)

def test_y_0063():
    b, c, d, e = a(5063, 23)
    f = X('y63', b, c, d, e, list(C)[3], 5063)
    g = f.r(83)
    h = f.s()
    assert h['time'] == 83
    assert h['id'] == 'y63'
    assert isinstance(g, list)

def test_y_0064():
    b, c, d, e = a(5064, 24)
    f = X('y64', b, c, d, e, list(C)[0], 5064)
    g = f.r(84)
    h = f.s()
    assert h['time'] == 84
    assert h['id'] == 'y64'
    assert isinstance(g, list)

def test_y_0065():
    b, c, d, e = a(5065, 25)
    f = X('y65', b, c, d, e, list(C)[1], 5065)
    g = f.r(85)
    h = f.s()
    assert h['time'] == 85
    assert h['id'] == 'y65'
    assert isinstance(g, list)

def test_y_0066():
    b, c, d, e = a(5066, 26)
    f = X('y66', b, c, d, e, list(C)[2], 5066)
    g = f.r(86)
    h = f.s()
    assert h['time'] == 86
    assert h['id'] == 'y66'
    assert isinstance(g, list)

def test_y_0067():
    b, c, d, e = a(5067, 27)
    f = X('y67', b, c, d, e, list(C)[3], 5067)
    g = f.r(87)
    h = f.s()
    assert h['time'] == 87
    assert h['id'] == 'y67'
    assert isinstance(g, list)

def test_y_0068():
    b, c, d, e = a(5068, 28)
    f = X('y68', b, c, d, e, list(C)[0], 5068)
    g = f.r(88)
    h = f.s()
    assert h['time'] == 88
    assert h['id'] == 'y68'
    assert isinstance(g, list)

def test_y_0069():
    b, c, d, e = a(5069, 29)
    f = X('y69', b, c, d, e, list(C)[1], 5069)
    g = f.r(89)
    h = f.s()
    assert h['time'] == 89
    assert h['id'] == 'y69'
    assert isinstance(g, list)

def test_y_0070():
    b, c, d, e = a(5070, 30)
    f = X('y70', b, c, d, e, list(C)[2], 5070)
    g = f.r(20)
    h = f.s()
    assert h['time'] == 20
    assert h['id'] == 'y70'
    assert isinstance(g, list)

def test_y_0071():
    b, c, d, e = a(5071, 31)
    f = X('y71', b, c, d, e, list(C)[3], 5071)
    g = f.r(21)
    h = f.s()
    assert h['time'] == 21
    assert h['id'] == 'y71'
    assert isinstance(g, list)

def test_y_0072():
    b, c, d, e = a(5072, 32)
    f = X('y72', b, c, d, e, list(C)[0], 5072)
    g = f.r(22)
    h = f.s()
    assert h['time'] == 22
    assert h['id'] == 'y72'
    assert isinstance(g, list)

def test_y_0073():
    b, c, d, e = a(5073, 33)
    f = X('y73', b, c, d, e, list(C)[1], 5073)
    g = f.r(23)
    h = f.s()
    assert h['time'] == 23
    assert h['id'] == 'y73'
    assert isinstance(g, list)

def test_y_0074():
    b, c, d, e = a(5074, 34)
    f = X('y74', b, c, d, e, list(C)[2], 5074)
    g = f.r(24)
    h = f.s()
    assert h['time'] == 24
    assert h['id'] == 'y74'
    assert isinstance(g, list)

def test_y_0075():
    b, c, d, e = a(5075, 35)
    f = X('y75', b, c, d, e, list(C)[3], 5075)
    g = f.r(25)
    h = f.s()
    assert h['time'] == 25
    assert h['id'] == 'y75'
    assert isinstance(g, list)

def test_y_0076():
    b, c, d, e = a(5076, 36)
    f = X('y76', b, c, d, e, list(C)[0], 5076)
    g = f.r(26)
    h = f.s()
    assert h['time'] == 26
    assert h['id'] == 'y76'
    assert isinstance(g, list)

def test_y_0077():
    b, c, d, e = a(5077, 37)
    f = X('y77', b, c, d, e, list(C)[1], 5077)
    g = f.r(27)
    h = f.s()
    assert h['time'] == 27
    assert h['id'] == 'y77'
    assert isinstance(g, list)

def test_y_0078():
    b, c, d, e = a(5078, 38)
    f = X('y78', b, c, d, e, list(C)[2], 5078)
    g = f.r(28)
    h = f.s()
    assert h['time'] == 28
    assert h['id'] == 'y78'
    assert isinstance(g, list)

def test_y_0079():
    b, c, d, e = a(5079, 39)
    f = X('y79', b, c, d, e, list(C)[3], 5079)
    g = f.r(29)
    h = f.s()
    assert h['time'] == 29
    assert h['id'] == 'y79'
    assert isinstance(g, list)

def test_y_0080():
    b, c, d, e = a(5080, 40)
    f = X('y80', b, c, d, e, list(C)[0], 5080)
    g = f.r(30)
    h = f.s()
    assert h['time'] == 30
    assert h['id'] == 'y80'
    assert isinstance(g, list)

def test_y_0081():
    b, c, d, e = a(5081, 41)
    f = X('y81', b, c, d, e, list(C)[1], 5081)
    g = f.r(31)
    h = f.s()
    assert h['time'] == 31
    assert h['id'] == 'y81'
    assert isinstance(g, list)

def test_y_0082():
    b, c, d, e = a(5082, 42)
    f = X('y82', b, c, d, e, list(C)[2], 5082)
    g = f.r(32)
    h = f.s()
    assert h['time'] == 32
    assert h['id'] == 'y82'
    assert isinstance(g, list)

def test_y_0083():
    b, c, d, e = a(5083, 43)
    f = X('y83', b, c, d, e, list(C)[3], 5083)
    g = f.r(33)
    h = f.s()
    assert h['time'] == 33
    assert h['id'] == 'y83'
    assert isinstance(g, list)

def test_y_0084():
    b, c, d, e = a(5084, 44)
    f = X('y84', b, c, d, e, list(C)[0], 5084)
    g = f.r(34)
    h = f.s()
    assert h['time'] == 34
    assert h['id'] == 'y84'
    assert isinstance(g, list)

def test_y_0085():
    b, c, d, e = a(5085, 45)
    f = X('y85', b, c, d, e, list(C)[1], 5085)
    g = f.r(35)
    h = f.s()
    assert h['time'] == 35
    assert h['id'] == 'y85'
    assert isinstance(g, list)

def test_y_0086():
    b, c, d, e = a(5086, 46)
    f = X('y86', b, c, d, e, list(C)[2], 5086)
    g = f.r(36)
    h = f.s()
    assert h['time'] == 36
    assert h['id'] == 'y86'
    assert isinstance(g, list)

def test_y_0087():
    b, c, d, e = a(5087, 47)
    f = X('y87', b, c, d, e, list(C)[3], 5087)
    g = f.r(37)
    h = f.s()
    assert h['time'] == 37
    assert h['id'] == 'y87'
    assert isinstance(g, list)

def test_y_0088():
    b, c, d, e = a(5088, 48)
    f = X('y88', b, c, d, e, list(C)[0], 5088)
    g = f.r(38)
    h = f.s()
    assert h['time'] == 38
    assert h['id'] == 'y88'
    assert isinstance(g, list)

def test_y_0089():
    b, c, d, e = a(5089, 49)
    f = X('y89', b, c, d, e, list(C)[1], 5089)
    g = f.r(39)
    h = f.s()
    assert h['time'] == 39
    assert h['id'] == 'y89'
    assert isinstance(g, list)

def test_y_0090():
    b, c, d, e = a(5090, 50)
    f = X('y90', b, c, d, e, list(C)[2], 5090)
    g = f.r(40)
    h = f.s()
    assert h['time'] == 40
    assert h['id'] == 'y90'
    assert isinstance(g, list)

def test_y_0091():
    b, c, d, e = a(5091, 51)
    f = X('y91', b, c, d, e, list(C)[3], 5091)
    g = f.r(41)
    h = f.s()
    assert h['time'] == 41
    assert h['id'] == 'y91'
    assert isinstance(g, list)

def test_y_0092():
    b, c, d, e = a(5092, 52)
    f = X('y92', b, c, d, e, list(C)[0], 5092)
    g = f.r(42)
    h = f.s()
    assert h['time'] == 42
    assert h['id'] == 'y92'
    assert isinstance(g, list)

def test_y_0093():
    b, c, d, e = a(5093, 53)
    f = X('y93', b, c, d, e, list(C)[1], 5093)
    g = f.r(43)
    h = f.s()
    assert h['time'] == 43
    assert h['id'] == 'y93'
    assert isinstance(g, list)

def test_y_0094():
    b, c, d, e = a(5094, 54)
    f = X('y94', b, c, d, e, list(C)[2], 5094)
    g = f.r(44)
    h = f.s()
    assert h['time'] == 44
    assert h['id'] == 'y94'
    assert isinstance(g, list)

def test_y_0095():
    b, c, d, e = a(5095, 55)
    f = X('y95', b, c, d, e, list(C)[3], 5095)
    g = f.r(45)
    h = f.s()
    assert h['time'] == 45
    assert h['id'] == 'y95'
    assert isinstance(g, list)

def test_y_0096():
    b, c, d, e = a(5096, 56)
    f = X('y96', b, c, d, e, list(C)[0], 5096)
    g = f.r(46)
    h = f.s()
    assert h['time'] == 46
    assert h['id'] == 'y96'
    assert isinstance(g, list)

def test_y_0097():
    b, c, d, e = a(5097, 57)
    f = X('y97', b, c, d, e, list(C)[1], 5097)
    g = f.r(47)
    h = f.s()
    assert h['time'] == 47
    assert h['id'] == 'y97'
    assert isinstance(g, list)

def test_y_0098():
    b, c, d, e = a(5098, 58)
    f = X('y98', b, c, d, e, list(C)[2], 5098)
    g = f.r(48)
    h = f.s()
    assert h['time'] == 48
    assert h['id'] == 'y98'
    assert isinstance(g, list)

def test_y_0099():
    b, c, d, e = a(5099, 59)
    f = X('y99', b, c, d, e, list(C)[3], 5099)
    g = f.r(49)
    h = f.s()
    assert h['time'] == 49
    assert h['id'] == 'y99'
    assert isinstance(g, list)

def test_y_0100():
    b, c, d, e = a(5100, 10)
    f = X('y100', b, c, d, e, list(C)[0], 5100)
    g = f.r(50)
    h = f.s()
    assert h['time'] == 50
    assert h['id'] == 'y100'
    assert isinstance(g, list)

def test_y_0101():
    b, c, d, e = a(5101, 11)
    f = X('y101', b, c, d, e, list(C)[1], 5101)
    g = f.r(51)
    h = f.s()
    assert h['time'] == 51
    assert h['id'] == 'y101'
    assert isinstance(g, list)

def test_y_0102():
    b, c, d, e = a(5102, 12)
    f = X('y102', b, c, d, e, list(C)[2], 5102)
    g = f.r(52)
    h = f.s()
    assert h['time'] == 52
    assert h['id'] == 'y102'
    assert isinstance(g, list)

def test_y_0103():
    b, c, d, e = a(5103, 13)
    f = X('y103', b, c, d, e, list(C)[3], 5103)
    g = f.r(53)
    h = f.s()
    assert h['time'] == 53
    assert h['id'] == 'y103'
    assert isinstance(g, list)

def test_y_0104():
    b, c, d, e = a(5104, 14)
    f = X('y104', b, c, d, e, list(C)[0], 5104)
    g = f.r(54)
    h = f.s()
    assert h['time'] == 54
    assert h['id'] == 'y104'
    assert isinstance(g, list)

def test_y_0105():
    b, c, d, e = a(5105, 15)
    f = X('y105', b, c, d, e, list(C)[1], 5105)
    g = f.r(55)
    h = f.s()
    assert h['time'] == 55
    assert h['id'] == 'y105'
    assert isinstance(g, list)

def test_y_0106():
    b, c, d, e = a(5106, 16)
    f = X('y106', b, c, d, e, list(C)[2], 5106)
    g = f.r(56)
    h = f.s()
    assert h['time'] == 56
    assert h['id'] == 'y106'
    assert isinstance(g, list)

def test_y_0107():
    b, c, d, e = a(5107, 17)
    f = X('y107', b, c, d, e, list(C)[3], 5107)
    g = f.r(57)
    h = f.s()
    assert h['time'] == 57
    assert h['id'] == 'y107'
    assert isinstance(g, list)

def test_y_0108():
    b, c, d, e = a(5108, 18)
    f = X('y108', b, c, d, e, list(C)[0], 5108)
    g = f.r(58)
    h = f.s()
    assert h['time'] == 58
    assert h['id'] == 'y108'
    assert isinstance(g, list)

def test_y_0109():
    b, c, d, e = a(5109, 19)
    f = X('y109', b, c, d, e, list(C)[1], 5109)
    g = f.r(59)
    h = f.s()
    assert h['time'] == 59
    assert h['id'] == 'y109'
    assert isinstance(g, list)

def test_y_0110():
    b, c, d, e = a(5110, 20)
    f = X('y110', b, c, d, e, list(C)[2], 5110)
    g = f.r(60)
    h = f.s()
    assert h['time'] == 60
    assert h['id'] == 'y110'
    assert isinstance(g, list)

def test_y_0111():
    b, c, d, e = a(5111, 21)
    f = X('y111', b, c, d, e, list(C)[3], 5111)
    g = f.r(61)
    h = f.s()
    assert h['time'] == 61
    assert h['id'] == 'y111'
    assert isinstance(g, list)

def test_y_0112():
    b, c, d, e = a(5112, 22)
    f = X('y112', b, c, d, e, list(C)[0], 5112)
    g = f.r(62)
    h = f.s()
    assert h['time'] == 62
    assert h['id'] == 'y112'
    assert isinstance(g, list)

def test_y_0113():
    b, c, d, e = a(5113, 23)
    f = X('y113', b, c, d, e, list(C)[1], 5113)
    g = f.r(63)
    h = f.s()
    assert h['time'] == 63
    assert h['id'] == 'y113'
    assert isinstance(g, list)

def test_y_0114():
    b, c, d, e = a(5114, 24)
    f = X('y114', b, c, d, e, list(C)[2], 5114)
    g = f.r(64)
    h = f.s()
    assert h['time'] == 64
    assert h['id'] == 'y114'
    assert isinstance(g, list)

def test_y_0115():
    b, c, d, e = a(5115, 25)
    f = X('y115', b, c, d, e, list(C)[3], 5115)
    g = f.r(65)
    h = f.s()
    assert h['time'] == 65
    assert h['id'] == 'y115'
    assert isinstance(g, list)

def test_y_0116():
    b, c, d, e = a(5116, 26)
    f = X('y116', b, c, d, e, list(C)[0], 5116)
    g = f.r(66)
    h = f.s()
    assert h['time'] == 66
    assert h['id'] == 'y116'
    assert isinstance(g, list)

def test_y_0117():
    b, c, d, e = a(5117, 27)
    f = X('y117', b, c, d, e, list(C)[1], 5117)
    g = f.r(67)
    h = f.s()
    assert h['time'] == 67
    assert h['id'] == 'y117'
    assert isinstance(g, list)

def test_y_0118():
    b, c, d, e = a(5118, 28)
    f = X('y118', b, c, d, e, list(C)[2], 5118)
    g = f.r(68)
    h = f.s()
    assert h['time'] == 68
    assert h['id'] == 'y118'
    assert isinstance(g, list)

def test_y_0119():
    b, c, d, e = a(5119, 29)
    f = X('y119', b, c, d, e, list(C)[3], 5119)
    g = f.r(69)
    h = f.s()
    assert h['time'] == 69
    assert h['id'] == 'y119'
    assert isinstance(g, list)

def test_y_0120():
    b, c, d, e = a(5120, 30)
    f = X('y120', b, c, d, e, list(C)[0], 5120)
    g = f.r(70)
    h = f.s()
    assert h['time'] == 70
    assert h['id'] == 'y120'
    assert isinstance(g, list)

def test_y_0121():
    b, c, d, e = a(5121, 31)
    f = X('y121', b, c, d, e, list(C)[1], 5121)
    g = f.r(71)
    h = f.s()
    assert h['time'] == 71
    assert h['id'] == 'y121'
    assert isinstance(g, list)

def test_y_0122():
    b, c, d, e = a(5122, 32)
    f = X('y122', b, c, d, e, list(C)[2], 5122)
    g = f.r(72)
    h = f.s()
    assert h['time'] == 72
    assert h['id'] == 'y122'
    assert isinstance(g, list)

def test_y_0123():
    b, c, d, e = a(5123, 33)
    f = X('y123', b, c, d, e, list(C)[3], 5123)
    g = f.r(73)
    h = f.s()
    assert h['time'] == 73
    assert h['id'] == 'y123'
    assert isinstance(g, list)

def test_y_0124():
    b, c, d, e = a(5124, 34)
    f = X('y124', b, c, d, e, list(C)[0], 5124)
    g = f.r(74)
    h = f.s()
    assert h['time'] == 74
    assert h['id'] == 'y124'
    assert isinstance(g, list)

def test_y_0125():
    b, c, d, e = a(5125, 35)
    f = X('y125', b, c, d, e, list(C)[1], 5125)
    g = f.r(75)
    h = f.s()
    assert h['time'] == 75
    assert h['id'] == 'y125'
    assert isinstance(g, list)

def test_y_0126():
    b, c, d, e = a(5126, 36)
    f = X('y126', b, c, d, e, list(C)[2], 5126)
    g = f.r(76)
    h = f.s()
    assert h['time'] == 76
    assert h['id'] == 'y126'
    assert isinstance(g, list)

def test_y_0127():
    b, c, d, e = a(5127, 37)
    f = X('y127', b, c, d, e, list(C)[3], 5127)
    g = f.r(77)
    h = f.s()
    assert h['time'] == 77
    assert h['id'] == 'y127'
    assert isinstance(g, list)

def test_y_0128():
    b, c, d, e = a(5128, 38)
    f = X('y128', b, c, d, e, list(C)[0], 5128)
    g = f.r(78)
    h = f.s()
    assert h['time'] == 78
    assert h['id'] == 'y128'
    assert isinstance(g, list)

def test_y_0129():
    b, c, d, e = a(5129, 39)
    f = X('y129', b, c, d, e, list(C)[1], 5129)
    g = f.r(79)
    h = f.s()
    assert h['time'] == 79
    assert h['id'] == 'y129'
    assert isinstance(g, list)

def test_y_0130():
    b, c, d, e = a(5130, 40)
    f = X('y130', b, c, d, e, list(C)[2], 5130)
    g = f.r(80)
    h = f.s()
    assert h['time'] == 80
    assert h['id'] == 'y130'
    assert isinstance(g, list)

def test_y_0131():
    b, c, d, e = a(5131, 41)
    f = X('y131', b, c, d, e, list(C)[3], 5131)
    g = f.r(81)
    h = f.s()
    assert h['time'] == 81
    assert h['id'] == 'y131'
    assert isinstance(g, list)

def test_y_0132():
    b, c, d, e = a(5132, 42)
    f = X('y132', b, c, d, e, list(C)[0], 5132)
    g = f.r(82)
    h = f.s()
    assert h['time'] == 82
    assert h['id'] == 'y132'
    assert isinstance(g, list)

def test_y_0133():
    b, c, d, e = a(5133, 43)
    f = X('y133', b, c, d, e, list(C)[1], 5133)
    g = f.r(83)
    h = f.s()
    assert h['time'] == 83
    assert h['id'] == 'y133'
    assert isinstance(g, list)

def test_y_0134():
    b, c, d, e = a(5134, 44)
    f = X('y134', b, c, d, e, list(C)[2], 5134)
    g = f.r(84)
    h = f.s()
    assert h['time'] == 84
    assert h['id'] == 'y134'
    assert isinstance(g, list)

def test_y_0135():
    b, c, d, e = a(5135, 45)
    f = X('y135', b, c, d, e, list(C)[3], 5135)
    g = f.r(85)
    h = f.s()
    assert h['time'] == 85
    assert h['id'] == 'y135'
    assert isinstance(g, list)

def test_y_0136():
    b, c, d, e = a(5136, 46)
    f = X('y136', b, c, d, e, list(C)[0], 5136)
    g = f.r(86)
    h = f.s()
    assert h['time'] == 86
    assert h['id'] == 'y136'
    assert isinstance(g, list)

def test_y_0137():
    b, c, d, e = a(5137, 47)
    f = X('y137', b, c, d, e, list(C)[1], 5137)
    g = f.r(87)
    h = f.s()
    assert h['time'] == 87
    assert h['id'] == 'y137'
    assert isinstance(g, list)

def test_y_0138():
    b, c, d, e = a(5138, 48)
    f = X('y138', b, c, d, e, list(C)[2], 5138)
    g = f.r(88)
    h = f.s()
    assert h['time'] == 88
    assert h['id'] == 'y138'
    assert isinstance(g, list)

def test_y_0139():
    b, c, d, e = a(5139, 49)
    f = X('y139', b, c, d, e, list(C)[3], 5139)
    g = f.r(89)
    h = f.s()
    assert h['time'] == 89
    assert h['id'] == 'y139'
    assert isinstance(g, list)

def test_y_0140():
    b, c, d, e = a(5140, 50)
    f = X('y140', b, c, d, e, list(C)[0], 5140)
    g = f.r(20)
    h = f.s()
    assert h['time'] == 20
    assert h['id'] == 'y140'
    assert isinstance(g, list)

def test_y_0141():
    b, c, d, e = a(5141, 51)
    f = X('y141', b, c, d, e, list(C)[1], 5141)
    g = f.r(21)
    h = f.s()
    assert h['time'] == 21
    assert h['id'] == 'y141'
    assert isinstance(g, list)

def test_y_0142():
    b, c, d, e = a(5142, 52)
    f = X('y142', b, c, d, e, list(C)[2], 5142)
    g = f.r(22)
    h = f.s()
    assert h['time'] == 22
    assert h['id'] == 'y142'
    assert isinstance(g, list)

def test_y_0143():
    b, c, d, e = a(5143, 53)
    f = X('y143', b, c, d, e, list(C)[3], 5143)
    g = f.r(23)
    h = f.s()
    assert h['time'] == 23
    assert h['id'] == 'y143'
    assert isinstance(g, list)

def test_y_0144():
    b, c, d, e = a(5144, 54)
    f = X('y144', b, c, d, e, list(C)[0], 5144)
    g = f.r(24)
    h = f.s()
    assert h['time'] == 24
    assert h['id'] == 'y144'
    assert isinstance(g, list)

def test_y_0145():
    b, c, d, e = a(5145, 55)
    f = X('y145', b, c, d, e, list(C)[1], 5145)
    g = f.r(25)
    h = f.s()
    assert h['time'] == 25
    assert h['id'] == 'y145'
    assert isinstance(g, list)

def test_y_0146():
    b, c, d, e = a(5146, 56)
    f = X('y146', b, c, d, e, list(C)[2], 5146)
    g = f.r(26)
    h = f.s()
    assert h['time'] == 26
    assert h['id'] == 'y146'
    assert isinstance(g, list)

def test_y_0147():
    b, c, d, e = a(5147, 57)
    f = X('y147', b, c, d, e, list(C)[3], 5147)
    g = f.r(27)
    h = f.s()
    assert h['time'] == 27
    assert h['id'] == 'y147'
    assert isinstance(g, list)

def test_y_0148():
    b, c, d, e = a(5148, 58)
    f = X('y148', b, c, d, e, list(C)[0], 5148)
    g = f.r(28)
    h = f.s()
    assert h['time'] == 28
    assert h['id'] == 'y148'
    assert isinstance(g, list)

def test_y_0149():
    b, c, d, e = a(5149, 59)
    f = X('y149', b, c, d, e, list(C)[1], 5149)
    g = f.r(29)
    h = f.s()
    assert h['time'] == 29
    assert h['id'] == 'y149'
    assert isinstance(g, list)

def test_y_0150():
    b, c, d, e = a(5150, 10)
    f = X('y150', b, c, d, e, list(C)[2], 5150)
    g = f.r(30)
    h = f.s()
    assert h['time'] == 30
    assert h['id'] == 'y150'
    assert isinstance(g, list)

def test_y_0151():
    b, c, d, e = a(5151, 11)
    f = X('y151', b, c, d, e, list(C)[3], 5151)
    g = f.r(31)
    h = f.s()
    assert h['time'] == 31
    assert h['id'] == 'y151'
    assert isinstance(g, list)

def test_y_0152():
    b, c, d, e = a(5152, 12)
    f = X('y152', b, c, d, e, list(C)[0], 5152)
    g = f.r(32)
    h = f.s()
    assert h['time'] == 32
    assert h['id'] == 'y152'
    assert isinstance(g, list)

def test_y_0153():
    b, c, d, e = a(5153, 13)
    f = X('y153', b, c, d, e, list(C)[1], 5153)
    g = f.r(33)
    h = f.s()
    assert h['time'] == 33
    assert h['id'] == 'y153'
    assert isinstance(g, list)

def test_y_0154():
    b, c, d, e = a(5154, 14)
    f = X('y154', b, c, d, e, list(C)[2], 5154)
    g = f.r(34)
    h = f.s()
    assert h['time'] == 34
    assert h['id'] == 'y154'
    assert isinstance(g, list)

def test_y_0155():
    b, c, d, e = a(5155, 15)
    f = X('y155', b, c, d, e, list(C)[3], 5155)
    g = f.r(35)
    h = f.s()
    assert h['time'] == 35
    assert h['id'] == 'y155'
    assert isinstance(g, list)

def test_y_0156():
    b, c, d, e = a(5156, 16)
    f = X('y156', b, c, d, e, list(C)[0], 5156)
    g = f.r(36)
    h = f.s()
    assert h['time'] == 36
    assert h['id'] == 'y156'
    assert isinstance(g, list)

def test_y_0157():
    b, c, d, e = a(5157, 17)
    f = X('y157', b, c, d, e, list(C)[1], 5157)
    g = f.r(37)
    h = f.s()
    assert h['time'] == 37
    assert h['id'] == 'y157'
    assert isinstance(g, list)

def test_y_0158():
    b, c, d, e = a(5158, 18)
    f = X('y158', b, c, d, e, list(C)[2], 5158)
    g = f.r(38)
    h = f.s()
    assert h['time'] == 38
    assert h['id'] == 'y158'
    assert isinstance(g, list)

def test_y_0159():
    b, c, d, e = a(5159, 19)
    f = X('y159', b, c, d, e, list(C)[3], 5159)
    g = f.r(39)
    h = f.s()
    assert h['time'] == 39
    assert h['id'] == 'y159'
    assert isinstance(g, list)

def test_y_0160():
    b, c, d, e = a(5160, 20)
    f = X('y160', b, c, d, e, list(C)[0], 5160)
    g = f.r(40)
    h = f.s()
    assert h['time'] == 40
    assert h['id'] == 'y160'
    assert isinstance(g, list)

def test_y_0161():
    b, c, d, e = a(5161, 21)
    f = X('y161', b, c, d, e, list(C)[1], 5161)
    g = f.r(41)
    h = f.s()
    assert h['time'] == 41
    assert h['id'] == 'y161'
    assert isinstance(g, list)

def test_y_0162():
    b, c, d, e = a(5162, 22)
    f = X('y162', b, c, d, e, list(C)[2], 5162)
    g = f.r(42)
    h = f.s()
    assert h['time'] == 42
    assert h['id'] == 'y162'
    assert isinstance(g, list)

def test_y_0163():
    b, c, d, e = a(5163, 23)
    f = X('y163', b, c, d, e, list(C)[3], 5163)
    g = f.r(43)
    h = f.s()
    assert h['time'] == 43
    assert h['id'] == 'y163'
    assert isinstance(g, list)

def test_y_0164():
    b, c, d, e = a(5164, 24)
    f = X('y164', b, c, d, e, list(C)[0], 5164)
    g = f.r(44)
    h = f.s()
    assert h['time'] == 44
    assert h['id'] == 'y164'
    assert isinstance(g, list)

def test_y_0165():
    b, c, d, e = a(5165, 25)
    f = X('y165', b, c, d, e, list(C)[1], 5165)
    g = f.r(45)
    h = f.s()
    assert h['time'] == 45
    assert h['id'] == 'y165'
    assert isinstance(g, list)

def test_y_0166():
    b, c, d, e = a(5166, 26)
    f = X('y166', b, c, d, e, list(C)[2], 5166)
    g = f.r(46)
    h = f.s()
    assert h['time'] == 46
    assert h['id'] == 'y166'
    assert isinstance(g, list)

def test_y_0167():
    b, c, d, e = a(5167, 27)
    f = X('y167', b, c, d, e, list(C)[3], 5167)
    g = f.r(47)
    h = f.s()
    assert h['time'] == 47
    assert h['id'] == 'y167'
    assert isinstance(g, list)

def test_y_0168():
    b, c, d, e = a(5168, 28)
    f = X('y168', b, c, d, e, list(C)[0], 5168)
    g = f.r(48)
    h = f.s()
    assert h['time'] == 48
    assert h['id'] == 'y168'
    assert isinstance(g, list)

def test_y_0169():
    b, c, d, e = a(5169, 29)
    f = X('y169', b, c, d, e, list(C)[1], 5169)
    g = f.r(49)
    h = f.s()
    assert h['time'] == 49
    assert h['id'] == 'y169'
    assert isinstance(g, list)

def test_y_0170():
    b, c, d, e = a(5170, 30)
    f = X('y170', b, c, d, e, list(C)[2], 5170)
    g = f.r(50)
    h = f.s()
    assert h['time'] == 50
    assert h['id'] == 'y170'
    assert isinstance(g, list)

def test_y_0171():
    b, c, d, e = a(5171, 31)
    f = X('y171', b, c, d, e, list(C)[3], 5171)
    g = f.r(51)
    h = f.s()
    assert h['time'] == 51
    assert h['id'] == 'y171'
    assert isinstance(g, list)

def test_y_0172():
    b, c, d, e = a(5172, 32)
    f = X('y172', b, c, d, e, list(C)[0], 5172)
    g = f.r(52)
    h = f.s()
    assert h['time'] == 52
    assert h['id'] == 'y172'
    assert isinstance(g, list)

def test_y_0173():
    b, c, d, e = a(5173, 33)
    f = X('y173', b, c, d, e, list(C)[1], 5173)
    g = f.r(53)
    h = f.s()
    assert h['time'] == 53
    assert h['id'] == 'y173'
    assert isinstance(g, list)

def test_y_0174():
    b, c, d, e = a(5174, 34)
    f = X('y174', b, c, d, e, list(C)[2], 5174)
    g = f.r(54)
    h = f.s()
    assert h['time'] == 54
    assert h['id'] == 'y174'
    assert isinstance(g, list)

def test_y_0175():
    b, c, d, e = a(5175, 35)
    f = X('y175', b, c, d, e, list(C)[3], 5175)
    g = f.r(55)
    h = f.s()
    assert h['time'] == 55
    assert h['id'] == 'y175'
    assert isinstance(g, list)

def test_y_0176():
    b, c, d, e = a(5176, 36)
    f = X('y176', b, c, d, e, list(C)[0], 5176)
    g = f.r(56)
    h = f.s()
    assert h['time'] == 56
    assert h['id'] == 'y176'
    assert isinstance(g, list)

def test_y_0177():
    b, c, d, e = a(5177, 37)
    f = X('y177', b, c, d, e, list(C)[1], 5177)
    g = f.r(57)
    h = f.s()
    assert h['time'] == 57
    assert h['id'] == 'y177'
    assert isinstance(g, list)

def test_y_0178():
    b, c, d, e = a(5178, 38)
    f = X('y178', b, c, d, e, list(C)[2], 5178)
    g = f.r(58)
    h = f.s()
    assert h['time'] == 58
    assert h['id'] == 'y178'
    assert isinstance(g, list)

def test_y_0179():
    b, c, d, e = a(5179, 39)
    f = X('y179', b, c, d, e, list(C)[3], 5179)
    g = f.r(59)
    h = f.s()
    assert h['time'] == 59
    assert h['id'] == 'y179'
    assert isinstance(g, list)

def test_y_0180():
    b, c, d, e = a(5180, 40)
    f = X('y180', b, c, d, e, list(C)[0], 5180)
    g = f.r(60)
    h = f.s()
    assert h['time'] == 60
    assert h['id'] == 'y180'
    assert isinstance(g, list)

def test_y_0181():
    b, c, d, e = a(5181, 41)
    f = X('y181', b, c, d, e, list(C)[1], 5181)
    g = f.r(61)
    h = f.s()
    assert h['time'] == 61
    assert h['id'] == 'y181'
    assert isinstance(g, list)

def test_y_0182():
    b, c, d, e = a(5182, 42)
    f = X('y182', b, c, d, e, list(C)[2], 5182)
    g = f.r(62)
    h = f.s()
    assert h['time'] == 62
    assert h['id'] == 'y182'
    assert isinstance(g, list)

def test_y_0183():
    b, c, d, e = a(5183, 43)
    f = X('y183', b, c, d, e, list(C)[3], 5183)
    g = f.r(63)
    h = f.s()
    assert h['time'] == 63
    assert h['id'] == 'y183'
    assert isinstance(g, list)

def test_y_0184():
    b, c, d, e = a(5184, 44)
    f = X('y184', b, c, d, e, list(C)[0], 5184)
    g = f.r(64)
    h = f.s()
    assert h['time'] == 64
    assert h['id'] == 'y184'
    assert isinstance(g, list)

def test_y_0185():
    b, c, d, e = a(5185, 45)
    f = X('y185', b, c, d, e, list(C)[1], 5185)
    g = f.r(65)
    h = f.s()
    assert h['time'] == 65
    assert h['id'] == 'y185'
    assert isinstance(g, list)

def test_y_0186():
    b, c, d, e = a(5186, 46)
    f = X('y186', b, c, d, e, list(C)[2], 5186)
    g = f.r(66)
    h = f.s()
    assert h['time'] == 66
    assert h['id'] == 'y186'
    assert isinstance(g, list)

def test_y_0187():
    b, c, d, e = a(5187, 47)
    f = X('y187', b, c, d, e, list(C)[3], 5187)
    g = f.r(67)
    h = f.s()
    assert h['time'] == 67
    assert h['id'] == 'y187'
    assert isinstance(g, list)

def test_y_0188():
    b, c, d, e = a(5188, 48)
    f = X('y188', b, c, d, e, list(C)[0], 5188)
    g = f.r(68)
    h = f.s()
    assert h['time'] == 68
    assert h['id'] == 'y188'
    assert isinstance(g, list)

def test_y_0189():
    b, c, d, e = a(5189, 49)
    f = X('y189', b, c, d, e, list(C)[1], 5189)
    g = f.r(69)
    h = f.s()
    assert h['time'] == 69
    assert h['id'] == 'y189'
    assert isinstance(g, list)

def test_y_0190():
    b, c, d, e = a(5190, 50)
    f = X('y190', b, c, d, e, list(C)[2], 5190)
    g = f.r(70)
    h = f.s()
    assert h['time'] == 70
    assert h['id'] == 'y190'
    assert isinstance(g, list)

def test_y_0191():
    b, c, d, e = a(5191, 51)
    f = X('y191', b, c, d, e, list(C)[3], 5191)
    g = f.r(71)
    h = f.s()
    assert h['time'] == 71
    assert h['id'] == 'y191'
    assert isinstance(g, list)

def test_y_0192():
    b, c, d, e = a(5192, 52)
    f = X('y192', b, c, d, e, list(C)[0], 5192)
    g = f.r(72)
    h = f.s()
    assert h['time'] == 72
    assert h['id'] == 'y192'
    assert isinstance(g, list)

def test_y_0193():
    b, c, d, e = a(5193, 53)
    f = X('y193', b, c, d, e, list(C)[1], 5193)
    g = f.r(73)
    h = f.s()
    assert h['time'] == 73
    assert h['id'] == 'y193'
    assert isinstance(g, list)

def test_y_0194():
    b, c, d, e = a(5194, 54)
    f = X('y194', b, c, d, e, list(C)[2], 5194)
    g = f.r(74)
    h = f.s()
    assert h['time'] == 74
    assert h['id'] == 'y194'
    assert isinstance(g, list)

def test_y_0195():
    b, c, d, e = a(5195, 55)
    f = X('y195', b, c, d, e, list(C)[3], 5195)
    g = f.r(75)
    h = f.s()
    assert h['time'] == 75
    assert h['id'] == 'y195'
    assert isinstance(g, list)

def test_y_0196():
    b, c, d, e = a(5196, 56)
    f = X('y196', b, c, d, e, list(C)[0], 5196)
    g = f.r(76)
    h = f.s()
    assert h['time'] == 76
    assert h['id'] == 'y196'
    assert isinstance(g, list)

def test_y_0197():
    b, c, d, e = a(5197, 57)
    f = X('y197', b, c, d, e, list(C)[1], 5197)
    g = f.r(77)
    h = f.s()
    assert h['time'] == 77
    assert h['id'] == 'y197'
    assert isinstance(g, list)

def test_y_0198():
    b, c, d, e = a(5198, 58)
    f = X('y198', b, c, d, e, list(C)[2], 5198)
    g = f.r(78)
    h = f.s()
    assert h['time'] == 78
    assert h['id'] == 'y198'
    assert isinstance(g, list)

def test_y_0199():
    b, c, d, e = a(5199, 59)
    f = X('y199', b, c, d, e, list(C)[3], 5199)
    g = f.r(79)
    h = f.s()
    assert h['time'] == 79
    assert h['id'] == 'y199'
    assert isinstance(g, list)

def test_y_0200():
    b, c, d, e = a(5200, 10)
    f = X('y200', b, c, d, e, list(C)[0], 5200)
    g = f.r(80)
    h = f.s()
    assert h['time'] == 80
    assert h['id'] == 'y200'
    assert isinstance(g, list)

def test_y_0201():
    b, c, d, e = a(5201, 11)
    f = X('y201', b, c, d, e, list(C)[1], 5201)
    g = f.r(81)
    h = f.s()
    assert h['time'] == 81
    assert h['id'] == 'y201'
    assert isinstance(g, list)

def test_y_0202():
    b, c, d, e = a(5202, 12)
    f = X('y202', b, c, d, e, list(C)[2], 5202)
    g = f.r(82)
    h = f.s()
    assert h['time'] == 82
    assert h['id'] == 'y202'
    assert isinstance(g, list)

def test_y_0203():
    b, c, d, e = a(5203, 13)
    f = X('y203', b, c, d, e, list(C)[3], 5203)
    g = f.r(83)
    h = f.s()
    assert h['time'] == 83
    assert h['id'] == 'y203'
    assert isinstance(g, list)

def test_y_0204():
    b, c, d, e = a(5204, 14)
    f = X('y204', b, c, d, e, list(C)[0], 5204)
    g = f.r(84)
    h = f.s()
    assert h['time'] == 84
    assert h['id'] == 'y204'
    assert isinstance(g, list)

def test_y_0205():
    b, c, d, e = a(5205, 15)
    f = X('y205', b, c, d, e, list(C)[1], 5205)
    g = f.r(85)
    h = f.s()
    assert h['time'] == 85
    assert h['id'] == 'y205'
    assert isinstance(g, list)

def test_y_0206():
    b, c, d, e = a(5206, 16)
    f = X('y206', b, c, d, e, list(C)[2], 5206)
    g = f.r(86)
    h = f.s()
    assert h['time'] == 86
    assert h['id'] == 'y206'
    assert isinstance(g, list)

def test_y_0207():
    b, c, d, e = a(5207, 17)
    f = X('y207', b, c, d, e, list(C)[3], 5207)
    g = f.r(87)
    h = f.s()
    assert h['time'] == 87
    assert h['id'] == 'y207'
    assert isinstance(g, list)

def test_y_0208():
    b, c, d, e = a(5208, 18)
    f = X('y208', b, c, d, e, list(C)[0], 5208)
    g = f.r(88)
    h = f.s()
    assert h['time'] == 88
    assert h['id'] == 'y208'
    assert isinstance(g, list)

def test_y_0209():
    b, c, d, e = a(5209, 19)
    f = X('y209', b, c, d, e, list(C)[1], 5209)
    g = f.r(89)
    h = f.s()
    assert h['time'] == 89
    assert h['id'] == 'y209'
    assert isinstance(g, list)

def test_y_0210():
    b, c, d, e = a(5210, 20)
    f = X('y210', b, c, d, e, list(C)[2], 5210)
    g = f.r(20)
    h = f.s()
    assert h['time'] == 20
    assert h['id'] == 'y210'
    assert isinstance(g, list)

def test_y_0211():
    b, c, d, e = a(5211, 21)
    f = X('y211', b, c, d, e, list(C)[3], 5211)
    g = f.r(21)
    h = f.s()
    assert h['time'] == 21
    assert h['id'] == 'y211'
    assert isinstance(g, list)

def test_y_0212():
    b, c, d, e = a(5212, 22)
    f = X('y212', b, c, d, e, list(C)[0], 5212)
    g = f.r(22)
    h = f.s()
    assert h['time'] == 22
    assert h['id'] == 'y212'
    assert isinstance(g, list)

def test_y_0213():
    b, c, d, e = a(5213, 23)
    f = X('y213', b, c, d, e, list(C)[1], 5213)
    g = f.r(23)
    h = f.s()
    assert h['time'] == 23
    assert h['id'] == 'y213'
    assert isinstance(g, list)

def test_y_0214():
    b, c, d, e = a(5214, 24)
    f = X('y214', b, c, d, e, list(C)[2], 5214)
    g = f.r(24)
    h = f.s()
    assert h['time'] == 24
    assert h['id'] == 'y214'
    assert isinstance(g, list)

def test_y_0215():
    b, c, d, e = a(5215, 25)
    f = X('y215', b, c, d, e, list(C)[3], 5215)
    g = f.r(25)
    h = f.s()
    assert h['time'] == 25
    assert h['id'] == 'y215'
    assert isinstance(g, list)

def test_y_0216():
    b, c, d, e = a(5216, 26)
    f = X('y216', b, c, d, e, list(C)[0], 5216)
    g = f.r(26)
    h = f.s()
    assert h['time'] == 26
    assert h['id'] == 'y216'
    assert isinstance(g, list)

def test_y_0217():
    b, c, d, e = a(5217, 27)
    f = X('y217', b, c, d, e, list(C)[1], 5217)
    g = f.r(27)
    h = f.s()
    assert h['time'] == 27
    assert h['id'] == 'y217'
    assert isinstance(g, list)

def test_y_0218():
    b, c, d, e = a(5218, 28)
    f = X('y218', b, c, d, e, list(C)[2], 5218)
    g = f.r(28)
    h = f.s()
    assert h['time'] == 28
    assert h['id'] == 'y218'
    assert isinstance(g, list)

def test_y_0219():
    b, c, d, e = a(5219, 29)
    f = X('y219', b, c, d, e, list(C)[3], 5219)
    g = f.r(29)
    h = f.s()
    assert h['time'] == 29
    assert h['id'] == 'y219'
    assert isinstance(g, list)

def test_y_0220():
    b, c, d, e = a(5220, 30)
    f = X('y220', b, c, d, e, list(C)[0], 5220)
    g = f.r(30)
    h = f.s()
    assert h['time'] == 30
    assert h['id'] == 'y220'
    assert isinstance(g, list)

def test_y_0221():
    b, c, d, e = a(5221, 31)
    f = X('y221', b, c, d, e, list(C)[1], 5221)
    g = f.r(31)
    h = f.s()
    assert h['time'] == 31
    assert h['id'] == 'y221'
    assert isinstance(g, list)

def test_y_0222():
    b, c, d, e = a(5222, 32)
    f = X('y222', b, c, d, e, list(C)[2], 5222)
    g = f.r(32)
    h = f.s()
    assert h['time'] == 32
    assert h['id'] == 'y222'
    assert isinstance(g, list)

def test_y_0223():
    b, c, d, e = a(5223, 33)
    f = X('y223', b, c, d, e, list(C)[3], 5223)
    g = f.r(33)
    h = f.s()
    assert h['time'] == 33
    assert h['id'] == 'y223'
    assert isinstance(g, list)

def test_y_0224():
    b, c, d, e = a(5224, 34)
    f = X('y224', b, c, d, e, list(C)[0], 5224)
    g = f.r(34)
    h = f.s()
    assert h['time'] == 34
    assert h['id'] == 'y224'
    assert isinstance(g, list)

def test_y_0225():
    b, c, d, e = a(5225, 35)
    f = X('y225', b, c, d, e, list(C)[1], 5225)
    g = f.r(35)
    h = f.s()
    assert h['time'] == 35
    assert h['id'] == 'y225'
    assert isinstance(g, list)

def test_y_0226():
    b, c, d, e = a(5226, 36)
    f = X('y226', b, c, d, e, list(C)[2], 5226)
    g = f.r(36)
    h = f.s()
    assert h['time'] == 36
    assert h['id'] == 'y226'
    assert isinstance(g, list)

def test_y_0227():
    b, c, d, e = a(5227, 37)
    f = X('y227', b, c, d, e, list(C)[3], 5227)
    g = f.r(37)
    h = f.s()
    assert h['time'] == 37
    assert h['id'] == 'y227'
    assert isinstance(g, list)

def test_y_0228():
    b, c, d, e = a(5228, 38)
    f = X('y228', b, c, d, e, list(C)[0], 5228)
    g = f.r(38)
    h = f.s()
    assert h['time'] == 38
    assert h['id'] == 'y228'
    assert isinstance(g, list)

def test_y_0229():
    b, c, d, e = a(5229, 39)
    f = X('y229', b, c, d, e, list(C)[1], 5229)
    g = f.r(39)
    h = f.s()
    assert h['time'] == 39
    assert h['id'] == 'y229'
    assert isinstance(g, list)

def test_y_0230():
    b, c, d, e = a(5230, 40)
    f = X('y230', b, c, d, e, list(C)[2], 5230)
    g = f.r(40)
    h = f.s()
    assert h['time'] == 40
    assert h['id'] == 'y230'
    assert isinstance(g, list)

def test_y_0231():
    b, c, d, e = a(5231, 41)
    f = X('y231', b, c, d, e, list(C)[3], 5231)
    g = f.r(41)
    h = f.s()
    assert h['time'] == 41
    assert h['id'] == 'y231'
    assert isinstance(g, list)

def test_y_0232():
    b, c, d, e = a(5232, 42)
    f = X('y232', b, c, d, e, list(C)[0], 5232)
    g = f.r(42)
    h = f.s()
    assert h['time'] == 42
    assert h['id'] == 'y232'
    assert isinstance(g, list)

def test_y_0233():
    b, c, d, e = a(5233, 43)
    f = X('y233', b, c, d, e, list(C)[1], 5233)
    g = f.r(43)
    h = f.s()
    assert h['time'] == 43
    assert h['id'] == 'y233'
    assert isinstance(g, list)

def test_y_0234():
    b, c, d, e = a(5234, 44)
    f = X('y234', b, c, d, e, list(C)[2], 5234)
    g = f.r(44)
    h = f.s()
    assert h['time'] == 44
    assert h['id'] == 'y234'
    assert isinstance(g, list)

def test_y_0235():
    b, c, d, e = a(5235, 45)
    f = X('y235', b, c, d, e, list(C)[3], 5235)
    g = f.r(45)
    h = f.s()
    assert h['time'] == 45
    assert h['id'] == 'y235'
    assert isinstance(g, list)

def test_y_0236():
    b, c, d, e = a(5236, 46)
    f = X('y236', b, c, d, e, list(C)[0], 5236)
    g = f.r(46)
    h = f.s()
    assert h['time'] == 46
    assert h['id'] == 'y236'
    assert isinstance(g, list)

def test_y_0237():
    b, c, d, e = a(5237, 47)
    f = X('y237', b, c, d, e, list(C)[1], 5237)
    g = f.r(47)
    h = f.s()
    assert h['time'] == 47
    assert h['id'] == 'y237'
    assert isinstance(g, list)

def test_y_0238():
    b, c, d, e = a(5238, 48)
    f = X('y238', b, c, d, e, list(C)[2], 5238)
    g = f.r(48)
    h = f.s()
    assert h['time'] == 48
    assert h['id'] == 'y238'
    assert isinstance(g, list)

def test_y_0239():
    b, c, d, e = a(5239, 49)
    f = X('y239', b, c, d, e, list(C)[3], 5239)
    g = f.r(49)
    h = f.s()
    assert h['time'] == 49
    assert h['id'] == 'y239'
    assert isinstance(g, list)

def test_y_0240():
    b, c, d, e = a(5240, 50)
    f = X('y240', b, c, d, e, list(C)[0], 5240)
    g = f.r(50)
    h = f.s()
    assert h['time'] == 50
    assert h['id'] == 'y240'
    assert isinstance(g, list)

def test_y_0241():
    b, c, d, e = a(5241, 51)
    f = X('y241', b, c, d, e, list(C)[1], 5241)
    g = f.r(51)
    h = f.s()
    assert h['time'] == 51
    assert h['id'] == 'y241'
    assert isinstance(g, list)

def test_y_0242():
    b, c, d, e = a(5242, 52)
    f = X('y242', b, c, d, e, list(C)[2], 5242)
    g = f.r(52)
    h = f.s()
    assert h['time'] == 52
    assert h['id'] == 'y242'
    assert isinstance(g, list)

def test_y_0243():
    b, c, d, e = a(5243, 53)
    f = X('y243', b, c, d, e, list(C)[3], 5243)
    g = f.r(53)
    h = f.s()
    assert h['time'] == 53
    assert h['id'] == 'y243'
    assert isinstance(g, list)

def test_y_0244():
    b, c, d, e = a(5244, 54)
    f = X('y244', b, c, d, e, list(C)[0], 5244)
    g = f.r(54)
    h = f.s()
    assert h['time'] == 54
    assert h['id'] == 'y244'
    assert isinstance(g, list)

def test_y_0245():
    b, c, d, e = a(5245, 55)
    f = X('y245', b, c, d, e, list(C)[1], 5245)
    g = f.r(55)
    h = f.s()
    assert h['time'] == 55
    assert h['id'] == 'y245'
    assert isinstance(g, list)

def test_y_0246():
    b, c, d, e = a(5246, 56)
    f = X('y246', b, c, d, e, list(C)[2], 5246)
    g = f.r(56)
    h = f.s()
    assert h['time'] == 56
    assert h['id'] == 'y246'
    assert isinstance(g, list)

def test_y_0247():
    b, c, d, e = a(5247, 57)
    f = X('y247', b, c, d, e, list(C)[3], 5247)
    g = f.r(57)
    h = f.s()
    assert h['time'] == 57
    assert h['id'] == 'y247'
    assert isinstance(g, list)

def test_y_0248():
    b, c, d, e = a(5248, 58)
    f = X('y248', b, c, d, e, list(C)[0], 5248)
    g = f.r(58)
    h = f.s()
    assert h['time'] == 58
    assert h['id'] == 'y248'
    assert isinstance(g, list)

def test_y_0249():
    b, c, d, e = a(5249, 59)
    f = X('y249', b, c, d, e, list(C)[1], 5249)
    g = f.r(59)
    h = f.s()
    assert h['time'] == 59
    assert h['id'] == 'y249'
    assert isinstance(g, list)

def test_y_0250():
    b, c, d, e = a(5250, 10)
    f = X('y250', b, c, d, e, list(C)[2], 5250)
    g = f.r(60)
    h = f.s()
    assert h['time'] == 60
    assert h['id'] == 'y250'
    assert isinstance(g, list)

def test_y_0251():
    b, c, d, e = a(5251, 11)
    f = X('y251', b, c, d, e, list(C)[3], 5251)
    g = f.r(61)
    h = f.s()
    assert h['time'] == 61
    assert h['id'] == 'y251'
    assert isinstance(g, list)

def test_y_0252():
    b, c, d, e = a(5252, 12)
    f = X('y252', b, c, d, e, list(C)[0], 5252)
    g = f.r(62)
    h = f.s()
    assert h['time'] == 62
    assert h['id'] == 'y252'
    assert isinstance(g, list)

def test_y_0253():
    b, c, d, e = a(5253, 13)
    f = X('y253', b, c, d, e, list(C)[1], 5253)
    g = f.r(63)
    h = f.s()
    assert h['time'] == 63
    assert h['id'] == 'y253'
    assert isinstance(g, list)

def test_y_0254():
    b, c, d, e = a(5254, 14)
    f = X('y254', b, c, d, e, list(C)[2], 5254)
    g = f.r(64)
    h = f.s()
    assert h['time'] == 64
    assert h['id'] == 'y254'
    assert isinstance(g, list)

def test_y_0255():
    b, c, d, e = a(5255, 15)
    f = X('y255', b, c, d, e, list(C)[3], 5255)
    g = f.r(65)
    h = f.s()
    assert h['time'] == 65
    assert h['id'] == 'y255'
    assert isinstance(g, list)

def test_y_0256():
    b, c, d, e = a(5256, 16)
    f = X('y256', b, c, d, e, list(C)[0], 5256)
    g = f.r(66)
    h = f.s()
    assert h['time'] == 66
    assert h['id'] == 'y256'
    assert isinstance(g, list)

def test_y_0257():
    b, c, d, e = a(5257, 17)
    f = X('y257', b, c, d, e, list(C)[1], 5257)
    g = f.r(67)
    h = f.s()
    assert h['time'] == 67
    assert h['id'] == 'y257'
    assert isinstance(g, list)

def test_y_0258():
    b, c, d, e = a(5258, 18)
    f = X('y258', b, c, d, e, list(C)[2], 5258)
    g = f.r(68)
    h = f.s()
    assert h['time'] == 68
    assert h['id'] == 'y258'
    assert isinstance(g, list)

def test_y_0259():
    b, c, d, e = a(5259, 19)
    f = X('y259', b, c, d, e, list(C)[3], 5259)
    g = f.r(69)
    h = f.s()
    assert h['time'] == 69
    assert h['id'] == 'y259'
    assert isinstance(g, list)

def test_y_0260():
    b, c, d, e = a(5260, 20)
    f = X('y260', b, c, d, e, list(C)[0], 5260)
    g = f.r(70)
    h = f.s()
    assert h['time'] == 70
    assert h['id'] == 'y260'
    assert isinstance(g, list)

def test_y_0261():
    b, c, d, e = a(5261, 21)
    f = X('y261', b, c, d, e, list(C)[1], 5261)
    g = f.r(71)
    h = f.s()
    assert h['time'] == 71
    assert h['id'] == 'y261'
    assert isinstance(g, list)

def test_y_0262():
    b, c, d, e = a(5262, 22)
    f = X('y262', b, c, d, e, list(C)[2], 5262)
    g = f.r(72)
    h = f.s()
    assert h['time'] == 72
    assert h['id'] == 'y262'
    assert isinstance(g, list)

def test_y_0263():
    b, c, d, e = a(5263, 23)
    f = X('y263', b, c, d, e, list(C)[3], 5263)
    g = f.r(73)
    h = f.s()
    assert h['time'] == 73
    assert h['id'] == 'y263'
    assert isinstance(g, list)

def test_y_0264():
    b, c, d, e = a(5264, 24)
    f = X('y264', b, c, d, e, list(C)[0], 5264)
    g = f.r(74)
    h = f.s()
    assert h['time'] == 74
    assert h['id'] == 'y264'
    assert isinstance(g, list)

def test_y_0265():
    b, c, d, e = a(5265, 25)
    f = X('y265', b, c, d, e, list(C)[1], 5265)
    g = f.r(75)
    h = f.s()
    assert h['time'] == 75
    assert h['id'] == 'y265'
    assert isinstance(g, list)

def test_y_0266():
    b, c, d, e = a(5266, 26)
    f = X('y266', b, c, d, e, list(C)[2], 5266)
    g = f.r(76)
    h = f.s()
    assert h['time'] == 76
    assert h['id'] == 'y266'
    assert isinstance(g, list)

def test_y_0267():
    b, c, d, e = a(5267, 27)
    f = X('y267', b, c, d, e, list(C)[3], 5267)
    g = f.r(77)
    h = f.s()
    assert h['time'] == 77
    assert h['id'] == 'y267'
    assert isinstance(g, list)

def test_y_0268():
    b, c, d, e = a(5268, 28)
    f = X('y268', b, c, d, e, list(C)[0], 5268)
    g = f.r(78)
    h = f.s()
    assert h['time'] == 78
    assert h['id'] == 'y268'
    assert isinstance(g, list)

def test_y_0269():
    b, c, d, e = a(5269, 29)
    f = X('y269', b, c, d, e, list(C)[1], 5269)
    g = f.r(79)
    h = f.s()
    assert h['time'] == 79
    assert h['id'] == 'y269'
    assert isinstance(g, list)

def test_y_0270():
    b, c, d, e = a(5270, 30)
    f = X('y270', b, c, d, e, list(C)[2], 5270)
    g = f.r(80)
    h = f.s()
    assert h['time'] == 80
    assert h['id'] == 'y270'
    assert isinstance(g, list)

def test_y_0271():
    b, c, d, e = a(5271, 31)
    f = X('y271', b, c, d, e, list(C)[3], 5271)
    g = f.r(81)
    h = f.s()
    assert h['time'] == 81
    assert h['id'] == 'y271'
    assert isinstance(g, list)

def test_y_0272():
    b, c, d, e = a(5272, 32)
    f = X('y272', b, c, d, e, list(C)[0], 5272)
    g = f.r(82)
    h = f.s()
    assert h['time'] == 82
    assert h['id'] == 'y272'
    assert isinstance(g, list)

def test_y_0273():
    b, c, d, e = a(5273, 33)
    f = X('y273', b, c, d, e, list(C)[1], 5273)
    g = f.r(83)
    h = f.s()
    assert h['time'] == 83
    assert h['id'] == 'y273'
    assert isinstance(g, list)

def test_y_0274():
    b, c, d, e = a(5274, 34)
    f = X('y274', b, c, d, e, list(C)[2], 5274)
    g = f.r(84)
    h = f.s()
    assert h['time'] == 84
    assert h['id'] == 'y274'
    assert isinstance(g, list)

def test_y_0275():
    b, c, d, e = a(5275, 35)
    f = X('y275', b, c, d, e, list(C)[3], 5275)
    g = f.r(85)
    h = f.s()
    assert h['time'] == 85
    assert h['id'] == 'y275'
    assert isinstance(g, list)

def test_y_0276():
    b, c, d, e = a(5276, 36)
    f = X('y276', b, c, d, e, list(C)[0], 5276)
    g = f.r(86)
    h = f.s()
    assert h['time'] == 86
    assert h['id'] == 'y276'
    assert isinstance(g, list)

def test_y_0277():
    b, c, d, e = a(5277, 37)
    f = X('y277', b, c, d, e, list(C)[1], 5277)
    g = f.r(87)
    h = f.s()
    assert h['time'] == 87
    assert h['id'] == 'y277'
    assert isinstance(g, list)

def test_y_0278():
    b, c, d, e = a(5278, 38)
    f = X('y278', b, c, d, e, list(C)[2], 5278)
    g = f.r(88)
    h = f.s()
    assert h['time'] == 88
    assert h['id'] == 'y278'
    assert isinstance(g, list)

def test_y_0279():
    b, c, d, e = a(5279, 39)
    f = X('y279', b, c, d, e, list(C)[3], 5279)
    g = f.r(89)
    h = f.s()
    assert h['time'] == 89
    assert h['id'] == 'y279'
    assert isinstance(g, list)

def test_y_0280():
    b, c, d, e = a(5280, 40)
    f = X('y280', b, c, d, e, list(C)[0], 5280)
    g = f.r(20)
    h = f.s()
    assert h['time'] == 20
    assert h['id'] == 'y280'
    assert isinstance(g, list)

def test_y_0281():
    b, c, d, e = a(5281, 41)
    f = X('y281', b, c, d, e, list(C)[1], 5281)
    g = f.r(21)
    h = f.s()
    assert h['time'] == 21
    assert h['id'] == 'y281'
    assert isinstance(g, list)

def test_y_0282():
    b, c, d, e = a(5282, 42)
    f = X('y282', b, c, d, e, list(C)[2], 5282)
    g = f.r(22)
    h = f.s()
    assert h['time'] == 22
    assert h['id'] == 'y282'
    assert isinstance(g, list)

def test_y_0283():
    b, c, d, e = a(5283, 43)
    f = X('y283', b, c, d, e, list(C)[3], 5283)
    g = f.r(23)
    h = f.s()
    assert h['time'] == 23
    assert h['id'] == 'y283'
    assert isinstance(g, list)

def test_y_0284():
    b, c, d, e = a(5284, 44)
    f = X('y284', b, c, d, e, list(C)[0], 5284)
    g = f.r(24)
    h = f.s()
    assert h['time'] == 24
    assert h['id'] == 'y284'
    assert isinstance(g, list)

def test_y_0285():
    b, c, d, e = a(5285, 45)
    f = X('y285', b, c, d, e, list(C)[1], 5285)
    g = f.r(25)
    h = f.s()
    assert h['time'] == 25
    assert h['id'] == 'y285'
    assert isinstance(g, list)

def test_y_0286():
    b, c, d, e = a(5286, 46)
    f = X('y286', b, c, d, e, list(C)[2], 5286)
    g = f.r(26)
    h = f.s()
    assert h['time'] == 26
    assert h['id'] == 'y286'
    assert isinstance(g, list)

def test_y_0287():
    b, c, d, e = a(5287, 47)
    f = X('y287', b, c, d, e, list(C)[3], 5287)
    g = f.r(27)
    h = f.s()
    assert h['time'] == 27
    assert h['id'] == 'y287'
    assert isinstance(g, list)

def test_y_0288():
    b, c, d, e = a(5288, 48)
    f = X('y288', b, c, d, e, list(C)[0], 5288)
    g = f.r(28)
    h = f.s()
    assert h['time'] == 28
    assert h['id'] == 'y288'
    assert isinstance(g, list)

def test_y_0289():
    b, c, d, e = a(5289, 49)
    f = X('y289', b, c, d, e, list(C)[1], 5289)
    g = f.r(29)
    h = f.s()
    assert h['time'] == 29
    assert h['id'] == 'y289'
    assert isinstance(g, list)

def test_y_0290():
    b, c, d, e = a(5290, 50)
    f = X('y290', b, c, d, e, list(C)[2], 5290)
    g = f.r(30)
    h = f.s()
    assert h['time'] == 30
    assert h['id'] == 'y290'
    assert isinstance(g, list)

def test_y_0291():
    b, c, d, e = a(5291, 51)
    f = X('y291', b, c, d, e, list(C)[3], 5291)
    g = f.r(31)
    h = f.s()
    assert h['time'] == 31
    assert h['id'] == 'y291'
    assert isinstance(g, list)

def test_y_0292():
    b, c, d, e = a(5292, 52)
    f = X('y292', b, c, d, e, list(C)[0], 5292)
    g = f.r(32)
    h = f.s()
    assert h['time'] == 32
    assert h['id'] == 'y292'
    assert isinstance(g, list)

def test_y_0293():
    b, c, d, e = a(5293, 53)
    f = X('y293', b, c, d, e, list(C)[1], 5293)
    g = f.r(33)
    h = f.s()
    assert h['time'] == 33
    assert h['id'] == 'y293'
    assert isinstance(g, list)

def test_y_0294():
    b, c, d, e = a(5294, 54)
    f = X('y294', b, c, d, e, list(C)[2], 5294)
    g = f.r(34)
    h = f.s()
    assert h['time'] == 34
    assert h['id'] == 'y294'
    assert isinstance(g, list)

def test_y_0295():
    b, c, d, e = a(5295, 55)
    f = X('y295', b, c, d, e, list(C)[3], 5295)
    g = f.r(35)
    h = f.s()
    assert h['time'] == 35
    assert h['id'] == 'y295'
    assert isinstance(g, list)

def test_y_0296():
    b, c, d, e = a(5296, 56)
    f = X('y296', b, c, d, e, list(C)[0], 5296)
    g = f.r(36)
    h = f.s()
    assert h['time'] == 36
    assert h['id'] == 'y296'
    assert isinstance(g, list)

def test_y_0297():
    b, c, d, e = a(5297, 57)
    f = X('y297', b, c, d, e, list(C)[1], 5297)
    g = f.r(37)
    h = f.s()
    assert h['time'] == 37
    assert h['id'] == 'y297'
    assert isinstance(g, list)

def test_y_0298():
    b, c, d, e = a(5298, 58)
    f = X('y298', b, c, d, e, list(C)[2], 5298)
    g = f.r(38)
    h = f.s()
    assert h['time'] == 38
    assert h['id'] == 'y298'
    assert isinstance(g, list)

def test_y_0299():
    b, c, d, e = a(5299, 59)
    f = X('y299', b, c, d, e, list(C)[3], 5299)
    g = f.r(39)
    h = f.s()
    assert h['time'] == 39
    assert h['id'] == 'y299'
    assert isinstance(g, list)

def test_y_0300():
    b, c, d, e = a(5300, 10)
    f = X('y300', b, c, d, e, list(C)[0], 5300)
    g = f.r(40)
    h = f.s()
    assert h['time'] == 40
    assert h['id'] == 'y300'
    assert isinstance(g, list)

def test_y_0301():
    b, c, d, e = a(5301, 11)
    f = X('y301', b, c, d, e, list(C)[1], 5301)
    g = f.r(41)
    h = f.s()
    assert h['time'] == 41
    assert h['id'] == 'y301'
    assert isinstance(g, list)

def test_y_0302():
    b, c, d, e = a(5302, 12)
    f = X('y302', b, c, d, e, list(C)[2], 5302)
    g = f.r(42)
    h = f.s()
    assert h['time'] == 42
    assert h['id'] == 'y302'
    assert isinstance(g, list)

def test_y_0303():
    b, c, d, e = a(5303, 13)
    f = X('y303', b, c, d, e, list(C)[3], 5303)
    g = f.r(43)
    h = f.s()
    assert h['time'] == 43
    assert h['id'] == 'y303'
    assert isinstance(g, list)

def test_y_0304():
    b, c, d, e = a(5304, 14)
    f = X('y304', b, c, d, e, list(C)[0], 5304)
    g = f.r(44)
    h = f.s()
    assert h['time'] == 44
    assert h['id'] == 'y304'
    assert isinstance(g, list)

def test_y_0305():
    b, c, d, e = a(5305, 15)
    f = X('y305', b, c, d, e, list(C)[1], 5305)
    g = f.r(45)
    h = f.s()
    assert h['time'] == 45
    assert h['id'] == 'y305'
    assert isinstance(g, list)

def test_y_0306():
    b, c, d, e = a(5306, 16)
    f = X('y306', b, c, d, e, list(C)[2], 5306)
    g = f.r(46)
    h = f.s()
    assert h['time'] == 46
    assert h['id'] == 'y306'
    assert isinstance(g, list)

def test_y_0307():
    b, c, d, e = a(5307, 17)
    f = X('y307', b, c, d, e, list(C)[3], 5307)
    g = f.r(47)
    h = f.s()
    assert h['time'] == 47
    assert h['id'] == 'y307'
    assert isinstance(g, list)

def test_y_0308():
    b, c, d, e = a(5308, 18)
    f = X('y308', b, c, d, e, list(C)[0], 5308)
    g = f.r(48)
    h = f.s()
    assert h['time'] == 48
    assert h['id'] == 'y308'
    assert isinstance(g, list)

def test_y_0309():
    b, c, d, e = a(5309, 19)
    f = X('y309', b, c, d, e, list(C)[1], 5309)
    g = f.r(49)
    h = f.s()
    assert h['time'] == 49
    assert h['id'] == 'y309'
    assert isinstance(g, list)

def test_y_0310():
    b, c, d, e = a(5310, 20)
    f = X('y310', b, c, d, e, list(C)[2], 5310)
    g = f.r(50)
    h = f.s()
    assert h['time'] == 50
    assert h['id'] == 'y310'
    assert isinstance(g, list)

def test_y_0311():
    b, c, d, e = a(5311, 21)
    f = X('y311', b, c, d, e, list(C)[3], 5311)
    g = f.r(51)
    h = f.s()
    assert h['time'] == 51
    assert h['id'] == 'y311'
    assert isinstance(g, list)

def test_y_0312():
    b, c, d, e = a(5312, 22)
    f = X('y312', b, c, d, e, list(C)[0], 5312)
    g = f.r(52)
    h = f.s()
    assert h['time'] == 52
    assert h['id'] == 'y312'
    assert isinstance(g, list)

def test_y_0313():
    b, c, d, e = a(5313, 23)
    f = X('y313', b, c, d, e, list(C)[1], 5313)
    g = f.r(53)
    h = f.s()
    assert h['time'] == 53
    assert h['id'] == 'y313'
    assert isinstance(g, list)

def test_y_0314():
    b, c, d, e = a(5314, 24)
    f = X('y314', b, c, d, e, list(C)[2], 5314)
    g = f.r(54)
    h = f.s()
    assert h['time'] == 54
    assert h['id'] == 'y314'
    assert isinstance(g, list)

def test_y_0315():
    b, c, d, e = a(5315, 25)
    f = X('y315', b, c, d, e, list(C)[3], 5315)
    g = f.r(55)
    h = f.s()
    assert h['time'] == 55
    assert h['id'] == 'y315'
    assert isinstance(g, list)

def test_y_0316():
    b, c, d, e = a(5316, 26)
    f = X('y316', b, c, d, e, list(C)[0], 5316)
    g = f.r(56)
    h = f.s()
    assert h['time'] == 56
    assert h['id'] == 'y316'
    assert isinstance(g, list)

def test_y_0317():
    b, c, d, e = a(5317, 27)
    f = X('y317', b, c, d, e, list(C)[1], 5317)
    g = f.r(57)
    h = f.s()
    assert h['time'] == 57
    assert h['id'] == 'y317'
    assert isinstance(g, list)

def test_y_0318():
    b, c, d, e = a(5318, 28)
    f = X('y318', b, c, d, e, list(C)[2], 5318)
    g = f.r(58)
    h = f.s()
    assert h['time'] == 58
    assert h['id'] == 'y318'
    assert isinstance(g, list)

def test_y_0319():
    b, c, d, e = a(5319, 29)
    f = X('y319', b, c, d, e, list(C)[3], 5319)
    g = f.r(59)
    h = f.s()
    assert h['time'] == 59
    assert h['id'] == 'y319'
    assert isinstance(g, list)

def test_y_0320():
    b, c, d, e = a(5320, 30)
    f = X('y320', b, c, d, e, list(C)[0], 5320)
    g = f.r(60)
    h = f.s()
    assert h['time'] == 60
    assert h['id'] == 'y320'
    assert isinstance(g, list)

def test_y_0321():
    b, c, d, e = a(5321, 31)
    f = X('y321', b, c, d, e, list(C)[1], 5321)
    g = f.r(61)
    h = f.s()
    assert h['time'] == 61
    assert h['id'] == 'y321'
    assert isinstance(g, list)

def test_y_0322():
    b, c, d, e = a(5322, 32)
    f = X('y322', b, c, d, e, list(C)[2], 5322)
    g = f.r(62)
    h = f.s()
    assert h['time'] == 62
    assert h['id'] == 'y322'
    assert isinstance(g, list)

def test_y_0323():
    b, c, d, e = a(5323, 33)
    f = X('y323', b, c, d, e, list(C)[3], 5323)
    g = f.r(63)
    h = f.s()
    assert h['time'] == 63
    assert h['id'] == 'y323'
    assert isinstance(g, list)

def test_y_0324():
    b, c, d, e = a(5324, 34)
    f = X('y324', b, c, d, e, list(C)[0], 5324)
    g = f.r(64)
    h = f.s()
    assert h['time'] == 64
    assert h['id'] == 'y324'
    assert isinstance(g, list)

def test_y_0325():
    b, c, d, e = a(5325, 35)
    f = X('y325', b, c, d, e, list(C)[1], 5325)
    g = f.r(65)
    h = f.s()
    assert h['time'] == 65
    assert h['id'] == 'y325'
    assert isinstance(g, list)

def test_y_0326():
    b, c, d, e = a(5326, 36)
    f = X('y326', b, c, d, e, list(C)[2], 5326)
    g = f.r(66)
    h = f.s()
    assert h['time'] == 66
    assert h['id'] == 'y326'
    assert isinstance(g, list)

def test_y_0327():
    b, c, d, e = a(5327, 37)
    f = X('y327', b, c, d, e, list(C)[3], 5327)
    g = f.r(67)
    h = f.s()
    assert h['time'] == 67
    assert h['id'] == 'y327'
    assert isinstance(g, list)

def test_y_0328():
    b, c, d, e = a(5328, 38)
    f = X('y328', b, c, d, e, list(C)[0], 5328)
    g = f.r(68)
    h = f.s()
    assert h['time'] == 68
    assert h['id'] == 'y328'
    assert isinstance(g, list)

def test_y_0329():
    b, c, d, e = a(5329, 39)
    f = X('y329', b, c, d, e, list(C)[1], 5329)
    g = f.r(69)
    h = f.s()
    assert h['time'] == 69
    assert h['id'] == 'y329'
    assert isinstance(g, list)

def test_y_0330():
    b, c, d, e = a(5330, 40)
    f = X('y330', b, c, d, e, list(C)[2], 5330)
    g = f.r(70)
    h = f.s()
    assert h['time'] == 70
    assert h['id'] == 'y330'
    assert isinstance(g, list)

def test_y_0331():
    b, c, d, e = a(5331, 41)
    f = X('y331', b, c, d, e, list(C)[3], 5331)
    g = f.r(71)
    h = f.s()
    assert h['time'] == 71
    assert h['id'] == 'y331'
    assert isinstance(g, list)

def test_y_0332():
    b, c, d, e = a(5332, 42)
    f = X('y332', b, c, d, e, list(C)[0], 5332)
    g = f.r(72)
    h = f.s()
    assert h['time'] == 72
    assert h['id'] == 'y332'
    assert isinstance(g, list)

def test_y_0333():
    b, c, d, e = a(5333, 43)
    f = X('y333', b, c, d, e, list(C)[1], 5333)
    g = f.r(73)
    h = f.s()
    assert h['time'] == 73
    assert h['id'] == 'y333'
    assert isinstance(g, list)

def test_y_0334():
    b, c, d, e = a(5334, 44)
    f = X('y334', b, c, d, e, list(C)[2], 5334)
    g = f.r(74)
    h = f.s()
    assert h['time'] == 74
    assert h['id'] == 'y334'
    assert isinstance(g, list)

def test_y_0335():
    b, c, d, e = a(5335, 45)
    f = X('y335', b, c, d, e, list(C)[3], 5335)
    g = f.r(75)
    h = f.s()
    assert h['time'] == 75
    assert h['id'] == 'y335'
    assert isinstance(g, list)

def test_y_0336():
    b, c, d, e = a(5336, 46)
    f = X('y336', b, c, d, e, list(C)[0], 5336)
    g = f.r(76)
    h = f.s()
    assert h['time'] == 76
    assert h['id'] == 'y336'
    assert isinstance(g, list)

def test_y_0337():
    b, c, d, e = a(5337, 47)
    f = X('y337', b, c, d, e, list(C)[1], 5337)
    g = f.r(77)
    h = f.s()
    assert h['time'] == 77
    assert h['id'] == 'y337'
    assert isinstance(g, list)

def test_y_0338():
    b, c, d, e = a(5338, 48)
    f = X('y338', b, c, d, e, list(C)[2], 5338)
    g = f.r(78)
    h = f.s()
    assert h['time'] == 78
    assert h['id'] == 'y338'
    assert isinstance(g, list)

def test_y_0339():
    b, c, d, e = a(5339, 49)
    f = X('y339', b, c, d, e, list(C)[3], 5339)
    g = f.r(79)
    h = f.s()
    assert h['time'] == 79
    assert h['id'] == 'y339'
    assert isinstance(g, list)

def test_y_0340():
    b, c, d, e = a(5340, 50)
    f = X('y340', b, c, d, e, list(C)[0], 5340)
    g = f.r(80)
    h = f.s()
    assert h['time'] == 80
    assert h['id'] == 'y340'
    assert isinstance(g, list)

def test_y_0341():
    b, c, d, e = a(5341, 51)
    f = X('y341', b, c, d, e, list(C)[1], 5341)
    g = f.r(81)
    h = f.s()
    assert h['time'] == 81
    assert h['id'] == 'y341'
    assert isinstance(g, list)

def test_y_0342():
    b, c, d, e = a(5342, 52)
    f = X('y342', b, c, d, e, list(C)[2], 5342)
    g = f.r(82)
    h = f.s()
    assert h['time'] == 82
    assert h['id'] == 'y342'
    assert isinstance(g, list)

def test_y_0343():
    b, c, d, e = a(5343, 53)
    f = X('y343', b, c, d, e, list(C)[3], 5343)
    g = f.r(83)
    h = f.s()
    assert h['time'] == 83
    assert h['id'] == 'y343'
    assert isinstance(g, list)

def test_y_0344():
    b, c, d, e = a(5344, 54)
    f = X('y344', b, c, d, e, list(C)[0], 5344)
    g = f.r(84)
    h = f.s()
    assert h['time'] == 84
    assert h['id'] == 'y344'
    assert isinstance(g, list)

def test_y_0345():
    b, c, d, e = a(5345, 55)
    f = X('y345', b, c, d, e, list(C)[1], 5345)
    g = f.r(85)
    h = f.s()
    assert h['time'] == 85
    assert h['id'] == 'y345'
    assert isinstance(g, list)

def test_y_0346():
    b, c, d, e = a(5346, 56)
    f = X('y346', b, c, d, e, list(C)[2], 5346)
    g = f.r(86)
    h = f.s()
    assert h['time'] == 86
    assert h['id'] == 'y346'
    assert isinstance(g, list)

def test_y_0347():
    b, c, d, e = a(5347, 57)
    f = X('y347', b, c, d, e, list(C)[3], 5347)
    g = f.r(87)
    h = f.s()
    assert h['time'] == 87
    assert h['id'] == 'y347'
    assert isinstance(g, list)

def test_y_0348():
    b, c, d, e = a(5348, 58)
    f = X('y348', b, c, d, e, list(C)[0], 5348)
    g = f.r(88)
    h = f.s()
    assert h['time'] == 88
    assert h['id'] == 'y348'
    assert isinstance(g, list)

def test_y_0349():
    b, c, d, e = a(5349, 59)
    f = X('y349', b, c, d, e, list(C)[1], 5349)
    g = f.r(89)
    h = f.s()
    assert h['time'] == 89
    assert h['id'] == 'y349'
    assert isinstance(g, list)
