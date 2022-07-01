import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0001_4_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0001_4 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map'
    header.mapModel       = 'T0001.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T0001._SN', 'ED6_DT21/T0001_1._SN', 'ED6_DT21/T0001_2._SN', 'ED6_DT21/T0001_3._SN', 'ED6_DT21/T0001_4._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5299
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0001,
            initScena       = 0x0000,
            initFunction    = 0x0002,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    Talk(
        (
            TxtCtl.ShowAll,
            '这是事件。请选择。',
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C7(): pass

    label('loc_C7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_224',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '●从最初开始\n'),
            TXT(0x01, '●序章\n'),
            TXT(0x02, '●一章\n'),
            TXT(0x03, '●二章\n'),
            TXT(0x04, '●三章\n'),
            TXT(0x05, '●四章\n'),
            TXT(0x06, '●五章\n'),
            TXT(0x07, '●六章\n'),
            TXT(0x08, '●七章\n'),
            TXT(0x09, '●八章\n'),
            TXT(0x0A, '●最终章\n'),
            TXT(0x0B, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    Call(4, 0x0002)
    Call(4, 0x0003)
    Call(4, 0x0006)
    Call(4, 0x0009)
    Call(4, 0x000C)
    Call(4, 0x000F)
    Call(4, 0x0012)
    Call(4, 0x0015)
    Call(4, 0x0018)
    Call(4, 0x001B)
    Call(4, 0x001E)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_19B'),
        (0x00000001, 'loc_1CA'),
        (0x00000002, 'loc_1D1'),
        (0x00000003, 'loc_1D8'),
        (0x00000004, 'loc_1DF'),
        (0x00000005, 'loc_1E6'),
        (0x00000006, 'loc_1ED'),
        (0x00000007, 'loc_1F4'),
        (0x00000008, 'loc_1FB'),
        (0x00000009, 'loc_202'),
        (0x0000000A, 'loc_209'),
        (-1, 'loc_210'),
    )

    def _loc_19B(): pass

    label('loc_19B')

    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    AddItem(ItemTable['利贝尔王国地图'], 1)
    OP_BB(0x00, 0x00, 0x00200042)
    OP_BB(0x00, 0x01, 0x0000001E)
    OP_BD()
    OP_56(0x00)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    NewScene('ED6_DT21/T4201._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_221')

    def _loc_1CA(): pass

    label('loc_1CA')

    Call(4, 0x0005)

    Jump('loc_221')

    def _loc_1D1(): pass

    label('loc_1D1')

    Call(4, 0x0008)

    Jump('loc_221')

    def _loc_1D8(): pass

    label('loc_1D8')

    Call(4, 0x000B)

    Jump('loc_221')

    def _loc_1DF(): pass

    label('loc_1DF')

    Call(4, 0x000E)

    Jump('loc_221')

    def _loc_1E6(): pass

    label('loc_1E6')

    Call(4, 0x0011)

    Jump('loc_221')

    def _loc_1ED(): pass

    label('loc_1ED')

    Call(4, 0x0014)

    Jump('loc_221')

    def _loc_1F4(): pass

    label('loc_1F4')

    Call(4, 0x0017)

    Jump('loc_221')

    def _loc_1FB(): pass

    label('loc_1FB')

    Call(4, 0x001A)

    Jump('loc_221')

    def _loc_202(): pass

    label('loc_202')

    Call(4, 0x001D)

    Jump('loc_221')

    def _loc_209(): pass

    label('loc_209')

    Call(4, 0x0020)

    Jump('loc_221')

    def _loc_210(): pass

    label('loc_210')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)

    Jump('loc_221')

    def _loc_221(): pass

    label('loc_221')

    Jump('loc_C7')

    def _loc_224(): pass

    label('loc_224')

    OP_5F(0x0001)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x234
@scena.Code('Init')
def Init():
    OP_56(0x00)
    Call(4, 0x0002)
    Call(4, 0x0003)
    Call(4, 0x0006)
    Call(4, 0x0009)
    Call(4, 0x000C)
    Call(4, 0x000F)
    Call(4, 0x0012)
    Call(4, 0x0015)
    Call(4, 0x0018)
    Call(4, 0x001B)
    Call(4, 0x001E)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    AddItem(ItemTable['利贝尔王国地图'], 1)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1002)
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    OP_A2(0x1003)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    FormationDelMember(0x08, 0xFF)
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    OP_BB(0x00, 0x00, 0x00200042)
    OP_BB(0x00, 0x01, 0x0000001E)
    OP_BD()
    OP_A3(0x10F1)
    OP_A2(0x10F1)
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    OP_A3(0x10F1)
    OP_A2(0x1004)
    OP_A2(0x1005)
    OP_A2(0x1006)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    OP_A2(0x1007)
    OP_A2(0x1008)
    OP_A2(0x1009)
    OP_A2(0x100A)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x100B)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF9, 0xFF)
    OP_A2(0x100C)
    OP_A2(0x100D)
    OP_A2(0x100E)
    OP_A2(0x100F)
    OP_A2(0x1010)
    OP_A2(0x1011)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1012)
    OP_A2(0x101B)
    OP_A2(0x101C)
    OP_A2(0x101D)
    OP_A2(0x101E)
    OP_A2(0x101F)
    OP_A2(0x1020)
    OP_A2(0x1021)
    OP_A2(0x1022)
    OP_A2(0x1023)
    OP_A2(0x1024)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1202)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x1203)
    OP_A2(0x1204)
    OP_A2(0x1205)
    OP_A2(0x1207)
    OP_A2(0x1208)
    OP_A2(0x1209)
    OP_A2(0x120A)
    OP_A2(0x120B)
    OP_A2(0x120C)
    OP_A2(0x120D)
    OP_A2(0x1206)
    OP_A2(0x120E)
    OP_A2(0x120F)
    OP_A2(0x1210)
    OP_A2(0x1211)
    OP_A2(0x1212)
    OP_A2(0x1213)
    OP_A2(0x1214)
    OP_A2(0x1215)
    OP_A2(0x1216)
    OP_A2(0x1217)
    OP_A2(0x1218)
    OP_A2(0x1219)
    OP_A2(0x10F0)
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    OP_A3(0x10F0)
    OP_A2(0x121A)
    FormationDelMember(0x08, 0xFF)
    OP_A2(0x121B)
    OP_A2(0x121C)
    OP_A2(0x10F0)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    OP_A3(0x10F0)
    FormationAddMember(ChrTable['朵洛希'], 0xFF, 0xFF)
    OP_A2(0x121D)
    OP_A2(0x10F0)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    OP_A3(0x10F0)
    OP_A2(0x121E)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x26, 0xFF)
    OP_A2(0x121F)
    OP_A2(0x1220)
    OP_A2(0x1221)
    FormationAddMember(ChrTable['朵洛希'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1222)
    OP_A2(0x1223)
    OP_A2(0x1224)
    OP_A2(0x1225)
    OP_A2(0x1226)
    OP_A2(0x1227)
    OP_A2(0x1228)
    OP_A2(0x1229)
    FormationDelMember(0x26, 0xFF)
    OP_A2(0x122A)
    OP_A2(0x10F1)
    OP_A3(0x10F1)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1400)
    OP_A2(0x1401)
    OP_A2(0x1402)
    OP_A2(0x1403)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    OP_A2(0x1404)
    OP_A2(0x1405)
    OP_A2(0x1406)
    OP_A2(0x1407)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1408)
    OP_A2(0x1409)
    OP_A2(0x140A)
    OP_A2(0x140B)
    OP_A2(0x140C)
    OP_A2(0x1410)
    OP_A2(0x140D)
    OP_A2(0x1411)
    OP_A2(0x140E)
    OP_A2(0x140F)
    OP_A2(0x1412)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1413)
    OP_A2(0x1414)
    OP_A2(0x1415)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1416)
    OP_A2(0x1417)
    OP_A2(0x1418)
    OP_A2(0x1419)
    OP_A2(0x141A)
    OP_A2(0x141B)
    OP_A2(0x141C)
    OP_A2(0x141D)
    OP_A2(0x141E)
    OP_A2(0x141F)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1420)
    OP_A2(0x1421)
    OP_A2(0x1422)
    OP_A2(0x1423)
    OP_A2(0x1424)
    OP_A2(0x10F1)
    OP_A3(0x10F1)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1600)
    OP_A2(0x1601)
    OP_A2(0x1602)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1603)
    OP_A2(0x1604)
    OP_A2(0x1607)
    OP_A2(0x1605)
    OP_A2(0x1606)
    OP_A2(0x1608)
    OP_A2(0x1609)
    OP_A2(0x160A)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x160B)
    OP_A2(0x160C)
    OP_A2(0x160D)
    OP_A2(0x160E)
    OP_A2(0x160F)
    OP_A2(0x1610)
    OP_A2(0x1611)
    OP_A2(0x1612)
    OP_A2(0x1614)
    OP_A2(0x1615)
    OP_A2(0x1616)
    OP_A2(0x1617)
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)
    OP_A2(0x1613)
    OP_A2(0x1618)
    OP_A2(0x1619)
    OP_A2(0x10F0)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x2E, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['金'], 0xF9, 0xFF)
    OP_A3(0x10F0)
    OP_A2(0x161A)
    OP_A2(0x161B)
    OP_A2(0x161C)
    OP_A2(0x161D)
    OP_A2(0x161F)
    OP_A2(0x1620)
    FormationAddMember(ChrTable['穆拉2'], 0xFF, 0xFF)
    OP_A2(0x1621)
    FormationDelMember(0x2F, 0xFF)
    OP_A2(0x1622)
    OP_A2(0x1623)
    OP_A2(0x1624)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1625)
    OP_A2(0x1626)
    OP_A2(0x1627)
    OP_A2(0x1628)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x04, 0xFF)
    OP_A2(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    FormationDelMember(0x00, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x162A)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x162B)
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)
    OP_A2(0x162C)
    OP_A2(0x10F1)
    FormationDelMember(0x2E, 0xFF)
    OP_A3(0x10F1)
    OP_A2(0x162D)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x162E)
    OP_A2(0x1630)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x1631)
    OP_A2(0x1632)
    OP_A2(0x1633)
    OP_A2(0x1634)
    OP_A2(0x1635)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1636)
    OP_A2(0x1637)
    OP_A2(0x10F0)
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1638)
    OP_A2(0x1639)
    FormationAddMember(ChrTable['管家菲利普'], 0xFF, 0xFF)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    FormationDelMember(0x42, 0xFF)
    FormationDelMember(0x08, 0xFF)
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    OP_A3(0x10F0)
    OP_A2(0x163A)
    OP_A2(0x163B)
    OP_A2(0x163C)
    OP_A2(0x10F0)
    FormationAddMember(ChrTable['尤莉亚上尉'], 0xF9, 0xFF)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    FormationDelMember(0x0E, 0xFF)
    OP_A3(0x10F1)
    FormationDelMember(0x08, 0xFF)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x163D)
    OP_A2(0x163E)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['乔丝特2'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['多伦'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['吉尔'], 0xFF, 0xFF)
    OP_A2(0x1800)
    OP_A2(0x1801)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x1802)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x1803)
    OP_A2(0x1804)
    OP_A2(0x1805)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x1806)
    OP_A2(0x1807)
    OP_A2(0x1808)
    OP_A2(0x1809)
    OP_A2(0x180A)
    OP_A2(0x180B)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x180C)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x180D)
    OP_A2(0x180E)
    OP_A2(0x180F)
    OP_A2(0x1810)
    OP_A2(0x1811)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x1812)
    OP_A2(0x1813)
    OP_A2(0x1814)
    OP_A2(0x1815)
    OP_A2(0x1816)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_BB(0x00, 0x01, 0x00000043)
    OP_A2(0x1817)
    OP_A2(0x1818)
    OP_A2(0x1819)
    OP_A2(0x181A)
    OP_A2(0x181B)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_BB(0x00, 0x01, 0x00000000)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    OP_A2(0x181C)
    OP_A2(0x181D)
    OP_A2(0x181E)
    OP_A2(0x181F)
    OP_A2(0x1820)
    OP_A2(0x1821)
    OP_A2(0x1822)
    OP_A2(0x1823)
    OP_A2(0x1824)
    OP_A2(0x10F0)
    OP_A3(0x10F0)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1825)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1826)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1827)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x10F1)
    OP_A3(0x10F1)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1828)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x1833)
    OP_BB(0x00, 0x01, 0x00000044)
    OP_BD()
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x1834)
    OP_A2(0x1835)
    OP_A2(0x1836)
    OP_A2(0x1837)
    OP_A2(0x1838)
    AddItem(ItemTable['储物室钥匙'], 1)
    OP_A2(0x1839)
    OP_A2(0x183A)
    AddItem(ItemTable['口琴'], 1)
    OP_A2(0x183B)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F2)
    OP_A3(0x10F2)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A2(0x1A00)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x1A01)
    OP_A2(0x1A02)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1A03)
    OP_A2(0x1A04)
    OP_A2(0x1A05)
    OP_A2(0x1A07)
    OP_A2(0x1A08)
    OP_A2(0x1A09)
    OP_A2(0x1A0A)
    OP_A2(0x1A0B)
    OP_A2(0x1A0C)
    OP_A2(0x1A06)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1A0D)
    OP_A2(0x1A0E)
    OP_A2(0x1A0F)
    OP_A2(0x1A10)
    OP_A2(0x1A11)
    OP_A2(0x1A12)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x1A13)
    OP_A2(0x1A14)
    OP_A2(0x1A15)
    OP_A2(0x1A16)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1A17)
    OP_A2(0x1A18)
    OP_A2(0x1A19)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1A1A)
    OP_A2(0x1A1B)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F6)
    OP_A3(0x10F6)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x1A1C)
    OP_A2(0x1A1D)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1A1E)
    OP_A2(0x1A1F)
    OP_A2(0x1A20)
    OP_A2(0x1A21)
    OP_A2(0x1A22)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F5)
    OP_A3(0x10F5)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F5)
    OP_A3(0x10F5)
    OP_A2(0x1A23)
    FormationAddMember(ChrTable['科洛丝'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF9, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFA, 0xFF)
    OP_A2(0x10F6)
    OP_A3(0x10F6)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F6)
    OP_A3(0x10F6)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F7)
    OP_A3(0x10F7)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x1A24)
    OP_A2(0x1A25)
    OP_A2(0x1A26)
    OP_A2(0x1A27)
    OP_A2(0x1A28)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x1A29)
    OP_A2(0x10F7)
    OP_A3(0x10F7)
    OP_A2(0x10F0)
    OP_A3(0x10F0)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x10F0)
    OP_A3(0x10F0)
    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    OP_A2(0x1C00)
    OP_A2(0x10F5)
    OP_A3(0x10F5)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1C01)
    OP_A2(0x1C02)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x1C03)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1C04)
    OP_A2(0x1C05)
    OP_A2(0x1C06)
    OP_A2(0x1C1A)
    OP_A2(0x1C07)
    OP_A2(0x1C08)
    AddItem(ItemTable['红色密码卡'], 1)
    OP_A2(0x1C09)
    OP_A2(0x1C0A)
    OP_A2(0x1C0B)
    AddItem(ItemTable['绿色密码卡'], 1)
    OP_A2(0x1C0C)
    OP_A2(0x1C0D)
    AddItem(ItemTable['蓝色密码卡'], 1)
    OP_A2(0x1C0E)
    OP_A2(0x1C0F)
    OP_A2(0x10F7)
    OP_A3(0x10F7)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x1C1B)
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)
    SetChrChipByIndex(0x0101, 6)
    SetChrChipByIndex(0x012F, 7)
    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x012F, 0x1000)
    SetMapFlags(0x80000000)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x1C1C)
    FormationDelMember(0x2E, 0xFF)
    SetChrChipByIndex(0x0101, 65535)
    ClearMapFlags(0x80000000)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F5)
    OP_A3(0x10F5)
    OP_A2(0x1C1D)
    OP_A2(0x1C26)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    OP_BB(0x01, 0x00, 0x00200033)
    OP_BB(0x01, 0x01, 0x00000001)
    OP_BD()
    OP_A2(0x1C27)
    OP_A2(0x1C28)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F5)
    OP_A3(0x10F5)
    OP_A2(0x10F9)
    OP_A3(0x10F9)
    OP_A2(0x10F6)
    OP_A3(0x10F6)
    OP_A2(0x10FA)
    OP_A3(0x10FA)
    OP_A2(0x10F7)
    OP_A3(0x10F7)
    OP_A2(0x10FB)
    OP_A3(0x10FB)
    OP_A2(0x10F8)
    OP_A3(0x10F8)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10FC)
    OP_A3(0x10FC)
    OP_A2(0x10F1)
    OP_A3(0x10F1)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F8)
    OP_A3(0x10F8)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F8)
    OP_A3(0x10F8)
    OP_A2(0x1E00)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10FF)
    OP_A2(0x10F0)
    OP_A3(0x10FF)
    OP_A3(0x10F0)
    OP_A2(0x10F9)
    OP_A3(0x10F9)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10FA)
    OP_A3(0x10FA)
    OP_A2(0x1E01)
    OP_A2(0x1E02)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1E03)
    OP_A2(0x1E04)
    OP_A2(0x1E05)
    AddItem(ItemTable['数据水晶０'], 1)
    OP_A2(0x1E06)
    AddItem(ItemTable['数据水晶１'], 1)
    AddItem(ItemTable['数据水晶２'], 1)
    AddItem(ItemTable['数据水晶３'], 1)
    OP_A2(0x1E31)
    OP_A2(0x1E07)
    OP_A2(0x1E08)
    OP_A2(0x1E09)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    RemoveItem(ItemTable['数据水晶０'], 1)
    RemoveItem(ItemTable['数据水晶１'], 1)
    RemoveItem(ItemTable['数据水晶２'], 1)
    RemoveItem(ItemTable['数据水晶３'], 1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10FF)
    OP_A2(0x10F1)
    OP_A3(0x10FF)
    OP_A3(0x10F1)
    OP_A2(0x10FB)
    OP_A3(0x10FB)
    OP_A2(0x1E0A)
    OP_A2(0x1E0B)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F0)
    OP_A2(0x1E0C)
    OP_A2(0x1E0D)
    AddItem(ItemTable['数据水晶４'], 1)
    AddItem(ItemTable['数据水晶５'], 1)
    AddItem(ItemTable['数据水晶６'], 1)
    AddItem(ItemTable['数据水晶７'], 1)
    OP_A2(0x1E0E)
    OP_A2(0x1E0F)
    OP_A2(0x1E10)
    OP_A2(0x1E1A)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F6)
    OP_A3(0x10F6)
    OP_A2(0x10FC)
    OP_A3(0x10FC)
    OP_A2(0x10FF)
    OP_A2(0x10F2)
    OP_A3(0x10FF)
    OP_A3(0x10F2)
    OP_A2(0x10FD)
    OP_A3(0x10FD)
    OP_A2(0x1E11)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1E12)
    OP_A2(0x1E13)
    OP_A2(0x1E14)
    OP_A2(0x1E15)
    AddItem(ItemTable['数据水晶８'], 1)
    OP_A2(0x1E1B)
    OP_A2(0x1E16)
    OP_A2(0x1E17)
    AddItem(ItemTable['数据水晶９'], 1)
    OP_A2(0x1E1C)
    OP_A2(0x1E18)
    OP_A2(0x1E19)
    AddItem(ItemTable['数据水晶１０'], 1)
    OP_A2(0x1E21)
    AddItem(ItemTable['数据水晶１１'], 1)
    OP_A2(0x1E22)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10FF)
    OP_A2(0x10F3)
    OP_A3(0x10FF)
    OP_A3(0x10F3)
    OP_A2(0x1E1D)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10FF)
    OP_A2(0x10F4)
    OP_A3(0x10FF)
    OP_A3(0x10F4)
    OP_A2(0x10FE)
    OP_A3(0x10FE)
    OP_A2(0x1E1E)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1E1F)
    OP_A2(0x1E20)
    OP_A2(0x1E23)
    OP_A2(0x1E32)
    OP_A2(0x1E33)
    OP_A2(0x1E34)
    AddItem(ItemTable['数据水晶１２'], 1)
    AddItem(ItemTable['数据水晶１３'], 1)
    AddItem(ItemTable['数据水晶１４'], 1)
    AddItem(ItemTable['数据水晶１５'], 1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x1E24)
    OP_A2(0x10FF)
    OP_A2(0x10F5)
    OP_A3(0x10FF)
    OP_A3(0x10F5)
    OP_A2(0x10F8)
    OP_A3(0x10F8)
    OP_A2(0x10FF)
    OP_A2(0x10F0)
    OP_A3(0x10FF)
    OP_A3(0x10F0)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x10F4)
    OP_A3(0x10F4)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x10FD)
    OP_A3(0x10FD)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F5)
    OP_A3(0x10F5)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F5)
    OP_A3(0x10F5)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x10F6)
    OP_A3(0x10F6)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x2000)
    OP_C4(0x00, 0x00000008)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AddItem(ItemTable['零力场发生器'], 4)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2001)
    OP_A2(0x2002)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2003)
    OP_A2(0x2091)
    OP_A2(0x2004)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2005)
    OP_A2(0x2091)
    OP_A2(0x2006)
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    OP_A2(0x2007)
    OP_A2(0x2008)
    OP_A2(0x2009)
    OP_A2(0x200A)
    OP_A2(0x200B)
    OP_A2(0x200D)
    OP_A3(0x200E)
    AddItem(ItemTable['内燃引擎'], 1)
    OP_A2(0x200F)
    AddItem(ItemTable['工房长的介绍信'], 1)
    OP_A2(0x2010)
    AddItem(ItemTable['汽油罐'], 3)
    OP_A2(0x2011)
    RemoveItem(ItemTable['汽油罐'], 3)
    RemoveItem(ItemTable['内燃引擎'], 1)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x2012)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    OP_A2(0x10FE)
    OP_A2(0x10F0)
    OP_A3(0x10FE)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10FE)
    OP_A2(0x10F1)
    OP_A3(0x10FE)
    OP_A3(0x10F1)
    OP_A2(0x2013)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10FE)
    OP_A2(0x10F2)
    OP_A3(0x10FE)
    OP_A3(0x10F2)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10FE)
    OP_A2(0x10F3)
    OP_A3(0x10FE)
    OP_A3(0x10F3)
    OP_A2(0x2014)
    OP_A2(0x2015)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10FE)
    OP_A2(0x10F4)
    OP_A3(0x10FE)
    OP_A3(0x10F4)
    OP_A2(0x2016)
    OP_A2(0x2017)
    OP_A2(0x2018)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10FE)
    OP_A2(0x10F5)
    OP_A3(0x10FE)
    OP_A3(0x10F5)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10FE)
    OP_A2(0x10F6)
    OP_A3(0x10FE)
    OP_A3(0x10F6)
    OP_A2(0x2019)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10FE)
    OP_A2(0x10F7)
    OP_A3(0x10FE)
    OP_A3(0x10F7)
    OP_A2(0x201A)
    OP_A2(0x201B)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x10FE)
    OP_A2(0x10F8)
    OP_A3(0x10FE)
    OP_A3(0x10F8)
    OP_A2(0x10F5)
    OP_A3(0x10F5)
    OP_A2(0x10FE)
    OP_A2(0x10F9)
    OP_A3(0x10FE)
    OP_A3(0x10F9)
    OP_A2(0x10F6)
    OP_A3(0x10F6)
    AddItem(ItemTable['人质名单'], 1)
    OP_A2(0x10FE)
    OP_A2(0x10FA)
    OP_A3(0x10FE)
    OP_A3(0x10FA)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10FE)
    OP_A2(0x10FB)
    OP_A3(0x10FE)
    OP_A3(0x10FB)
    OP_A2(0x201C)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10FE)
    OP_A2(0x10FC)
    OP_A3(0x10FE)
    OP_A3(0x10FC)
    OP_A2(0x201D)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x10FE)
    OP_A2(0x10FD)
    OP_A3(0x10FE)
    OP_A3(0x10FD)
    OP_A2(0x201E)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['克鲁茨'], 0xF9, 0xFF)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x201F)
    OP_A2(0x2020)
    OP_A2(0x2021)
    OP_A2(0x2022)
    OP_A2(0x2023)
    OP_A2(0x2024)
    OP_A2(0x2025)
    OP_A2(0x2026)
    OP_A2(0x2027)
    OP_A2(0x2028)
    OP_A2(0x2029)
    OP_A2(0x202A)
    OP_A2(0x202B)
    OP_A2(0x202C)
    OP_A2(0x202D)
    OP_A2(0x202E)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x202F)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F5)
    OP_A3(0x10F5)
    OP_A2(0x2037)
    OP_A2(0x10FF)
    OP_A2(0x10F8)
    OP_A3(0x10FF)
    OP_A3(0x10F8)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10FF)
    OP_A2(0x10F9)
    OP_A3(0x10FF)
    OP_A3(0x10F9)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x2038)
    OP_A2(0x2039)
    OP_A2(0x203A)
    OP_A2(0x203B)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x203C)
    OP_A2(0x203D)
    OP_A2(0x10F3)
    OP_A3(0x10F3)
    OP_A2(0x203E)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10FF)
    OP_A2(0x10FB)
    OP_A3(0x10FF)
    OP_A3(0x10FB)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x10F7)
    OP_A3(0x10F7)
    OP_A2(0x10FF)
    OP_A2(0x10F1)
    OP_A3(0x10FF)
    OP_A3(0x10F1)
    OP_A2(0x10FF)
    OP_A2(0x10F6)
    OP_A3(0x10FF)
    OP_A3(0x10F6)
    OP_A2(0x2200)
    OP_A2(0x10FF)
    OP_A2(0x10F2)
    OP_A3(0x10FF)
    OP_A3(0x10F2)
    OP_A2(0x10FF)
    OP_A2(0x10F7)
    OP_A3(0x10FF)
    OP_A3(0x10F7)
    OP_A2(0x10FF)
    OP_A2(0x10F3)
    OP_A3(0x10FF)
    OP_A3(0x10F3)
    OP_A2(0x10FF)
    OP_A2(0x10F4)
    OP_A3(0x10FF)
    OP_A3(0x10F4)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F5)
    OP_A3(0x10F5)
    OP_A2(0x2201)
    OP_C4(0x01, 0x00000008)
    OP_A2(0x2202)
    OP_A2(0x2203)
    OP_A2(0x2204)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x220D)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A3(0x2210)
    OP_A3(0x2211)
    OP_A3(0x2212)
    OP_A3(0x2213)
    OP_A3(0x2214)
    OP_A3(0x2215)
    OP_A3(0x2216)
    OP_A3(0x2217)
    OP_A2(0x10F1)
    OP_A2(0x10F0)
    OP_A3(0x10F1)
    OP_A3(0x10F0)
    OP_A3(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x2218)
    FormationAddMember(ChrTable['乔丝特2'], 0xFA, 0xFF)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    FormationDelMember(0x45, 0xFF)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x2219)
    OP_A2(0x221A)
    OP_A2(0x221B)
    AddItem(ItemTable['原福音'], 1)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x221C)
    OP_A2(0x221E)
    OP_A2(0x222F)
    OP_A2(0x221F)
    OP_A2(0x2220)
    OP_A2(0x2221)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x2222)
    OP_A2(0x2223)
    OP_A2(0x2224)
    OP_A2(0x22B2)
    AddItem(ItemTable['安全卡片'], 1)
    OP_A2(0x2225)
    OP_A2(0x2226)
    OP_A2(0x2227)
    OP_A2(0x2228)
    OP_A2(0x2229)
    OP_A2(0x222A)
    OP_A2(0x222B)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F2)
    OP_A3(0x10F2)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x222C)
    OP_A2(0x222D)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x222E)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x2230)
    OP_A2(0x2231)
    OP_A2(0x223C)
    OP_A2(0x2232)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x2233)
    OP_A2(0x2234)
    OP_A2(0x2235)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x2236)
    OP_A2(0x2237)
    OP_A2(0x2238)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x2239)
    OP_A2(0x10FF)
    OP_A2(0x10FA)
    OP_A3(0x10FF)
    OP_A3(0x10FA)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x223A)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    OP_A3(0x10F1)
    OP_A2(0x223B)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    FormationDelMember(0x01, 0xFF)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x223D)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    OP_BB(0x01, 0x00, 0x00200033)
    OP_BB(0x01, 0x01, 0x0000001C)
    OP_BD()
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x08, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    OP_A2(0x223E)
    OP_A2(0x10F4)
    OP_A3(0x10F4)
    OP_A2(0x10FF)
    OP_A2(0x10F5)
    OP_A3(0x10FF)
    OP_A3(0x10F5)
    OP_A2(0x10FF)
    OP_A2(0x10FC)
    OP_A3(0x10FF)
    OP_A3(0x10FC)
    OP_A2(0x10F0)
    OP_A3(0x10F0)
    OP_A2(0x10F1)
    OP_A3(0x10F1)

    Return()

