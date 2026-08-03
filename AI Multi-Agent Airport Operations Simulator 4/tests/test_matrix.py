import pytest
from app.sim.scenarios import a
from app.sim.engine import X
from app.domain.enums import C

def test_x_0000():
    b, c, d, e = a(10, 5)
    f = X('x0', b, c, d, e, list(C)[0], 10)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0001():
    b, c, d, e = a(11, 6)
    f = X('x1', b, c, d, e, list(C)[1], 11)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0002():
    b, c, d, e = a(12, 7)
    f = X('x2', b, c, d, e, list(C)[2], 12)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0003():
    b, c, d, e = a(13, 8)
    f = X('x3', b, c, d, e, list(C)[3], 13)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0004():
    b, c, d, e = a(14, 9)
    f = X('x4', b, c, d, e, list(C)[0], 14)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0005():
    b, c, d, e = a(15, 10)
    f = X('x5', b, c, d, e, list(C)[1], 15)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0006():
    b, c, d, e = a(16, 11)
    f = X('x6', b, c, d, e, list(C)[2], 16)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0007():
    b, c, d, e = a(17, 12)
    f = X('x7', b, c, d, e, list(C)[3], 17)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0008():
    b, c, d, e = a(18, 13)
    f = X('x8', b, c, d, e, list(C)[0], 18)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0009():
    b, c, d, e = a(19, 14)
    f = X('x9', b, c, d, e, list(C)[1], 19)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0010():
    b, c, d, e = a(20, 15)
    f = X('x10', b, c, d, e, list(C)[2], 20)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0011():
    b, c, d, e = a(21, 16)
    f = X('x11', b, c, d, e, list(C)[3], 21)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0012():
    b, c, d, e = a(22, 17)
    f = X('x12', b, c, d, e, list(C)[0], 22)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0013():
    b, c, d, e = a(23, 18)
    f = X('x13', b, c, d, e, list(C)[1], 23)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0014():
    b, c, d, e = a(24, 19)
    f = X('x14', b, c, d, e, list(C)[2], 24)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0015():
    b, c, d, e = a(25, 20)
    f = X('x15', b, c, d, e, list(C)[3], 25)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0016():
    b, c, d, e = a(26, 21)
    f = X('x16', b, c, d, e, list(C)[0], 26)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0017():
    b, c, d, e = a(27, 22)
    f = X('x17', b, c, d, e, list(C)[1], 27)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0018():
    b, c, d, e = a(28, 23)
    f = X('x18', b, c, d, e, list(C)[2], 28)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0019():
    b, c, d, e = a(29, 24)
    f = X('x19', b, c, d, e, list(C)[3], 29)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0020():
    b, c, d, e = a(30, 25)
    f = X('x20', b, c, d, e, list(C)[0], 30)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0021():
    b, c, d, e = a(31, 26)
    f = X('x21', b, c, d, e, list(C)[1], 31)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0022():
    b, c, d, e = a(32, 27)
    f = X('x22', b, c, d, e, list(C)[2], 32)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0023():
    b, c, d, e = a(33, 28)
    f = X('x23', b, c, d, e, list(C)[3], 33)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0024():
    b, c, d, e = a(34, 29)
    f = X('x24', b, c, d, e, list(C)[0], 34)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0025():
    b, c, d, e = a(35, 30)
    f = X('x25', b, c, d, e, list(C)[1], 35)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0026():
    b, c, d, e = a(36, 31)
    f = X('x26', b, c, d, e, list(C)[2], 36)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0027():
    b, c, d, e = a(37, 32)
    f = X('x27', b, c, d, e, list(C)[3], 37)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0028():
    b, c, d, e = a(38, 33)
    f = X('x28', b, c, d, e, list(C)[0], 38)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0029():
    b, c, d, e = a(39, 34)
    f = X('x29', b, c, d, e, list(C)[1], 39)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0030():
    b, c, d, e = a(40, 35)
    f = X('x30', b, c, d, e, list(C)[2], 40)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0031():
    b, c, d, e = a(41, 36)
    f = X('x31', b, c, d, e, list(C)[3], 41)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0032():
    b, c, d, e = a(42, 37)
    f = X('x32', b, c, d, e, list(C)[0], 42)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0033():
    b, c, d, e = a(43, 38)
    f = X('x33', b, c, d, e, list(C)[1], 43)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0034():
    b, c, d, e = a(44, 39)
    f = X('x34', b, c, d, e, list(C)[2], 44)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0035():
    b, c, d, e = a(45, 40)
    f = X('x35', b, c, d, e, list(C)[3], 45)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0036():
    b, c, d, e = a(46, 41)
    f = X('x36', b, c, d, e, list(C)[0], 46)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0037():
    b, c, d, e = a(47, 42)
    f = X('x37', b, c, d, e, list(C)[1], 47)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0038():
    b, c, d, e = a(48, 43)
    f = X('x38', b, c, d, e, list(C)[2], 48)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0039():
    b, c, d, e = a(49, 44)
    f = X('x39', b, c, d, e, list(C)[3], 49)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0040():
    b, c, d, e = a(50, 5)
    f = X('x40', b, c, d, e, list(C)[0], 50)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0041():
    b, c, d, e = a(51, 6)
    f = X('x41', b, c, d, e, list(C)[1], 51)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0042():
    b, c, d, e = a(52, 7)
    f = X('x42', b, c, d, e, list(C)[2], 52)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0043():
    b, c, d, e = a(53, 8)
    f = X('x43', b, c, d, e, list(C)[3], 53)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0044():
    b, c, d, e = a(54, 9)
    f = X('x44', b, c, d, e, list(C)[0], 54)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0045():
    b, c, d, e = a(55, 10)
    f = X('x45', b, c, d, e, list(C)[1], 55)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0046():
    b, c, d, e = a(56, 11)
    f = X('x46', b, c, d, e, list(C)[2], 56)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0047():
    b, c, d, e = a(57, 12)
    f = X('x47', b, c, d, e, list(C)[3], 57)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0048():
    b, c, d, e = a(58, 13)
    f = X('x48', b, c, d, e, list(C)[0], 58)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0049():
    b, c, d, e = a(59, 14)
    f = X('x49', b, c, d, e, list(C)[1], 59)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59

def test_x_0050():
    b, c, d, e = a(60, 15)
    f = X('x50', b, c, d, e, list(C)[2], 60)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0051():
    b, c, d, e = a(61, 16)
    f = X('x51', b, c, d, e, list(C)[3], 61)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0052():
    b, c, d, e = a(62, 17)
    f = X('x52', b, c, d, e, list(C)[0], 62)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0053():
    b, c, d, e = a(63, 18)
    f = X('x53', b, c, d, e, list(C)[1], 63)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0054():
    b, c, d, e = a(64, 19)
    f = X('x54', b, c, d, e, list(C)[2], 64)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0055():
    b, c, d, e = a(65, 20)
    f = X('x55', b, c, d, e, list(C)[3], 65)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0056():
    b, c, d, e = a(66, 21)
    f = X('x56', b, c, d, e, list(C)[0], 66)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0057():
    b, c, d, e = a(67, 22)
    f = X('x57', b, c, d, e, list(C)[1], 67)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0058():
    b, c, d, e = a(68, 23)
    f = X('x58', b, c, d, e, list(C)[2], 68)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0059():
    b, c, d, e = a(69, 24)
    f = X('x59', b, c, d, e, list(C)[3], 69)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0060():
    b, c, d, e = a(70, 25)
    f = X('x60', b, c, d, e, list(C)[0], 70)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0061():
    b, c, d, e = a(71, 26)
    f = X('x61', b, c, d, e, list(C)[1], 71)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0062():
    b, c, d, e = a(72, 27)
    f = X('x62', b, c, d, e, list(C)[2], 72)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0063():
    b, c, d, e = a(73, 28)
    f = X('x63', b, c, d, e, list(C)[3], 73)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0064():
    b, c, d, e = a(74, 29)
    f = X('x64', b, c, d, e, list(C)[0], 74)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0065():
    b, c, d, e = a(75, 30)
    f = X('x65', b, c, d, e, list(C)[1], 75)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0066():
    b, c, d, e = a(76, 31)
    f = X('x66', b, c, d, e, list(C)[2], 76)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0067():
    b, c, d, e = a(77, 32)
    f = X('x67', b, c, d, e, list(C)[3], 77)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0068():
    b, c, d, e = a(78, 33)
    f = X('x68', b, c, d, e, list(C)[0], 78)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0069():
    b, c, d, e = a(79, 34)
    f = X('x69', b, c, d, e, list(C)[1], 79)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0070():
    b, c, d, e = a(80, 35)
    f = X('x70', b, c, d, e, list(C)[2], 80)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0071():
    b, c, d, e = a(81, 36)
    f = X('x71', b, c, d, e, list(C)[3], 81)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0072():
    b, c, d, e = a(82, 37)
    f = X('x72', b, c, d, e, list(C)[0], 82)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0073():
    b, c, d, e = a(83, 38)
    f = X('x73', b, c, d, e, list(C)[1], 83)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0074():
    b, c, d, e = a(84, 39)
    f = X('x74', b, c, d, e, list(C)[2], 84)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0075():
    b, c, d, e = a(85, 40)
    f = X('x75', b, c, d, e, list(C)[3], 85)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0076():
    b, c, d, e = a(86, 41)
    f = X('x76', b, c, d, e, list(C)[0], 86)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0077():
    b, c, d, e = a(87, 42)
    f = X('x77', b, c, d, e, list(C)[1], 87)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0078():
    b, c, d, e = a(88, 43)
    f = X('x78', b, c, d, e, list(C)[2], 88)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0079():
    b, c, d, e = a(89, 44)
    f = X('x79', b, c, d, e, list(C)[3], 89)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0080():
    b, c, d, e = a(90, 5)
    f = X('x80', b, c, d, e, list(C)[0], 90)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0081():
    b, c, d, e = a(91, 6)
    f = X('x81', b, c, d, e, list(C)[1], 91)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0082():
    b, c, d, e = a(92, 7)
    f = X('x82', b, c, d, e, list(C)[2], 92)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0083():
    b, c, d, e = a(93, 8)
    f = X('x83', b, c, d, e, list(C)[3], 93)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0084():
    b, c, d, e = a(94, 9)
    f = X('x84', b, c, d, e, list(C)[0], 94)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0085():
    b, c, d, e = a(95, 10)
    f = X('x85', b, c, d, e, list(C)[1], 95)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0086():
    b, c, d, e = a(96, 11)
    f = X('x86', b, c, d, e, list(C)[2], 96)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0087():
    b, c, d, e = a(97, 12)
    f = X('x87', b, c, d, e, list(C)[3], 97)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0088():
    b, c, d, e = a(98, 13)
    f = X('x88', b, c, d, e, list(C)[0], 98)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0089():
    b, c, d, e = a(99, 14)
    f = X('x89', b, c, d, e, list(C)[1], 99)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0090():
    b, c, d, e = a(100, 15)
    f = X('x90', b, c, d, e, list(C)[2], 100)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0091():
    b, c, d, e = a(101, 16)
    f = X('x91', b, c, d, e, list(C)[3], 101)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0092():
    b, c, d, e = a(102, 17)
    f = X('x92', b, c, d, e, list(C)[0], 102)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0093():
    b, c, d, e = a(103, 18)
    f = X('x93', b, c, d, e, list(C)[1], 103)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0094():
    b, c, d, e = a(104, 19)
    f = X('x94', b, c, d, e, list(C)[2], 104)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0095():
    b, c, d, e = a(105, 20)
    f = X('x95', b, c, d, e, list(C)[3], 105)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0096():
    b, c, d, e = a(106, 21)
    f = X('x96', b, c, d, e, list(C)[0], 106)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0097():
    b, c, d, e = a(107, 22)
    f = X('x97', b, c, d, e, list(C)[1], 107)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0098():
    b, c, d, e = a(108, 23)
    f = X('x98', b, c, d, e, list(C)[2], 108)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0099():
    b, c, d, e = a(109, 24)
    f = X('x99', b, c, d, e, list(C)[3], 109)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59

def test_x_0100():
    b, c, d, e = a(110, 25)
    f = X('x100', b, c, d, e, list(C)[0], 110)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0101():
    b, c, d, e = a(111, 26)
    f = X('x101', b, c, d, e, list(C)[1], 111)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0102():
    b, c, d, e = a(112, 27)
    f = X('x102', b, c, d, e, list(C)[2], 112)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0103():
    b, c, d, e = a(113, 28)
    f = X('x103', b, c, d, e, list(C)[3], 113)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0104():
    b, c, d, e = a(114, 29)
    f = X('x104', b, c, d, e, list(C)[0], 114)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0105():
    b, c, d, e = a(115, 30)
    f = X('x105', b, c, d, e, list(C)[1], 115)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0106():
    b, c, d, e = a(116, 31)
    f = X('x106', b, c, d, e, list(C)[2], 116)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0107():
    b, c, d, e = a(117, 32)
    f = X('x107', b, c, d, e, list(C)[3], 117)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0108():
    b, c, d, e = a(118, 33)
    f = X('x108', b, c, d, e, list(C)[0], 118)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0109():
    b, c, d, e = a(119, 34)
    f = X('x109', b, c, d, e, list(C)[1], 119)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0110():
    b, c, d, e = a(120, 35)
    f = X('x110', b, c, d, e, list(C)[2], 120)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0111():
    b, c, d, e = a(121, 36)
    f = X('x111', b, c, d, e, list(C)[3], 121)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0112():
    b, c, d, e = a(122, 37)
    f = X('x112', b, c, d, e, list(C)[0], 122)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0113():
    b, c, d, e = a(123, 38)
    f = X('x113', b, c, d, e, list(C)[1], 123)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0114():
    b, c, d, e = a(124, 39)
    f = X('x114', b, c, d, e, list(C)[2], 124)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0115():
    b, c, d, e = a(125, 40)
    f = X('x115', b, c, d, e, list(C)[3], 125)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0116():
    b, c, d, e = a(126, 41)
    f = X('x116', b, c, d, e, list(C)[0], 126)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0117():
    b, c, d, e = a(127, 42)
    f = X('x117', b, c, d, e, list(C)[1], 127)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0118():
    b, c, d, e = a(128, 43)
    f = X('x118', b, c, d, e, list(C)[2], 128)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0119():
    b, c, d, e = a(129, 44)
    f = X('x119', b, c, d, e, list(C)[3], 129)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0120():
    b, c, d, e = a(130, 5)
    f = X('x120', b, c, d, e, list(C)[0], 130)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0121():
    b, c, d, e = a(131, 6)
    f = X('x121', b, c, d, e, list(C)[1], 131)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0122():
    b, c, d, e = a(132, 7)
    f = X('x122', b, c, d, e, list(C)[2], 132)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0123():
    b, c, d, e = a(133, 8)
    f = X('x123', b, c, d, e, list(C)[3], 133)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0124():
    b, c, d, e = a(134, 9)
    f = X('x124', b, c, d, e, list(C)[0], 134)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0125():
    b, c, d, e = a(135, 10)
    f = X('x125', b, c, d, e, list(C)[1], 135)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0126():
    b, c, d, e = a(136, 11)
    f = X('x126', b, c, d, e, list(C)[2], 136)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0127():
    b, c, d, e = a(137, 12)
    f = X('x127', b, c, d, e, list(C)[3], 137)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0128():
    b, c, d, e = a(138, 13)
    f = X('x128', b, c, d, e, list(C)[0], 138)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0129():
    b, c, d, e = a(139, 14)
    f = X('x129', b, c, d, e, list(C)[1], 139)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0130():
    b, c, d, e = a(140, 15)
    f = X('x130', b, c, d, e, list(C)[2], 140)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0131():
    b, c, d, e = a(141, 16)
    f = X('x131', b, c, d, e, list(C)[3], 141)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0132():
    b, c, d, e = a(142, 17)
    f = X('x132', b, c, d, e, list(C)[0], 142)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0133():
    b, c, d, e = a(143, 18)
    f = X('x133', b, c, d, e, list(C)[1], 143)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0134():
    b, c, d, e = a(144, 19)
    f = X('x134', b, c, d, e, list(C)[2], 144)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0135():
    b, c, d, e = a(145, 20)
    f = X('x135', b, c, d, e, list(C)[3], 145)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0136():
    b, c, d, e = a(146, 21)
    f = X('x136', b, c, d, e, list(C)[0], 146)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0137():
    b, c, d, e = a(147, 22)
    f = X('x137', b, c, d, e, list(C)[1], 147)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0138():
    b, c, d, e = a(148, 23)
    f = X('x138', b, c, d, e, list(C)[2], 148)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0139():
    b, c, d, e = a(149, 24)
    f = X('x139', b, c, d, e, list(C)[3], 149)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0140():
    b, c, d, e = a(150, 25)
    f = X('x140', b, c, d, e, list(C)[0], 150)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0141():
    b, c, d, e = a(151, 26)
    f = X('x141', b, c, d, e, list(C)[1], 151)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0142():
    b, c, d, e = a(152, 27)
    f = X('x142', b, c, d, e, list(C)[2], 152)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0143():
    b, c, d, e = a(153, 28)
    f = X('x143', b, c, d, e, list(C)[3], 153)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0144():
    b, c, d, e = a(154, 29)
    f = X('x144', b, c, d, e, list(C)[0], 154)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0145():
    b, c, d, e = a(155, 30)
    f = X('x145', b, c, d, e, list(C)[1], 155)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0146():
    b, c, d, e = a(156, 31)
    f = X('x146', b, c, d, e, list(C)[2], 156)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0147():
    b, c, d, e = a(157, 32)
    f = X('x147', b, c, d, e, list(C)[3], 157)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0148():
    b, c, d, e = a(158, 33)
    f = X('x148', b, c, d, e, list(C)[0], 158)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0149():
    b, c, d, e = a(159, 34)
    f = X('x149', b, c, d, e, list(C)[1], 159)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59

def test_x_0150():
    b, c, d, e = a(160, 35)
    f = X('x150', b, c, d, e, list(C)[2], 160)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0151():
    b, c, d, e = a(161, 36)
    f = X('x151', b, c, d, e, list(C)[3], 161)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0152():
    b, c, d, e = a(162, 37)
    f = X('x152', b, c, d, e, list(C)[0], 162)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0153():
    b, c, d, e = a(163, 38)
    f = X('x153', b, c, d, e, list(C)[1], 163)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0154():
    b, c, d, e = a(164, 39)
    f = X('x154', b, c, d, e, list(C)[2], 164)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0155():
    b, c, d, e = a(165, 40)
    f = X('x155', b, c, d, e, list(C)[3], 165)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0156():
    b, c, d, e = a(166, 41)
    f = X('x156', b, c, d, e, list(C)[0], 166)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0157():
    b, c, d, e = a(167, 42)
    f = X('x157', b, c, d, e, list(C)[1], 167)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0158():
    b, c, d, e = a(168, 43)
    f = X('x158', b, c, d, e, list(C)[2], 168)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0159():
    b, c, d, e = a(169, 44)
    f = X('x159', b, c, d, e, list(C)[3], 169)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0160():
    b, c, d, e = a(170, 5)
    f = X('x160', b, c, d, e, list(C)[0], 170)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0161():
    b, c, d, e = a(171, 6)
    f = X('x161', b, c, d, e, list(C)[1], 171)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0162():
    b, c, d, e = a(172, 7)
    f = X('x162', b, c, d, e, list(C)[2], 172)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0163():
    b, c, d, e = a(173, 8)
    f = X('x163', b, c, d, e, list(C)[3], 173)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0164():
    b, c, d, e = a(174, 9)
    f = X('x164', b, c, d, e, list(C)[0], 174)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0165():
    b, c, d, e = a(175, 10)
    f = X('x165', b, c, d, e, list(C)[1], 175)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0166():
    b, c, d, e = a(176, 11)
    f = X('x166', b, c, d, e, list(C)[2], 176)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0167():
    b, c, d, e = a(177, 12)
    f = X('x167', b, c, d, e, list(C)[3], 177)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0168():
    b, c, d, e = a(178, 13)
    f = X('x168', b, c, d, e, list(C)[0], 178)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0169():
    b, c, d, e = a(179, 14)
    f = X('x169', b, c, d, e, list(C)[1], 179)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0170():
    b, c, d, e = a(180, 15)
    f = X('x170', b, c, d, e, list(C)[2], 180)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0171():
    b, c, d, e = a(181, 16)
    f = X('x171', b, c, d, e, list(C)[3], 181)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0172():
    b, c, d, e = a(182, 17)
    f = X('x172', b, c, d, e, list(C)[0], 182)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0173():
    b, c, d, e = a(183, 18)
    f = X('x173', b, c, d, e, list(C)[1], 183)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0174():
    b, c, d, e = a(184, 19)
    f = X('x174', b, c, d, e, list(C)[2], 184)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0175():
    b, c, d, e = a(185, 20)
    f = X('x175', b, c, d, e, list(C)[3], 185)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0176():
    b, c, d, e = a(186, 21)
    f = X('x176', b, c, d, e, list(C)[0], 186)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0177():
    b, c, d, e = a(187, 22)
    f = X('x177', b, c, d, e, list(C)[1], 187)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0178():
    b, c, d, e = a(188, 23)
    f = X('x178', b, c, d, e, list(C)[2], 188)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0179():
    b, c, d, e = a(189, 24)
    f = X('x179', b, c, d, e, list(C)[3], 189)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0180():
    b, c, d, e = a(190, 25)
    f = X('x180', b, c, d, e, list(C)[0], 190)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0181():
    b, c, d, e = a(191, 26)
    f = X('x181', b, c, d, e, list(C)[1], 191)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0182():
    b, c, d, e = a(192, 27)
    f = X('x182', b, c, d, e, list(C)[2], 192)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0183():
    b, c, d, e = a(193, 28)
    f = X('x183', b, c, d, e, list(C)[3], 193)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0184():
    b, c, d, e = a(194, 29)
    f = X('x184', b, c, d, e, list(C)[0], 194)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0185():
    b, c, d, e = a(195, 30)
    f = X('x185', b, c, d, e, list(C)[1], 195)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0186():
    b, c, d, e = a(196, 31)
    f = X('x186', b, c, d, e, list(C)[2], 196)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0187():
    b, c, d, e = a(197, 32)
    f = X('x187', b, c, d, e, list(C)[3], 197)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0188():
    b, c, d, e = a(198, 33)
    f = X('x188', b, c, d, e, list(C)[0], 198)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0189():
    b, c, d, e = a(199, 34)
    f = X('x189', b, c, d, e, list(C)[1], 199)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0190():
    b, c, d, e = a(200, 35)
    f = X('x190', b, c, d, e, list(C)[2], 200)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0191():
    b, c, d, e = a(201, 36)
    f = X('x191', b, c, d, e, list(C)[3], 201)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0192():
    b, c, d, e = a(202, 37)
    f = X('x192', b, c, d, e, list(C)[0], 202)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0193():
    b, c, d, e = a(203, 38)
    f = X('x193', b, c, d, e, list(C)[1], 203)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0194():
    b, c, d, e = a(204, 39)
    f = X('x194', b, c, d, e, list(C)[2], 204)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0195():
    b, c, d, e = a(205, 40)
    f = X('x195', b, c, d, e, list(C)[3], 205)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0196():
    b, c, d, e = a(206, 41)
    f = X('x196', b, c, d, e, list(C)[0], 206)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0197():
    b, c, d, e = a(207, 42)
    f = X('x197', b, c, d, e, list(C)[1], 207)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0198():
    b, c, d, e = a(208, 43)
    f = X('x198', b, c, d, e, list(C)[2], 208)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0199():
    b, c, d, e = a(209, 44)
    f = X('x199', b, c, d, e, list(C)[3], 209)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59