# id: 0x0002 offset: 0x1486
@scena.Code('ReInit')
def ReInit():
    FormationReset()
    OP_A3(0x10F0)
    OP_A3(0x10F1)
    OP_A3(0x10F2)
    OP_A3(0x10F3)
    OP_A3(0x10F4)
    OP_A3(0x10F5)
    OP_A3(0x10F6)
    OP_A3(0x10F7)
    OP_A3(0x10F8)
    OP_A3(0x10F9)
    OP_A3(0x10FA)
    OP_A3(0x10FB)
    OP_A3(0x10FC)
    OP_A3(0x10FD)
    OP_A3(0x10FE)
    OP_A3(0x10FF)

    Return()

# id: 0x0003 offset: 0x14B8
@scena.Code('func_03_14B8')
def func_03_14B8():
    OP_A3(0x1002)
    OP_A3(0x1003)
    OP_A3(0x1004)
    OP_A3(0x1005)
    OP_A3(0x1006)
    OP_A3(0x1008)
    OP_A3(0x1007)
    OP_A3(0x1009)
    OP_A3(0x100A)
    OP_A3(0x100B)
    OP_A3(0x100C)
    OP_A3(0x100D)
    OP_A3(0x100E)
    OP_A3(0x100F)
    OP_A3(0x1010)
    OP_A3(0x1011)
    OP_A3(0x1012)
    OP_A3(0x1013)
    OP_A3(0x1014)
    OP_A3(0x1015)
    OP_A3(0x1016)
    OP_A3(0x1017)
    OP_A3(0x1018)
    OP_A3(0x1019)
    OP_A3(0x101A)
    OP_A3(0x101B)
    OP_A3(0x101C)
    OP_A3(0x101D)
    OP_A3(0x101E)
    OP_A3(0x101F)
    OP_A3(0x1020)
    OP_A3(0x1021)
    OP_A3(0x1022)
    OP_A3(0x1023)
    OP_A3(0x1024)
    OP_A3(0x1120)
    OP_A3(0x1121)
    OP_A3(0x1122)
    OP_A3(0x1123)
    OP_A3(0x1130)
    OP_A3(0x1131)
    OP_A3(0x1132)
    OP_A3(0x1133)

    Return()

# id: 0x0004 offset: 0x153A
@scena.Code('func_04_153A')
def func_04_153A():
    OP_A2(0x1002)
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    OP_A2(0x1003)
    FormationDelMember(0x08, 0xFF)
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    OP_A2(0x1004)
    OP_A2(0x1005)
    OP_A2(0x1006)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    OP_A2(0x1007)
    OP_A2(0x1008)
    OP_A2(0x1009)
    OP_A2(0x100A)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x100B)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF9, 0xFF)
    OP_A2(0x100C)
    OP_A2(0x100D)
    OP_A2(0x100E)
    OP_A2(0x100F)
    OP_A2(0x1010)
    OP_A2(0x1011)
    OP_A2(0x1012)
    OP_A2(0x101B)
    OP_A2(0x101C)
    OP_A2(0x101D)
    OP_A2(0x101E)
    OP_A2(0x101F)
    OP_A2(0x1020)
    OP_A2(0x1021)
    OP_A2(0x1022)
    OP_A2(0x1023)
    OP_A2(0x1024)

    Return()

# id: 0x0005 offset: 0x15AD
@scena.Code('func_05_15AD')
def func_05_15AD():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17F5',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '①·王都～洛连特自宅\n'),
            TXT(0x01, '②·卢·洛克尔训练场\n'),
            TXT(0x02, '③·圣科洛瓦森林\n'),
            TXT(0x03, '④·格林姆瑟尔小要塞\n'),
            TXT(0x04, '⑤·尾声\n'),
            TXT(0x05, '　·序章洛连特普通\n'),
            TXT(0x06, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    AddItem(ItemTable['利贝尔王国地图'], 1)
    OP_BB(0x00, 0x00, 0x00200042)
    OP_BB(0x00, 0x01, 0x0000001E)
    OP_BD()
    OP_56(0x00)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_167B'),
        (0x00000001, 'loc_1687'),
        (0x00000002, 'loc_16A3'),
        (0x00000003, 'loc_16F1'),
        (0x00000004, 'loc_1751'),
        (0x00000005, 'loc_17CF'),
        (-1, 'loc_17E5'),
    )

    def _loc_167B(): pass

    label('loc_167B')

    NewScene('ED6_DT21/T4201._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_17F2')

    def _loc_1687(): pass

    label('loc_1687')

    OP_A2(0x1002)
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    OP_A2(0x1003)
    OP_A2(0x10F0)
    FormationDelMember(0x08, 0xFF)
    NewScene('ED6_DT21/T5100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_17F2')

    def _loc_16A3(): pass

    label('loc_16A3')

    OP_A2(0x1002)
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    OP_A2(0x1003)
    FormationDelMember(0x08, 0xFF)
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    OP_A2(0x1004)
    OP_A2(0x1005)
    OP_A2(0x1006)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    OP_A2(0x1007)
    OP_A2(0x1008)
    OP_A2(0x1009)
    OP_A2(0x100A)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x100B)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF9, 0xFF)
    OP_A2(0x100C)
    NewScene('ED6_DT21/C5504._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_17F2')

    def _loc_16F1(): pass

    label('loc_16F1')

    OP_A2(0x1002)
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    OP_A2(0x1003)
    FormationDelMember(0x08, 0xFF)
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    OP_A2(0x1004)
    OP_A2(0x1005)
    OP_A2(0x1006)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    OP_A2(0x1007)
    OP_A2(0x1008)
    OP_A2(0x1009)
    OP_A2(0x100A)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x100B)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF9, 0xFF)
    OP_A2(0x100C)
    OP_A2(0x100D)
    OP_A2(0x100E)
    OP_A2(0x100F)
    OP_A2(0x1010)
    OP_A2(0x1011)
    OP_A2(0x1012)
    NewScene('ED6_DT21/T5100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_17F2')

    def _loc_1751(): pass

    label('loc_1751')

    OP_A2(0x1002)
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    OP_A2(0x1003)
    FormationDelMember(0x08, 0xFF)
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    OP_A2(0x1004)
    OP_A2(0x1005)
    OP_A2(0x1006)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    OP_A2(0x1007)
    OP_A2(0x1008)
    OP_A2(0x1009)
    OP_A2(0x100A)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x100B)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF9, 0xFF)
    OP_A2(0x100C)
    OP_A2(0x100D)
    OP_A2(0x100E)
    OP_A2(0x100F)
    OP_A2(0x1010)
    OP_A2(0x1011)
    OP_A2(0x1012)
    OP_A2(0x101B)
    OP_A2(0x101C)
    OP_A2(0x101D)
    OP_A2(0x101E)
    OP_A2(0x101F)
    OP_A2(0x1020)
    OP_A2(0x1021)
    OP_A2(0x1022)
    OP_A2(0x1023)
    OP_A2(0x1024)
    NewScene('ED6_DT21/C5600._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_17F2')

    def _loc_17CF(): pass

    label('loc_17CF')

    OP_A2(0x1002)
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    OP_A2(0x1003)
    NewScene('ED6_DT21/T0100._SN', 122, 0, 0)
    IdleLoop()

    Jump('loc_17F2')

    def _loc_17E5(): pass

    label('loc_17E5')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_17F2')

    def _loc_17F2(): pass

    label('loc_17F2')

    Jump('func_05_15AD')

    def _loc_17F5(): pass

    label('loc_17F5')

    OP_5F(0x0002)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0006 offset: 0x1805
@scena.Code('func_06_1805')
def func_06_1805():
    RemoveItem(ItemTable['船票'], 1)
    RemoveItem(ItemTable['后门的钥匙'], 1)
    RemoveItem(ItemTable['旧钥匙'], 1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    OP_A3(0x1202)
    OP_A3(0x1203)
    OP_A3(0x1204)
    OP_A3(0x1205)
    OP_A3(0x1206)
    OP_A3(0x1207)
    OP_A3(0x1208)
    OP_A3(0x1209)
    OP_A3(0x120A)
    OP_A3(0x120B)
    OP_A3(0x120C)
    OP_A3(0x120D)
    OP_A3(0x120E)
    OP_A3(0x120F)
    OP_A3(0x1210)
    OP_A3(0x1211)
    OP_A3(0x1212)
    OP_A3(0x1213)
    OP_A3(0x1214)
    OP_A3(0x1215)
    OP_A3(0x1216)
    OP_A3(0x1217)
    OP_A3(0x1218)
    OP_A3(0x1219)
    OP_A3(0x121A)
    OP_A3(0x121B)
    OP_A3(0x121C)
    OP_A3(0x121D)
    OP_A3(0x121E)
    OP_A3(0x121F)
    OP_A3(0x1220)
    OP_A3(0x1221)
    OP_A3(0x1222)
    OP_A3(0x1223)
    OP_A3(0x1224)
    OP_A3(0x1225)
    OP_A3(0x1226)
    OP_A3(0x1227)
    OP_A3(0x1228)
    OP_A3(0x1229)
    OP_A3(0x122A)

    Return()

# id: 0x0007 offset: 0x1896
@scena.Code('func_07_1896')
def func_07_1896():
    OP_A2(0x1202)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x1203)
    OP_A2(0x1204)
    OP_A2(0x1205)
    OP_A2(0x1206)
    OP_A2(0x120E)
    OP_A2(0x120F)
    OP_A2(0x1210)
    OP_A2(0x1211)
    OP_A2(0x1212)
    OP_A2(0x1213)
    OP_A2(0x1214)
    OP_A2(0x1215)
    OP_A2(0x1216)
    OP_A2(0x1217)
    OP_A2(0x1218)
    OP_A2(0x1219)
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    OP_A2(0x121A)
    FormationDelMember(0x08, 0xFF)
    OP_A2(0x121B)
    OP_A2(0x121C)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['朵洛希'], 0xF9, 0xFF)
    OP_A2(0x121D)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    OP_A2(0x121E)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x26, 0xFF)
    OP_A2(0x121F)
    OP_A2(0x1220)
    OP_A2(0x1221)
    FormationAddMember(ChrTable['朵洛希'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    OP_A2(0x1222)
    OP_A2(0x1223)
    OP_A2(0x1224)
    OP_A2(0x1225)
    OP_A2(0x1226)
    OP_A2(0x1227)
    OP_A2(0x1228)
    OP_A2(0x1229)
    FormationDelMember(0x26, 0xFF)
    OP_A2(0x122A)

    Return()

# id: 0x0008 offset: 0x192A
@scena.Code('func_08_192A')
def func_08_192A():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CD7',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '0·序\n'),
            TXT(0x01, '①·到达王都～卢安地区\n'),
            TXT(0x02, '②·定期船～到达卢安\n'),
            TXT(0x03, '③·对渡鸦帮\n'),
            TXT(0x04, '④·在艾尔·雷登的探听\n'),
            TXT(0x05, '⑤·在孤儿院的探听\n'),
            TXT(0x06, '⑥·奥利维尔登场～王立学院\n'),
            TXT(0x07, '⑦·王立学院～与科洛丝重逢\n'),
            TXT(0x08, '⑧·旧校舍的探索\n'),
            TXT(0x09, '⑨·尾声\n'),
            TXT(0x0A, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    AddItem(ItemTable['利贝尔王国地图'], 1)
    Call(4, 0x0004)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1A4A'),
        (0x00000001, 'loc_1A56'),
        (0x00000002, 'loc_1A62'),
        (0x00000003, 'loc_1A7A'),
        (0x00000004, 'loc_1A98'),
        (0x00000005, 'loc_1ABF'),
        (0x00000006, 'loc_1AF5'),
        (0x00000007, 'loc_1B44'),
        (0x00000008, 'loc_1BA1'),
        (0x00000009, 'loc_1C25'),
        (-1, 'loc_1CC7'),
    )

    def _loc_1A4A(): pass

    label('loc_1A4A')

    NewScene('ED6_DT21/C4302._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1A56(): pass

    label('loc_1A56')

    NewScene('ED6_DT21/T4105._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1A62(): pass

    label('loc_1A62')

    OP_A2(0x1202)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x1203)
    OP_A2(0x1204)
    NewScene('ED6_DT21/E0000._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1A7A(): pass

    label('loc_1A7A')

    OP_A2(0x1202)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x1203)
    OP_A2(0x1204)
    OP_A2(0x1205)
    OP_A2(0x1206)
    NewScene('ED6_DT21/T2130._SN', 108, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1A98(): pass

    label('loc_1A98')

    OP_A2(0x1202)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x1203)
    OP_A2(0x1204)
    OP_A2(0x1205)
    OP_A2(0x1206)
    OP_A2(0x120E)
    OP_A2(0x120F)
    OP_A2(0x1210)
    NewScene('ED6_DT21/T2700._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1ABF(): pass

    label('loc_1ABF')

    OP_A2(0x1202)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x1203)
    OP_A2(0x1204)
    OP_A2(0x1205)
    OP_A2(0x1206)
    OP_A2(0x120E)
    OP_A2(0x120F)
    OP_A2(0x1210)
    OP_A2(0x1211)
    OP_A2(0x1212)
    OP_A2(0x1213)
    OP_A2(0x1214)
    OP_A2(0x1215)
    NewScene('ED6_DT21/T2402._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1AF5(): pass

    label('loc_1AF5')

    OP_A2(0x1202)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x1203)
    OP_A2(0x1204)
    OP_A2(0x1205)
    OP_A2(0x1206)
    OP_A2(0x120E)
    OP_A2(0x120F)
    OP_A2(0x1210)
    OP_A2(0x1211)
    OP_A2(0x1212)
    OP_A2(0x1213)
    OP_A2(0x1214)
    OP_A2(0x1215)
    OP_A2(0x1216)
    OP_A2(0x1217)
    OP_A2(0x1218)
    OP_A2(0x1219)
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    OP_A2(0x121A)
    FormationDelMember(0x08, 0xFF)
    OP_A2(0x121B)
    NewScene('ED6_DT21/T2120._SN', 105, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1B44(): pass

    label('loc_1B44')

    OP_A2(0x1202)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x1203)
    OP_A2(0x1204)
    OP_A2(0x1205)
    OP_A2(0x1206)
    OP_A2(0x120E)
    OP_A2(0x120F)
    OP_A2(0x1210)
    OP_A2(0x1211)
    OP_A2(0x1212)
    OP_A2(0x1213)
    OP_A2(0x1214)
    OP_A2(0x1215)
    OP_A2(0x1216)
    OP_A2(0x1217)
    OP_A2(0x1218)
    OP_A2(0x1219)
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    OP_A2(0x121A)
    FormationDelMember(0x08, 0xFF)
    OP_A2(0x121B)
    OP_A2(0x121C)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['朵洛希'], 0xF9, 0xFF)
    OP_A2(0x121D)
    NewScene('ED6_DT21/T2500._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1BA1(): pass

    label('loc_1BA1')

    OP_A2(0x1202)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x1203)
    OP_A2(0x1204)
    OP_A2(0x1205)
    OP_A2(0x1206)
    OP_A2(0x120E)
    OP_A2(0x120F)
    OP_A2(0x1210)
    OP_A2(0x1211)
    OP_A2(0x1212)
    OP_A2(0x1213)
    OP_A2(0x1214)
    OP_A2(0x1215)
    OP_A2(0x1216)
    OP_A2(0x1217)
    OP_A2(0x1218)
    OP_A2(0x1219)
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    OP_A2(0x121A)
    FormationDelMember(0x08, 0xFF)
    OP_A2(0x121B)
    OP_A2(0x121C)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['朵洛希'], 0xF9, 0xFF)
    OP_A2(0x121D)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    OP_A2(0x121E)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x26, 0xFF)
    OP_A2(0x121F)
    OP_A2(0x1220)
    OP_A2(0x1221)
    FormationAddMember(ChrTable['朵洛希'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    OP_A2(0x1222)
    NewScene('ED6_DT21/T2800._SN', 120, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1C25(): pass

    label('loc_1C25')

    OP_A2(0x1202)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x1203)
    OP_A2(0x1204)
    OP_A2(0x1205)
    OP_A2(0x1206)
    OP_A2(0x120E)
    OP_A2(0x120F)
    OP_A2(0x1210)
    OP_A2(0x1211)
    OP_A2(0x1212)
    OP_A2(0x1213)
    OP_A2(0x1214)
    OP_A2(0x1215)
    OP_A2(0x1216)
    OP_A2(0x1217)
    OP_A2(0x1218)
    OP_A2(0x1219)
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    OP_A2(0x121A)
    FormationDelMember(0x08, 0xFF)
    OP_A2(0x121B)
    OP_A2(0x121C)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['朵洛希'], 0xF9, 0xFF)
    OP_A2(0x121D)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    OP_A2(0x121E)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x26, 0xFF)
    OP_A2(0x121F)
    OP_A2(0x1220)
    OP_A2(0x1221)
    FormationAddMember(ChrTable['朵洛希'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    OP_A2(0x1222)
    OP_A2(0x1223)
    OP_A2(0x1224)
    OP_A2(0x1225)
    OP_A2(0x1226)
    OP_A2(0x1227)
    OP_A2(0x1228)
    OP_A2(0x1229)
    FormationDelMember(0x26, 0xFF)
    OP_A2(0x122A)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T2120._SN', 105, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1CC7(): pass

    label('loc_1CC7')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CD4')

    def _loc_1CD4(): pass

    label('loc_1CD4')

    Jump('func_08_192A')

    def _loc_1CD7(): pass

    label('loc_1CD7')

    OP_5F(0x0002)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0009 offset: 0x1CE7
@scena.Code('func_09_1CE7')
def func_09_1CE7():
    RemoveItem(ItemTable['后山的钥匙'], 1)
    OP_A3(0x1400)
    OP_A3(0x1401)
    OP_A3(0x1402)
    OP_A3(0x1403)
    OP_A3(0x1404)
    OP_A3(0x1405)
    OP_A3(0x1406)
    OP_A3(0x1407)
    OP_A3(0x1408)
    OP_A3(0x1409)
    OP_A3(0x140A)
    OP_A3(0x140B)
    OP_A3(0x140C)
    OP_A3(0x1410)
    OP_A3(0x140D)
    OP_A3(0x1411)
    OP_A3(0x1412)
    OP_A3(0x140E)
    OP_A3(0x140F)
    OP_A3(0x1413)
    OP_A3(0x1414)
    OP_A3(0x1415)
    OP_A3(0x1416)
    OP_A3(0x1417)
    OP_A3(0x1418)
    OP_A3(0x1419)
    OP_A3(0x141A)
    OP_A3(0x141B)
    OP_A3(0x141C)
    OP_A3(0x141D)
    OP_A3(0x141E)
    OP_A3(0x141F)
    OP_A3(0x1420)
    OP_A3(0x1421)
    OP_A3(0x1422)
    OP_A3(0x1423)
    OP_A3(0x1424)
    OP_A3(0x1480)
    OP_A3(0x1481)
    OP_A3(0x1482)

    Return()

# id: 0x000A offset: 0x1D65
@scena.Code('func_0A_1D65')
def func_0A_1D65():
    OP_A2(0x1400)
    OP_A2(0x1401)
    OP_A2(0x1402)
    OP_A2(0x1403)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    OP_A2(0x1404)
    OP_A2(0x1405)
    OP_A2(0x1406)
    OP_A2(0x1407)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    OP_A2(0x1408)
    OP_A2(0x1409)
    OP_A2(0x140A)
    OP_A2(0x140B)
    OP_A2(0x140C)
    OP_A2(0x1410)
    OP_A2(0x140D)
    OP_A2(0x1411)
    OP_A2(0x140E)
    OP_A2(0x140F)
    OP_A2(0x1412)
    OP_A2(0x1413)
    OP_A2(0x1414)
    OP_A2(0x1415)
    OP_A2(0x1416)
    OP_A2(0x1417)
    OP_A2(0x1418)
    OP_A2(0x1419)
    OP_A2(0x141A)
    OP_A2(0x141B)
    OP_A2(0x141C)
    OP_A2(0x141D)
    OP_A2(0x141E)
    OP_A2(0x141F)
    OP_A2(0x1420)
    OP_A2(0x1421)
    OP_A2(0x1422)
    OP_A2(0x1423)
    OP_A2(0x1424)

    Return()

# id: 0x000B offset: 0x1DE9
@scena.Code('func_0B_1DE9')
def func_0B_1DE9():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2186',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '0·序\n'),
            TXT(0x01, '①·从卢安出发\n'),
            TXT(0x02, '②·乘定期船移动\n'),
            TXT(0x03, '③·到达蔡斯～与提妲重逢\n'),
            TXT(0x04, '④·沃尔费堡垒的调查\n'),
            TXT(0x05, '⑤·圣海姆门的调查\n'),
            TXT(0x06, '⑥·七耀脉测量仪的设置\n'),
            TXT(0x07, '⑦·亚尔摩后山～温泉洞窟\n'),
            TXT(0x08, '⑧·尾声\n'),
            TXT(0x09, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    AddItem(ItemTable['利贝尔王国地图'], 1)
    Call(4, 0x0004)
    Call(4, 0x0007)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1EF0'),
        (0x00000001, 'loc_1EFC'),
        (0x00000002, 'loc_1F0B'),
        (0x00000003, 'loc_1F2F'),
        (0x00000004, 'loc_1F5F'),
        (0x00000005, 'loc_1FA0'),
        (0x00000006, 'loc_1FF9'),
        (0x00000007, 'loc_2061'),
        (0x00000008, 'loc_20E4'),
        (-1, 'loc_2176'),
    )

    def _loc_1EF0(): pass

    label('loc_1EF0')

    NewScene('ED6_DT21/T2105._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_1EFC(): pass

    label('loc_1EFC')

    OP_A2(0x1400)
    NewScene('ED6_DT21/T2100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_1F0B(): pass

    label('loc_1F0B')

    OP_A2(0x1400)
    OP_A2(0x1401)
    OP_A2(0x1402)
    OP_A2(0x1403)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    NewScene('ED6_DT21/E0011._SN', 114, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_1F2F(): pass

    label('loc_1F2F')

    OP_A2(0x1400)
    OP_A2(0x1401)
    OP_A2(0x1402)
    OP_A2(0x1403)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    OP_A2(0x1404)
    OP_A2(0x1405)
    OP_A2(0x1406)
    OP_A2(0x1407)
    NewScene('ED6_DT21/E0011._SN', 110, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_1F5F(): pass

    label('loc_1F5F')

    OP_A2(0x1400)
    OP_A2(0x1401)
    OP_A2(0x1402)
    OP_A2(0x1403)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    OP_A2(0x1404)
    OP_A2(0x1405)
    OP_A2(0x1406)
    OP_A2(0x1407)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    OP_A2(0x1408)
    OP_A2(0x1409)
    OP_A2(0x140A)
    NewScene('ED6_DT21/T3300._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_1FA0(): pass

    label('loc_1FA0')

    OP_A2(0x1400)
    OP_A2(0x1401)
    OP_A2(0x1402)
    OP_A2(0x1403)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    OP_A2(0x1404)
    OP_A2(0x1405)
    OP_A2(0x1406)
    OP_A2(0x1407)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    OP_A2(0x1408)
    OP_A2(0x1409)
    OP_A2(0x140A)
    OP_A2(0x140B)
    OP_A2(0x140C)
    OP_A2(0x1410)
    OP_A2(0x140D)
    OP_A2(0x1411)
    OP_A2(0x140E)
    OP_A2(0x140F)
    OP_A2(0x1412)
    NewScene('ED6_DT21/T3401._SN', 106, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_1FF9(): pass

    label('loc_1FF9')

    OP_A2(0x1400)
    OP_A2(0x1401)
    OP_A2(0x1402)
    OP_A2(0x1403)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    OP_A2(0x1404)
    OP_A2(0x1405)
    OP_A2(0x1406)
    OP_A2(0x1407)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    OP_A2(0x1408)
    OP_A2(0x1409)
    OP_A2(0x140A)
    OP_A2(0x140B)
    OP_A2(0x140C)
    OP_A2(0x1410)
    OP_A2(0x140D)
    OP_A2(0x1411)
    OP_A2(0x140E)
    OP_A2(0x140F)
    OP_A2(0x1412)
    OP_A2(0x1413)
    OP_A2(0x1414)
    OP_A2(0x1415)
    OP_A2(0x1416)
    OP_A2(0x1417)
    NewScene('ED6_DT21/T3120._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_2061(): pass

    label('loc_2061')

    OP_A2(0x1400)
    OP_A2(0x1401)
    OP_A2(0x1402)
    OP_A2(0x1403)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    OP_A2(0x1404)
    OP_A2(0x1405)
    OP_A2(0x1406)
    OP_A2(0x1407)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    OP_A2(0x1408)
    OP_A2(0x1409)
    OP_A2(0x140A)
    OP_A2(0x140B)
    OP_A2(0x140C)
    OP_A2(0x1410)
    OP_A2(0x140D)
    OP_A2(0x1411)
    OP_A2(0x140E)
    OP_A2(0x140F)
    OP_A2(0x1412)
    OP_A2(0x1413)
    OP_A2(0x1414)
    OP_A2(0x1415)
    OP_A2(0x1416)
    OP_A2(0x1417)
    OP_A2(0x1418)
    OP_A2(0x1419)
    OP_A2(0x141A)
    OP_A2(0x141B)
    OP_A2(0x141C)
    OP_A2(0x141D)
    OP_A2(0x141E)
    OP_A2(0x141F)
    OP_A2(0x1420)
    NewScene('ED6_DT21/T3200._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_20E4(): pass

    label('loc_20E4')

    OP_A2(0x1400)
    OP_A2(0x1401)
    OP_A2(0x1402)
    OP_A2(0x1403)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    OP_A2(0x1404)
    OP_A2(0x1405)
    OP_A2(0x1406)
    OP_A2(0x1407)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    OP_A2(0x1408)
    OP_A2(0x1409)
    OP_A2(0x140A)
    OP_A2(0x140B)
    OP_A2(0x140C)
    OP_A2(0x1410)
    OP_A2(0x140D)
    OP_A2(0x1411)
    OP_A2(0x140E)
    OP_A2(0x140F)
    OP_A2(0x1412)
    OP_A2(0x1413)
    OP_A2(0x1414)
    OP_A2(0x1415)
    OP_A2(0x1416)
    OP_A2(0x1417)
    OP_A2(0x1418)
    OP_A2(0x1419)
    OP_A2(0x141A)
    OP_A2(0x141B)
    OP_A2(0x141C)
    OP_A2(0x141D)
    OP_A2(0x141E)
    OP_A2(0x141F)
    OP_A2(0x1420)
    OP_A2(0x1421)
    OP_A2(0x1422)
    OP_A2(0x1423)
    OP_A2(0x1424)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T3120._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_2176(): pass

    label('loc_2176')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2183')

    def _loc_2183(): pass

    label('loc_2183')

    Jump('func_0B_1DE9')

    def _loc_2186(): pass

    label('loc_2186')

    OP_5F(0x0002)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000C offset: 0x2196
@scena.Code('func_0C_2196')
def func_0C_2196():
    OP_A3(0x1600)
    OP_A3(0x1601)
    OP_A3(0x1602)
    OP_A3(0x1603)
    OP_A3(0x1604)
    OP_A3(0x1605)
    OP_A3(0x1606)
    OP_A3(0x1607)
    OP_A3(0x1608)
    OP_A3(0x1609)
    OP_A3(0x160A)
    OP_A3(0x160B)
    OP_A3(0x160C)
    OP_A3(0x160D)
    OP_A3(0x160E)
    OP_A3(0x160F)
    OP_A3(0x1610)
    OP_A3(0x1611)
    OP_A3(0x1612)
    OP_A3(0x1614)
    OP_A3(0x1615)
    OP_A3(0x1616)
    OP_A3(0x1617)
    OP_A3(0x1613)
    OP_A3(0x1618)
    OP_A3(0x1619)
    OP_A3(0x161A)
    OP_A3(0x161B)
    OP_A3(0x161C)
    OP_A3(0x161D)
    OP_A3(0x161E)
    OP_A3(0x161F)
    OP_A3(0x1620)
    OP_A3(0x1621)
    OP_A3(0x1622)
    OP_A3(0x1623)
    OP_A3(0x1624)
    OP_A3(0x1625)
    OP_A3(0x1626)
    OP_A3(0x1627)
    OP_A3(0x1628)
    OP_A3(0x1680)
    OP_A3(0x1629)
    OP_A3(0x162A)
    OP_A3(0x162B)
    OP_A3(0x162C)
    OP_A3(0x162D)
    OP_A3(0x162E)
    OP_A3(0x162F)
    OP_A3(0x1630)
    OP_A3(0x1631)
    OP_A3(0x1632)
    OP_A3(0x1633)
    OP_A3(0x1634)
    OP_A3(0x1635)
    OP_A3(0x1636)
    OP_A3(0x1637)
    OP_A3(0x1638)
    OP_A3(0x1639)
    OP_A3(0x163A)
    OP_A3(0x163B)
    OP_A3(0x163C)
    OP_A3(0x163D)
    OP_A3(0x163E)

    Return()

# id: 0x000D offset: 0x2257
@scena.Code('func_0D_2257')
def func_0D_2257():
    OP_A2(0x1600)
    OP_A2(0x1601)
    OP_A2(0x1602)
    OP_A2(0x1603)
    OP_A2(0x1604)
    OP_A2(0x1607)
    OP_A2(0x1605)
    OP_A2(0x1606)
    OP_A2(0x1608)
    OP_A2(0x1609)
    OP_A2(0x160A)
    OP_A2(0x160B)
    OP_A2(0x160C)
    OP_A2(0x160D)
    OP_A2(0x160E)
    OP_A2(0x160F)
    OP_A2(0x1610)
    OP_A2(0x1611)
    OP_A2(0x1612)
    OP_A2(0x1614)
    OP_A2(0x1615)
    OP_A2(0x1616)
    OP_A2(0x1617)
    OP_A2(0x1613)
    OP_A2(0x1618)
    OP_A2(0x1619)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x161A)
    OP_A2(0x161B)
    OP_A2(0x161C)
    OP_A2(0x161D)
    OP_A2(0x161F)
    OP_A2(0x1620)
    OP_A2(0x1621)
    OP_A2(0x1622)
    OP_A2(0x1623)
    OP_A2(0x1624)
    OP_A2(0x1625)
    OP_A2(0x1626)
    OP_A2(0x1627)
    OP_A2(0x1628)
    OP_A2(0x162A)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x162B)
    OP_A2(0x162C)
    OP_A2(0x162D)
    OP_A2(0x162E)
    OP_A2(0x1630)
    OP_A2(0x1631)
    OP_A2(0x1632)
    OP_A2(0x1633)
    OP_A2(0x1634)
    OP_A2(0x1635)
    OP_A2(0x1636)
    OP_A2(0x1637)
    OP_A2(0x1638)
    OP_A2(0x1639)
    OP_A2(0x163A)
    OP_A2(0x163B)
    OP_A2(0x163C)
    OP_A2(0x163D)
    OP_A2(0x163E)

    Return()

# id: 0x000E offset: 0x231E
@scena.Code('func_0E_231E')
def func_0E_231E():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A49',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '0·序\n'),
            TXT(0x01, '①·从蔡斯出发～乘定期船移动\n'),
            TXT(0x02, '②·到达王都～与玲重逢\n'),
            TXT(0x03, '③·希德来访～搜查开始\n'),
            TXT(0x04, '④·各地的暗中活动\n'),
            TXT(0x05, '⑤·第２日开始\n'),
            TXT(0x06, '⑥·对玲的搜索\n'),
            TXT(0x07, '⑦·亚宁堡\n'),
            TXT(0x08, '⑧·协会～码头\n'),
            TXT(0x09, '⑨·尾声\n'),
            TXT(0x0A, '⑩·尾声 2\n'),
            TXT(0x0B, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    AddItem(ItemTable['利贝尔王国地图'], 1)
    Call(4, 0x0004)
    Call(4, 0x0007)
    Call(4, 0x000A)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2441'),
        (0x00000001, 'loc_244D'),
        (0x00000002, 'loc_245F'),
        (0x00000003, 'loc_249E'),
        (0x00000004, 'loc_2508'),
        (0x00000005, 'loc_25A1'),
        (0x00000006, 'loc_2641'),
        (0x00000007, 'loc_26E7'),
        (0x00000008, 'loc_27B4'),
        (0x00000009, 'loc_288B'),
        (0x0000000A, 'loc_2962'),
        (-1, 'loc_2A39'),
    )

    def _loc_2441(): pass

    label('loc_2441')

    NewScene('ED6_DT21/C3108._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_244D(): pass

    label('loc_244D')

    OP_A2(0x1600)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T3100._SN', 110, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_245F(): pass

    label('loc_245F')

    OP_A2(0x1600)
    OP_A2(0x1601)
    OP_A2(0x1602)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1603)
    OP_A2(0x1604)
    OP_A2(0x1607)
    OP_A2(0x1605)
    OP_A2(0x1606)
    OP_A2(0x1608)
    OP_A2(0x1609)
    OP_A2(0x160A)
    NewScene('ED6_DT21/T4106._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_249E(): pass

    label('loc_249E')

    OP_A2(0x1600)
    OP_A2(0x1601)
    OP_A2(0x1602)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1603)
    OP_A2(0x1604)
    OP_A2(0x1607)
    OP_A2(0x1605)
    OP_A2(0x1606)
    OP_A2(0x1608)
    OP_A2(0x1609)
    OP_A2(0x160A)
    OP_A2(0x160B)
    OP_A2(0x160C)
    OP_A2(0x160D)
    OP_A2(0x160E)
    OP_A2(0x160F)
    OP_A2(0x1610)
    OP_A2(0x1611)
    OP_A2(0x1612)
    OP_A2(0x1614)
    OP_A2(0x1615)
    OP_A2(0x1616)
    OP_A2(0x1617)
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)
    OP_A2(0x1613)
    NewScene('ED6_DT21/R4100._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_2508(): pass

    label('loc_2508')

    OP_A2(0x1600)
    OP_A2(0x1601)
    OP_A2(0x1602)
    OP_A2(0x1603)
    OP_A2(0x1604)
    OP_A2(0x1607)
    OP_A2(0x1605)
    OP_A2(0x1606)
    OP_A2(0x1608)
    OP_A2(0x1609)
    OP_A2(0x160A)
    OP_A2(0x160B)
    OP_A2(0x160C)
    OP_A2(0x160D)
    OP_A2(0x160E)
    OP_A2(0x160F)
    OP_A2(0x1610)
    OP_A2(0x1611)
    OP_A2(0x1612)
    OP_A2(0x1614)
    OP_A2(0x1615)
    OP_A2(0x1616)
    OP_A2(0x1617)
    OP_A2(0x1613)
    OP_A2(0x1618)
    OP_A2(0x1619)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x161A)
    OP_A2(0x161B)
    OP_A2(0x161C)
    OP_A2(0x161D)
    OP_A2(0x161F)
    OP_A2(0x1620)
    OP_A2(0x1621)
    OP_A2(0x1622)
    OP_A2(0x1623)
    OP_A2(0x1624)
    OP_A2(0x1625)
    OP_A2(0x1626)
    OP_A2(0x1627)
    OP_A2(0x1628)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/R1504._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_25A1(): pass

    label('loc_25A1')

    OP_A2(0x1600)
    OP_A2(0x1601)
    OP_A2(0x1602)
    OP_A2(0x1603)
    OP_A2(0x1604)
    OP_A2(0x1607)
    OP_A2(0x1605)
    OP_A2(0x1606)
    OP_A2(0x1608)
    OP_A2(0x1609)
    OP_A2(0x160A)
    OP_A2(0x160B)
    OP_A2(0x160C)
    OP_A2(0x160D)
    OP_A2(0x160E)
    OP_A2(0x160F)
    OP_A2(0x1610)
    OP_A2(0x1611)
    OP_A2(0x1612)
    OP_A2(0x1614)
    OP_A2(0x1615)
    OP_A2(0x1616)
    OP_A2(0x1617)
    OP_A2(0x1613)
    OP_A2(0x1618)
    OP_A2(0x1619)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x161A)
    OP_A2(0x161B)
    OP_A2(0x161C)
    OP_A2(0x161D)
    OP_A2(0x161F)
    OP_A2(0x1620)
    OP_A2(0x1621)
    OP_A2(0x1622)
    OP_A2(0x1623)
    OP_A2(0x1624)
    OP_A2(0x1625)
    OP_A2(0x1626)
    OP_A2(0x1627)
    OP_A2(0x1628)
    FormationDelMember(0x00, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T4302._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_2641(): pass

    label('loc_2641')

    OP_A2(0x1600)
    OP_A2(0x1601)
    OP_A2(0x1602)
    OP_A2(0x1603)
    OP_A2(0x1604)
    OP_A2(0x1607)
    OP_A2(0x1605)
    OP_A2(0x1606)
    OP_A2(0x1608)
    OP_A2(0x1609)
    OP_A2(0x160A)
    OP_A2(0x160B)
    OP_A2(0x160C)
    OP_A2(0x160D)
    OP_A2(0x160E)
    OP_A2(0x160F)
    OP_A2(0x1610)
    OP_A2(0x1611)
    OP_A2(0x1612)
    OP_A2(0x1614)
    OP_A2(0x1615)
    OP_A2(0x1616)
    OP_A2(0x1617)
    OP_A2(0x1613)
    OP_A2(0x1618)
    OP_A2(0x1619)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x161A)
    OP_A2(0x161B)
    OP_A2(0x161C)
    OP_A2(0x161D)
    OP_A2(0x161F)
    OP_A2(0x1620)
    OP_A2(0x1621)
    OP_A2(0x1622)
    OP_A2(0x1623)
    OP_A2(0x1624)
    OP_A2(0x1625)
    OP_A2(0x1626)
    OP_A2(0x1627)
    OP_A2(0x1628)
    OP_A2(0x162A)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x162B)
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    OP_A2(0x162C)
    OP_A2(0x162D)
    NewScene('ED6_DT21/T4101._SN', 108, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_26E7(): pass

    label('loc_26E7')

    OP_A2(0x1600)
    OP_A2(0x1601)
    OP_A2(0x1602)
    OP_A2(0x1603)
    OP_A2(0x1604)
    OP_A2(0x1607)
    OP_A2(0x1605)
    OP_A2(0x1606)
    OP_A2(0x1608)
    OP_A2(0x1609)
    OP_A2(0x160A)
    OP_A2(0x160B)
    OP_A2(0x160C)
    OP_A2(0x160D)
    OP_A2(0x160E)
    OP_A2(0x160F)
    OP_A2(0x1610)
    OP_A2(0x1611)
    OP_A2(0x1612)
    OP_A2(0x1614)
    OP_A2(0x1615)
    OP_A2(0x1616)
    OP_A2(0x1617)
    OP_A2(0x1613)
    OP_A2(0x1618)
    OP_A2(0x1619)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x161A)
    OP_A2(0x161B)
    OP_A2(0x161C)
    OP_A2(0x161D)
    OP_A2(0x161F)
    OP_A2(0x1620)
    OP_A2(0x1621)
    OP_A2(0x1622)
    OP_A2(0x1623)
    OP_A2(0x1624)
    OP_A2(0x1625)
    OP_A2(0x1626)
    OP_A2(0x1627)
    OP_A2(0x1628)
    OP_A2(0x162A)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x162B)
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    OP_A2(0x162C)
    OP_A2(0x162D)
    OP_A2(0x162E)
    OP_A2(0x1630)
    OP_A2(0x1631)
    OP_A2(0x1632)
    OP_A2(0x1633)
    OP_A2(0x1634)
    OP_A2(0x1635)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1636)
    NewScene('ED6_DT21/T0600._SN', 107, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_27B4(): pass

    label('loc_27B4')

    OP_A2(0x1600)
    OP_A2(0x1601)
    OP_A2(0x1602)
    OP_A2(0x1603)
    OP_A2(0x1604)
    OP_A2(0x1607)
    OP_A2(0x1605)
    OP_A2(0x1606)
    OP_A2(0x1608)
    OP_A2(0x1609)
    OP_A2(0x160A)
    OP_A2(0x160B)
    OP_A2(0x160C)
    OP_A2(0x160D)
    OP_A2(0x160E)
    OP_A2(0x160F)
    OP_A2(0x1610)
    OP_A2(0x1611)
    OP_A2(0x1612)
    OP_A2(0x1614)
    OP_A2(0x1615)
    OP_A2(0x1616)
    OP_A2(0x1617)
    OP_A2(0x1613)
    OP_A2(0x1618)
    OP_A2(0x1619)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x161A)
    OP_A2(0x161B)
    OP_A2(0x161C)
    OP_A2(0x161D)
    OP_A2(0x161F)
    OP_A2(0x1620)
    OP_A2(0x1621)
    OP_A2(0x1622)
    OP_A2(0x1623)
    OP_A2(0x1624)
    OP_A2(0x1625)
    OP_A2(0x1626)
    OP_A2(0x1627)
    OP_A2(0x1628)
    OP_A2(0x162A)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x162B)
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    OP_A2(0x162C)
    OP_A2(0x162D)
    OP_A2(0x162E)
    OP_A2(0x1630)
    OP_A2(0x1631)
    OP_A2(0x1632)
    OP_A2(0x1633)
    OP_A2(0x1634)
    OP_A2(0x1635)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1636)
    OP_A2(0x1637)
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    OP_A2(0x1638)
    NewScene('ED6_DT21/T4150._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_288B(): pass

    label('loc_288B')

    OP_A2(0x1600)
    OP_A2(0x1601)
    OP_A2(0x1602)
    OP_A2(0x1603)
    OP_A2(0x1604)
    OP_A2(0x1607)
    OP_A2(0x1605)
    OP_A2(0x1606)
    OP_A2(0x1608)
    OP_A2(0x1609)
    OP_A2(0x160A)
    OP_A2(0x160B)
    OP_A2(0x160C)
    OP_A2(0x160D)
    OP_A2(0x160E)
    OP_A2(0x160F)
    OP_A2(0x1610)
    OP_A2(0x1611)
    OP_A2(0x1612)
    OP_A2(0x1614)
    OP_A2(0x1615)
    OP_A2(0x1616)
    OP_A2(0x1617)
    OP_A2(0x1613)
    OP_A2(0x1618)
    OP_A2(0x1619)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x161A)
    OP_A2(0x161B)
    OP_A2(0x161C)
    OP_A2(0x161D)
    OP_A2(0x161F)
    OP_A2(0x1620)
    OP_A2(0x1621)
    OP_A2(0x1622)
    OP_A2(0x1623)
    OP_A2(0x1624)
    OP_A2(0x1625)
    OP_A2(0x1626)
    OP_A2(0x1627)
    OP_A2(0x1628)
    OP_A2(0x162A)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x162B)
    OP_A2(0x162C)
    OP_A2(0x162D)
    OP_A2(0x162E)
    OP_A2(0x1630)
    OP_A2(0x1631)
    OP_A2(0x1632)
    OP_A2(0x1633)
    OP_A2(0x1634)
    OP_A2(0x1635)
    OP_A2(0x1636)
    OP_A2(0x1637)
    OP_A2(0x1638)
    OP_A2(0x1639)
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    OP_A2(0x163A)
    OP_A2(0x163B)
    OP_A2(0x163C)
    FormationAddMember(ChrTable['尤莉亚上尉'], 0xF9, 0xFF)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T4313._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_2962(): pass

    label('loc_2962')

    OP_A2(0x1600)
    OP_A2(0x1601)
    OP_A2(0x1602)
    OP_A2(0x1603)
    OP_A2(0x1604)
    OP_A2(0x1607)
    OP_A2(0x1605)
    OP_A2(0x1606)
    OP_A2(0x1608)
    OP_A2(0x1609)
    OP_A2(0x160A)
    OP_A2(0x160B)
    OP_A2(0x160C)
    OP_A2(0x160D)
    OP_A2(0x160E)
    OP_A2(0x160F)
    OP_A2(0x1610)
    OP_A2(0x1611)
    OP_A2(0x1612)
    OP_A2(0x1614)
    OP_A2(0x1615)
    OP_A2(0x1616)
    OP_A2(0x1617)
    OP_A2(0x1613)
    OP_A2(0x1618)
    OP_A2(0x1619)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x161A)
    OP_A2(0x161B)
    OP_A2(0x161C)
    OP_A2(0x161D)
    OP_A2(0x161F)
    OP_A2(0x1620)
    OP_A2(0x1621)
    OP_A2(0x1622)
    OP_A2(0x1623)
    OP_A2(0x1624)
    OP_A2(0x1625)
    OP_A2(0x1626)
    OP_A2(0x1627)
    OP_A2(0x1628)
    OP_A2(0x162A)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x162B)
    OP_A2(0x162C)
    OP_A2(0x162D)
    OP_A2(0x162E)
    OP_A2(0x1630)
    OP_A2(0x1631)
    OP_A2(0x1632)
    OP_A2(0x1633)
    OP_A2(0x1634)
    OP_A2(0x1635)
    OP_A2(0x1636)
    OP_A2(0x1637)
    OP_A2(0x1638)
    OP_A2(0x1639)
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    OP_A2(0x163A)
    OP_A2(0x163B)
    OP_A2(0x163C)
    FormationAddMember(ChrTable['尤莉亚上尉'], 0xF9, 0xFF)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/C5601._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_2A39(): pass

    label('loc_2A39')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2A46')

    def _loc_2A46(): pass

    label('loc_2A46')

    Jump('func_0E_231E')

    def _loc_2A49(): pass

    label('loc_2A49')

    OP_5F(0x0002)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000F offset: 0x2A59