def test_x_0200():
    b, c, d, e = a(210, 5)
    f = X('x200', b, c, d, e, list(C)[0], 210)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0201():
    b, c, d, e = a(211, 6)
    f = X('x201', b, c, d, e, list(C)[1], 211)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0202():
    b, c, d, e = a(212, 7)
    f = X('x202', b, c, d, e, list(C)[2], 212)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0203():
    b, c, d, e = a(213, 8)
    f = X('x203', b, c, d, e, list(C)[3], 213)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0204():
    b, c, d, e = a(214, 9)
    f = X('x204', b, c, d, e, list(C)[0], 214)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0205():
    b, c, d, e = a(215, 10)
    f = X('x205', b, c, d, e, list(C)[1], 215)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0206():
    b, c, d, e = a(216, 11)
    f = X('x206', b, c, d, e, list(C)[2], 216)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0207():
    b, c, d, e = a(217, 12)
    f = X('x207', b, c, d, e, list(C)[3], 217)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0208():
    b, c, d, e = a(218, 13)
    f = X('x208', b, c, d, e, list(C)[0], 218)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0209():
    b, c, d, e = a(219, 14)
    f = X('x209', b, c, d, e, list(C)[1], 219)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0210():
    b, c, d, e = a(220, 15)
    f = X('x210', b, c, d, e, list(C)[2], 220)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0211():
    b, c, d, e = a(221, 16)
    f = X('x211', b, c, d, e, list(C)[3], 221)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0212():
    b, c, d, e = a(222, 17)
    f = X('x212', b, c, d, e, list(C)[0], 222)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0213():
    b, c, d, e = a(223, 18)
    f = X('x213', b, c, d, e, list(C)[1], 223)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0214():
    b, c, d, e = a(224, 19)
    f = X('x214', b, c, d, e, list(C)[2], 224)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0215():
    b, c, d, e = a(225, 20)
    f = X('x215', b, c, d, e, list(C)[3], 225)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0216():
    b, c, d, e = a(226, 21)
    f = X('x216', b, c, d, e, list(C)[0], 226)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0217():
    b, c, d, e = a(227, 22)
    f = X('x217', b, c, d, e, list(C)[1], 227)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0218():
    b, c, d, e = a(228, 23)
    f = X('x218', b, c, d, e, list(C)[2], 228)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0219():
    b, c, d, e = a(229, 24)
    f = X('x219', b, c, d, e, list(C)[3], 229)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0220():
    b, c, d, e = a(230, 25)
    f = X('x220', b, c, d, e, list(C)[0], 230)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0221():
    b, c, d, e = a(231, 26)
    f = X('x221', b, c, d, e, list(C)[1], 231)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0222():
    b, c, d, e = a(232, 27)
    f = X('x222', b, c, d, e, list(C)[2], 232)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0223():
    b, c, d, e = a(233, 28)
    f = X('x223', b, c, d, e, list(C)[3], 233)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0224():
    b, c, d, e = a(234, 29)
    f = X('x224', b, c, d, e, list(C)[0], 234)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0225():
    b, c, d, e = a(235, 30)
    f = X('x225', b, c, d, e, list(C)[1], 235)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0226():
    b, c, d, e = a(236, 31)
    f = X('x226', b, c, d, e, list(C)[2], 236)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0227():
    b, c, d, e = a(237, 32)
    f = X('x227', b, c, d, e, list(C)[3], 237)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0228():
    b, c, d, e = a(238, 33)
    f = X('x228', b, c, d, e, list(C)[0], 238)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0229():
    b, c, d, e = a(239, 34)
    f = X('x229', b, c, d, e, list(C)[1], 239)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0230():
    b, c, d, e = a(240, 35)
    f = X('x230', b, c, d, e, list(C)[2], 240)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0231():
    b, c, d, e = a(241, 36)
    f = X('x231', b, c, d, e, list(C)[3], 241)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0232():
    b, c, d, e = a(242, 37)
    f = X('x232', b, c, d, e, list(C)[0], 242)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0233():
    b, c, d, e = a(243, 38)
    f = X('x233', b, c, d, e, list(C)[1], 243)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0234():
    b, c, d, e = a(244, 39)
    f = X('x234', b, c, d, e, list(C)[2], 244)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0235():
    b, c, d, e = a(245, 40)
    f = X('x235', b, c, d, e, list(C)[3], 245)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0236():
    b, c, d, e = a(246, 41)
    f = X('x236', b, c, d, e, list(C)[0], 246)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0237():
    b, c, d, e = a(247, 42)
    f = X('x237', b, c, d, e, list(C)[1], 247)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0238():
    b, c, d, e = a(248, 43)
    f = X('x238', b, c, d, e, list(C)[2], 248)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0239():
    b, c, d, e = a(249, 44)
    f = X('x239', b, c, d, e, list(C)[3], 249)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0240():
    b, c, d, e = a(250, 5)
    f = X('x240', b, c, d, e, list(C)[0], 250)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0241():
    b, c, d, e = a(251, 6)
    f = X('x241', b, c, d, e, list(C)[1], 251)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0242():
    b, c, d, e = a(252, 7)
    f = X('x242', b, c, d, e, list(C)[2], 252)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0243():
    b, c, d, e = a(253, 8)
    f = X('x243', b, c, d, e, list(C)[3], 253)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0244():
    b, c, d, e = a(254, 9)
    f = X('x244', b, c, d, e, list(C)[0], 254)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0245():
    b, c, d, e = a(255, 10)
    f = X('x245', b, c, d, e, list(C)[1], 255)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0246():
    b, c, d, e = a(256, 11)
    f = X('x246', b, c, d, e, list(C)[2], 256)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0247():
    b, c, d, e = a(257, 12)
    f = X('x247', b, c, d, e, list(C)[3], 257)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0248():
    b, c, d, e = a(258, 13)
    f = X('x248', b, c, d, e, list(C)[0], 258)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0249():
    b, c, d, e = a(259, 14)
    f = X('x249', b, c, d, e, list(C)[1], 259)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59

def test_x_0250():
    b, c, d, e = a(260, 15)
    f = X('x250', b, c, d, e, list(C)[2], 260)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0251():
    b, c, d, e = a(261, 16)
    f = X('x251', b, c, d, e, list(C)[3], 261)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0252():
    b, c, d, e = a(262, 17)
    f = X('x252', b, c, d, e, list(C)[0], 262)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0253():
    b, c, d, e = a(263, 18)
    f = X('x253', b, c, d, e, list(C)[1], 263)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0254():
    b, c, d, e = a(264, 19)
    f = X('x254', b, c, d, e, list(C)[2], 264)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0255():
    b, c, d, e = a(265, 20)
    f = X('x255', b, c, d, e, list(C)[3], 265)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0256():
    b, c, d, e = a(266, 21)
    f = X('x256', b, c, d, e, list(C)[0], 266)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0257():
    b, c, d, e = a(267, 22)
    f = X('x257', b, c, d, e, list(C)[1], 267)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0258():
    b, c, d, e = a(268, 23)
    f = X('x258', b, c, d, e, list(C)[2], 268)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0259():
    b, c, d, e = a(269, 24)
    f = X('x259', b, c, d, e, list(C)[3], 269)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0260():
    b, c, d, e = a(270, 25)
    f = X('x260', b, c, d, e, list(C)[0], 270)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0261():
    b, c, d, e = a(271, 26)
    f = X('x261', b, c, d, e, list(C)[1], 271)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0262():
    b, c, d, e = a(272, 27)
    f = X('x262', b, c, d, e, list(C)[2], 272)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0263():
    b, c, d, e = a(273, 28)
    f = X('x263', b, c, d, e, list(C)[3], 273)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0264():
    b, c, d, e = a(274, 29)
    f = X('x264', b, c, d, e, list(C)[0], 274)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0265():
    b, c, d, e = a(275, 30)
    f = X('x265', b, c, d, e, list(C)[1], 275)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0266():
    b, c, d, e = a(276, 31)
    f = X('x266', b, c, d, e, list(C)[2], 276)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0267():
    b, c, d, e = a(277, 32)
    f = X('x267', b, c, d, e, list(C)[3], 277)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0268():
    b, c, d, e = a(278, 33)
    f = X('x268', b, c, d, e, list(C)[0], 278)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0269():
    b, c, d, e = a(279, 34)
    f = X('x269', b, c, d, e, list(C)[1], 279)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0270():
    b, c, d, e = a(280, 35)
    f = X('x270', b, c, d, e, list(C)[2], 280)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0271():
    b, c, d, e = a(281, 36)
    f = X('x271', b, c, d, e, list(C)[3], 281)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0272():
    b, c, d, e = a(282, 37)
    f = X('x272', b, c, d, e, list(C)[0], 282)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0273():
    b, c, d, e = a(283, 38)
    f = X('x273', b, c, d, e, list(C)[1], 283)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0274():
    b, c, d, e = a(284, 39)
    f = X('x274', b, c, d, e, list(C)[2], 284)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0275():
    b, c, d, e = a(285, 40)
    f = X('x275', b, c, d, e, list(C)[3], 285)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0276():
    b, c, d, e = a(286, 41)
    f = X('x276', b, c, d, e, list(C)[0], 286)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0277():
    b, c, d, e = a(287, 42)
    f = X('x277', b, c, d, e, list(C)[1], 287)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0278():
    b, c, d, e = a(288, 43)
    f = X('x278', b, c, d, e, list(C)[2], 288)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0279():
    b, c, d, e = a(289, 44)
    f = X('x279', b, c, d, e, list(C)[3], 289)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0280():
    b, c, d, e = a(290, 5)
    f = X('x280', b, c, d, e, list(C)[0], 290)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0281():
    b, c, d, e = a(291, 6)
    f = X('x281', b, c, d, e, list(C)[1], 291)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0282():
    b, c, d, e = a(292, 7)
    f = X('x282', b, c, d, e, list(C)[2], 292)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0283():
    b, c, d, e = a(293, 8)
    f = X('x283', b, c, d, e, list(C)[3], 293)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0284():
    b, c, d, e = a(294, 9)
    f = X('x284', b, c, d, e, list(C)[0], 294)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0285():
    b, c, d, e = a(295, 10)
    f = X('x285', b, c, d, e, list(C)[1], 295)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0286():
    b, c, d, e = a(296, 11)
    f = X('x286', b, c, d, e, list(C)[2], 296)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0287():
    b, c, d, e = a(297, 12)
    f = X('x287', b, c, d, e, list(C)[3], 297)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0288():
    b, c, d, e = a(298, 13)
    f = X('x288', b, c, d, e, list(C)[0], 298)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0289():
    b, c, d, e = a(299, 14)
    f = X('x289', b, c, d, e, list(C)[1], 299)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0290():
    b, c, d, e = a(300, 15)
    f = X('x290', b, c, d, e, list(C)[2], 300)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0291():
    b, c, d, e = a(301, 16)
    f = X('x291', b, c, d, e, list(C)[3], 301)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0292():
    b, c, d, e = a(302, 17)
    f = X('x292', b, c, d, e, list(C)[0], 302)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0293():
    b, c, d, e = a(303, 18)
    f = X('x293', b, c, d, e, list(C)[1], 303)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0294():
    b, c, d, e = a(304, 19)
    f = X('x294', b, c, d, e, list(C)[2], 304)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0295():
    b, c, d, e = a(305, 20)
    f = X('x295', b, c, d, e, list(C)[3], 305)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0296():
    b, c, d, e = a(306, 21)
    f = X('x296', b, c, d, e, list(C)[0], 306)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0297():
    b, c, d, e = a(307, 22)
    f = X('x297', b, c, d, e, list(C)[1], 307)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0298():
    b, c, d, e = a(308, 23)
    f = X('x298', b, c, d, e, list(C)[2], 308)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0299():
    b, c, d, e = a(309, 24)
    f = X('x299', b, c, d, e, list(C)[3], 309)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59

def test_x_0300():
    b, c, d, e = a(310, 25)
    f = X('x300', b, c, d, e, list(C)[0], 310)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0301():
    b, c, d, e = a(311, 26)
    f = X('x301', b, c, d, e, list(C)[1], 311)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0302():
    b, c, d, e = a(312, 27)
    f = X('x302', b, c, d, e, list(C)[2], 312)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0303():
    b, c, d, e = a(313, 28)
    f = X('x303', b, c, d, e, list(C)[3], 313)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0304():
    b, c, d, e = a(314, 29)
    f = X('x304', b, c, d, e, list(C)[0], 314)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0305():
    b, c, d, e = a(315, 30)
    f = X('x305', b, c, d, e, list(C)[1], 315)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0306():
    b, c, d, e = a(316, 31)
    f = X('x306', b, c, d, e, list(C)[2], 316)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0307():
    b, c, d, e = a(317, 32)
    f = X('x307', b, c, d, e, list(C)[3], 317)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0308():
    b, c, d, e = a(318, 33)
    f = X('x308', b, c, d, e, list(C)[0], 318)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0309():
    b, c, d, e = a(319, 34)
    f = X('x309', b, c, d, e, list(C)[1], 319)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0310():
    b, c, d, e = a(320, 35)
    f = X('x310', b, c, d, e, list(C)[2], 320)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0311():
    b, c, d, e = a(321, 36)
    f = X('x311', b, c, d, e, list(C)[3], 321)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0312():
    b, c, d, e = a(322, 37)
    f = X('x312', b, c, d, e, list(C)[0], 322)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0313():
    b, c, d, e = a(323, 38)
    f = X('x313', b, c, d, e, list(C)[1], 323)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0314():
    b, c, d, e = a(324, 39)
    f = X('x314', b, c, d, e, list(C)[2], 324)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0315():
    b, c, d, e = a(325, 40)
    f = X('x315', b, c, d, e, list(C)[3], 325)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0316():
    b, c, d, e = a(326, 41)
    f = X('x316', b, c, d, e, list(C)[0], 326)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0317():
    b, c, d, e = a(327, 42)
    f = X('x317', b, c, d, e, list(C)[1], 327)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0318():
    b, c, d, e = a(328, 43)
    f = X('x318', b, c, d, e, list(C)[2], 328)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0319():
    b, c, d, e = a(329, 44)
    f = X('x319', b, c, d, e, list(C)[3], 329)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0320():
    b, c, d, e = a(330, 5)
    f = X('x320', b, c, d, e, list(C)[0], 330)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0321():
    b, c, d, e = a(331, 6)
    f = X('x321', b, c, d, e, list(C)[1], 331)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0322():
    b, c, d, e = a(332, 7)
    f = X('x322', b, c, d, e, list(C)[2], 332)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0323():
    b, c, d, e = a(333, 8)
    f = X('x323', b, c, d, e, list(C)[3], 333)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0324():
    b, c, d, e = a(334, 9)
    f = X('x324', b, c, d, e, list(C)[0], 334)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0325():
    b, c, d, e = a(335, 10)
    f = X('x325', b, c, d, e, list(C)[1], 335)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0326():
    b, c, d, e = a(336, 11)
    f = X('x326', b, c, d, e, list(C)[2], 336)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0327():
    b, c, d, e = a(337, 12)
    f = X('x327', b, c, d, e, list(C)[3], 337)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0328():
    b, c, d, e = a(338, 13)
    f = X('x328', b, c, d, e, list(C)[0], 338)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0329():
    b, c, d, e = a(339, 14)
    f = X('x329', b, c, d, e, list(C)[1], 339)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0330():
    b, c, d, e = a(340, 15)
    f = X('x330', b, c, d, e, list(C)[2], 340)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0331():
    b, c, d, e = a(341, 16)
    f = X('x331', b, c, d, e, list(C)[3], 341)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0332():
    b, c, d, e = a(342, 17)
    f = X('x332', b, c, d, e, list(C)[0], 342)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0333():
    b, c, d, e = a(343, 18)
    f = X('x333', b, c, d, e, list(C)[1], 343)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0334():
    b, c, d, e = a(344, 19)
    f = X('x334', b, c, d, e, list(C)[2], 344)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0335():
    b, c, d, e = a(345, 20)
    f = X('x335', b, c, d, e, list(C)[3], 345)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0336():
    b, c, d, e = a(346, 21)
    f = X('x336', b, c, d, e, list(C)[0], 346)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0337():
    b, c, d, e = a(347, 22)
    f = X('x337', b, c, d, e, list(C)[1], 347)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0338():
    b, c, d, e = a(348, 23)
    f = X('x338', b, c, d, e, list(C)[2], 348)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0339():
    b, c, d, e = a(349, 24)
    f = X('x339', b, c, d, e, list(C)[3], 349)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0340():
    b, c, d, e = a(350, 25)
    f = X('x340', b, c, d, e, list(C)[0], 350)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0341():
    b, c, d, e = a(351, 26)
    f = X('x341', b, c, d, e, list(C)[1], 351)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0342():
    b, c, d, e = a(352, 27)
    f = X('x342', b, c, d, e, list(C)[2], 352)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0343():
    b, c, d, e = a(353, 28)
    f = X('x343', b, c, d, e, list(C)[3], 353)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0344():
    b, c, d, e = a(354, 29)
    f = X('x344', b, c, d, e, list(C)[0], 354)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0345():
    b, c, d, e = a(355, 30)
    f = X('x345', b, c, d, e, list(C)[1], 355)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0346():
    b, c, d, e = a(356, 31)
    f = X('x346', b, c, d, e, list(C)[2], 356)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0347():
    b, c, d, e = a(357, 32)
    f = X('x347', b, c, d, e, list(C)[3], 357)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0348():
    b, c, d, e = a(358, 33)
    f = X('x348', b, c, d, e, list(C)[0], 358)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0349():
    b, c, d, e = a(359, 34)
    f = X('x349', b, c, d, e, list(C)[1], 359)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59