@scena.Code('func_0F_2A59')
def func_0F_2A59():
    RemoveItem(ItemTable['山猫号启动钥匙'], 1)
    RemoveItem(ItemTable['黑巧克力'], 3)
    RemoveItem(ItemTable['储物室钥匙'], 1)
    RemoveItem(ItemTable['口琴'], 1)
    OP_A3(0x1800)
    OP_A3(0x1801)
    OP_A3(0x1802)
    OP_A3(0x1803)
    OP_A3(0x1804)
    OP_A3(0x1805)
    OP_A3(0x1806)
    OP_A3(0x1807)
    OP_A3(0x1808)
    OP_A3(0x1809)
    OP_A3(0x180A)
    OP_A3(0x180B)
    OP_A3(0x180C)
    OP_A3(0x180D)
    OP_A3(0x180E)
    OP_A3(0x180F)
    OP_A3(0x1810)
    OP_A3(0x1811)
    OP_A3(0x1812)
    OP_A3(0x1813)
    OP_A3(0x1814)
    OP_A3(0x1815)
    OP_A3(0x1816)
    OP_A3(0x1817)
    OP_A3(0x1818)
    OP_A3(0x1819)
    OP_A3(0x181A)
    OP_A3(0x181B)
    OP_A3(0x181C)
    OP_A3(0x181D)
    OP_A3(0x181E)
    OP_A3(0x181F)
    OP_A3(0x1820)
    OP_A3(0x1821)
    OP_A3(0x1822)
    OP_A3(0x1823)
    OP_A3(0x1824)
    OP_A3(0x1825)
    OP_A3(0x1826)
    OP_A3(0x1827)
    OP_A3(0x1828)
    OP_A3(0x1829)
    OP_A3(0x182A)
    OP_A3(0x182B)
    OP_A3(0x182C)
    OP_A3(0x182D)
    OP_A3(0x182E)
    OP_A3(0x182F)
    OP_A3(0x1830)
    OP_A3(0x1831)
    OP_A3(0x1832)
    OP_A3(0x1833)
    OP_A3(0x1834)
    OP_A3(0x1835)
    OP_A3(0x1836)
    OP_A3(0x1837)
    OP_A3(0x1838)
    OP_A3(0x1839)
    OP_A3(0x183A)
    OP_A3(0x183B)
    OP_A3(0x183C)
    OP_A3(0x183D)
    OP_A3(0x183E)
    OP_A3(0x183F)
    OP_A3(0x1840)
    OP_A3(0x1880)
    OP_A3(0x1881)
    OP_A3(0x1882)
    OP_A3(0x1883)
    OP_A3(0x1885)
    OP_A3(0x1886)

    Return()

# id: 0x0010 offset: 0x2B43
@scena.Code('func_10_2B43')
def func_10_2B43():
    OP_A2(0x1800)
    OP_A2(0x1801)
    OP_A2(0x1802)
    OP_A2(0x1803)
    OP_A2(0x1804)
    OP_A2(0x1805)
    OP_A2(0x1806)
    OP_A2(0x1807)
    OP_A2(0x1808)
    OP_A2(0x1809)
    OP_A2(0x180A)
    OP_A2(0x180B)
    OP_A2(0x180C)
    OP_A2(0x180D)
    OP_A2(0x180E)
    OP_A2(0x180F)
    OP_A2(0x1810)
    OP_A2(0x1811)
    OP_A2(0x1812)
    OP_A2(0x1813)
    OP_A2(0x1814)
    OP_A2(0x1815)
    OP_A2(0x1816)
    OP_BB(0x00, 0x01, 0x00000043)
    OP_A2(0x1817)
    OP_A2(0x1818)
    OP_A2(0x1819)
    OP_A2(0x181A)
    OP_A2(0x181B)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_A2(0x181C)
    OP_A2(0x181D)
    OP_A2(0x181E)
    OP_A2(0x181F)
    OP_A2(0x1820)
    OP_A2(0x1821)
    OP_A2(0x1822)
    OP_A2(0x1823)
    OP_A2(0x1824)
    OP_A2(0x1825)
    OP_A2(0x1826)

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1827)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1828)
    OP_A2(0x1833)
    OP_BB(0x00, 0x01, 0x00000044)
    OP_A2(0x1834)
    OP_A2(0x1835)
    OP_A2(0x1836)
    OP_A2(0x1837)
    OP_A2(0x1838)
    AddItem(ItemTable['储物室钥匙'], 1)
    OP_A2(0x1839)
    OP_A2(0x183A)
    AddItem(ItemTable['口琴'], 1)
    OP_A2(0x183B)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()

    Return()

# id: 0x0011 offset: 0x2C18
@scena.Code('func_11_2C18')
def func_11_2C18():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3144',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '0·序（约修亚篇）\n'),
            TXT(0x01, '①·乘定期船移动\n'),
            TXT(0x02, '②·调查雾的发生范围\n'),
            TXT(0x03, '③·调查昏睡状态的人们\n'),
            TXT(0x04, '④·布莱特家投宿\n'),
            TXT(0x05, '⑤·帕赛尔农场的危机\n'),
            TXT(0x06, '⑥·神秘森林\n'),
            TXT(0x07, '⑦·幻影的布莱特家\n'),
            TXT(0x08, '⑧·尾声\n'),
            TXT(0x09, '③_第２夜的洛连特市街\n'),
            TXT(0x0A, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    AddItem(ItemTable['利贝尔王国地图'], 1)
    Call(4, 0x0004)
    Call(4, 0x0007)
    Call(4, 0x000A)
    Call(4, 0x000D)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2D3F'),
        (0x00000001, 'loc_2D4E'),
        (0x00000002, 'loc_2D7D'),
        (0x00000003, 'loc_2DB5'),
        (0x00000004, 'loc_2DFF'),
        (0x00000005, 'loc_2E55'),
        (0x00000006, 'loc_2EC4'),
        (0x00000007, 'loc_2F5B'),
        (0x00000008, 'loc_300A'),
        (0x00000009, 'loc_30EA'),
        (-1, 'loc_3134'),
    )

    def _loc_2D3F(): pass

    label('loc_2D3F')

    OP_A2(0x10F0)
    NewScene('ED6_DT21/C1402._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_2D4E(): pass

    label('loc_2D4E')

    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['乔丝特2'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['多伦'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['吉尔'], 0xFF, 0xFF)
    OP_A2(0x1800)
    OP_A2(0x1801)
    OP_A2(0x1802)
    OP_A2(0x1803)
    OP_A2(0x1804)
    OP_A2(0x1805)
    NewScene('ED6_DT21/E0001._SN', 104, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_2D7D(): pass

    label('loc_2D7D')

    FormationReset()
    OP_A2(0x1800)
    OP_A2(0x1801)
    OP_A2(0x1802)
    OP_A2(0x1803)
    OP_A2(0x1804)
    OP_A2(0x1805)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x1806)
    OP_A2(0x1807)
    OP_A2(0x1808)
    OP_A2(0x1809)
    OP_A2(0x180A)
    OP_A2(0x180B)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T0121._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_2DB5(): pass

    label('loc_2DB5')

    FormationReset()
    OP_A2(0x1800)
    OP_A2(0x1801)
    OP_A2(0x1802)
    OP_A2(0x1803)
    OP_A2(0x1804)
    OP_A2(0x1805)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x1806)
    OP_A2(0x1807)
    OP_A2(0x1808)
    OP_A2(0x1809)
    OP_A2(0x180A)
    OP_A2(0x180B)
    OP_A2(0x180C)
    OP_A2(0x180D)
    OP_A2(0x180E)
    OP_A2(0x180F)
    OP_A2(0x1810)
    OP_A2(0x1811)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T0121._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_2DFF(): pass

    label('loc_2DFF')

    FormationReset()
    OP_A2(0x1800)
    OP_A2(0x1801)
    OP_A2(0x1802)
    OP_A2(0x1803)
    OP_A2(0x1804)
    OP_A2(0x1805)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x1806)
    OP_A2(0x1807)
    OP_A2(0x1808)
    OP_A2(0x1809)
    OP_A2(0x180A)
    OP_A2(0x180B)
    OP_A2(0x180C)
    OP_A2(0x180D)
    OP_A2(0x180E)
    OP_A2(0x180F)
    OP_A2(0x1810)
    OP_A2(0x1811)
    OP_A2(0x1812)
    OP_A2(0x1813)
    OP_A2(0x1814)
    OP_A2(0x1815)
    OP_A2(0x1816)
    NewScene('ED6_DT21/T0123._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_2E55(): pass

    label('loc_2E55')

    OP_A2(0x1800)
    OP_A2(0x1801)
    OP_A2(0x1802)
    OP_A2(0x1803)
    OP_A2(0x1804)
    OP_A2(0x1805)
    OP_A2(0x1806)
    OP_A2(0x1807)
    OP_A2(0x1808)
    OP_A2(0x1809)
    OP_A2(0x180A)
    OP_A2(0x180B)
    OP_A2(0x180C)
    OP_A2(0x180D)
    OP_A2(0x180E)
    OP_A2(0x180F)
    OP_A2(0x1810)
    OP_A2(0x1811)
    OP_A2(0x1812)
    OP_A2(0x1813)
    OP_A2(0x1814)
    OP_A2(0x1815)
    OP_A2(0x1816)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_BB(0x00, 0x01, 0x00000043)
    OP_A2(0x1817)
    OP_A2(0x1818)
    OP_A2(0x1819)
    OP_A2(0x181A)
    OP_A2(0x181B)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T0300._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_2EC4(): pass

    label('loc_2EC4')

    OP_A2(0x1800)
    OP_A2(0x1801)
    OP_A2(0x1802)
    OP_A2(0x1803)
    OP_A2(0x1804)
    OP_A2(0x1805)
    OP_A2(0x1806)
    OP_A2(0x1807)
    OP_A2(0x1808)
    OP_A2(0x1809)
    OP_A2(0x180A)
    OP_A2(0x180B)
    OP_A2(0x180C)
    OP_A2(0x180D)
    OP_A2(0x180E)
    OP_A2(0x180F)
    OP_A2(0x1810)
    OP_A2(0x1811)
    OP_A2(0x1812)
    OP_A2(0x1813)
    OP_A2(0x1814)
    OP_A2(0x1815)
    OP_A2(0x1816)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_BB(0x00, 0x01, 0x00000043)
    OP_A2(0x1817)
    OP_A2(0x1818)
    OP_A2(0x1819)
    OP_A2(0x181A)
    OP_A2(0x181B)
    OP_BB(0x00, 0x01, 0x00000000)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    OP_A2(0x181C)
    OP_A2(0x181D)
    OP_A2(0x181E)
    OP_A2(0x181F)
    OP_A2(0x1820)
    OP_A2(0x1821)
    OP_A2(0x1822)
    OP_A2(0x1823)
    NewScene('ED6_DT21/C0300._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_2F5B(): pass

    label('loc_2F5B')

    OP_A2(0x1800)
    OP_A2(0x1801)
    OP_A2(0x1802)
    OP_A2(0x1803)
    OP_A2(0x1804)
    OP_A2(0x1805)
    OP_A2(0x1806)
    OP_A2(0x1807)
    OP_A2(0x1808)
    OP_A2(0x1809)
    OP_A2(0x180A)
    OP_A2(0x180B)
    OP_A2(0x180C)
    OP_A2(0x180D)
    OP_A2(0x180E)
    OP_A2(0x180F)
    OP_A2(0x1810)
    OP_A2(0x1811)
    OP_A2(0x1812)
    OP_A2(0x1813)
    OP_A2(0x1814)
    OP_A2(0x1815)
    OP_A2(0x1816)
    OP_BB(0x00, 0x01, 0x00000043)
    OP_A2(0x1817)
    OP_A2(0x1818)
    OP_A2(0x1819)
    OP_A2(0x181A)
    OP_A2(0x181B)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_A2(0x181C)
    OP_A2(0x181D)
    OP_A2(0x181E)
    OP_A2(0x181F)
    OP_A2(0x1820)
    OP_A2(0x1821)
    OP_A2(0x1822)
    OP_A2(0x1823)
    OP_A2(0x1824)
    OP_A2(0x1825)
    OP_A2(0x1826)

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1827)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1828)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T0300._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_300A(): pass

    label('loc_300A')

    OP_A2(0x1800)
    OP_A2(0x1801)
    OP_A2(0x1802)
    OP_A2(0x1803)
    OP_A2(0x1804)
    OP_A2(0x1805)
    OP_A2(0x1806)
    OP_A2(0x1807)
    OP_A2(0x1808)
    OP_A2(0x1809)
    OP_A2(0x180A)
    OP_A2(0x180B)
    OP_A2(0x180C)
    OP_A2(0x180D)
    OP_A2(0x180E)
    OP_A2(0x180F)
    OP_A2(0x1810)
    OP_A2(0x1811)
    OP_A2(0x1812)
    OP_A2(0x1813)
    OP_A2(0x1814)
    OP_A2(0x1815)
    OP_A2(0x1816)
    OP_BB(0x00, 0x01, 0x00000043)
    OP_A2(0x1817)
    OP_A2(0x1818)
    OP_A2(0x1819)
    OP_A2(0x181A)
    OP_A2(0x181B)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_A2(0x181C)
    OP_A2(0x181D)
    OP_A2(0x181E)
    OP_A2(0x181F)
    OP_A2(0x1820)
    OP_A2(0x1821)
    OP_A2(0x1822)
    OP_A2(0x1823)
    OP_A2(0x1824)
    OP_A2(0x1825)
    OP_A2(0x1826)

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1827)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x1828)
    OP_A2(0x1833)
    OP_BB(0x00, 0x01, 0x00000044)
    OP_A2(0x1834)
    OP_A2(0x1835)
    OP_A2(0x1836)
    OP_A2(0x1837)
    OP_A2(0x1838)
    AddItem(ItemTable['储物室钥匙'], 1)
    OP_A2(0x1839)
    OP_A2(0x183A)
    AddItem(ItemTable['口琴'], 1)
    OP_A2(0x183B)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T0100._SN', 119, 0, 0)
    IdleLoop()

    def _loc_30EA(): pass

    label('loc_30EA')

    FormationReset()
    OP_A2(0x1800)
    OP_A2(0x1801)
    OP_A2(0x1802)
    OP_A2(0x1803)
    OP_A2(0x1804)
    OP_A2(0x1805)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x1806)
    OP_A2(0x1807)
    OP_A2(0x1808)
    OP_A2(0x1809)
    OP_A2(0x180A)
    OP_A2(0x180B)
    OP_A2(0x180C)
    OP_A2(0x180D)
    OP_A2(0x180E)
    OP_A2(0x180F)
    OP_A2(0x1810)
    OP_A2(0x1811)
    OP_A2(0x1812)
    NewScene('ED6_DT21/T0123._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_3134(): pass

    label('loc_3134')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3141')

    def _loc_3141(): pass

    label('loc_3141')

    Jump('func_11_2C18')

    def _loc_3144(): pass

    label('loc_3144')

    OP_5F(0x0002)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0012 offset: 0x3154
@scena.Code('func_12_3154')
def func_12_3154():
    OP_A3(0x1A00)
    OP_A3(0x1A01)
    OP_A3(0x1A02)
    OP_A3(0x1A03)
    OP_A3(0x1A04)
    OP_A3(0x1A05)
    OP_A3(0x1A06)
    OP_A3(0x1A07)
    OP_A3(0x1A08)
    OP_A3(0x1A09)
    OP_A3(0x1A0A)
    OP_A3(0x1A0B)
    OP_A3(0x1A0C)
    OP_A3(0x1A0D)
    OP_A3(0x1A0E)
    OP_A3(0x1A0F)
    OP_A3(0x1A10)
    OP_A3(0x1A11)
    OP_A3(0x1A12)
    OP_A3(0x1A13)
    OP_A3(0x1A14)
    OP_A3(0x1A15)
    OP_A3(0x1A16)
    OP_A3(0x1A17)
    OP_A3(0x1A18)
    OP_A3(0x1A19)
    OP_A3(0x1A1A)
    OP_A3(0x1A83)
    OP_A3(0x1A1B)
    OP_A3(0x1A1C)
    OP_A3(0x1A1D)
    OP_A3(0x1A1E)
    OP_A3(0x1A1F)
    OP_A3(0x1A20)
    OP_A3(0x1A21)
    OP_A3(0x1A22)
    OP_A3(0x1A23)
    OP_A3(0x1A24)
    OP_A3(0x1A25)
    OP_A3(0x1A26)
    OP_A3(0x1A27)
    OP_A3(0x1A28)
    OP_A3(0x1A29)
    OP_A3(0x1A79)

    Return()

# id: 0x0013 offset: 0x31D9
@scena.Code('func_13_31D9')
def func_13_31D9():
    OP_A2(0x1A00)
    OP_A2(0x1A01)
    OP_A2(0x1A02)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1A03)
    OP_A2(0x1A04)
    OP_A2(0x1A05)
    OP_A2(0x1A07)
    OP_A2(0x1A08)
    OP_A2(0x1A09)
    OP_A2(0x1A0A)
    OP_A2(0x1A0B)
    OP_A2(0x1A0C)
    OP_A2(0x1A06)
    OP_A2(0x1A0D)
    OP_A2(0x1A0E)
    OP_A2(0x1A0F)
    OP_A2(0x1A10)
    OP_A2(0x1A11)
    OP_A2(0x1A12)
    OP_A2(0x1A13)
    OP_A2(0x1A14)
    OP_A2(0x1A15)
    OP_A2(0x1A16)
    OP_A2(0x1A17)
    OP_A2(0x1A18)
    OP_A2(0x1A19)
    OP_A2(0x1A1A)
    OP_A2(0x1A83)
    OP_A2(0x1A1B)
    OP_A2(0x1A1C)
    OP_A2(0x1A1D)
    OP_A2(0x1A1E)
    OP_A2(0x1A1F)
    OP_A2(0x1A20)
    OP_A2(0x1A21)
    OP_A2(0x1A22)
    OP_A2(0x1A23)
    OP_A2(0x1A24)
    OP_A2(0x1A25)
    OP_A2(0x1A26)
    OP_A2(0x1A27)
    OP_A2(0x1A28)
    OP_A2(0x1A29)
    OP_A2(0x1A79)

    Return()