def test_x_0350():
    b, c, d, e = a(360, 35)
    f = X('x350', b, c, d, e, list(C)[2], 360)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0351():
    b, c, d, e = a(361, 36)
    f = X('x351', b, c, d, e, list(C)[3], 361)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0352():
    b, c, d, e = a(362, 37)
    f = X('x352', b, c, d, e, list(C)[0], 362)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0353():
    b, c, d, e = a(363, 38)
    f = X('x353', b, c, d, e, list(C)[1], 363)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0354():
    b, c, d, e = a(364, 39)
    f = X('x354', b, c, d, e, list(C)[2], 364)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0355():
    b, c, d, e = a(365, 40)
    f = X('x355', b, c, d, e, list(C)[3], 365)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0356():
    b, c, d, e = a(366, 41)
    f = X('x356', b, c, d, e, list(C)[0], 366)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0357():
    b, c, d, e = a(367, 42)
    f = X('x357', b, c, d, e, list(C)[1], 367)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0358():
    b, c, d, e = a(368, 43)
    f = X('x358', b, c, d, e, list(C)[2], 368)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0359():
    b, c, d, e = a(369, 44)
    f = X('x359', b, c, d, e, list(C)[3], 369)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0360():
    b, c, d, e = a(370, 5)
    f = X('x360', b, c, d, e, list(C)[0], 370)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0361():
    b, c, d, e = a(371, 6)
    f = X('x361', b, c, d, e, list(C)[1], 371)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0362():
    b, c, d, e = a(372, 7)
    f = X('x362', b, c, d, e, list(C)[2], 372)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0363():
    b, c, d, e = a(373, 8)
    f = X('x363', b, c, d, e, list(C)[3], 373)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0364():
    b, c, d, e = a(374, 9)
    f = X('x364', b, c, d, e, list(C)[0], 374)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0365():
    b, c, d, e = a(375, 10)
    f = X('x365', b, c, d, e, list(C)[1], 375)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0366():
    b, c, d, e = a(376, 11)
    f = X('x366', b, c, d, e, list(C)[2], 376)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0367():
    b, c, d, e = a(377, 12)
    f = X('x367', b, c, d, e, list(C)[3], 377)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0368():
    b, c, d, e = a(378, 13)
    f = X('x368', b, c, d, e, list(C)[0], 378)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0369():
    b, c, d, e = a(379, 14)
    f = X('x369', b, c, d, e, list(C)[1], 379)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0370():
    b, c, d, e = a(380, 15)
    f = X('x370', b, c, d, e, list(C)[2], 380)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0371():
    b, c, d, e = a(381, 16)
    f = X('x371', b, c, d, e, list(C)[3], 381)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0372():
    b, c, d, e = a(382, 17)
    f = X('x372', b, c, d, e, list(C)[0], 382)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0373():
    b, c, d, e = a(383, 18)
    f = X('x373', b, c, d, e, list(C)[1], 383)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0374():
    b, c, d, e = a(384, 19)
    f = X('x374', b, c, d, e, list(C)[2], 384)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0375():
    b, c, d, e = a(385, 20)
    f = X('x375', b, c, d, e, list(C)[3], 385)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0376():
    b, c, d, e = a(386, 21)
    f = X('x376', b, c, d, e, list(C)[0], 386)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0377():
    b, c, d, e = a(387, 22)
    f = X('x377', b, c, d, e, list(C)[1], 387)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0378():
    b, c, d, e = a(388, 23)
    f = X('x378', b, c, d, e, list(C)[2], 388)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0379():
    b, c, d, e = a(389, 24)
    f = X('x379', b, c, d, e, list(C)[3], 389)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0380():
    b, c, d, e = a(390, 25)
    f = X('x380', b, c, d, e, list(C)[0], 390)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0381():
    b, c, d, e = a(391, 26)
    f = X('x381', b, c, d, e, list(C)[1], 391)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0382():
    b, c, d, e = a(392, 27)
    f = X('x382', b, c, d, e, list(C)[2], 392)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0383():
    b, c, d, e = a(393, 28)
    f = X('x383', b, c, d, e, list(C)[3], 393)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0384():
    b, c, d, e = a(394, 29)
    f = X('x384', b, c, d, e, list(C)[0], 394)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0385():
    b, c, d, e = a(395, 30)
    f = X('x385', b, c, d, e, list(C)[1], 395)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0386():
    b, c, d, e = a(396, 31)
    f = X('x386', b, c, d, e, list(C)[2], 396)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0387():
    b, c, d, e = a(397, 32)
    f = X('x387', b, c, d, e, list(C)[3], 397)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0388():
    b, c, d, e = a(398, 33)
    f = X('x388', b, c, d, e, list(C)[0], 398)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0389():
    b, c, d, e = a(399, 34)
    f = X('x389', b, c, d, e, list(C)[1], 399)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0390():
    b, c, d, e = a(400, 35)
    f = X('x390', b, c, d, e, list(C)[2], 400)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0391():
    b, c, d, e = a(401, 36)
    f = X('x391', b, c, d, e, list(C)[3], 401)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0392():
    b, c, d, e = a(402, 37)
    f = X('x392', b, c, d, e, list(C)[0], 402)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0393():
    b, c, d, e = a(403, 38)
    f = X('x393', b, c, d, e, list(C)[1], 403)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0394():
    b, c, d, e = a(404, 39)
    f = X('x394', b, c, d, e, list(C)[2], 404)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0395():
    b, c, d, e = a(405, 40)
    f = X('x395', b, c, d, e, list(C)[3], 405)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0396():
    b, c, d, e = a(406, 41)
    f = X('x396', b, c, d, e, list(C)[0], 406)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0397():
    b, c, d, e = a(407, 42)
    f = X('x397', b, c, d, e, list(C)[1], 407)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0398():
    b, c, d, e = a(408, 43)
    f = X('x398', b, c, d, e, list(C)[2], 408)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0399():
    b, c, d, e = a(409, 44)
    f = X('x399', b, c, d, e, list(C)[3], 409)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59

def test_x_0400():
    b, c, d, e = a(410, 5)
    f = X('x400', b, c, d, e, list(C)[0], 410)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0401():
    b, c, d, e = a(411, 6)
    f = X('x401', b, c, d, e, list(C)[1], 411)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0402():
    b, c, d, e = a(412, 7)
    f = X('x402', b, c, d, e, list(C)[2], 412)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0403():
    b, c, d, e = a(413, 8)
    f = X('x403', b, c, d, e, list(C)[3], 413)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0404():
    b, c, d, e = a(414, 9)
    f = X('x404', b, c, d, e, list(C)[0], 414)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0405():
    b, c, d, e = a(415, 10)
    f = X('x405', b, c, d, e, list(C)[1], 415)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0406():
    b, c, d, e = a(416, 11)
    f = X('x406', b, c, d, e, list(C)[2], 416)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0407():
    b, c, d, e = a(417, 12)
    f = X('x407', b, c, d, e, list(C)[3], 417)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0408():
    b, c, d, e = a(418, 13)
    f = X('x408', b, c, d, e, list(C)[0], 418)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0409():
    b, c, d, e = a(419, 14)
    f = X('x409', b, c, d, e, list(C)[1], 419)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0410():
    b, c, d, e = a(420, 15)
    f = X('x410', b, c, d, e, list(C)[2], 420)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0411():
    b, c, d, e = a(421, 16)
    f = X('x411', b, c, d, e, list(C)[3], 421)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0412():
    b, c, d, e = a(422, 17)
    f = X('x412', b, c, d, e, list(C)[0], 422)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0413():
    b, c, d, e = a(423, 18)
    f = X('x413', b, c, d, e, list(C)[1], 423)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0414():
    b, c, d, e = a(424, 19)
    f = X('x414', b, c, d, e, list(C)[2], 424)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0415():
    b, c, d, e = a(425, 20)
    f = X('x415', b, c, d, e, list(C)[3], 425)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0416():
    b, c, d, e = a(426, 21)
    f = X('x416', b, c, d, e, list(C)[0], 426)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0417():
    b, c, d, e = a(427, 22)
    f = X('x417', b, c, d, e, list(C)[1], 427)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0418():
    b, c, d, e = a(428, 23)
    f = X('x418', b, c, d, e, list(C)[2], 428)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0419():
    b, c, d, e = a(429, 24)
    f = X('x419', b, c, d, e, list(C)[3], 429)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0420():
    b, c, d, e = a(430, 25)
    f = X('x420', b, c, d, e, list(C)[0], 430)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0421():
    b, c, d, e = a(431, 26)
    f = X('x421', b, c, d, e, list(C)[1], 431)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0422():
    b, c, d, e = a(432, 27)
    f = X('x422', b, c, d, e, list(C)[2], 432)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0423():
    b, c, d, e = a(433, 28)
    f = X('x423', b, c, d, e, list(C)[3], 433)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0424():
    b, c, d, e = a(434, 29)
    f = X('x424', b, c, d, e, list(C)[0], 434)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0425():
    b, c, d, e = a(435, 30)
    f = X('x425', b, c, d, e, list(C)[1], 435)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0426():
    b, c, d, e = a(436, 31)
    f = X('x426', b, c, d, e, list(C)[2], 436)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0427():
    b, c, d, e = a(437, 32)
    f = X('x427', b, c, d, e, list(C)[3], 437)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0428():
    b, c, d, e = a(438, 33)
    f = X('x428', b, c, d, e, list(C)[0], 438)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0429():
    b, c, d, e = a(439, 34)
    f = X('x429', b, c, d, e, list(C)[1], 439)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0430():
    b, c, d, e = a(440, 35)
    f = X('x430', b, c, d, e, list(C)[2], 440)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0431():
    b, c, d, e = a(441, 36)
    f = X('x431', b, c, d, e, list(C)[3], 441)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0432():
    b, c, d, e = a(442, 37)
    f = X('x432', b, c, d, e, list(C)[0], 442)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0433():
    b, c, d, e = a(443, 38)
    f = X('x433', b, c, d, e, list(C)[1], 443)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0434():
    b, c, d, e = a(444, 39)
    f = X('x434', b, c, d, e, list(C)[2], 444)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0435():
    b, c, d, e = a(445, 40)
    f = X('x435', b, c, d, e, list(C)[3], 445)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0436():
    b, c, d, e = a(446, 41)
    f = X('x436', b, c, d, e, list(C)[0], 446)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0437():
    b, c, d, e = a(447, 42)
    f = X('x437', b, c, d, e, list(C)[1], 447)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0438():
    b, c, d, e = a(448, 43)
    f = X('x438', b, c, d, e, list(C)[2], 448)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0439():
    b, c, d, e = a(449, 44)
    f = X('x439', b, c, d, e, list(C)[3], 449)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0440():
    b, c, d, e = a(450, 5)
    f = X('x440', b, c, d, e, list(C)[0], 450)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0441():
    b, c, d, e = a(451, 6)
    f = X('x441', b, c, d, e, list(C)[1], 451)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0442():
    b, c, d, e = a(452, 7)
    f = X('x442', b, c, d, e, list(C)[2], 452)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0443():
    b, c, d, e = a(453, 8)
    f = X('x443', b, c, d, e, list(C)[3], 453)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0444():
    b, c, d, e = a(454, 9)
    f = X('x444', b, c, d, e, list(C)[0], 454)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0445():
    b, c, d, e = a(455, 10)
    f = X('x445', b, c, d, e, list(C)[1], 455)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0446():
    b, c, d, e = a(456, 11)
    f = X('x446', b, c, d, e, list(C)[2], 456)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0447():
    b, c, d, e = a(457, 12)
    f = X('x447', b, c, d, e, list(C)[3], 457)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0448():
    b, c, d, e = a(458, 13)
    f = X('x448', b, c, d, e, list(C)[0], 458)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0449():
    b, c, d, e = a(459, 14)
    f = X('x449', b, c, d, e, list(C)[1], 459)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59