# id: 0x0014 offset: 0x3270
@scena.Code('func_14_3270')
def func_14_3270():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3720',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '0·序\n'),
            TXT(0x01, '①·从洛连特出发\n'),
            TXT(0x02, '②·剿灭通缉的魔兽～古龙的登场\n'),
            TXT(0x03, '③·拉文努村～废坑\n'),
            TXT(0x04, '④·拉文努村～Boss归还\n'),
            TXT(0x05, '⑤·古龙捕获作战\n'),
            TXT(0x06, '⑥·古龙的住处\n'),
            TXT(0x07, '⑦·尾声\n'),
            TXT(0x08, '②_2古龙登场之前\n'),
            TXT(0x09, '5-·Dragon Op.·Mission Explanation~(Warning· Breaks Flags)\n'),
            TXT(0x0A, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    AddItem(ItemTable['利贝尔王国地图'], 1)
    Call(4, 0x0004)
    Call(4, 0x0007)
    Call(4, 0x000A)
    Call(4, 0x000D)
    Call(4, 0x0010)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_33BE'),
        (0x00000001, 'loc_33CD'),
        (0x00000002, 'loc_33DF'),
        (0x00000003, 'loc_3427'),
        (0x00000004, 'loc_3481'),
        (0x00000005, 'loc_34F3'),
        (0x00000006, 'loc_356B'),
        (0x00000007, 'loc_360B'),
        (0x00000008, 'loc_36AD'),
        (0x00000009, 'loc_3701'),
        (-1, 'loc_3710'),
    )

    def _loc_33BE(): pass

    label('loc_33BE')

    OP_A2(0x10F0)
    NewScene('ED6_DT21/C0705._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_33CD(): pass

    label('loc_33CD')

    OP_A2(0x10F1)
    OP_A2(0x1A00)
    NewScene('ED6_DT21/T0100._SN', 110, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_33DF(): pass

    label('loc_33DF')

    OP_A2(0x1A00)
    OP_A2(0x1A01)
    OP_A2(0x1A02)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1A03)
    OP_A2(0x1A04)
    OP_A2(0x1A05)
    OP_A2(0x1A07)
    OP_A2(0x1A08)
    OP_A2(0x1A09)
    OP_A2(0x1A0A)
    OP_A2(0x1A0B)
    OP_A2(0x1A0C)
    OP_A2(0x1A06)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T1121._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_3427(): pass

    label('loc_3427')

    OP_A2(0x1A00)
    OP_A2(0x1A01)
    OP_A2(0x1A02)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1A03)
    OP_A2(0x1A04)
    OP_A2(0x1A05)
    OP_A2(0x1A07)
    OP_A2(0x1A08)
    OP_A2(0x1A09)
    OP_A2(0x1A0A)
    OP_A2(0x1A0B)
    OP_A2(0x1A0C)
    OP_A2(0x1A06)
    OP_A2(0x1A0D)
    OP_A2(0x1A0E)
    OP_A2(0x1A0F)
    OP_A2(0x1A10)
    OP_A2(0x1A11)
    OP_A2(0x1A12)
    OP_A2(0x1A13)
    NewScene('ED6_DT21/T1201._SN', 108, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_3481(): pass

    label('loc_3481')

    OP_A2(0x1A00)
    OP_A2(0x1A01)
    OP_A2(0x1A02)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1A03)
    OP_A2(0x1A04)
    OP_A2(0x1A05)
    OP_A2(0x1A07)
    OP_A2(0x1A08)
    OP_A2(0x1A09)
    OP_A2(0x1A0A)
    OP_A2(0x1A0B)
    OP_A2(0x1A0C)
    OP_A2(0x1A06)
    OP_A2(0x1A0D)
    OP_A2(0x1A0E)
    OP_A2(0x1A0F)
    OP_A2(0x1A10)
    OP_A2(0x1A11)
    OP_A2(0x1A12)
    OP_A2(0x1A13)
    OP_A2(0x1A14)
    OP_A2(0x1A15)
    OP_A2(0x1A16)
    OP_A2(0x1A17)
    OP_A2(0x1A18)
    OP_A2(0x1A19)
    OP_A2(0x1A83)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T1201._SN', 108, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_34F3(): pass

    label('loc_34F3')

    OP_A2(0x1A00)
    OP_A2(0x1A01)
    OP_A2(0x1A02)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1A03)
    OP_A2(0x1A04)
    OP_A2(0x1A05)
    OP_A2(0x1A07)
    OP_A2(0x1A08)
    OP_A2(0x1A09)
    OP_A2(0x1A0A)
    OP_A2(0x1A0B)
    OP_A2(0x1A0C)
    OP_A2(0x1A06)
    OP_A2(0x1A0D)
    OP_A2(0x1A0E)
    OP_A2(0x1A0F)
    OP_A2(0x1A10)
    OP_A2(0x1A11)
    OP_A2(0x1A12)
    OP_A2(0x1A13)
    OP_A2(0x1A14)
    OP_A2(0x1A15)
    OP_A2(0x1A16)
    OP_A2(0x1A17)
    OP_A2(0x1A18)
    OP_A2(0x1A19)
    OP_A2(0x1A83)
    OP_A2(0x1A1A)
    OP_A2(0x1A1B)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T1103._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_356B(): pass

    label('loc_356B')

    OP_A2(0x1A00)
    OP_A2(0x1A01)
    OP_A2(0x1A02)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1A03)
    OP_A2(0x1A04)
    OP_A2(0x1A05)
    OP_A2(0x1A07)
    OP_A2(0x1A08)
    OP_A2(0x1A09)
    OP_A2(0x1A0A)
    OP_A2(0x1A0B)
    OP_A2(0x1A0C)
    OP_A2(0x1A06)
    OP_A2(0x1A0D)
    OP_A2(0x1A0E)
    OP_A2(0x1A0F)
    OP_A2(0x1A10)
    OP_A2(0x1A11)
    OP_A2(0x1A12)
    OP_A2(0x1A13)
    OP_A2(0x1A14)
    OP_A2(0x1A15)
    OP_A2(0x1A16)
    OP_A2(0x1A17)
    OP_A2(0x1A18)
    OP_A2(0x1A19)
    OP_A2(0x1A83)
    OP_A2(0x1A1A)
    OP_A2(0x1A1B)
    OP_A2(0x1A1C)
    OP_A2(0x1A1D)
    OP_A2(0x1A1E)
    OP_A2(0x1A1F)
    OP_A2(0x1A20)
    OP_A2(0x1A21)
    OP_A2(0x1A22)
    OP_A2(0x1A23)
    FormationAddMember(ChrTable['科洛丝'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF9, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFA, 0xFF)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T1102._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_360B(): pass

    label('loc_360B')

    OP_A2(0x1A00)
    OP_A2(0x1A01)
    OP_A2(0x1A02)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1A03)
    OP_A2(0x1A04)
    OP_A2(0x1A05)
    OP_A2(0x1A07)
    OP_A2(0x1A08)
    OP_A2(0x1A09)
    OP_A2(0x1A0A)
    OP_A2(0x1A0B)
    OP_A2(0x1A0C)
    OP_A2(0x1A06)
    OP_A2(0x1A0D)
    OP_A2(0x1A0E)
    OP_A2(0x1A0F)
    OP_A2(0x1A10)
    OP_A2(0x1A11)
    OP_A2(0x1A12)
    OP_A2(0x1A13)
    OP_A2(0x1A14)
    OP_A2(0x1A15)
    OP_A2(0x1A16)
    OP_A2(0x1A17)
    OP_A2(0x1A18)
    OP_A2(0x1A19)
    OP_A2(0x1A1A)
    OP_A2(0x1A83)
    OP_A2(0x1A1B)
    OP_A2(0x1A1C)
    OP_A2(0x1A1D)
    OP_A2(0x1A1E)
    OP_A2(0x1A1F)
    OP_A2(0x1A20)
    OP_A2(0x1A21)
    OP_A2(0x1A22)
    OP_A2(0x1A23)
    OP_A2(0x1A24)
    OP_A2(0x1A25)
    OP_A2(0x1A26)
    OP_A2(0x1A27)
    OP_A2(0x1A28)
    OP_A2(0x1A29)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T1202._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_36AD(): pass

    label('loc_36AD')

    OP_A2(0x1A00)
    OP_A2(0x1A01)
    OP_A2(0x1A02)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_A2(0x1A03)
    OP_A2(0x1A04)
    OP_A2(0x1A05)
    OP_A2(0x1A07)
    OP_A2(0x1A08)
    OP_A2(0x1A09)
    OP_A2(0x1A0A)
    OP_A2(0x1A0B)
    OP_A2(0x1A0C)
    OP_A2(0x1A06)
    OP_A2(0x1A0D)
    OP_A2(0x1A0E)
    OP_A2(0x1A0F)
    OP_A2(0x1A10)
    OP_A2(0x1A11)
    NewScene('ED6_DT21/T1121._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_3701(): pass

    label('loc_3701')

    OP_A2(0x10F0)
    NewScene('ED6_DT21/E0311._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_3710(): pass

    label('loc_3710')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_371D')

    def _loc_371D(): pass

    label('loc_371D')

    Jump('func_14_3270')

    def _loc_3720(): pass

    label('loc_3720')

    OP_5F(0x0002)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0015 offset: 0x3730
@scena.Code('func_15_3730')
def func_15_3730():
    RemoveItem(ItemTable['红色密码卡'], 1)
    RemoveItem(ItemTable['绿色密码卡'], 1)
    RemoveItem(ItemTable['蓝色密码卡'], 1)
    OP_A3(0x1C00)
    OP_A3(0x1C01)
    OP_A3(0x1C02)
    OP_A3(0x1C03)
    OP_A3(0x1C80)
    OP_A3(0x1C04)
    OP_A3(0x1C05)
    OP_A3(0x1C06)
    OP_A3(0x1C07)
    OP_A3(0x1C08)
    OP_A3(0x1C09)
    OP_A3(0x1C0A)
    OP_A3(0x1C0B)
    OP_A3(0x1C0C)
    OP_A3(0x1C0D)
    OP_A3(0x1C0E)
    OP_A3(0x1C0F)
    OP_A3(0x1C10)
    OP_A3(0x1C11)
    OP_A3(0x1C12)
    OP_A3(0x1C13)
    OP_A3(0x1C14)
    OP_A3(0x1C15)
    OP_A3(0x1C16)
    OP_A3(0x1C17)
    OP_A3(0x1C18)
    OP_A3(0x1C19)
    OP_A3(0x1C1A)
    OP_A3(0x1C1B)
    OP_A3(0x1C1C)
    OP_A3(0x1C81)
    OP_A3(0x1C82)
    OP_A3(0x1C83)
    OP_A3(0x1C84)
    OP_A3(0x1C85)
    OP_A3(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)
    OP_A3(0x1C1D)
    OP_A3(0x1C1E)
    OP_A3(0x1C1F)
    OP_A3(0x1C20)
    OP_A3(0x1C21)
    OP_A3(0x1C22)
    OP_A3(0x1C23)
    OP_A3(0x1C24)
    OP_A3(0x1C25)
    OP_A3(0x1C26)
    OP_A3(0x1C27)
    OP_A3(0x1C28)
    OP_A3(0x1CA5)

    Return()

# id: 0x0016 offset: 0x37D9
@scena.Code('func_16_37D9')
def func_16_37D9():
    OP_A2(0x1C00)
    OP_A2(0x1C01)
    OP_A2(0x1C02)
    OP_A2(0x1C03)
    OP_A2(0x1C04)
    OP_A2(0x1C05)
    OP_A2(0x1C06)
    OP_A2(0x1C1A)
    OP_A2(0x1C07)
    OP_A2(0x1C08)
    AddItem(ItemTable['红色密码卡'], 1)
    OP_A2(0x1C09)
    OP_A2(0x1C0A)
    OP_A2(0x1C0B)
    AddItem(ItemTable['绿色密码卡'], 1)
    OP_A2(0x1C0C)
    OP_A2(0x1C0D)
    AddItem(ItemTable['蓝色密码卡'], 1)
    OP_A2(0x1C0E)
    OP_A2(0x1C0F)
    OP_A2(0x1C10)
    OP_A2(0x1C11)
    OP_A2(0x1C12)
    OP_A2(0x1C13)
    OP_A2(0x1C14)
    OP_A2(0x1C15)
    OP_A2(0x1C16)
    OP_A2(0x1C17)
    OP_A2(0x1C18)
    OP_A2(0x1C19)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x1C1B)
    OP_A2(0x1C1C)
    OP_A2(0x1C1D)
    OP_A2(0x1C26)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    OP_BB(0x01, 0x00, 0x00200033)
    OP_BB(0x01, 0x01, 0x00000001)
    OP_BD()
    OP_A2(0x1C27)
    OP_A2(0x1C28)
    OP_A2(0x1CA5)

    Return()

# id: 0x0017 offset: 0x3867
@scena.Code('func_17_3867')
def func_17_3867():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B40',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '0·序\n'),
            TXT(0x01, '①·去湖畔旅店\n'),
            TXT(0x02, '②·在川蝉亭的短暂时间\n'),
            TXT(0x03, '③·湖畔的研究所\n'),
            TXT(0x04, '④·飞行战舰古罗力亚斯\n'),
            TXT(0x05, '⑤·古罗力亚斯脱逃\n'),
            TXT(0x06, '⑥·尾声\n'),
            TXT(0x07, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    AddItem(ItemTable['利贝尔王国地图'], 1)
    Call(4, 0x0004)
    Call(4, 0x0007)
    Call(4, 0x000A)
    Call(4, 0x000D)
    Call(4, 0x0010)
    Call(4, 0x0013)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3946'),
        (0x00000001, 'loc_3955'),
        (0x00000002, 'loc_396C'),
        (0x00000003, 'loc_3989'),
        (0x00000004, 'loc_39A9'),
        (0x00000005, 'loc_3A1D'),
        (0x00000006, 'loc_3A97'),
        (-1, 'loc_3B30'),
    )

    def _loc_3946(): pass

    label('loc_3946')

    OP_A2(0x10F0)
    NewScene('ED6_DT21/E0101._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3B3D')

    def _loc_3955(): pass

    label('loc_3955')

    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    OP_A2(0x1C00)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T1121._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3B3D')

    def _loc_396C(): pass

    label('loc_396C')

    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    OP_A2(0x1C00)
    OP_A2(0x1C01)
    OP_A2(0x1C02)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T1510._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3B3D')

    def _loc_3989(): pass

    label('loc_3989')

    OP_A2(0x1C00)
    OP_A2(0x1C01)
    OP_A2(0x1C02)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x1C03)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/E0901._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3B3D')

    def _loc_39A9(): pass

    label('loc_39A9')

    OP_A2(0x1C00)
    OP_A2(0x1C01)
    OP_A2(0x1C02)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x1C03)
    OP_A2(0x1C04)
    OP_A2(0x1C05)
    OP_A2(0x1C06)
    OP_A2(0x1C1A)
    OP_A2(0x1C07)
    OP_A2(0x1C08)
    AddItem(ItemTable['红色密码卡'], 1)
    OP_A2(0x1C09)
    OP_A2(0x1C0A)
    OP_A2(0x1C0B)
    AddItem(ItemTable['绿色密码卡'], 1)
    OP_A2(0x1C0C)
    OP_A2(0x1C0D)
    AddItem(ItemTable['蓝色密码卡'], 1)
    OP_A2(0x1C0E)
    OP_A2(0x1C0F)
    OP_A2(0x1C10)
    OP_A2(0x1C11)
    OP_A2(0x1C12)
    OP_A2(0x1C13)
    OP_A2(0x1C14)
    OP_A2(0x1C15)
    OP_A2(0x1C16)
    OP_A2(0x1C17)
    OP_A2(0x1C18)
    OP_A2(0x1C19)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5400._SN', 111, 0, 0)
    IdleLoop()

    Jump('loc_3B3D')

    def _loc_3A1D(): pass

    label('loc_3A1D')

    OP_A2(0x1C00)
    OP_A2(0x1C01)
    OP_A2(0x1C02)
    OP_A2(0x1C03)
    OP_A2(0x1C04)
    OP_A2(0x1C05)
    OP_A2(0x1C06)
    OP_A2(0x1C1A)
    OP_A2(0x1C07)
    OP_A2(0x1C08)
    AddItem(ItemTable['红色密码卡'], 1)
    OP_A2(0x1C09)
    OP_A2(0x1C0A)
    OP_A2(0x1C0B)
    AddItem(ItemTable['绿色密码卡'], 1)
    OP_A2(0x1C0C)
    OP_A2(0x1C0D)
    AddItem(ItemTable['蓝色密码卡'], 1)
    OP_A2(0x1C0E)
    OP_A2(0x1C0F)
    OP_A2(0x1C10)
    OP_A2(0x1C11)
    OP_A2(0x1C12)
    OP_A2(0x1C13)
    OP_A2(0x1C14)
    OP_A2(0x1C15)
    OP_A2(0x1C16)
    OP_A2(0x1C17)
    OP_A2(0x1C18)
    OP_A2(0x1C19)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x1C1B)
    OP_A2(0x1C1C)
    OP_A2(0x10F5)
    NewScene('ED6_DT21/C5400._SN', 110, 0, 0)
    IdleLoop()

    Jump('loc_3B3D')

    def _loc_3A97(): pass

    label('loc_3A97')

    OP_A2(0x1C00)
    OP_A2(0x1C01)
    OP_A2(0x1C02)
    OP_A2(0x1C03)
    OP_A2(0x1C04)
    OP_A2(0x1C05)
    OP_A2(0x1C06)
    OP_A2(0x1C1A)
    OP_A2(0x1C07)
    OP_A2(0x1C08)
    AddItem(ItemTable['红色密码卡'], 1)
    OP_A2(0x1C09)
    OP_A2(0x1C0A)
    OP_A2(0x1C0B)
    AddItem(ItemTable['绿色密码卡'], 1)
    OP_A2(0x1C0C)
    OP_A2(0x1C0D)
    AddItem(ItemTable['蓝色密码卡'], 1)
    OP_A2(0x1C0E)
    OP_A2(0x1C0F)
    OP_A2(0x1C10)
    OP_A2(0x1C11)
    OP_A2(0x1C12)
    OP_A2(0x1C13)
    OP_A2(0x1C14)
    OP_A2(0x1C15)
    OP_A2(0x1C16)
    OP_A2(0x1C17)
    OP_A2(0x1C18)
    OP_A2(0x1C19)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x1C1B)
    OP_A2(0x1C1C)
    OP_A2(0x1C1D)
    OP_A2(0x1C26)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    OP_BB(0x01, 0x00, 0x00200033)
    OP_BB(0x01, 0x01, 0x00000001)
    OP_BD()
    OP_A2(0x1C27)
    OP_A2(0x1C28)
    OP_A2(0x10FB)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3B3D')

    def _loc_3B30(): pass

    label('loc_3B30')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3B3D')

    def _loc_3B3D(): pass

    label('loc_3B3D')

    Jump('func_17_3867')

    def _loc_3B40(): pass

    label('loc_3B40')

    OP_5F(0x0002)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0018 offset: 0x3B50
@scena.Code('func_18_3B50')
def func_18_3B50():
    RemoveItem(ItemTable['数据水晶０'], 1)
    RemoveItem(ItemTable['数据水晶１'], 1)
    RemoveItem(ItemTable['数据水晶２'], 1)
    RemoveItem(ItemTable['数据水晶３'], 1)
    RemoveItem(ItemTable['数据水晶４'], 1)
    RemoveItem(ItemTable['数据水晶５'], 1)
    RemoveItem(ItemTable['数据水晶６'], 1)
    RemoveItem(ItemTable['数据水晶７'], 1)
    RemoveItem(ItemTable['数据水晶８'], 1)
    RemoveItem(ItemTable['数据水晶９'], 1)
    RemoveItem(ItemTable['数据水晶１０'], 1)
    RemoveItem(ItemTable['数据水晶１１'], 1)
    RemoveItem(ItemTable['数据水晶１２'], 1)
    RemoveItem(ItemTable['数据水晶１３'], 1)
    RemoveItem(ItemTable['数据水晶１４'], 1)
    RemoveItem(ItemTable['数据水晶１５'], 1)
    OP_A3(0x1E00)
    OP_A3(0x1E01)
    OP_A3(0x1E02)
    OP_A3(0x1E03)
    OP_A3(0x1E04)
    OP_A3(0x1E05)
    OP_A3(0x1E06)
    OP_A3(0x1E31)
    OP_A3(0x1E07)
    OP_A3(0x1E08)
    OP_A3(0x1E09)
    OP_A3(0x1E0A)
    OP_A3(0x1E0B)
    OP_A3(0x1E0C)
    OP_A3(0x1E0D)
    OP_A3(0x1E0E)
    OP_A3(0x1E0F)
    OP_A3(0x1E10)
    OP_A3(0x1E1A)
    OP_A3(0x1E11)
    OP_A3(0x1E12)
    OP_A3(0x1E13)
    OP_A3(0x1E14)
    OP_A3(0x1E15)
    OP_A3(0x1E16)
    OP_A3(0x1E17)
    OP_A3(0x1E18)
    OP_A3(0x1E19)
    OP_A3(0x1E1B)
    OP_A3(0x1E1C)
    OP_A3(0x1E21)
    OP_A3(0x1E22)
    OP_A3(0x1E1D)
    OP_A3(0x1E1E)
    OP_A3(0x1E1F)
    OP_A3(0x1E20)
    OP_A3(0x1E23)
    OP_A3(0x1E32)
    OP_A3(0x1E33)
    OP_A3(0x1E34)
    OP_A3(0x1E24)

    Return()

# id: 0x0019 offset: 0x3C1C
@scena.Code('func_19_3C1C')
def func_19_3C1C():
    OP_A2(0x1E00)
    OP_A2(0x1E01)
    OP_A2(0x1E02)
    OP_A2(0x1E03)
    OP_A2(0x1E04)
    OP_A2(0x1E05)
    OP_A2(0x1E06)
    OP_A2(0x1E31)
    OP_A2(0x1E07)
    OP_A2(0x1E08)
    OP_A2(0x1E09)
    AddItem(ItemTable['数据水晶０'], 1)
    AddItem(ItemTable['数据水晶１'], 1)
    AddItem(ItemTable['数据水晶２'], 1)
    AddItem(ItemTable['数据水晶３'], 1)
    OP_A2(0x1E0A)
    OP_A2(0x1E0B)
    OP_A2(0x1E0C)
    OP_A2(0x1E0D)
    OP_A2(0x1E0E)
    OP_A2(0x1E0F)
    OP_A2(0x1E10)
    OP_A2(0x1E1A)
    AddItem(ItemTable['数据水晶４'], 1)
    AddItem(ItemTable['数据水晶５'], 1)
    AddItem(ItemTable['数据水晶６'], 1)
    AddItem(ItemTable['数据水晶７'], 1)
    OP_A2(0x1E11)
    OP_A2(0x1E12)
    OP_A2(0x1E13)
    OP_A2(0x1E14)
    OP_A2(0x1E15)
    AddItem(ItemTable['数据水晶８'], 1)
    OP_A2(0x1E1B)
    OP_A2(0x1E16)
    OP_A2(0x1E17)
    AddItem(ItemTable['数据水晶９'], 1)
    OP_A2(0x1E1C)
    OP_A2(0x1E18)
    OP_A2(0x1E19)
    AddItem(ItemTable['数据水晶１０'], 1)
    OP_A2(0x1E21)
    AddItem(ItemTable['数据水晶１１'], 1)
    OP_A2(0x1E22)
    OP_A2(0x1E1D)
    OP_A2(0x1E1E)
    OP_A2(0x1E1F)
    OP_A2(0x1E20)
    OP_A2(0x1E23)
    OP_A2(0x1E32)
    OP_A2(0x1E33)
    OP_A2(0x1E34)
    AddItem(ItemTable['数据水晶１２'], 1)
    AddItem(ItemTable['数据水晶１３'], 1)
    AddItem(ItemTable['数据水晶１４'], 1)
    AddItem(ItemTable['数据水晶１５'], 1)
    OP_A2(0x1E24)

    Return()

# id: 0x001A offset: 0x3CE8
@scena.Code('func_1A_3CE8')
def func_1A_3CE8():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_402E',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '0·序\n'),
            TXT(0x01, '①·约修亚的回归\n'),
            TXT(0x02, '②·翡翠之塔\n'),
            TXT(0x03, '③·红莲之塔\n'),
            TXT(0x04, '④·绀碧之塔\n'),
            TXT(0x05, '⑤·琥珀之塔\n'),
            TXT(0x06, '⑥·尾声\n'),
            TXT(0x07, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    AddItem(ItemTable['利贝尔王国地图'], 1)
    Call(4, 0x0004)
    Call(4, 0x0007)
    Call(4, 0x000A)
    Call(4, 0x000D)
    Call(4, 0x0010)
    Call(4, 0x0013)
    Call(4, 0x0016)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3DAF'),
        (0x00000001, 'loc_3DBE'),
        (0x00000002, 'loc_3DCD'),
        (0x00000003, 'loc_3DE2'),
        (0x00000004, 'loc_3E26'),
        (0x00000005, 'loc_3E96'),
        (0x00000006, 'loc_3F44'),
        (-1, 'loc_401E'),
    )

    def _loc_3DAF(): pass

    label('loc_3DAF')

    OP_A2(0x10F1)
    NewScene('ED6_DT21/C0705._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_402B')

    def _loc_3DBE(): pass

    label('loc_3DBE')

    OP_A2(0x10F0)
    NewScene('ED6_DT21/T4201._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_402B')

    def _loc_3DCD(): pass

    label('loc_3DCD')

    OP_A2(0x1E00)
    OP_A2(0x10FF)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_402B')

    def _loc_3DE2(): pass

    label('loc_3DE2')

    OP_A2(0x1E00)
    OP_A2(0x1E01)
    OP_A2(0x1E02)
    OP_A2(0x1E03)
    OP_A2(0x1E04)
    OP_A2(0x1E05)
    OP_A2(0x1E06)
    AddItem(ItemTable['数据水晶０'], 1)
    AddItem(ItemTable['数据水晶１'], 1)
    AddItem(ItemTable['数据水晶２'], 1)
    AddItem(ItemTable['数据水晶３'], 1)
    OP_A2(0x1E31)
    OP_A2(0x1E07)
    OP_A2(0x1E08)
    OP_A2(0x1E09)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/R3100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_402B')

    def _loc_3E26(): pass

    label('loc_3E26')

    OP_A2(0x1E00)
    OP_A2(0x1E01)
    OP_A2(0x1E02)
    OP_A2(0x1E03)
    OP_A2(0x1E04)
    OP_A2(0x1E05)
    OP_A2(0x1E06)
    AddItem(ItemTable['数据水晶０'], 1)
    AddItem(ItemTable['数据水晶１'], 1)
    AddItem(ItemTable['数据水晶２'], 1)
    AddItem(ItemTable['数据水晶３'], 1)
    OP_A2(0x1E31)
    OP_A2(0x1E07)
    OP_A2(0x1E08)
    OP_A2(0x1E09)
    OP_A2(0x1E0A)
    OP_A2(0x1E0B)
    OP_A2(0x1E0C)
    OP_A2(0x1E0D)
    AddItem(ItemTable['数据水晶４'], 1)
    AddItem(ItemTable['数据水晶５'], 1)
    AddItem(ItemTable['数据水晶６'], 1)
    AddItem(ItemTable['数据水晶７'], 1)
    OP_A2(0x1E0E)
    OP_A2(0x1E0F)
    OP_A2(0x1E10)
    OP_A2(0x1E1A)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/R2200._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_402B')

    def _loc_3E96(): pass

    label('loc_3E96')

    OP_A2(0x1E00)
    OP_A2(0x1E01)
    OP_A2(0x1E02)
    OP_A2(0x1E03)
    OP_A2(0x1E04)
    OP_A2(0x1E05)
    OP_A2(0x1E06)
    AddItem(ItemTable['数据水晶０'], 1)
    AddItem(ItemTable['数据水晶１'], 1)
    AddItem(ItemTable['数据水晶２'], 1)
    AddItem(ItemTable['数据水晶３'], 1)
    OP_A2(0x1E31)
    OP_A2(0x1E07)
    OP_A2(0x1E08)
    OP_A2(0x1E09)
    OP_A2(0x1E0A)
    OP_A2(0x1E0B)
    OP_A2(0x1E0C)
    OP_A2(0x1E0D)
    AddItem(ItemTable['数据水晶４'], 1)
    AddItem(ItemTable['数据水晶５'], 1)
    AddItem(ItemTable['数据水晶６'], 1)
    AddItem(ItemTable['数据水晶７'], 1)
    OP_A2(0x1E0E)
    OP_A2(0x1E0F)
    OP_A2(0x1E10)
    OP_A2(0x1E1A)
    OP_A2(0x1E11)
    OP_A2(0x1E12)
    OP_A2(0x1E13)
    OP_A2(0x1E14)
    OP_A2(0x1E15)
    AddItem(ItemTable['数据水晶８'], 1)
    OP_A2(0x1E1B)
    OP_A2(0x1E16)
    OP_A2(0x1E17)
    AddItem(ItemTable['数据水晶９'], 1)
    OP_A2(0x1E1C)
    OP_A2(0x1E18)
    OP_A2(0x1E19)
    AddItem(ItemTable['数据水晶１０'], 1)
    OP_A2(0x1E21)
    AddItem(ItemTable['数据水晶１１'], 1)
    OP_A2(0x1E22)
    OP_A2(0x10FF)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_402B')

    def _loc_3F44(): pass

    label('loc_3F44')

    OP_A2(0x1E00)
    OP_A2(0x1E01)
    OP_A2(0x1E02)
    OP_A2(0x1E03)
    OP_A2(0x1E04)
    OP_A2(0x1E05)
    OP_A2(0x1E06)
    AddItem(ItemTable['数据水晶０'], 1)
    AddItem(ItemTable['数据水晶１'], 1)
    AddItem(ItemTable['数据水晶２'], 1)
    AddItem(ItemTable['数据水晶３'], 1)
    OP_A2(0x1E31)
    OP_A2(0x1E07)
    OP_A2(0x1E08)
    OP_A2(0x1E09)
    OP_A2(0x1E0A)
    OP_A2(0x1E0B)
    OP_A2(0x1E0C)
    OP_A2(0x1E0D)
    AddItem(ItemTable['数据水晶４'], 1)
    AddItem(ItemTable['数据水晶５'], 1)
    AddItem(ItemTable['数据水晶６'], 1)
    AddItem(ItemTable['数据水晶７'], 1)
    OP_A2(0x1E0E)
    OP_A2(0x1E0F)
    OP_A2(0x1E10)
    OP_A2(0x1E1A)
    OP_A2(0x1E11)
    OP_A2(0x1E12)
    OP_A2(0x1E13)
    OP_A2(0x1E14)
    OP_A2(0x1E15)
    AddItem(ItemTable['数据水晶８'], 1)
    OP_A2(0x1E1B)
    OP_A2(0x1E16)
    OP_A2(0x1E17)
    AddItem(ItemTable['数据水晶９'], 1)
    OP_A2(0x1E1C)
    OP_A2(0x1E18)
    OP_A2(0x1E19)
    AddItem(ItemTable['数据水晶１０'], 1)
    OP_A2(0x1E21)
    AddItem(ItemTable['数据水晶１１'], 1)
    OP_A2(0x1E22)
    OP_A2(0x1E1D)
    OP_A2(0x1E1E)
    OP_A2(0x1E1F)
    OP_A2(0x1E20)
    AddItem(ItemTable['数据水晶１１'], 1)
    AddItem(ItemTable['数据水晶１３'], 1)
    AddItem(ItemTable['数据水晶１４'], 1)
    AddItem(ItemTable['数据水晶１５'], 1)
    OP_A2(0x1E23)
    OP_A2(0x1E32)
    OP_A2(0x1E33)
    OP_A2(0x1E34)
    OP_A2(0x1E24)
    OP_A2(0x10F8)
    NewScene('ED6_DT21/E0811._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_402B')

    def _loc_401E(): pass

    label('loc_401E')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_402B')

    def _loc_402B(): pass

    label('loc_402B')

    Jump('func_1A_3CE8')

    def _loc_402E(): pass

    label('loc_402E')

    OP_5F(0x0002)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001B offset: 0x403E
@scena.Code('func_1B_403E')
def func_1B_403E():
    RemoveItem(ItemTable['零力场发生器'], 4)
    RemoveItem(ItemTable['水泵小屋的钥匙'], 1)
    RemoveItem(ItemTable['工房长的介绍信'], 1)
    RemoveItem(ItemTable['汽油罐'], 3)
    RemoveItem(ItemTable['内燃引擎'], 1)
    RemoveItem(ItemTable['人质名单'], 1)
    OP_A3(0x2000)
    OP_A3(0x2001)
    OP_A3(0x2002)
    OP_A3(0x2003)
    OP_A3(0x2004)
    OP_A3(0x2005)
    OP_A3(0x2006)
    OP_A3(0x2007)
    OP_A3(0x2008)
    OP_A3(0x2009)
    OP_A3(0x200A)
    OP_A3(0x200B)
    OP_A3(0x200C)
    OP_A3(0x200D)
    OP_A3(0x200E)
    OP_A3(0x200F)
    OP_A3(0x2010)
    OP_A3(0x2011)
    OP_A3(0x2012)
    OP_A3(0x2013)
    OP_A3(0x2014)
    OP_A3(0x2015)
    OP_A3(0x2016)
    OP_A3(0x2017)
    OP_A3(0x2018)
    OP_A3(0x2019)
    OP_A3(0x201A)
    OP_A3(0x201B)
    OP_A3(0x201C)
    OP_A3(0x201D)
    OP_A3(0x201E)
    OP_A3(0x201F)
    OP_A3(0x2020)
    OP_A3(0x2021)
    OP_A3(0x2022)
    OP_A3(0x2023)
    OP_A3(0x2024)
    OP_A3(0x2025)
    OP_A3(0x2026)
    OP_A3(0x2027)
    OP_A3(0x2028)
    OP_A3(0x2029)
    OP_A3(0x202A)
    OP_A3(0x202B)
    OP_A3(0x202C)
    OP_A3(0x202D)
    OP_A3(0x202E)
    OP_A3(0x202F)
    OP_A3(0x2030)
    OP_A3(0x2031)
    OP_A3(0x2032)
    OP_A3(0x2033)
    OP_A3(0x2034)
    OP_A3(0x2035)
    OP_A3(0x2036)
    OP_A3(0x2037)
    OP_A3(0x2038)
    OP_A3(0x2039)
    OP_A3(0x203A)
    OP_A3(0x203B)
    OP_A3(0x203C)
    OP_A3(0x203D)
    OP_A3(0x203E)
    OP_A3(0x203F)
    OP_A3(0x2080)
    OP_A3(0x2081)
    OP_A3(0x2082)
    OP_A3(0x2083)
    OP_A3(0x2084)
    OP_A3(0x2090)
    OP_A3(0x2091)
    OP_A3(0x20B7)
    OP_A3(0x20B8)
    OP_A3(0x20B9)

    Return()

# id: 0x001C offset: 0x413B
@scena.Code('func_1C_413B')
def func_1C_413B():
    OP_A2(0x2000)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AddItem(ItemTable['零力场发生器'], 4)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2001)
    OP_A2(0x2002)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2003)
    OP_A2(0x2091)
    OP_A2(0x2004)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2005)
    OP_A2(0x2006)
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    OP_A2(0x2007)
    OP_A2(0x2008)
    OP_A2(0x2009)
    OP_A2(0x200A)
    OP_A2(0x200B)
    OP_A2(0x200D)
    OP_A3(0x200E)
    OP_A2(0x200F)
    AddItem(ItemTable['工房长的介绍信'], 1)
    OP_A2(0x2010)
    OP_A2(0x2011)
    OP_A2(0x2012)
    OP_A2(0x2013)
    OP_A2(0x2014)
    OP_A2(0x2015)
    OP_A2(0x2016)
    OP_A2(0x2017)
    OP_A2(0x2018)
    OP_A2(0x2019)
    OP_A2(0x201A)
    OP_A2(0x201B)
    AddItem(ItemTable['人质名单'], 1)
    OP_A2(0x201C)
    OP_A2(0x201D)
    OP_A2(0x201E)
    OP_A2(0x201F)
    OP_A2(0x2020)
    OP_A2(0x2021)
    OP_A2(0x2022)
    OP_A2(0x2023)
    OP_A2(0x2024)
    OP_A2(0x2025)
    OP_A2(0x2026)
    OP_A2(0x2027)
    OP_A2(0x2028)
    OP_A2(0x2029)
    OP_A2(0x202A)
    OP_A2(0x202B)
    OP_A2(0x202C)
    OP_A2(0x202D)
    OP_A2(0x202E)
    OP_A2(0x202F)
    OP_A2(0x2038)
    OP_A2(0x2039)
    OP_A2(0x203A)
    OP_A2(0x203B)
    OP_A2(0x203C)
    OP_A2(0x203D)
    OP_A2(0x203E)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)

    Return()

# id: 0x001D offset: 0x4216
@scena.Code('func_1D_4216')
def func_1D_4216():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_48A1',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '0·序\n'),
            TXT(0x01, '①·协会间的联络\n'),
            TXT(0x02, '②·亚尔摩的水泵复活（任务）\n'),
            TXT(0x03, '③·王立学院袭击（任务）\n'),
            TXT(0x04, '④·王国各地的困难状况\n'),
            TXT(0x05, '⑤·王都袭击\n'),
            TXT(0x06, '⑥·哈肯门\n'),
            TXT(0x07, '●·婚礼事件\n'),
            TXT(0x08, '●·地方任务\n'),
            TXT(0x09, '＊·The Hard-Fighting Special Forces\n'),
            TXT(0x0A, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    AddItem(ItemTable['利贝尔王国地图'], 1)
    Call(4, 0x0004)
    Call(4, 0x0007)
    Call(4, 0x000A)
    Call(4, 0x000D)
    Call(4, 0x0010)
    Call(4, 0x0013)
    Call(4, 0x0016)
    Call(4, 0x0019)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_28(0x0065, 0x04, 0x40)
    OP_28(0x0066, 0x04, 0x40)
    OP_28(0x0067, 0x04, 0x40)
    OP_28(0x0068, 0x04, 0x40)
    OP_28(0x0069, 0x04, 0x40)
    OP_28(0x006B, 0x04, 0x40)
    OP_28(0x006C, 0x04, 0x40)
    OP_28(0x006D, 0x04, 0x40)
    OP_28(0x006E, 0x04, 0x40)
    OP_28(0x006F, 0x04, 0x40)
    OP_28(0x0070, 0x04, 0x40)
    OP_28(0x0071, 0x04, 0x40)
    OP_28(0x0074, 0x04, 0x40)
    OP_28(0x0072, 0x04, 0x40)
    OP_28(0x0073, 0x04, 0x40)
    OP_28(0x0075, 0x04, 0x40)
    OP_28(0x0076, 0x04, 0x40)
    OP_28(0x0077, 0x04, 0x40)
    OP_28(0x0078, 0x04, 0x40)
    OP_28(0x0079, 0x04, 0x40)
    OP_28(0x007A, 0x04, 0x40)
    OP_28(0x007B, 0x04, 0x40)
    OP_28(0x007C, 0x04, 0x40)
    OP_28(0x007D, 0x04, 0x40)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_43CC'),
        (0x00000001, 'loc_43DB'),
        (0x00000002, 'loc_43EA'),
        (0x00000003, 'loc_442B'),
        (0x00000004, 'loc_4497'),
        (0x00000005, 'loc_4570'),
        (0x00000006, 'loc_4649'),
        (0x00000007, 'loc_473A'),
        (0x00000008, 'loc_4760'),
        (0x00000009, 'loc_47A0'),
        (-1, 'loc_4891'),
    )

    def _loc_43CC(): pass

    label('loc_43CC')

    OP_A2(0x10FD)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_43DB(): pass

    label('loc_43DB')

    OP_A2(0x10F1)
    NewScene('ED6_DT21/T2100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_43EA(): pass

    label('loc_43EA')

    OP_A2(0x2000)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AddItem(ItemTable['零力场发生器'], 4)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2001)
    OP_A2(0x2002)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2003)
    OP_A2(0x2091)
    OP_A2(0x2004)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2005)
    OP_A2(0x2006)
    NewScene('ED6_DT21/T3221._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_442B(): pass

    label('loc_442B')

    OP_A2(0x2000)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AddItem(ItemTable['零力场发生器'], 4)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2001)
    OP_A2(0x2002)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2003)
    OP_A2(0x2091)
    OP_A2(0x2004)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2005)
    OP_A2(0x2006)
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    OP_A2(0x2007)
    OP_A2(0x2008)
    OP_A2(0x2009)
    OP_A2(0x200A)
    OP_A2(0x200B)
    OP_A2(0x200D)
    OP_A3(0x200E)
    OP_A2(0x200F)
    AddItem(ItemTable['工房长的介绍信'], 1)
    OP_A2(0x2010)
    OP_A2(0x2011)
    OP_A2(0x2012)
    NewScene('ED6_DT21/R2300._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_4497(): pass

    label('loc_4497')

    OP_A2(0x2000)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AddItem(ItemTable['零力场发生器'], 4)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2001)
    OP_A2(0x2002)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2003)
    OP_A2(0x2091)
    OP_A2(0x2004)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2005)
    OP_A2(0x2006)
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    OP_A2(0x2007)
    OP_A2(0x2008)
    OP_A2(0x2009)
    OP_A2(0x200A)
    OP_A2(0x200B)
    OP_A2(0x200D)
    OP_A3(0x200E)
    OP_A2(0x200F)
    AddItem(ItemTable['工房长的介绍信'], 1)
    OP_A2(0x2010)
    OP_A2(0x2011)
    OP_A2(0x2012)
    OP_A2(0x2013)
    OP_A2(0x2014)
    OP_A2(0x2015)
    OP_A2(0x2016)
    OP_A2(0x2017)
    OP_A2(0x2018)
    OP_A2(0x2019)
    OP_A2(0x201A)
    OP_A2(0x201B)
    AddItem(ItemTable['人质名单'], 1)
    OP_A2(0x201C)
    OP_A2(0x201D)
    OP_A2(0x201E)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['克鲁茨'], 0xF9, 0xFF)
    OP_A2(0x201F)
    OP_A2(0x2020)
    OP_A2(0x2021)
    OP_A2(0x2022)
    OP_A2(0x2023)
    OP_A2(0x2024)
    OP_A2(0x2025)
    OP_A2(0x2026)
    OP_A2(0x2027)
    OP_A2(0x2028)
    OP_A2(0x2029)
    OP_A2(0x202A)
    OP_A2(0x202B)
    OP_A2(0x202C)
    OP_A2(0x202D)
    OP_A2(0x202E)
    OP_A2(0x202F)
    NewScene('ED6_DT21/T2100._SN', 105, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_4570(): pass

    label('loc_4570')

    OP_A2(0x2000)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AddItem(ItemTable['零力场发生器'], 4)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2001)
    OP_A2(0x2002)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2003)
    OP_A2(0x2091)
    OP_A2(0x2004)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2005)
    OP_A2(0x2006)
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    OP_A2(0x2007)
    OP_A2(0x2008)
    OP_A2(0x2009)
    OP_A2(0x200A)
    OP_A2(0x200B)
    OP_A2(0x200D)
    OP_A3(0x200E)
    OP_A2(0x200F)
    AddItem(ItemTable['工房长的介绍信'], 1)
    OP_A2(0x2010)
    OP_A2(0x2011)
    OP_A2(0x2012)
    OP_A2(0x2013)
    OP_A2(0x2014)
    OP_A2(0x2015)
    OP_A2(0x2016)
    OP_A2(0x2017)
    OP_A2(0x2018)
    OP_A2(0x2019)
    OP_A2(0x201A)
    OP_A2(0x201B)
    AddItem(ItemTable['人质名单'], 1)
    OP_A2(0x201C)
    OP_A2(0x201D)
    OP_A2(0x201E)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['克鲁茨'], 0xF9, 0xFF)
    OP_A2(0x201F)
    OP_A2(0x2020)
    OP_A2(0x2021)
    OP_A2(0x2022)
    OP_A2(0x2023)
    OP_A2(0x2024)
    OP_A2(0x2025)
    OP_A2(0x2026)
    OP_A2(0x2027)
    OP_A2(0x2028)
    OP_A2(0x2029)
    OP_A2(0x202A)
    OP_A2(0x202B)
    OP_A2(0x202C)
    OP_A2(0x202D)
    OP_A2(0x202E)
    OP_A2(0x202F)
    NewScene('ED6_DT21/R4100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_4649(): pass

    label('loc_4649')

    OP_A2(0x2000)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AddItem(ItemTable['零力场发生器'], 4)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2001)
    OP_A2(0x2002)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2003)
    OP_A2(0x2091)
    OP_A2(0x2004)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2005)
    OP_A2(0x2006)
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    OP_A2(0x2007)
    OP_A2(0x2008)
    OP_A2(0x2009)
    OP_A2(0x200A)
    OP_A2(0x200B)
    OP_A2(0x200D)
    OP_A3(0x200E)
    OP_A2(0x200F)
    AddItem(ItemTable['工房长的介绍信'], 1)
    OP_A2(0x2010)
    OP_A2(0x2011)
    OP_A2(0x2012)
    OP_A2(0x2013)
    OP_A2(0x2014)
    OP_A2(0x2015)
    OP_A2(0x2016)
    OP_A2(0x2017)
    OP_A2(0x2018)
    OP_A2(0x2019)
    OP_A2(0x201A)
    OP_A2(0x201B)
    AddItem(ItemTable['人质名单'], 1)
    OP_A2(0x201C)
    OP_A2(0x201D)
    OP_A2(0x201E)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['克鲁茨'], 0xF9, 0xFF)
    OP_A2(0x201F)
    OP_A2(0x2020)
    OP_A2(0x2021)
    OP_A2(0x2022)
    OP_A2(0x2023)
    OP_A2(0x2024)
    OP_A2(0x2025)
    OP_A2(0x2026)
    OP_A2(0x2027)
    OP_A2(0x2028)
    OP_A2(0x2029)
    OP_A2(0x202A)
    OP_A2(0x202B)
    OP_A2(0x202C)
    OP_A2(0x202D)
    OP_A2(0x202E)
    OP_A2(0x202F)
    OP_A2(0x2038)
    OP_A2(0x2039)
    OP_A2(0x203A)
    OP_A2(0x203B)
    OP_A2(0x203C)
    OP_A2(0x203D)
    OP_A2(0x203E)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T1400._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_473A(): pass

    label('loc_473A')

    OP_A2(0x2000)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AddItem(ItemTable['零力场发生器'], 4)
    OP_A3(0x2091)
    OP_A2(0x2085)
    OP_A3(0x2086)
    NewScene('ED6_DT21/T0130._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_4760(): pass

    label('loc_4760')

    OP_A2(0x2000)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AddItem(ItemTable['零力场发生器'], 4)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2003)
    OP_A3(0x2087)
    OP_A3(0x2088)
    OP_A3(0x2089)
    OP_A3(0x208A)
    OP_A3(0x208B)
    OP_A3(0x208C)
    OP_A3(0x208D)
    OP_A3(0x2085)
    OP_A3(0x208E)
    NewScene('ED6_DT21/C0101._SN', 102, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_47A0(): pass

    label('loc_47A0')

    OP_A2(0x2000)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AddItem(ItemTable['零力场发生器'], 4)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2001)
    OP_A2(0x2002)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2003)
    OP_A2(0x2091)
    OP_A2(0x2004)
    RemoveItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x2005)
    OP_A2(0x2006)
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    OP_A2(0x2007)
    OP_A2(0x2008)
    OP_A2(0x2009)
    OP_A2(0x200A)
    OP_A2(0x200B)
    OP_A2(0x200D)
    OP_A3(0x200E)
    OP_A2(0x200F)
    AddItem(ItemTable['工房长的介绍信'], 1)
    OP_A2(0x2010)
    OP_A2(0x2011)
    OP_A2(0x2012)
    OP_A2(0x2013)
    OP_A2(0x2014)
    OP_A2(0x2015)
    OP_A2(0x2016)
    OP_A2(0x2017)
    OP_A2(0x2018)
    OP_A2(0x2019)
    OP_A2(0x201A)
    OP_A2(0x201B)
    AddItem(ItemTable['人质名单'], 1)
    OP_A2(0x201C)
    OP_A2(0x201D)
    OP_A2(0x201E)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['克鲁茨'], 0xF9, 0xFF)
    OP_A2(0x201F)
    OP_A2(0x2020)
    OP_A2(0x2021)
    OP_A2(0x2022)
    OP_A2(0x2023)
    OP_A2(0x2024)
    OP_A2(0x2025)
    OP_A2(0x2026)
    OP_A2(0x2027)
    OP_A2(0x2028)
    OP_A2(0x2029)
    OP_A2(0x202A)
    OP_A2(0x202B)
    OP_A2(0x202C)
    OP_A2(0x202D)
    OP_A2(0x202E)
    OP_A2(0x202F)
    OP_A2(0x2038)
    OP_A2(0x2039)
    OP_A2(0x203A)
    OP_A2(0x203B)
    OP_A2(0x203C)
    OP_A2(0x203D)
    OP_A2(0x203E)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T4101._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_4891(): pass

    label('loc_4891')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_489E')

    def _loc_489E(): pass

    label('loc_489E')

    Jump('func_1D_4216')

    def _loc_48A1(): pass

    label('loc_48A1')

    OP_5F(0x0002)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001E offset: 0x48B1