def test_x_0450():
    b, c, d, e = a(460, 15)
    f = X('x450', b, c, d, e, list(C)[2], 460)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0451():
    b, c, d, e = a(461, 16)
    f = X('x451', b, c, d, e, list(C)[3], 461)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0452():
    b, c, d, e = a(462, 17)
    f = X('x452', b, c, d, e, list(C)[0], 462)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0453():
    b, c, d, e = a(463, 18)
    f = X('x453', b, c, d, e, list(C)[1], 463)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0454():
    b, c, d, e = a(464, 19)
    f = X('x454', b, c, d, e, list(C)[2], 464)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0455():
    b, c, d, e = a(465, 20)
    f = X('x455', b, c, d, e, list(C)[3], 465)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0456():
    b, c, d, e = a(466, 21)
    f = X('x456', b, c, d, e, list(C)[0], 466)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0457():
    b, c, d, e = a(467, 22)
    f = X('x457', b, c, d, e, list(C)[1], 467)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0458():
    b, c, d, e = a(468, 23)
    f = X('x458', b, c, d, e, list(C)[2], 468)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0459():
    b, c, d, e = a(469, 24)
    f = X('x459', b, c, d, e, list(C)[3], 469)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0460():
    b, c, d, e = a(470, 25)
    f = X('x460', b, c, d, e, list(C)[0], 470)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0461():
    b, c, d, e = a(471, 26)
    f = X('x461', b, c, d, e, list(C)[1], 471)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0462():
    b, c, d, e = a(472, 27)
    f = X('x462', b, c, d, e, list(C)[2], 472)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0463():
    b, c, d, e = a(473, 28)
    f = X('x463', b, c, d, e, list(C)[3], 473)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0464():
    b, c, d, e = a(474, 29)
    f = X('x464', b, c, d, e, list(C)[0], 474)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0465():
    b, c, d, e = a(475, 30)
    f = X('x465', b, c, d, e, list(C)[1], 475)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0466():
    b, c, d, e = a(476, 31)
    f = X('x466', b, c, d, e, list(C)[2], 476)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0467():
    b, c, d, e = a(477, 32)
    f = X('x467', b, c, d, e, list(C)[3], 477)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0468():
    b, c, d, e = a(478, 33)
    f = X('x468', b, c, d, e, list(C)[0], 478)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0469():
    b, c, d, e = a(479, 34)
    f = X('x469', b, c, d, e, list(C)[1], 479)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0470():
    b, c, d, e = a(480, 35)
    f = X('x470', b, c, d, e, list(C)[2], 480)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0471():
    b, c, d, e = a(481, 36)
    f = X('x471', b, c, d, e, list(C)[3], 481)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0472():
    b, c, d, e = a(482, 37)
    f = X('x472', b, c, d, e, list(C)[0], 482)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0473():
    b, c, d, e = a(483, 38)
    f = X('x473', b, c, d, e, list(C)[1], 483)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0474():
    b, c, d, e = a(484, 39)
    f = X('x474', b, c, d, e, list(C)[2], 484)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0475():
    b, c, d, e = a(485, 40)
    f = X('x475', b, c, d, e, list(C)[3], 485)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0476():
    b, c, d, e = a(486, 41)
    f = X('x476', b, c, d, e, list(C)[0], 486)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0477():
    b, c, d, e = a(487, 42)
    f = X('x477', b, c, d, e, list(C)[1], 487)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0478():
    b, c, d, e = a(488, 43)
    f = X('x478', b, c, d, e, list(C)[2], 488)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0479():
    b, c, d, e = a(489, 44)
    f = X('x479', b, c, d, e, list(C)[3], 489)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0480():
    b, c, d, e = a(490, 5)
    f = X('x480', b, c, d, e, list(C)[0], 490)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0481():
    b, c, d, e = a(491, 6)
    f = X('x481', b, c, d, e, list(C)[1], 491)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0482():
    b, c, d, e = a(492, 7)
    f = X('x482', b, c, d, e, list(C)[2], 492)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0483():
    b, c, d, e = a(493, 8)
    f = X('x483', b, c, d, e, list(C)[3], 493)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0484():
    b, c, d, e = a(494, 9)
    f = X('x484', b, c, d, e, list(C)[0], 494)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0485():
    b, c, d, e = a(495, 10)
    f = X('x485', b, c, d, e, list(C)[1], 495)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0486():
    b, c, d, e = a(496, 11)
    f = X('x486', b, c, d, e, list(C)[2], 496)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0487():
    b, c, d, e = a(497, 12)
    f = X('x487', b, c, d, e, list(C)[3], 497)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0488():
    b, c, d, e = a(498, 13)
    f = X('x488', b, c, d, e, list(C)[0], 498)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0489():
    b, c, d, e = a(499, 14)
    f = X('x489', b, c, d, e, list(C)[1], 499)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0490():
    b, c, d, e = a(500, 15)
    f = X('x490', b, c, d, e, list(C)[2], 500)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0491():
    b, c, d, e = a(501, 16)
    f = X('x491', b, c, d, e, list(C)[3], 501)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0492():
    b, c, d, e = a(502, 17)
    f = X('x492', b, c, d, e, list(C)[0], 502)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0493():
    b, c, d, e = a(503, 18)
    f = X('x493', b, c, d, e, list(C)[1], 503)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0494():
    b, c, d, e = a(504, 19)
    f = X('x494', b, c, d, e, list(C)[2], 504)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0495():
    b, c, d, e = a(505, 20)
    f = X('x495', b, c, d, e, list(C)[3], 505)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0496():
    b, c, d, e = a(506, 21)
    f = X('x496', b, c, d, e, list(C)[0], 506)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0497():
    b, c, d, e = a(507, 22)
    f = X('x497', b, c, d, e, list(C)[1], 507)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0498():
    b, c, d, e = a(508, 23)
    f = X('x498', b, c, d, e, list(C)[2], 508)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0499():
    b, c, d, e = a(509, 24)
    f = X('x499', b, c, d, e, list(C)[3], 509)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59

def test_x_0500():
    b, c, d, e = a(510, 25)
    f = X('x500', b, c, d, e, list(C)[0], 510)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0501():
    b, c, d, e = a(511, 26)
    f = X('x501', b, c, d, e, list(C)[1], 511)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0502():
    b, c, d, e = a(512, 27)
    f = X('x502', b, c, d, e, list(C)[2], 512)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0503():
    b, c, d, e = a(513, 28)
    f = X('x503', b, c, d, e, list(C)[3], 513)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0504():
    b, c, d, e = a(514, 29)
    f = X('x504', b, c, d, e, list(C)[0], 514)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0505():
    b, c, d, e = a(515, 30)
    f = X('x505', b, c, d, e, list(C)[1], 515)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0506():
    b, c, d, e = a(516, 31)
    f = X('x506', b, c, d, e, list(C)[2], 516)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0507():
    b, c, d, e = a(517, 32)
    f = X('x507', b, c, d, e, list(C)[3], 517)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0508():
    b, c, d, e = a(518, 33)
    f = X('x508', b, c, d, e, list(C)[0], 518)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0509():
    b, c, d, e = a(519, 34)
    f = X('x509', b, c, d, e, list(C)[1], 519)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0510():
    b, c, d, e = a(520, 35)
    f = X('x510', b, c, d, e, list(C)[2], 520)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0511():
    b, c, d, e = a(521, 36)
    f = X('x511', b, c, d, e, list(C)[3], 521)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0512():
    b, c, d, e = a(522, 37)
    f = X('x512', b, c, d, e, list(C)[0], 522)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0513():
    b, c, d, e = a(523, 38)
    f = X('x513', b, c, d, e, list(C)[1], 523)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0514():
    b, c, d, e = a(524, 39)
    f = X('x514', b, c, d, e, list(C)[2], 524)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0515():
    b, c, d, e = a(525, 40)
    f = X('x515', b, c, d, e, list(C)[3], 525)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0516():
    b, c, d, e = a(526, 41)
    f = X('x516', b, c, d, e, list(C)[0], 526)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0517():
    b, c, d, e = a(527, 42)
    f = X('x517', b, c, d, e, list(C)[1], 527)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0518():
    b, c, d, e = a(528, 43)
    f = X('x518', b, c, d, e, list(C)[2], 528)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0519():
    b, c, d, e = a(529, 44)
    f = X('x519', b, c, d, e, list(C)[3], 529)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0520():
    b, c, d, e = a(530, 5)
    f = X('x520', b, c, d, e, list(C)[0], 530)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0521():
    b, c, d, e = a(531, 6)
    f = X('x521', b, c, d, e, list(C)[1], 531)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0522():
    b, c, d, e = a(532, 7)
    f = X('x522', b, c, d, e, list(C)[2], 532)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0523():
    b, c, d, e = a(533, 8)
    f = X('x523', b, c, d, e, list(C)[3], 533)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0524():
    b, c, d, e = a(534, 9)
    f = X('x524', b, c, d, e, list(C)[0], 534)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0525():
    b, c, d, e = a(535, 10)
    f = X('x525', b, c, d, e, list(C)[1], 535)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0526():
    b, c, d, e = a(536, 11)
    f = X('x526', b, c, d, e, list(C)[2], 536)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0527():
    b, c, d, e = a(537, 12)
    f = X('x527', b, c, d, e, list(C)[3], 537)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0528():
    b, c, d, e = a(538, 13)
    f = X('x528', b, c, d, e, list(C)[0], 538)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0529():
    b, c, d, e = a(539, 14)
    f = X('x529', b, c, d, e, list(C)[1], 539)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0530():
    b, c, d, e = a(540, 15)
    f = X('x530', b, c, d, e, list(C)[2], 540)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0531():
    b, c, d, e = a(541, 16)
    f = X('x531', b, c, d, e, list(C)[3], 541)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0532():
    b, c, d, e = a(542, 17)
    f = X('x532', b, c, d, e, list(C)[0], 542)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0533():
    b, c, d, e = a(543, 18)
    f = X('x533', b, c, d, e, list(C)[1], 543)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0534():
    b, c, d, e = a(544, 19)
    f = X('x534', b, c, d, e, list(C)[2], 544)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0535():
    b, c, d, e = a(545, 20)
    f = X('x535', b, c, d, e, list(C)[3], 545)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0536():
    b, c, d, e = a(546, 21)
    f = X('x536', b, c, d, e, list(C)[0], 546)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0537():
    b, c, d, e = a(547, 22)
    f = X('x537', b, c, d, e, list(C)[1], 547)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0538():
    b, c, d, e = a(548, 23)
    f = X('x538', b, c, d, e, list(C)[2], 548)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0539():
    b, c, d, e = a(549, 24)
    f = X('x539', b, c, d, e, list(C)[3], 549)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0540():
    b, c, d, e = a(550, 25)
    f = X('x540', b, c, d, e, list(C)[0], 550)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0541():
    b, c, d, e = a(551, 26)
    f = X('x541', b, c, d, e, list(C)[1], 551)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0542():
    b, c, d, e = a(552, 27)
    f = X('x542', b, c, d, e, list(C)[2], 552)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0543():
    b, c, d, e = a(553, 28)
    f = X('x543', b, c, d, e, list(C)[3], 553)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0544():
    b, c, d, e = a(554, 29)
    f = X('x544', b, c, d, e, list(C)[0], 554)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0545():
    b, c, d, e = a(555, 30)
    f = X('x545', b, c, d, e, list(C)[1], 555)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0546():
    b, c, d, e = a(556, 31)
    f = X('x546', b, c, d, e, list(C)[2], 556)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0547():
    b, c, d, e = a(557, 32)
    f = X('x547', b, c, d, e, list(C)[3], 557)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0548():
    b, c, d, e = a(558, 33)
    f = X('x548', b, c, d, e, list(C)[0], 558)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0549():
    b, c, d, e = a(559, 34)
    f = X('x549', b, c, d, e, list(C)[1], 559)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59

def test_x_0550():
    b, c, d, e = a(560, 35)
    f = X('x550', b, c, d, e, list(C)[2], 560)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0551():
    b, c, d, e = a(561, 36)
    f = X('x551', b, c, d, e, list(C)[3], 561)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0552():
    b, c, d, e = a(562, 37)
    f = X('x552', b, c, d, e, list(C)[0], 562)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0553():
    b, c, d, e = a(563, 38)
    f = X('x553', b, c, d, e, list(C)[1], 563)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0554():
    b, c, d, e = a(564, 39)
    f = X('x554', b, c, d, e, list(C)[2], 564)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0555():
    b, c, d, e = a(565, 40)
    f = X('x555', b, c, d, e, list(C)[3], 565)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0556():
    b, c, d, e = a(566, 41)
    f = X('x556', b, c, d, e, list(C)[0], 566)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0557():
    b, c, d, e = a(567, 42)
    f = X('x557', b, c, d, e, list(C)[1], 567)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0558():
    b, c, d, e = a(568, 43)
    f = X('x558', b, c, d, e, list(C)[2], 568)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0559():
    b, c, d, e = a(569, 44)
    f = X('x559', b, c, d, e, list(C)[3], 569)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0560():
    b, c, d, e = a(570, 5)
    f = X('x560', b, c, d, e, list(C)[0], 570)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0561():
    b, c, d, e = a(571, 6)
    f = X('x561', b, c, d, e, list(C)[1], 571)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0562():
    b, c, d, e = a(572, 7)
    f = X('x562', b, c, d, e, list(C)[2], 572)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0563():
    b, c, d, e = a(573, 8)
    f = X('x563', b, c, d, e, list(C)[3], 573)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0564():
    b, c, d, e = a(574, 9)
    f = X('x564', b, c, d, e, list(C)[0], 574)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0565():
    b, c, d, e = a(575, 10)
    f = X('x565', b, c, d, e, list(C)[1], 575)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0566():
    b, c, d, e = a(576, 11)
    f = X('x566', b, c, d, e, list(C)[2], 576)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0567():
    b, c, d, e = a(577, 12)
    f = X('x567', b, c, d, e, list(C)[3], 577)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0568():
    b, c, d, e = a(578, 13)
    f = X('x568', b, c, d, e, list(C)[0], 578)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0569():
    b, c, d, e = a(579, 14)
    f = X('x569', b, c, d, e, list(C)[1], 579)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0570():
    b, c, d, e = a(580, 15)
    f = X('x570', b, c, d, e, list(C)[2], 580)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0571():
    b, c, d, e = a(581, 16)
    f = X('x571', b, c, d, e, list(C)[3], 581)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0572():
    b, c, d, e = a(582, 17)
    f = X('x572', b, c, d, e, list(C)[0], 582)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0573():
    b, c, d, e = a(583, 18)
    f = X('x573', b, c, d, e, list(C)[1], 583)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0574():
    b, c, d, e = a(584, 19)
    f = X('x574', b, c, d, e, list(C)[2], 584)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0575():
    b, c, d, e = a(585, 20)
    f = X('x575', b, c, d, e, list(C)[3], 585)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0576():
    b, c, d, e = a(586, 21)
    f = X('x576', b, c, d, e, list(C)[0], 586)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0577():
    b, c, d, e = a(587, 22)
    f = X('x577', b, c, d, e, list(C)[1], 587)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0578():
    b, c, d, e = a(588, 23)
    f = X('x578', b, c, d, e, list(C)[2], 588)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0579():
    b, c, d, e = a(589, 24)
    f = X('x579', b, c, d, e, list(C)[3], 589)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0580():
    b, c, d, e = a(590, 25)
    f = X('x580', b, c, d, e, list(C)[0], 590)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0581():
    b, c, d, e = a(591, 26)
    f = X('x581', b, c, d, e, list(C)[1], 591)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0582():
    b, c, d, e = a(592, 27)
    f = X('x582', b, c, d, e, list(C)[2], 592)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0583():
    b, c, d, e = a(593, 28)
    f = X('x583', b, c, d, e, list(C)[3], 593)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0584():
    b, c, d, e = a(594, 29)
    f = X('x584', b, c, d, e, list(C)[0], 594)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0585():
    b, c, d, e = a(595, 30)
    f = X('x585', b, c, d, e, list(C)[1], 595)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0586():
    b, c, d, e = a(596, 31)
    f = X('x586', b, c, d, e, list(C)[2], 596)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0587():
    b, c, d, e = a(597, 32)
    f = X('x587', b, c, d, e, list(C)[3], 597)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0588():
    b, c, d, e = a(598, 33)
    f = X('x588', b, c, d, e, list(C)[0], 598)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0589():
    b, c, d, e = a(599, 34)
    f = X('x589', b, c, d, e, list(C)[1], 599)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0590():
    b, c, d, e = a(600, 35)
    f = X('x590', b, c, d, e, list(C)[2], 600)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0591():
    b, c, d, e = a(601, 36)
    f = X('x591', b, c, d, e, list(C)[3], 601)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0592():
    b, c, d, e = a(602, 37)
    f = X('x592', b, c, d, e, list(C)[0], 602)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0593():
    b, c, d, e = a(603, 38)
    f = X('x593', b, c, d, e, list(C)[1], 603)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0594():
    b, c, d, e = a(604, 39)
    f = X('x594', b, c, d, e, list(C)[2], 604)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0595():
    b, c, d, e = a(605, 40)
    f = X('x595', b, c, d, e, list(C)[3], 605)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0596():
    b, c, d, e = a(606, 41)
    f = X('x596', b, c, d, e, list(C)[0], 606)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0597():
    b, c, d, e = a(607, 42)
    f = X('x597', b, c, d, e, list(C)[1], 607)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0598():
    b, c, d, e = a(608, 43)
    f = X('x598', b, c, d, e, list(C)[2], 608)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0599():
    b, c, d, e = a(609, 44)
    f = X('x599', b, c, d, e, list(C)[3], 609)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59

def test_x_0600():
    b, c, d, e = a(610, 5)
    f = X('x600', b, c, d, e, list(C)[0], 610)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0601():
    b, c, d, e = a(611, 6)
    f = X('x601', b, c, d, e, list(C)[1], 611)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0602():
    b, c, d, e = a(612, 7)
    f = X('x602', b, c, d, e, list(C)[2], 612)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0603():
    b, c, d, e = a(613, 8)
    f = X('x603', b, c, d, e, list(C)[3], 613)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0604():
    b, c, d, e = a(614, 9)
    f = X('x604', b, c, d, e, list(C)[0], 614)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0605():
    b, c, d, e = a(615, 10)
    f = X('x605', b, c, d, e, list(C)[1], 615)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0606():
    b, c, d, e = a(616, 11)
    f = X('x606', b, c, d, e, list(C)[2], 616)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0607():
    b, c, d, e = a(617, 12)
    f = X('x607', b, c, d, e, list(C)[3], 617)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0608():
    b, c, d, e = a(618, 13)
    f = X('x608', b, c, d, e, list(C)[0], 618)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0609():
    b, c, d, e = a(619, 14)
    f = X('x609', b, c, d, e, list(C)[1], 619)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0610():
    b, c, d, e = a(620, 15)
    f = X('x610', b, c, d, e, list(C)[2], 620)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0611():
    b, c, d, e = a(621, 16)
    f = X('x611', b, c, d, e, list(C)[3], 621)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0612():
    b, c, d, e = a(622, 17)
    f = X('x612', b, c, d, e, list(C)[0], 622)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0613():
    b, c, d, e = a(623, 18)
    f = X('x613', b, c, d, e, list(C)[1], 623)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0614():
    b, c, d, e = a(624, 19)
    f = X('x614', b, c, d, e, list(C)[2], 624)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0615():
    b, c, d, e = a(625, 20)
    f = X('x615', b, c, d, e, list(C)[3], 625)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0616():
    b, c, d, e = a(626, 21)
    f = X('x616', b, c, d, e, list(C)[0], 626)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0617():
    b, c, d, e = a(627, 22)
    f = X('x617', b, c, d, e, list(C)[1], 627)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0618():
    b, c, d, e = a(628, 23)
    f = X('x618', b, c, d, e, list(C)[2], 628)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0619():
    b, c, d, e = a(629, 24)
    f = X('x619', b, c, d, e, list(C)[3], 629)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0620():
    b, c, d, e = a(630, 25)
    f = X('x620', b, c, d, e, list(C)[0], 630)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0621():
    b, c, d, e = a(631, 26)
    f = X('x621', b, c, d, e, list(C)[1], 631)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0622():
    b, c, d, e = a(632, 27)
    f = X('x622', b, c, d, e, list(C)[2], 632)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0623():
    b, c, d, e = a(633, 28)
    f = X('x623', b, c, d, e, list(C)[3], 633)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0624():
    b, c, d, e = a(634, 29)
    f = X('x624', b, c, d, e, list(C)[0], 634)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0625():
    b, c, d, e = a(635, 30)
    f = X('x625', b, c, d, e, list(C)[1], 635)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0626():
    b, c, d, e = a(636, 31)
    f = X('x626', b, c, d, e, list(C)[2], 636)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0627():
    b, c, d, e = a(637, 32)
    f = X('x627', b, c, d, e, list(C)[3], 637)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0628():
    b, c, d, e = a(638, 33)
    f = X('x628', b, c, d, e, list(C)[0], 638)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0629():
    b, c, d, e = a(639, 34)
    f = X('x629', b, c, d, e, list(C)[1], 639)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0630():
    b, c, d, e = a(640, 35)
    f = X('x630', b, c, d, e, list(C)[2], 640)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0631():
    b, c, d, e = a(641, 36)
    f = X('x631', b, c, d, e, list(C)[3], 641)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0632():
    b, c, d, e = a(642, 37)
    f = X('x632', b, c, d, e, list(C)[0], 642)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0633():
    b, c, d, e = a(643, 38)
    f = X('x633', b, c, d, e, list(C)[1], 643)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0634():
    b, c, d, e = a(644, 39)
    f = X('x634', b, c, d, e, list(C)[2], 644)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0635():
    b, c, d, e = a(645, 40)
    f = X('x635', b, c, d, e, list(C)[3], 645)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0636():
    b, c, d, e = a(646, 41)
    f = X('x636', b, c, d, e, list(C)[0], 646)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0637():
    b, c, d, e = a(647, 42)
    f = X('x637', b, c, d, e, list(C)[1], 647)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0638():
    b, c, d, e = a(648, 43)
    f = X('x638', b, c, d, e, list(C)[2], 648)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0639():
    b, c, d, e = a(649, 44)
    f = X('x639', b, c, d, e, list(C)[3], 649)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0640():
    b, c, d, e = a(650, 5)
    f = X('x640', b, c, d, e, list(C)[0], 650)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0641():
    b, c, d, e = a(651, 6)
    f = X('x641', b, c, d, e, list(C)[1], 651)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0642():
    b, c, d, e = a(652, 7)
    f = X('x642', b, c, d, e, list(C)[2], 652)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0643():
    b, c, d, e = a(653, 8)
    f = X('x643', b, c, d, e, list(C)[3], 653)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0644():
    b, c, d, e = a(654, 9)
    f = X('x644', b, c, d, e, list(C)[0], 654)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0645():
    b, c, d, e = a(655, 10)
    f = X('x645', b, c, d, e, list(C)[1], 655)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0646():
    b, c, d, e = a(656, 11)
    f = X('x646', b, c, d, e, list(C)[2], 656)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0647():
    b, c, d, e = a(657, 12)
    f = X('x647', b, c, d, e, list(C)[3], 657)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0648():
    b, c, d, e = a(658, 13)
    f = X('x648', b, c, d, e, list(C)[0], 658)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0649():
    b, c, d, e = a(659, 14)
    f = X('x649', b, c, d, e, list(C)[1], 659)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59