@scena.Code('func_1E_48B1')
def func_1E_48B1():
    RemoveItem(ItemTable['原福音'], 1)
    OP_A3(0x2200)
    OP_A3(0x22AF)
    OP_A3(0x2201)
    OP_A3(0x2202)
    OP_A3(0x2203)
    OP_A3(0x2204)
    OP_A3(0x2205)
    OP_A3(0x2207)
    OP_A3(0x2208)
    OP_A3(0x2209)
    OP_A3(0x220A)
    OP_A3(0x220B)
    OP_A3(0x220C)
    OP_A3(0x2206)
    OP_A3(0x220D)
    OP_A3(0x220E)
    OP_A3(0x220F)
    OP_A3(0x2218)
    OP_A3(0x2219)
    OP_A3(0x221A)
    OP_A3(0x221B)
    OP_A3(0x221C)
    OP_A3(0x221D)
    OP_A3(0x221E)
    OP_A3(0x221F)
    OP_A3(0x2220)
    OP_A3(0x2221)
    OP_A3(0x2222)
    OP_A3(0x2223)
    OP_A3(0x2224)
    OP_A3(0x22B2)
    OP_A3(0x2225)
    OP_A3(0x2226)
    OP_A3(0x2227)
    OP_A3(0x2228)
    OP_A3(0x2229)
    OP_A3(0x222A)
    OP_A3(0x222B)
    OP_A3(0x222C)
    OP_A3(0x222D)
    OP_A3(0x222E)
    OP_A3(0x222F)
    OP_A3(0x2230)
    OP_A3(0x2231)
    OP_A3(0x2232)
    OP_A3(0x2233)
    OP_A3(0x2234)
    OP_A3(0x2235)
    OP_A3(0x2236)
    OP_A3(0x2237)
    OP_A3(0x2238)
    OP_A3(0x2239)
    OP_A3(0x223A)
    OP_A3(0x223B)
    OP_A3(0x223C)
    OP_A3(0x223E)
    OP_A3(0x223D)
    OP_A3(0x2281)
    OP_A3(0x2282)
    OP_A3(0x2283)
    OP_A3(0x2284)
    OP_A3(0x2285)
    OP_A3(0x2286)
    OP_A3(0x2287)
    OP_A3(0x2288)
    OP_A3(0x2289)
    OP_A3(0x228A)
    OP_A3(0x228B)
    OP_A3(0x2276)

    Return()

# id: 0x001F offset: 0x4986
@scena.Code('func_1F_4986')
def func_1F_4986():
    OP_A2(0x2200)
    OP_A2(0x22AF)
    OP_A2(0x2201)
    OP_A2(0x2202)
    OP_A2(0x2203)
    OP_A2(0x2204)
    OP_A2(0x220D)
    OP_A3(0x2210)
    OP_A3(0x2211)
    OP_A3(0x2212)
    OP_A3(0x2213)
    OP_A3(0x2214)
    OP_A3(0x2215)
    OP_A3(0x2216)
    OP_A3(0x2217)
    OP_A2(0x2218)
    OP_A2(0x2219)
    OP_A2(0x221A)
    OP_A2(0x221B)
    AddItem(ItemTable['原福音'], 1)
    OP_A2(0x221C)
    OP_A2(0x221E)
    OP_A2(0x222F)
    OP_A2(0x221F)
    OP_A2(0x2220)
    OP_A2(0x2221)
    OP_A2(0x2222)
    OP_A2(0x2223)
    OP_A2(0x2224)
    OP_A2(0x22B2)
    AddItem(ItemTable['安全卡片'], 1)
    OP_A2(0x2225)
    OP_A2(0x2226)
    OP_A2(0x2227)
    OP_A2(0x2228)
    OP_A2(0x2229)
    OP_A2(0x222A)
    OP_A2(0x222B)
    OP_A2(0x222C)
    OP_A2(0x222D)
    OP_A2(0x222E)
    OP_A2(0x2230)
    OP_A2(0x2231)
    OP_A2(0x223C)
    OP_A2(0x2232)
    OP_A2(0x2233)
    OP_A2(0x2234)
    OP_A2(0x2235)
    OP_A2(0x2236)
    OP_A2(0x2237)
    OP_A2(0x2238)
    OP_A2(0x2239)
    OP_A2(0x223A)
    OP_A2(0x223B)
    OP_A2(0x223D)
    OP_BB(0x01, 0x00, 0x00200033)
    OP_BB(0x01, 0x01, 0x0000001C)
    OP_BD()
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x08, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    OP_A2(0x223E)

    Return()

# id: 0x0020 offset: 0x4A5A
@scena.Code('func_20_4A5A')
def func_20_4A5A():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5247',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '0·序\n'),
            TXT(0x01, '①·公园区域（卡尔玛丽）\n'),
            TXT(0x02, '②·居住区域（克雷德尔）\n'),
            TXT(0x03, '③·工业区域（法克特里亚）\n'),
            TXT(0x04, '④·中枢塔（阿克斯佩拉）\n'),
            TXT(0x05, '⑤·根源区域\n'),
            TXT(0x06, '⑥·尾声\n'),
            TXT(0x07, '＊·For checking ultimate weapons\n'),
            TXT(0x08, '＊·Loewe Combat Event\n'),
            TXT(0x09, '＊·Weissmann Combat Event\n'),
            TXT(0x0A, '＊·Angel Combat Event\n'),
            TXT(0x0B, '＊·Angel Post-Combat Event 1\n'),
            TXT(0x0C, '＊·Angel Post-Combat Event 2\n'),
            TXT(0x0D, '＊·Angel Post-Combat Event 3\n'),
            TXT(0x0E, '＊·Liberl Ark Collapses\n'),
            TXT(0x0F, '＊·Essentialy prior to ending\n'),
            TXT(0x10, 'Cancel\n'),
        ),
    )

    MenuEnd(0x0000)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    AddItem(ItemTable['利贝尔王国地图'], 1)
    Call(4, 0x0004)
    Call(4, 0x0007)
    Call(4, 0x000A)
    Call(4, 0x000D)
    Call(4, 0x0010)
    Call(4, 0x0013)
    Call(4, 0x0016)
    Call(4, 0x0019)
    Call(4, 0x001C)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4C83'),
        (0x00000001, 'loc_4C92'),
        (0x00000002, 'loc_4CAA'),
        (0x00000003, 'loc_4CEB'),
        (0x00000004, 'loc_4D40'),
        (0x00000005, 'loc_4DD3'),
        (0x00000006, 'loc_4E93'),
        (0x00000007, 'loc_4F7D'),
        (0x00000008, 'loc_5013'),
        (0x00000009, 'loc_505F'),
        (0x0000000A, 'loc_50AB'),
        (0x0000000B, 'loc_50F7'),
        (0x0000000C, 'loc_5143'),
        (0x0000000D, 'loc_518F'),
        (0x0000000E, 'loc_51DB'),
        (0x0000000F, 'loc_5209'),
        (-1, 'loc_5237'),
    )

    def _loc_4C83(): pass

    label('loc_4C83')

    OP_A2(0x10F7)
    NewScene('ED6_DT21/E0800._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4C92(): pass

    label('loc_4C92')

    OP_A2(0x2200)
    OP_A2(0x22AF)
    OP_A2(0x10FF)
    OP_A2(0x10F4)
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4CAA(): pass

    label('loc_4CAA')

    OP_A2(0x2200)
    OP_A2(0x22AF)
    OP_A2(0x2201)
    OP_A2(0x2202)
    OP_A2(0x2203)
    OP_A2(0x2204)
    OP_A2(0x220D)
    OP_A3(0x2210)
    OP_A3(0x2211)
    OP_A3(0x2212)
    OP_A3(0x2213)
    OP_A3(0x2214)
    OP_A3(0x2215)
    OP_A3(0x2216)
    OP_A3(0x2217)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    NewScene('ED6_DT21/C5800._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4CEB(): pass

    label('loc_4CEB')

    OP_A2(0x2200)
    OP_A2(0x22AF)
    OP_A2(0x2201)
    OP_A2(0x2202)
    OP_A2(0x2203)
    OP_A2(0x2204)
    OP_A2(0x220D)
    OP_A3(0x2210)
    OP_A3(0x2211)
    OP_A3(0x2212)
    OP_A3(0x2213)
    OP_A3(0x2214)
    OP_A3(0x2215)
    OP_A3(0x2216)
    OP_A3(0x2217)
    OP_A2(0x2218)
    OP_A2(0x2219)
    OP_A2(0x221A)
    OP_A2(0x221B)
    AddItem(ItemTable['原福音'], 1)
    OP_A2(0x221C)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    NewScene('ED6_DT21/C5700._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4D40(): pass

    label('loc_4D40')

    OP_A2(0x2200)
    OP_A2(0x22AF)
    OP_A2(0x2201)
    OP_A2(0x2202)
    OP_A2(0x2203)
    OP_A2(0x2204)
    OP_A2(0x220D)
    OP_A3(0x2210)
    OP_A3(0x2211)
    OP_A3(0x2212)
    OP_A3(0x2213)
    OP_A3(0x2214)
    OP_A3(0x2215)
    OP_A3(0x2216)
    OP_A3(0x2217)
    OP_A2(0x2218)
    OP_A2(0x2219)
    OP_A2(0x221A)
    OP_A2(0x221B)
    AddItem(ItemTable['原福音'], 1)
    OP_A2(0x221C)
    OP_A2(0x221E)
    OP_A2(0x222F)
    OP_A2(0x221F)
    OP_A2(0x2220)
    OP_A2(0x2221)
    OP_A2(0x2222)
    OP_A2(0x2223)
    OP_A2(0x2224)
    OP_A2(0x22B2)
    AddItem(ItemTable['安全卡片'], 1)
    OP_A2(0x2225)
    OP_A2(0x2226)
    OP_A2(0x2227)
    OP_A2(0x2228)
    OP_A2(0x2229)
    OP_A2(0x222A)
    OP_A2(0x222B)
    OP_A2(0x222C)
    OP_A2(0x222D)
    OP_A2(0x222E)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    NewScene('ED6_DT21/C5100._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4DD3(): pass

    label('loc_4DD3')

    OP_A2(0x2200)
    OP_A2(0x22AF)
    OP_A2(0x2201)
    OP_A2(0x2202)
    OP_A2(0x2203)
    OP_A2(0x2204)
    OP_A2(0x220D)
    OP_A3(0x2210)
    OP_A3(0x2211)
    OP_A3(0x2212)
    OP_A3(0x2213)
    OP_A3(0x2214)
    OP_A3(0x2215)
    OP_A3(0x2216)
    OP_A3(0x2217)
    OP_A2(0x2218)
    OP_A2(0x2219)
    OP_A2(0x221A)
    OP_A2(0x221B)
    AddItem(ItemTable['原福音'], 1)
    OP_A2(0x221C)
    OP_A2(0x221E)
    OP_A2(0x222F)
    OP_A2(0x221F)
    OP_A2(0x2220)
    OP_A2(0x2221)
    OP_A2(0x2222)
    OP_A2(0x2223)
    OP_A2(0x2224)
    OP_A2(0x22B2)
    AddItem(ItemTable['安全卡片'], 1)
    OP_A2(0x2225)
    OP_A2(0x2226)
    OP_A2(0x2227)
    OP_A2(0x2228)
    OP_A2(0x2229)
    OP_A2(0x222A)
    OP_A2(0x222B)
    OP_A2(0x222C)
    OP_A2(0x222D)
    OP_A2(0x222E)
    OP_A2(0x2230)
    OP_A2(0x2231)
    OP_A2(0x223C)
    OP_A2(0x2232)
    OP_A2(0x2233)
    OP_A2(0x2234)
    OP_A2(0x2235)
    OP_A2(0x2236)
    OP_A2(0x2237)
    OP_A2(0x2238)
    OP_A2(0x2239)
    OP_A2(0x223A)
    OP_A2(0x223B)
    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5315._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4E93(): pass

    label('loc_4E93')

    OP_A2(0x2200)
    OP_A2(0x22AF)
    OP_A2(0x2201)
    OP_A2(0x2202)
    OP_A2(0x2203)
    OP_A2(0x2204)
    OP_A2(0x220D)
    OP_A3(0x2210)
    OP_A3(0x2211)
    OP_A3(0x2212)
    OP_A3(0x2213)
    OP_A3(0x2214)
    OP_A3(0x2215)
    OP_A3(0x2216)
    OP_A3(0x2217)
    OP_A2(0x2218)
    OP_A2(0x2219)
    OP_A2(0x221A)
    OP_A2(0x221B)
    AddItem(ItemTable['原福音'], 1)
    OP_A2(0x221C)
    OP_A2(0x221E)
    OP_A2(0x222F)
    OP_A2(0x221F)
    OP_A2(0x2220)
    OP_A2(0x2221)
    OP_A2(0x2222)
    OP_A2(0x2223)
    OP_A2(0x2224)
    OP_A2(0x22B2)
    AddItem(ItemTable['安全卡片'], 1)
    OP_A2(0x2225)
    OP_A2(0x2226)
    OP_A2(0x2227)
    OP_A2(0x2228)
    OP_A2(0x2229)
    OP_A2(0x222A)
    OP_A2(0x222B)
    OP_A2(0x222C)
    OP_A2(0x222D)
    OP_A2(0x222E)
    OP_A2(0x2230)
    OP_A2(0x2231)
    OP_A2(0x223C)
    OP_A2(0x2232)
    OP_A2(0x2233)
    OP_A2(0x2234)
    OP_A2(0x2235)
    OP_A2(0x2236)
    OP_A2(0x2237)
    OP_A2(0x2238)
    OP_A2(0x2239)
    OP_A2(0x223A)
    OP_A2(0x223B)
    OP_A2(0x223D)
    OP_BB(0x01, 0x00, 0x00200033)
    OP_BB(0x01, 0x01, 0x0000001C)
    OP_BD()
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x08, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    OP_A2(0x223E)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T5200._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4F7D(): pass

    label('loc_4F7D')

    OP_A2(0x2200)
    OP_A2(0x22AF)
    OP_A2(0x2201)
    OP_A2(0x2202)
    OP_A2(0x2203)
    OP_A2(0x2204)
    OP_A2(0x220D)
    OP_A3(0x2210)
    OP_A3(0x2211)
    OP_A3(0x2212)
    OP_A3(0x2213)
    OP_A3(0x2214)
    OP_A3(0x2215)
    OP_A3(0x2216)
    OP_A3(0x2217)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    RemoveItem(ItemTable['数据水晶０'], 1)
    RemoveItem(ItemTable['数据水晶１'], 1)
    RemoveItem(ItemTable['数据水晶２'], 1)
    RemoveItem(ItemTable['数据水晶３'], 1)
    RemoveItem(ItemTable['数据水晶４'], 1)
    RemoveItem(ItemTable['数据水晶５'], 1)
    RemoveItem(ItemTable['数据水晶６'], 1)
    RemoveItem(ItemTable['数据水晶７'], 1)
    RemoveItem(ItemTable['数据水晶８'], 1)
    RemoveItem(ItemTable['数据水晶９'], 1)
    RemoveItem(ItemTable['数据水晶１０'], 1)
    RemoveItem(ItemTable['数据水晶１１'], 1)
    RemoveItem(ItemTable['数据水晶１２'], 1)
    RemoveItem(ItemTable['数据水晶１３'], 1)
    RemoveItem(ItemTable['数据水晶１４'], 1)
    RemoveItem(ItemTable['数据水晶１５'], 1)
    AddItem(ItemTable['塞姆里亚石'], 1)
    NewScene('ED6_DT21/C5800._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_5013(): pass

    label('loc_5013')

    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    OP_A2(0x1200)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0x000E,
            0x000F,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5313._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_505F(): pass

    label('loc_505F')

    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    OP_A2(0x1200)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0x000E,
            0x000F,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FormationDelMember(0x01, 0xFF)
    NewScene('ED6_DT21/C5317._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_50AB(): pass

    label('loc_50AB')

    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    OP_A2(0x1200)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0x000E,
            0x000F,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5318._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_50F7(): pass

    label('loc_50F7')

    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    OP_A2(0x1200)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0x000E,
            0x000F,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5317._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_5143(): pass

    label('loc_5143')

    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    OP_A2(0x1200)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0x000E,
            0x000F,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5300._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_518F(): pass

    label('loc_518F')

    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    OP_A2(0x1200)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0x000E,
            0x000F,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5208._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_51DB(): pass

    label('loc_51DB')

    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_20(0x00000000)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    NewScene('ED6_DT21/C5207._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_5209(): pass

    label('loc_5209')

    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_20(0x00000000)
    OP_A2(0x223E)
    OP_A2(0x10FF)
    OP_A2(0x10FC)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_5237(): pass

    label('loc_5237')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5244')

    def _loc_5244(): pass

    label('loc_5244')

    Jump('func_20_4A5A')

    def _loc_5247(): pass

    label('loc_5247')

    OP_5F(0x0002)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