def test_x_0650():
    b, c, d, e = a(660, 15)
    f = X('x650', b, c, d, e, list(C)[2], 660)
    g = f.r(10)
    assert f.i == 10
    assert len(g) >= 10

def test_x_0651():
    b, c, d, e = a(661, 16)
    f = X('x651', b, c, d, e, list(C)[3], 661)
    g = f.r(11)
    assert f.i == 11
    assert len(g) >= 11

def test_x_0652():
    b, c, d, e = a(662, 17)
    f = X('x652', b, c, d, e, list(C)[0], 662)
    g = f.r(12)
    assert f.i == 12
    assert len(g) >= 12

def test_x_0653():
    b, c, d, e = a(663, 18)
    f = X('x653', b, c, d, e, list(C)[1], 663)
    g = f.r(13)
    assert f.i == 13
    assert len(g) >= 13

def test_x_0654():
    b, c, d, e = a(664, 19)
    f = X('x654', b, c, d, e, list(C)[2], 664)
    g = f.r(14)
    assert f.i == 14
    assert len(g) >= 14

def test_x_0655():
    b, c, d, e = a(665, 20)
    f = X('x655', b, c, d, e, list(C)[3], 665)
    g = f.r(15)
    assert f.i == 15
    assert len(g) >= 15

def test_x_0656():
    b, c, d, e = a(666, 21)
    f = X('x656', b, c, d, e, list(C)[0], 666)
    g = f.r(16)
    assert f.i == 16
    assert len(g) >= 16

def test_x_0657():
    b, c, d, e = a(667, 22)
    f = X('x657', b, c, d, e, list(C)[1], 667)
    g = f.r(17)
    assert f.i == 17
    assert len(g) >= 17

def test_x_0658():
    b, c, d, e = a(668, 23)
    f = X('x658', b, c, d, e, list(C)[2], 668)
    g = f.r(18)
    assert f.i == 18
    assert len(g) >= 18

def test_x_0659():
    b, c, d, e = a(669, 24)
    f = X('x659', b, c, d, e, list(C)[3], 669)
    g = f.r(19)
    assert f.i == 19
    assert len(g) >= 19

def test_x_0660():
    b, c, d, e = a(670, 25)
    f = X('x660', b, c, d, e, list(C)[0], 670)
    g = f.r(20)
    assert f.i == 20
    assert len(g) >= 20

def test_x_0661():
    b, c, d, e = a(671, 26)
    f = X('x661', b, c, d, e, list(C)[1], 671)
    g = f.r(21)
    assert f.i == 21
    assert len(g) >= 21

def test_x_0662():
    b, c, d, e = a(672, 27)
    f = X('x662', b, c, d, e, list(C)[2], 672)
    g = f.r(22)
    assert f.i == 22
    assert len(g) >= 22

def test_x_0663():
    b, c, d, e = a(673, 28)
    f = X('x663', b, c, d, e, list(C)[3], 673)
    g = f.r(23)
    assert f.i == 23
    assert len(g) >= 23

def test_x_0664():
    b, c, d, e = a(674, 29)
    f = X('x664', b, c, d, e, list(C)[0], 674)
    g = f.r(24)
    assert f.i == 24
    assert len(g) >= 24

def test_x_0665():
    b, c, d, e = a(675, 30)
    f = X('x665', b, c, d, e, list(C)[1], 675)
    g = f.r(25)
    assert f.i == 25
    assert len(g) >= 25

def test_x_0666():
    b, c, d, e = a(676, 31)
    f = X('x666', b, c, d, e, list(C)[2], 676)
    g = f.r(26)
    assert f.i == 26
    assert len(g) >= 26

def test_x_0667():
    b, c, d, e = a(677, 32)
    f = X('x667', b, c, d, e, list(C)[3], 677)
    g = f.r(27)
    assert f.i == 27
    assert len(g) >= 27

def test_x_0668():
    b, c, d, e = a(678, 33)
    f = X('x668', b, c, d, e, list(C)[0], 678)
    g = f.r(28)
    assert f.i == 28
    assert len(g) >= 28

def test_x_0669():
    b, c, d, e = a(679, 34)
    f = X('x669', b, c, d, e, list(C)[1], 679)
    g = f.r(29)
    assert f.i == 29
    assert len(g) >= 29

def test_x_0670():
    b, c, d, e = a(680, 35)
    f = X('x670', b, c, d, e, list(C)[2], 680)
    g = f.r(30)
    assert f.i == 30
    assert len(g) >= 30

def test_x_0671():
    b, c, d, e = a(681, 36)
    f = X('x671', b, c, d, e, list(C)[3], 681)
    g = f.r(31)
    assert f.i == 31
    assert len(g) >= 31

def test_x_0672():
    b, c, d, e = a(682, 37)
    f = X('x672', b, c, d, e, list(C)[0], 682)
    g = f.r(32)
    assert f.i == 32
    assert len(g) >= 32

def test_x_0673():
    b, c, d, e = a(683, 38)
    f = X('x673', b, c, d, e, list(C)[1], 683)
    g = f.r(33)
    assert f.i == 33
    assert len(g) >= 33

def test_x_0674():
    b, c, d, e = a(684, 39)
    f = X('x674', b, c, d, e, list(C)[2], 684)
    g = f.r(34)
    assert f.i == 34
    assert len(g) >= 34

def test_x_0675():
    b, c, d, e = a(685, 40)
    f = X('x675', b, c, d, e, list(C)[3], 685)
    g = f.r(35)
    assert f.i == 35
    assert len(g) >= 35

def test_x_0676():
    b, c, d, e = a(686, 41)
    f = X('x676', b, c, d, e, list(C)[0], 686)
    g = f.r(36)
    assert f.i == 36
    assert len(g) >= 36

def test_x_0677():
    b, c, d, e = a(687, 42)
    f = X('x677', b, c, d, e, list(C)[1], 687)
    g = f.r(37)
    assert f.i == 37
    assert len(g) >= 37

def test_x_0678():
    b, c, d, e = a(688, 43)
    f = X('x678', b, c, d, e, list(C)[2], 688)
    g = f.r(38)
    assert f.i == 38
    assert len(g) >= 38

def test_x_0679():
    b, c, d, e = a(689, 44)
    f = X('x679', b, c, d, e, list(C)[3], 689)
    g = f.r(39)
    assert f.i == 39
    assert len(g) >= 39

def test_x_0680():
    b, c, d, e = a(690, 5)
    f = X('x680', b, c, d, e, list(C)[0], 690)
    g = f.r(40)
    assert f.i == 40
    assert len(g) >= 40

def test_x_0681():
    b, c, d, e = a(691, 6)
    f = X('x681', b, c, d, e, list(C)[1], 691)
    g = f.r(41)
    assert f.i == 41
    assert len(g) >= 41

def test_x_0682():
    b, c, d, e = a(692, 7)
    f = X('x682', b, c, d, e, list(C)[2], 692)
    g = f.r(42)
    assert f.i == 42
    assert len(g) >= 42

def test_x_0683():
    b, c, d, e = a(693, 8)
    f = X('x683', b, c, d, e, list(C)[3], 693)
    g = f.r(43)
    assert f.i == 43
    assert len(g) >= 43

def test_x_0684():
    b, c, d, e = a(694, 9)
    f = X('x684', b, c, d, e, list(C)[0], 694)
    g = f.r(44)
    assert f.i == 44
    assert len(g) >= 44

def test_x_0685():
    b, c, d, e = a(695, 10)
    f = X('x685', b, c, d, e, list(C)[1], 695)
    g = f.r(45)
    assert f.i == 45
    assert len(g) >= 45

def test_x_0686():
    b, c, d, e = a(696, 11)
    f = X('x686', b, c, d, e, list(C)[2], 696)
    g = f.r(46)
    assert f.i == 46
    assert len(g) >= 46

def test_x_0687():
    b, c, d, e = a(697, 12)
    f = X('x687', b, c, d, e, list(C)[3], 697)
    g = f.r(47)
    assert f.i == 47
    assert len(g) >= 47

def test_x_0688():
    b, c, d, e = a(698, 13)
    f = X('x688', b, c, d, e, list(C)[0], 698)
    g = f.r(48)
    assert f.i == 48
    assert len(g) >= 48

def test_x_0689():
    b, c, d, e = a(699, 14)
    f = X('x689', b, c, d, e, list(C)[1], 699)
    g = f.r(49)
    assert f.i == 49
    assert len(g) >= 49

def test_x_0690():
    b, c, d, e = a(700, 15)
    f = X('x690', b, c, d, e, list(C)[2], 700)
    g = f.r(50)
    assert f.i == 50
    assert len(g) >= 50

def test_x_0691():
    b, c, d, e = a(701, 16)
    f = X('x691', b, c, d, e, list(C)[3], 701)
    g = f.r(51)
    assert f.i == 51
    assert len(g) >= 51

def test_x_0692():
    b, c, d, e = a(702, 17)
    f = X('x692', b, c, d, e, list(C)[0], 702)
    g = f.r(52)
    assert f.i == 52
    assert len(g) >= 52

def test_x_0693():
    b, c, d, e = a(703, 18)
    f = X('x693', b, c, d, e, list(C)[1], 703)
    g = f.r(53)
    assert f.i == 53
    assert len(g) >= 53

def test_x_0694():
    b, c, d, e = a(704, 19)
    f = X('x694', b, c, d, e, list(C)[2], 704)
    g = f.r(54)
    assert f.i == 54
    assert len(g) >= 54

def test_x_0695():
    b, c, d, e = a(705, 20)
    f = X('x695', b, c, d, e, list(C)[3], 705)
    g = f.r(55)
    assert f.i == 55
    assert len(g) >= 55

def test_x_0696():
    b, c, d, e = a(706, 21)
    f = X('x696', b, c, d, e, list(C)[0], 706)
    g = f.r(56)
    assert f.i == 56
    assert len(g) >= 56

def test_x_0697():
    b, c, d, e = a(707, 22)
    f = X('x697', b, c, d, e, list(C)[1], 707)
    g = f.r(57)
    assert f.i == 57
    assert len(g) >= 57

def test_x_0698():
    b, c, d, e = a(708, 23)
    f = X('x698', b, c, d, e, list(C)[2], 708)
    g = f.r(58)
    assert f.i == 58
    assert len(g) >= 58

def test_x_0699():
    b, c, d, e = a(709, 24)
    f = X('x699', b, c, d, e, list(C)[3], 709)
    g = f.r(59)
    assert f.i == 59
    assert len(g) >= 59
