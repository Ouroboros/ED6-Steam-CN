import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0001_4_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0001_4 ._SN')

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

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
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
@scena.Code('func_01_234')
def func_01_234():
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

    SetScenaFlags(ScenaFlag(0x0200, 2, 0x1002))
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x0200, 3, 0x1003))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationDelMember(0x08, 0xFF)
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    OP_BB(0x00, 0x00, 0x00200042)
    OP_BB(0x00, 0x01, 0x0000001E)
    OP_BD()
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0200, 4, 0x1004))
    SetScenaFlags(ScenaFlag(0x0200, 5, 0x1005))
    SetScenaFlags(ScenaFlag(0x0200, 6, 0x1006))
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x0200, 7, 0x1007))
    SetScenaFlags(ScenaFlag(0x0201, 0, 0x1008))
    SetScenaFlags(ScenaFlag(0x0201, 1, 0x1009))
    SetScenaFlags(ScenaFlag(0x0201, 2, 0x100A))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0201, 3, 0x100B))
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0201, 4, 0x100C))
    SetScenaFlags(ScenaFlag(0x0201, 5, 0x100D))
    SetScenaFlags(ScenaFlag(0x0201, 6, 0x100E))
    SetScenaFlags(ScenaFlag(0x0201, 7, 0x100F))
    SetScenaFlags(ScenaFlag(0x0202, 0, 0x1010))
    SetScenaFlags(ScenaFlag(0x0202, 1, 0x1011))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0202, 2, 0x1012))
    SetScenaFlags(ScenaFlag(0x0203, 3, 0x101B))
    SetScenaFlags(ScenaFlag(0x0203, 4, 0x101C))
    SetScenaFlags(ScenaFlag(0x0203, 5, 0x101D))
    SetScenaFlags(ScenaFlag(0x0203, 6, 0x101E))
    SetScenaFlags(ScenaFlag(0x0203, 7, 0x101F))
    SetScenaFlags(ScenaFlag(0x0204, 0, 0x1020))
    SetScenaFlags(ScenaFlag(0x0204, 1, 0x1021))
    SetScenaFlags(ScenaFlag(0x0204, 2, 0x1022))
    SetScenaFlags(ScenaFlag(0x0204, 3, 0x1023))
    SetScenaFlags(ScenaFlag(0x0204, 4, 0x1024))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0240, 2, 0x1202))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0240, 3, 0x1203))
    SetScenaFlags(ScenaFlag(0x0240, 4, 0x1204))
    SetScenaFlags(ScenaFlag(0x0240, 5, 0x1205))
    SetScenaFlags(ScenaFlag(0x0240, 7, 0x1207))
    SetScenaFlags(ScenaFlag(0x0241, 0, 0x1208))
    SetScenaFlags(ScenaFlag(0x0241, 1, 0x1209))
    SetScenaFlags(ScenaFlag(0x0241, 2, 0x120A))
    SetScenaFlags(ScenaFlag(0x0241, 3, 0x120B))
    SetScenaFlags(ScenaFlag(0x0241, 4, 0x120C))
    SetScenaFlags(ScenaFlag(0x0241, 5, 0x120D))
    SetScenaFlags(ScenaFlag(0x0240, 6, 0x1206))
    SetScenaFlags(ScenaFlag(0x0241, 6, 0x120E))
    SetScenaFlags(ScenaFlag(0x0241, 7, 0x120F))
    SetScenaFlags(ScenaFlag(0x0242, 0, 0x1210))
    SetScenaFlags(ScenaFlag(0x0242, 1, 0x1211))
    SetScenaFlags(ScenaFlag(0x0242, 2, 0x1212))
    SetScenaFlags(ScenaFlag(0x0242, 3, 0x1213))
    SetScenaFlags(ScenaFlag(0x0242, 4, 0x1214))
    SetScenaFlags(ScenaFlag(0x0242, 5, 0x1215))
    SetScenaFlags(ScenaFlag(0x0242, 6, 0x1216))
    SetScenaFlags(ScenaFlag(0x0242, 7, 0x1217))
    SetScenaFlags(ScenaFlag(0x0243, 0, 0x1218))
    SetScenaFlags(ScenaFlag(0x0243, 1, 0x1219))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0243, 2, 0x121A))
    FormationDelMember(0x08, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 3, 0x121B))
    SetScenaFlags(ScenaFlag(0x0243, 4, 0x121C))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationAddMember(ChrTable['朵洛希'], 0xFF, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 5, 0x121D))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0243, 6, 0x121E))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x26, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 7, 0x121F))
    SetScenaFlags(ScenaFlag(0x0244, 0, 0x1220))
    SetScenaFlags(ScenaFlag(0x0244, 1, 0x1221))
    FormationAddMember(ChrTable['朵洛希'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0244, 2, 0x1222))
    SetScenaFlags(ScenaFlag(0x0244, 3, 0x1223))
    SetScenaFlags(ScenaFlag(0x0244, 4, 0x1224))
    SetScenaFlags(ScenaFlag(0x0244, 5, 0x1225))
    SetScenaFlags(ScenaFlag(0x0244, 6, 0x1226))
    SetScenaFlags(ScenaFlag(0x0244, 7, 0x1227))
    SetScenaFlags(ScenaFlag(0x0245, 0, 0x1228))
    SetScenaFlags(ScenaFlag(0x0245, 1, 0x1229))
    FormationDelMember(0x26, 0xFF)
    SetScenaFlags(ScenaFlag(0x0245, 2, 0x122A))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0280, 0, 0x1400))
    SetScenaFlags(ScenaFlag(0x0280, 1, 0x1401))
    SetScenaFlags(ScenaFlag(0x0280, 2, 0x1402))
    SetScenaFlags(ScenaFlag(0x0280, 3, 0x1403))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    SetScenaFlags(ScenaFlag(0x0280, 4, 0x1404))
    SetScenaFlags(ScenaFlag(0x0280, 5, 0x1405))
    SetScenaFlags(ScenaFlag(0x0280, 6, 0x1406))
    SetScenaFlags(ScenaFlag(0x0280, 7, 0x1407))
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0281, 0, 0x1408))
    SetScenaFlags(ScenaFlag(0x0281, 1, 0x1409))
    SetScenaFlags(ScenaFlag(0x0281, 2, 0x140A))
    SetScenaFlags(ScenaFlag(0x0281, 3, 0x140B))
    SetScenaFlags(ScenaFlag(0x0281, 4, 0x140C))
    SetScenaFlags(ScenaFlag(0x0282, 0, 0x1410))
    SetScenaFlags(ScenaFlag(0x0281, 5, 0x140D))
    SetScenaFlags(ScenaFlag(0x0282, 1, 0x1411))
    SetScenaFlags(ScenaFlag(0x0281, 6, 0x140E))
    SetScenaFlags(ScenaFlag(0x0281, 7, 0x140F))
    SetScenaFlags(ScenaFlag(0x0282, 2, 0x1412))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0282, 3, 0x1413))
    SetScenaFlags(ScenaFlag(0x0282, 4, 0x1414))
    SetScenaFlags(ScenaFlag(0x0282, 5, 0x1415))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0282, 6, 0x1416))
    SetScenaFlags(ScenaFlag(0x0282, 7, 0x1417))
    SetScenaFlags(ScenaFlag(0x0283, 0, 0x1418))
    SetScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    SetScenaFlags(ScenaFlag(0x0283, 2, 0x141A))
    SetScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    SetScenaFlags(ScenaFlag(0x0283, 4, 0x141C))
    SetScenaFlags(ScenaFlag(0x0283, 5, 0x141D))
    SetScenaFlags(ScenaFlag(0x0283, 6, 0x141E))
    SetScenaFlags(ScenaFlag(0x0283, 7, 0x141F))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0284, 0, 0x1420))
    SetScenaFlags(ScenaFlag(0x0284, 1, 0x1421))
    SetScenaFlags(ScenaFlag(0x0284, 2, 0x1422))
    SetScenaFlags(ScenaFlag(0x0284, 3, 0x1423))
    SetScenaFlags(ScenaFlag(0x0284, 4, 0x1424))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    SetScenaFlags(ScenaFlag(0x02C0, 1, 0x1601))
    SetScenaFlags(ScenaFlag(0x02C0, 2, 0x1602))
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C0, 3, 0x1603))
    SetScenaFlags(ScenaFlag(0x02C0, 4, 0x1604))
    SetScenaFlags(ScenaFlag(0x02C0, 7, 0x1607))
    SetScenaFlags(ScenaFlag(0x02C0, 5, 0x1605))
    SetScenaFlags(ScenaFlag(0x02C0, 6, 0x1606))
    SetScenaFlags(ScenaFlag(0x02C1, 0, 0x1608))
    SetScenaFlags(ScenaFlag(0x02C1, 1, 0x1609))
    SetScenaFlags(ScenaFlag(0x02C1, 2, 0x160A))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x02C1, 3, 0x160B))
    SetScenaFlags(ScenaFlag(0x02C1, 4, 0x160C))
    SetScenaFlags(ScenaFlag(0x02C1, 5, 0x160D))
    SetScenaFlags(ScenaFlag(0x02C1, 6, 0x160E))
    SetScenaFlags(ScenaFlag(0x02C1, 7, 0x160F))
    SetScenaFlags(ScenaFlag(0x02C2, 0, 0x1610))
    SetScenaFlags(ScenaFlag(0x02C2, 1, 0x1611))
    SetScenaFlags(ScenaFlag(0x02C2, 2, 0x1612))
    SetScenaFlags(ScenaFlag(0x02C2, 4, 0x1614))
    SetScenaFlags(ScenaFlag(0x02C2, 5, 0x1615))
    SetScenaFlags(ScenaFlag(0x02C2, 6, 0x1616))
    SetScenaFlags(ScenaFlag(0x02C2, 7, 0x1617))
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C2, 3, 0x1613))
    SetScenaFlags(ScenaFlag(0x02C3, 0, 0x1618))
    SetScenaFlags(ScenaFlag(0x02C3, 1, 0x1619))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
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
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x02C3, 2, 0x161A))
    SetScenaFlags(ScenaFlag(0x02C3, 3, 0x161B))
    SetScenaFlags(ScenaFlag(0x02C3, 4, 0x161C))
    SetScenaFlags(ScenaFlag(0x02C3, 5, 0x161D))
    SetScenaFlags(ScenaFlag(0x02C3, 7, 0x161F))
    SetScenaFlags(ScenaFlag(0x02C4, 0, 0x1620))
    FormationAddMember(ChrTable['穆拉2'], 0xFF, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C4, 1, 0x1621))
    FormationDelMember(0x2F, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C4, 2, 0x1622))
    SetScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    SetScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    SetScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    SetScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    SetScenaFlags(ScenaFlag(0x02C5, 0, 0x1628))
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x04, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationDelMember(0x00, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x02C5, 2, 0x162A))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C5, 3, 0x162B))
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C5, 4, 0x162C))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    FormationDelMember(0x2E, 0xFF)
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x02C5, 5, 0x162D))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x02C5, 6, 0x162E))
    SetScenaFlags(ScenaFlag(0x02C6, 0, 0x1630))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x02C6, 1, 0x1631))
    SetScenaFlags(ScenaFlag(0x02C6, 2, 0x1632))
    SetScenaFlags(ScenaFlag(0x02C6, 3, 0x1633))
    SetScenaFlags(ScenaFlag(0x02C6, 4, 0x1634))
    SetScenaFlags(ScenaFlag(0x02C6, 5, 0x1635))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C6, 6, 0x1636))
    SetScenaFlags(ScenaFlag(0x02C6, 7, 0x1637))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x02C7, 0, 0x1638))
    SetScenaFlags(ScenaFlag(0x02C7, 1, 0x1639))
    FormationAddMember(ChrTable['管家菲利普'], 0xFF, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationDelMember(0x42, 0xFF)
    FormationDelMember(0x08, 0xFF)
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x02C7, 2, 0x163A))
    SetScenaFlags(ScenaFlag(0x02C7, 3, 0x163B))
    SetScenaFlags(ScenaFlag(0x02C7, 4, 0x163C))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationAddMember(ChrTable['尤莉亚上尉'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    FormationDelMember(0x0E, 0xFF)
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    FormationDelMember(0x08, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x02C7, 5, 0x163D))
    SetScenaFlags(ScenaFlag(0x02C7, 6, 0x163E))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['乔丝特2'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['多伦'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['吉尔'], 0xFF, 0xFF)
    SetScenaFlags(ScenaFlag(0x0300, 0, 0x1800))
    SetScenaFlags(ScenaFlag(0x0300, 1, 0x1801))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x0300, 2, 0x1802))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0300, 3, 0x1803))
    SetScenaFlags(ScenaFlag(0x0300, 4, 0x1804))
    SetScenaFlags(ScenaFlag(0x0300, 5, 0x1805))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x0300, 6, 0x1806))
    SetScenaFlags(ScenaFlag(0x0300, 7, 0x1807))
    SetScenaFlags(ScenaFlag(0x0301, 0, 0x1808))
    SetScenaFlags(ScenaFlag(0x0301, 1, 0x1809))
    SetScenaFlags(ScenaFlag(0x0301, 2, 0x180A))
    SetScenaFlags(ScenaFlag(0x0301, 3, 0x180B))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0301, 4, 0x180C))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x0301, 5, 0x180D))
    SetScenaFlags(ScenaFlag(0x0301, 6, 0x180E))
    SetScenaFlags(ScenaFlag(0x0301, 7, 0x180F))
    SetScenaFlags(ScenaFlag(0x0302, 0, 0x1810))
    SetScenaFlags(ScenaFlag(0x0302, 1, 0x1811))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0302, 2, 0x1812))
    SetScenaFlags(ScenaFlag(0x0302, 3, 0x1813))
    SetScenaFlags(ScenaFlag(0x0302, 4, 0x1814))
    SetScenaFlags(ScenaFlag(0x0302, 5, 0x1815))
    SetScenaFlags(ScenaFlag(0x0302, 6, 0x1816))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    OP_BB(0x00, 0x01, 0x00000043)
    SetScenaFlags(ScenaFlag(0x0302, 7, 0x1817))
    SetScenaFlags(ScenaFlag(0x0303, 0, 0x1818))
    SetScenaFlags(ScenaFlag(0x0303, 1, 0x1819))
    SetScenaFlags(ScenaFlag(0x0303, 2, 0x181A))
    SetScenaFlags(ScenaFlag(0x0303, 3, 0x181B))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    OP_BB(0x00, 0x01, 0x00000000)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0303, 4, 0x181C))
    SetScenaFlags(ScenaFlag(0x0303, 5, 0x181D))
    SetScenaFlags(ScenaFlag(0x0303, 6, 0x181E))
    SetScenaFlags(ScenaFlag(0x0303, 7, 0x181F))
    SetScenaFlags(ScenaFlag(0x0304, 0, 0x1820))
    SetScenaFlags(ScenaFlag(0x0304, 1, 0x1821))
    SetScenaFlags(ScenaFlag(0x0304, 2, 0x1822))
    SetScenaFlags(ScenaFlag(0x0304, 3, 0x1823))
    SetScenaFlags(ScenaFlag(0x0304, 4, 0x1824))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))

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

    SetScenaFlags(ScenaFlag(0x0304, 5, 0x1825))

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

    SetScenaFlags(ScenaFlag(0x0304, 6, 0x1826))

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

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0304, 7, 0x1827))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0305, 0, 0x1828))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x0306, 3, 0x1833))
    OP_BB(0x00, 0x01, 0x00000044)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x0306, 4, 0x1834))
    SetScenaFlags(ScenaFlag(0x0306, 5, 0x1835))
    SetScenaFlags(ScenaFlag(0x0306, 6, 0x1836))
    SetScenaFlags(ScenaFlag(0x0306, 7, 0x1837))
    SetScenaFlags(ScenaFlag(0x0307, 0, 0x1838))
    AddItem(ItemTable['储物室钥匙'], 1)
    SetScenaFlags(ScenaFlag(0x0307, 1, 0x1839))
    SetScenaFlags(ScenaFlag(0x0307, 2, 0x183A))
    AddItem(ItemTable['口琴'], 1)
    SetScenaFlags(ScenaFlag(0x0307, 3, 0x183B))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0340, 0, 0x1A00))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0340, 1, 0x1A01))
    SetScenaFlags(ScenaFlag(0x0340, 2, 0x1A02))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x0340, 3, 0x1A03))
    SetScenaFlags(ScenaFlag(0x0340, 4, 0x1A04))
    SetScenaFlags(ScenaFlag(0x0340, 5, 0x1A05))
    SetScenaFlags(ScenaFlag(0x0340, 7, 0x1A07))
    SetScenaFlags(ScenaFlag(0x0341, 0, 0x1A08))
    SetScenaFlags(ScenaFlag(0x0341, 1, 0x1A09))
    SetScenaFlags(ScenaFlag(0x0341, 2, 0x1A0A))
    SetScenaFlags(ScenaFlag(0x0341, 3, 0x1A0B))
    SetScenaFlags(ScenaFlag(0x0341, 4, 0x1A0C))
    SetScenaFlags(ScenaFlag(0x0340, 6, 0x1A06))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0341, 5, 0x1A0D))
    SetScenaFlags(ScenaFlag(0x0341, 6, 0x1A0E))
    SetScenaFlags(ScenaFlag(0x0341, 7, 0x1A0F))
    SetScenaFlags(ScenaFlag(0x0342, 0, 0x1A10))
    SetScenaFlags(ScenaFlag(0x0342, 1, 0x1A11))
    SetScenaFlags(ScenaFlag(0x0342, 2, 0x1A12))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x0342, 3, 0x1A13))
    SetScenaFlags(ScenaFlag(0x0342, 4, 0x1A14))
    SetScenaFlags(ScenaFlag(0x0342, 5, 0x1A15))
    SetScenaFlags(ScenaFlag(0x0342, 6, 0x1A16))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0342, 7, 0x1A17))
    SetScenaFlags(ScenaFlag(0x0343, 0, 0x1A18))
    SetScenaFlags(ScenaFlag(0x0343, 1, 0x1A19))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0343, 2, 0x1A1A))
    SetScenaFlags(ScenaFlag(0x0343, 3, 0x1A1B))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x0343, 4, 0x1A1C))
    SetScenaFlags(ScenaFlag(0x0343, 5, 0x1A1D))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0343, 6, 0x1A1E))
    SetScenaFlags(ScenaFlag(0x0343, 7, 0x1A1F))
    SetScenaFlags(ScenaFlag(0x0344, 0, 0x1A20))
    SetScenaFlags(ScenaFlag(0x0344, 1, 0x1A21))
    SetScenaFlags(ScenaFlag(0x0344, 2, 0x1A22))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    SetScenaFlags(ScenaFlag(0x0344, 3, 0x1A23))
    FormationAddMember(ChrTable['科洛丝'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF9, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFA, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    ClearScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x0344, 4, 0x1A24))
    SetScenaFlags(ScenaFlag(0x0344, 5, 0x1A25))
    SetScenaFlags(ScenaFlag(0x0344, 6, 0x1A26))
    SetScenaFlags(ScenaFlag(0x0344, 7, 0x1A27))
    SetScenaFlags(ScenaFlag(0x0345, 0, 0x1A28))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0345, 1, 0x1A29))
    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    ClearScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x0380, 0, 0x1C00))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0380, 1, 0x1C01))
    SetScenaFlags(ScenaFlag(0x0380, 2, 0x1C02))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x0380, 3, 0x1C03))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0380, 4, 0x1C04))
    SetScenaFlags(ScenaFlag(0x0380, 5, 0x1C05))
    SetScenaFlags(ScenaFlag(0x0380, 6, 0x1C06))
    SetScenaFlags(ScenaFlag(0x0383, 2, 0x1C1A))
    SetScenaFlags(ScenaFlag(0x0380, 7, 0x1C07))
    SetScenaFlags(ScenaFlag(0x0381, 0, 0x1C08))
    AddItem(ItemTable['红色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 1, 0x1C09))
    SetScenaFlags(ScenaFlag(0x0381, 2, 0x1C0A))
    SetScenaFlags(ScenaFlag(0x0381, 3, 0x1C0B))
    AddItem(ItemTable['绿色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 4, 0x1C0C))
    SetScenaFlags(ScenaFlag(0x0381, 5, 0x1C0D))
    AddItem(ItemTable['蓝色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 6, 0x1C0E))
    SetScenaFlags(ScenaFlag(0x0381, 7, 0x1C0F))
    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    ClearScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0383, 3, 0x1C1B))
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)
    ChrSetChipByIndex(0x0101, 6)
    ChrSetChipByIndex(0x012F, 7)
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x012F, 0x1000)
    MapSetFlags(0x80000000)
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x0383, 4, 0x1C1C))
    FormationDelMember(0x2E, 0xFF)
    ChrSetChipByIndex(0x0101, 65535)
    MapClearFlags(0x80000000)
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    SetScenaFlags(ScenaFlag(0x0383, 5, 0x1C1D))
    SetScenaFlags(ScenaFlag(0x0384, 6, 0x1C26))
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    OP_BB(0x01, 0x00, 0x00200033)
    OP_BB(0x01, 0x01, 0x00000001)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x0384, 7, 0x1C27))
    SetScenaFlags(ScenaFlag(0x0385, 0, 0x1C28))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    SetScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    ClearScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    SetScenaFlags(ScenaFlag(0x021F, 2, 0x10FA))
    ClearScenaFlags(ScenaFlag(0x021F, 2, 0x10FA))
    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    ClearScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    SetScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
    ClearScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
    SetScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    ClearScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    ClearScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    ClearScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    ClearScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    SetScenaFlags(ScenaFlag(0x03C0, 0, 0x1E00))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    ClearScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021F, 2, 0x10FA))
    ClearScenaFlags(ScenaFlag(0x021F, 2, 0x10FA))
    SetScenaFlags(ScenaFlag(0x03C0, 1, 0x1E01))
    SetScenaFlags(ScenaFlag(0x03C0, 2, 0x1E02))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x03C0, 3, 0x1E03))
    SetScenaFlags(ScenaFlag(0x03C0, 4, 0x1E04))
    SetScenaFlags(ScenaFlag(0x03C0, 5, 0x1E05))
    AddItem(ItemTable['数据水晶０'], 1)
    SetScenaFlags(ScenaFlag(0x03C0, 6, 0x1E06))
    AddItem(ItemTable['数据水晶１'], 1)
    AddItem(ItemTable['数据水晶２'], 1)
    AddItem(ItemTable['数据水晶３'], 1)
    SetScenaFlags(ScenaFlag(0x03C6, 1, 0x1E31))
    SetScenaFlags(ScenaFlag(0x03C0, 7, 0x1E07))
    SetScenaFlags(ScenaFlag(0x03C1, 0, 0x1E08))
    SetScenaFlags(ScenaFlag(0x03C1, 1, 0x1E09))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    RemoveItem(ItemTable['数据水晶０'], 1)
    RemoveItem(ItemTable['数据水晶１'], 1)
    RemoveItem(ItemTable['数据水晶２'], 1)
    RemoveItem(ItemTable['数据水晶３'], 1)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
    ClearScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
    SetScenaFlags(ScenaFlag(0x03C1, 2, 0x1E0A))
    SetScenaFlags(ScenaFlag(0x03C1, 3, 0x1E0B))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x03C1, 4, 0x1E0C))
    SetScenaFlags(ScenaFlag(0x03C1, 5, 0x1E0D))
    AddItem(ItemTable['数据水晶４'], 1)
    AddItem(ItemTable['数据水晶５'], 1)
    AddItem(ItemTable['数据水晶６'], 1)
    AddItem(ItemTable['数据水晶７'], 1)
    SetScenaFlags(ScenaFlag(0x03C1, 6, 0x1E0E))
    SetScenaFlags(ScenaFlag(0x03C1, 7, 0x1E0F))
    SetScenaFlags(ScenaFlag(0x03C2, 0, 0x1E10))
    SetScenaFlags(ScenaFlag(0x03C3, 2, 0x1E1A))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    SetScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    ClearScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021F, 5, 0x10FD))
    ClearScenaFlags(ScenaFlag(0x021F, 5, 0x10FD))
    SetScenaFlags(ScenaFlag(0x03C2, 1, 0x1E11))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x03C2, 2, 0x1E12))
    SetScenaFlags(ScenaFlag(0x03C2, 3, 0x1E13))
    SetScenaFlags(ScenaFlag(0x03C2, 4, 0x1E14))
    SetScenaFlags(ScenaFlag(0x03C2, 5, 0x1E15))
    AddItem(ItemTable['数据水晶８'], 1)
    SetScenaFlags(ScenaFlag(0x03C3, 3, 0x1E1B))
    SetScenaFlags(ScenaFlag(0x03C2, 6, 0x1E16))
    SetScenaFlags(ScenaFlag(0x03C2, 7, 0x1E17))
    AddItem(ItemTable['数据水晶９'], 1)
    SetScenaFlags(ScenaFlag(0x03C3, 4, 0x1E1C))
    SetScenaFlags(ScenaFlag(0x03C3, 0, 0x1E18))
    SetScenaFlags(ScenaFlag(0x03C3, 1, 0x1E19))
    AddItem(ItemTable['数据水晶１０'], 1)
    SetScenaFlags(ScenaFlag(0x03C4, 1, 0x1E21))
    AddItem(ItemTable['数据水晶１１'], 1)
    SetScenaFlags(ScenaFlag(0x03C4, 2, 0x1E22))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x03C3, 5, 0x1E1D))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x03C3, 6, 0x1E1E))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x03C3, 7, 0x1E1F))
    SetScenaFlags(ScenaFlag(0x03C4, 0, 0x1E20))
    SetScenaFlags(ScenaFlag(0x03C4, 3, 0x1E23))
    SetScenaFlags(ScenaFlag(0x03C6, 2, 0x1E32))
    SetScenaFlags(ScenaFlag(0x03C6, 3, 0x1E33))
    SetScenaFlags(ScenaFlag(0x03C6, 4, 0x1E34))
    AddItem(ItemTable['数据水晶１２'], 1)
    AddItem(ItemTable['数据水晶１３'], 1)
    AddItem(ItemTable['数据水晶１４'], 1)
    AddItem(ItemTable['数据水晶１５'], 1)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x03C4, 4, 0x1E24))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    SetScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    ClearScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x021F, 5, 0x10FD))
    ClearScenaFlags(ScenaFlag(0x021F, 5, 0x10FD))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x0400, 0, 0x2000))
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
    SetScenaFlags(ScenaFlag(0x0400, 1, 0x2001))
    SetScenaFlags(ScenaFlag(0x0400, 2, 0x2002))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 3, 0x2003))
    SetScenaFlags(ScenaFlag(0x0412, 1, 0x2091))
    SetScenaFlags(ScenaFlag(0x0400, 4, 0x2004))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 5, 0x2005))
    SetScenaFlags(ScenaFlag(0x0412, 1, 0x2091))
    SetScenaFlags(ScenaFlag(0x0400, 6, 0x2006))
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 7, 0x2007))
    SetScenaFlags(ScenaFlag(0x0401, 0, 0x2008))
    SetScenaFlags(ScenaFlag(0x0401, 1, 0x2009))
    SetScenaFlags(ScenaFlag(0x0401, 2, 0x200A))
    SetScenaFlags(ScenaFlag(0x0401, 3, 0x200B))
    SetScenaFlags(ScenaFlag(0x0401, 5, 0x200D))
    ClearScenaFlags(ScenaFlag(0x0401, 6, 0x200E))
    AddItem(ItemTable['内燃引擎'], 1)
    SetScenaFlags(ScenaFlag(0x0401, 7, 0x200F))
    AddItem(ItemTable['工房长的介绍信'], 1)
    SetScenaFlags(ScenaFlag(0x0402, 0, 0x2010))
    AddItem(ItemTable['汽油罐'], 3)
    SetScenaFlags(ScenaFlag(0x0402, 1, 0x2011))
    RemoveItem(ItemTable['汽油罐'], 3)
    RemoveItem(ItemTable['内燃引擎'], 1)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x0402, 2, 0x2012))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0402, 3, 0x2013))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x0402, 4, 0x2014))
    SetScenaFlags(ScenaFlag(0x0402, 5, 0x2015))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x0402, 6, 0x2016))
    SetScenaFlags(ScenaFlag(0x0402, 7, 0x2017))
    SetScenaFlags(ScenaFlag(0x0403, 0, 0x2018))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    SetScenaFlags(ScenaFlag(0x0403, 1, 0x2019))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    SetScenaFlags(ScenaFlag(0x0403, 2, 0x201A))
    SetScenaFlags(ScenaFlag(0x0403, 3, 0x201B))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    AddItem(ItemTable['人质名单'], 1)
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021F, 2, 0x10FA))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021F, 2, 0x10FA))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
    SetScenaFlags(ScenaFlag(0x0403, 4, 0x201C))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    SetScenaFlags(ScenaFlag(0x0403, 5, 0x201D))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021F, 5, 0x10FD))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021F, 5, 0x10FD))
    SetScenaFlags(ScenaFlag(0x0403, 6, 0x201E))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['克鲁茨'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0403, 7, 0x201F))
    SetScenaFlags(ScenaFlag(0x0404, 0, 0x2020))
    SetScenaFlags(ScenaFlag(0x0404, 1, 0x2021))
    SetScenaFlags(ScenaFlag(0x0404, 2, 0x2022))
    SetScenaFlags(ScenaFlag(0x0404, 3, 0x2023))
    SetScenaFlags(ScenaFlag(0x0404, 4, 0x2024))
    SetScenaFlags(ScenaFlag(0x0404, 5, 0x2025))
    SetScenaFlags(ScenaFlag(0x0404, 6, 0x2026))
    SetScenaFlags(ScenaFlag(0x0404, 7, 0x2027))
    SetScenaFlags(ScenaFlag(0x0405, 0, 0x2028))
    SetScenaFlags(ScenaFlag(0x0405, 1, 0x2029))
    SetScenaFlags(ScenaFlag(0x0405, 2, 0x202A))
    SetScenaFlags(ScenaFlag(0x0405, 3, 0x202B))
    SetScenaFlags(ScenaFlag(0x0405, 4, 0x202C))
    SetScenaFlags(ScenaFlag(0x0405, 5, 0x202D))
    SetScenaFlags(ScenaFlag(0x0405, 6, 0x202E))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x0405, 7, 0x202F))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    SetScenaFlags(ScenaFlag(0x0406, 7, 0x2037))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0407, 0, 0x2038))
    SetScenaFlags(ScenaFlag(0x0407, 1, 0x2039))
    SetScenaFlags(ScenaFlag(0x0407, 2, 0x203A))
    SetScenaFlags(ScenaFlag(0x0407, 3, 0x203B))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0407, 4, 0x203C))
    SetScenaFlags(ScenaFlag(0x0407, 5, 0x203D))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x0407, 6, 0x203E))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
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

    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    ClearScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    SetScenaFlags(ScenaFlag(0x0440, 0, 0x2200))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    SetScenaFlags(ScenaFlag(0x0440, 1, 0x2201))
    OP_C4(0x01, 0x00000008)
    SetScenaFlags(ScenaFlag(0x0440, 2, 0x2202))
    SetScenaFlags(ScenaFlag(0x0440, 3, 0x2203))
    SetScenaFlags(ScenaFlag(0x0440, 4, 0x2204))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0441, 5, 0x220D))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x0442, 0, 0x2210))
    ClearScenaFlags(ScenaFlag(0x0442, 1, 0x2211))
    ClearScenaFlags(ScenaFlag(0x0442, 2, 0x2212))
    ClearScenaFlags(ScenaFlag(0x0442, 3, 0x2213))
    ClearScenaFlags(ScenaFlag(0x0442, 4, 0x2214))
    ClearScenaFlags(ScenaFlag(0x0442, 5, 0x2215))
    ClearScenaFlags(ScenaFlag(0x0442, 6, 0x2216))
    ClearScenaFlags(ScenaFlag(0x0442, 7, 0x2217))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0443, 0, 0x2218))
    FormationAddMember(ChrTable['乔丝特2'], 0xFA, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationDelMember(0x45, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0443, 1, 0x2219))
    SetScenaFlags(ScenaFlag(0x0443, 2, 0x221A))
    SetScenaFlags(ScenaFlag(0x0443, 3, 0x221B))
    AddItem(ItemTable['原福音'], 1)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0443, 4, 0x221C))
    SetScenaFlags(ScenaFlag(0x0443, 6, 0x221E))
    SetScenaFlags(ScenaFlag(0x0445, 7, 0x222F))
    SetScenaFlags(ScenaFlag(0x0443, 7, 0x221F))
    SetScenaFlags(ScenaFlag(0x0444, 0, 0x2220))
    SetScenaFlags(ScenaFlag(0x0444, 1, 0x2221))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0444, 2, 0x2222))
    SetScenaFlags(ScenaFlag(0x0444, 3, 0x2223))
    SetScenaFlags(ScenaFlag(0x0444, 4, 0x2224))
    SetScenaFlags(ScenaFlag(0x0456, 2, 0x22B2))
    AddItem(ItemTable['安全卡片'], 1)
    SetScenaFlags(ScenaFlag(0x0444, 5, 0x2225))
    SetScenaFlags(ScenaFlag(0x0444, 6, 0x2226))
    SetScenaFlags(ScenaFlag(0x0444, 7, 0x2227))
    SetScenaFlags(ScenaFlag(0x0445, 0, 0x2228))
    SetScenaFlags(ScenaFlag(0x0445, 1, 0x2229))
    SetScenaFlags(ScenaFlag(0x0445, 2, 0x222A))
    SetScenaFlags(ScenaFlag(0x0445, 3, 0x222B))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0445, 4, 0x222C))
    SetScenaFlags(ScenaFlag(0x0445, 5, 0x222D))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0445, 6, 0x222E))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0446, 0, 0x2230))
    SetScenaFlags(ScenaFlag(0x0446, 1, 0x2231))
    SetScenaFlags(ScenaFlag(0x0447, 4, 0x223C))
    SetScenaFlags(ScenaFlag(0x0446, 2, 0x2232))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0446, 3, 0x2233))
    SetScenaFlags(ScenaFlag(0x0446, 4, 0x2234))
    SetScenaFlags(ScenaFlag(0x0446, 5, 0x2235))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0446, 6, 0x2236))
    SetScenaFlags(ScenaFlag(0x0446, 7, 0x2237))
    SetScenaFlags(ScenaFlag(0x0447, 0, 0x2238))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0447, 1, 0x2239))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021F, 2, 0x10FA))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021F, 2, 0x10FA))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0447, 2, 0x223A))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0447, 3, 0x223B))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationDelMember(0x01, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x0447, 5, 0x223D))
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    OP_BB(0x01, 0x00, 0x00200033)
    OP_BB(0x01, 0x01, 0x0000001C)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x08, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    SetScenaFlags(ScenaFlag(0x0447, 6, 0x223E))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))

    Return()

# id: 0x0002 offset: 0x1486
@scena.Code('func_02_1486')
def func_02_1486():
    FormationReset()
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    ClearScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    ClearScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    ClearScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    ClearScenaFlags(ScenaFlag(0x021F, 2, 0x10FA))
    ClearScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
    ClearScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    ClearScenaFlags(ScenaFlag(0x021F, 5, 0x10FD))
    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))

    Return()

# id: 0x0003 offset: 0x14B8
@scena.Code('func_03_14B8')
def func_03_14B8():
    ClearScenaFlags(ScenaFlag(0x0200, 2, 0x1002))
    ClearScenaFlags(ScenaFlag(0x0200, 3, 0x1003))
    ClearScenaFlags(ScenaFlag(0x0200, 4, 0x1004))
    ClearScenaFlags(ScenaFlag(0x0200, 5, 0x1005))
    ClearScenaFlags(ScenaFlag(0x0200, 6, 0x1006))
    ClearScenaFlags(ScenaFlag(0x0201, 0, 0x1008))
    ClearScenaFlags(ScenaFlag(0x0200, 7, 0x1007))
    ClearScenaFlags(ScenaFlag(0x0201, 1, 0x1009))
    ClearScenaFlags(ScenaFlag(0x0201, 2, 0x100A))
    ClearScenaFlags(ScenaFlag(0x0201, 3, 0x100B))
    ClearScenaFlags(ScenaFlag(0x0201, 4, 0x100C))
    ClearScenaFlags(ScenaFlag(0x0201, 5, 0x100D))
    ClearScenaFlags(ScenaFlag(0x0201, 6, 0x100E))
    ClearScenaFlags(ScenaFlag(0x0201, 7, 0x100F))
    ClearScenaFlags(ScenaFlag(0x0202, 0, 0x1010))
    ClearScenaFlags(ScenaFlag(0x0202, 1, 0x1011))
    ClearScenaFlags(ScenaFlag(0x0202, 2, 0x1012))
    ClearScenaFlags(ScenaFlag(0x0202, 3, 0x1013))
    ClearScenaFlags(ScenaFlag(0x0202, 4, 0x1014))
    ClearScenaFlags(ScenaFlag(0x0202, 5, 0x1015))
    ClearScenaFlags(ScenaFlag(0x0202, 6, 0x1016))
    ClearScenaFlags(ScenaFlag(0x0202, 7, 0x1017))
    ClearScenaFlags(ScenaFlag(0x0203, 0, 0x1018))
    ClearScenaFlags(ScenaFlag(0x0203, 1, 0x1019))
    ClearScenaFlags(ScenaFlag(0x0203, 2, 0x101A))
    ClearScenaFlags(ScenaFlag(0x0203, 3, 0x101B))
    ClearScenaFlags(ScenaFlag(0x0203, 4, 0x101C))
    ClearScenaFlags(ScenaFlag(0x0203, 5, 0x101D))
    ClearScenaFlags(ScenaFlag(0x0203, 6, 0x101E))
    ClearScenaFlags(ScenaFlag(0x0203, 7, 0x101F))
    ClearScenaFlags(ScenaFlag(0x0204, 0, 0x1020))
    ClearScenaFlags(ScenaFlag(0x0204, 1, 0x1021))
    ClearScenaFlags(ScenaFlag(0x0204, 2, 0x1022))
    ClearScenaFlags(ScenaFlag(0x0204, 3, 0x1023))
    ClearScenaFlags(ScenaFlag(0x0204, 4, 0x1024))
    ClearScenaFlags(ScenaFlag(0x0224, 0, 0x1120))
    ClearScenaFlags(ScenaFlag(0x0224, 1, 0x1121))
    ClearScenaFlags(ScenaFlag(0x0224, 2, 0x1122))
    ClearScenaFlags(ScenaFlag(0x0224, 3, 0x1123))
    ClearScenaFlags(ScenaFlag(0x0226, 0, 0x1130))
    ClearScenaFlags(ScenaFlag(0x0226, 1, 0x1131))
    ClearScenaFlags(ScenaFlag(0x0226, 2, 0x1132))
    ClearScenaFlags(ScenaFlag(0x0226, 3, 0x1133))

    Return()

# id: 0x0004 offset: 0x153A
@scena.Code('func_04_153A')
def func_04_153A():
    SetScenaFlags(ScenaFlag(0x0200, 2, 0x1002))
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x0200, 3, 0x1003))
    FormationDelMember(0x08, 0xFF)
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x0200, 4, 0x1004))
    SetScenaFlags(ScenaFlag(0x0200, 5, 0x1005))
    SetScenaFlags(ScenaFlag(0x0200, 6, 0x1006))
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x0200, 7, 0x1007))
    SetScenaFlags(ScenaFlag(0x0201, 0, 0x1008))
    SetScenaFlags(ScenaFlag(0x0201, 1, 0x1009))
    SetScenaFlags(ScenaFlag(0x0201, 2, 0x100A))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0201, 3, 0x100B))
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0201, 4, 0x100C))
    SetScenaFlags(ScenaFlag(0x0201, 5, 0x100D))
    SetScenaFlags(ScenaFlag(0x0201, 6, 0x100E))
    SetScenaFlags(ScenaFlag(0x0201, 7, 0x100F))
    SetScenaFlags(ScenaFlag(0x0202, 0, 0x1010))
    SetScenaFlags(ScenaFlag(0x0202, 1, 0x1011))
    SetScenaFlags(ScenaFlag(0x0202, 2, 0x1012))
    SetScenaFlags(ScenaFlag(0x0203, 3, 0x101B))
    SetScenaFlags(ScenaFlag(0x0203, 4, 0x101C))
    SetScenaFlags(ScenaFlag(0x0203, 5, 0x101D))
    SetScenaFlags(ScenaFlag(0x0203, 6, 0x101E))
    SetScenaFlags(ScenaFlag(0x0203, 7, 0x101F))
    SetScenaFlags(ScenaFlag(0x0204, 0, 0x1020))
    SetScenaFlags(ScenaFlag(0x0204, 1, 0x1021))
    SetScenaFlags(ScenaFlag(0x0204, 2, 0x1022))
    SetScenaFlags(ScenaFlag(0x0204, 3, 0x1023))
    SetScenaFlags(ScenaFlag(0x0204, 4, 0x1024))

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

    SetScenaFlags(ScenaFlag(0x0200, 2, 0x1002))
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x0200, 3, 0x1003))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FormationDelMember(0x08, 0xFF)
    NewScene('ED6_DT21/T5100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_17F2')

    def _loc_16A3(): pass

    label('loc_16A3')

    SetScenaFlags(ScenaFlag(0x0200, 2, 0x1002))
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x0200, 3, 0x1003))
    FormationDelMember(0x08, 0xFF)
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x0200, 4, 0x1004))
    SetScenaFlags(ScenaFlag(0x0200, 5, 0x1005))
    SetScenaFlags(ScenaFlag(0x0200, 6, 0x1006))
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x0200, 7, 0x1007))
    SetScenaFlags(ScenaFlag(0x0201, 0, 0x1008))
    SetScenaFlags(ScenaFlag(0x0201, 1, 0x1009))
    SetScenaFlags(ScenaFlag(0x0201, 2, 0x100A))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0201, 3, 0x100B))
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0201, 4, 0x100C))
    NewScene('ED6_DT21/C5504._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_17F2')

    def _loc_16F1(): pass

    label('loc_16F1')

    SetScenaFlags(ScenaFlag(0x0200, 2, 0x1002))
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x0200, 3, 0x1003))
    FormationDelMember(0x08, 0xFF)
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x0200, 4, 0x1004))
    SetScenaFlags(ScenaFlag(0x0200, 5, 0x1005))
    SetScenaFlags(ScenaFlag(0x0200, 6, 0x1006))
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x0200, 7, 0x1007))
    SetScenaFlags(ScenaFlag(0x0201, 0, 0x1008))
    SetScenaFlags(ScenaFlag(0x0201, 1, 0x1009))
    SetScenaFlags(ScenaFlag(0x0201, 2, 0x100A))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0201, 3, 0x100B))
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0201, 4, 0x100C))
    SetScenaFlags(ScenaFlag(0x0201, 5, 0x100D))
    SetScenaFlags(ScenaFlag(0x0201, 6, 0x100E))
    SetScenaFlags(ScenaFlag(0x0201, 7, 0x100F))
    SetScenaFlags(ScenaFlag(0x0202, 0, 0x1010))
    SetScenaFlags(ScenaFlag(0x0202, 1, 0x1011))
    SetScenaFlags(ScenaFlag(0x0202, 2, 0x1012))
    NewScene('ED6_DT21/T5100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_17F2')

    def _loc_1751(): pass

    label('loc_1751')

    SetScenaFlags(ScenaFlag(0x0200, 2, 0x1002))
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x0200, 3, 0x1003))
    FormationDelMember(0x08, 0xFF)
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x0200, 4, 0x1004))
    SetScenaFlags(ScenaFlag(0x0200, 5, 0x1005))
    SetScenaFlags(ScenaFlag(0x0200, 6, 0x1006))
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x0200, 7, 0x1007))
    SetScenaFlags(ScenaFlag(0x0201, 0, 0x1008))
    SetScenaFlags(ScenaFlag(0x0201, 1, 0x1009))
    SetScenaFlags(ScenaFlag(0x0201, 2, 0x100A))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0201, 3, 0x100B))
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0201, 4, 0x100C))
    SetScenaFlags(ScenaFlag(0x0201, 5, 0x100D))
    SetScenaFlags(ScenaFlag(0x0201, 6, 0x100E))
    SetScenaFlags(ScenaFlag(0x0201, 7, 0x100F))
    SetScenaFlags(ScenaFlag(0x0202, 0, 0x1010))
    SetScenaFlags(ScenaFlag(0x0202, 1, 0x1011))
    SetScenaFlags(ScenaFlag(0x0202, 2, 0x1012))
    SetScenaFlags(ScenaFlag(0x0203, 3, 0x101B))
    SetScenaFlags(ScenaFlag(0x0203, 4, 0x101C))
    SetScenaFlags(ScenaFlag(0x0203, 5, 0x101D))
    SetScenaFlags(ScenaFlag(0x0203, 6, 0x101E))
    SetScenaFlags(ScenaFlag(0x0203, 7, 0x101F))
    SetScenaFlags(ScenaFlag(0x0204, 0, 0x1020))
    SetScenaFlags(ScenaFlag(0x0204, 1, 0x1021))
    SetScenaFlags(ScenaFlag(0x0204, 2, 0x1022))
    SetScenaFlags(ScenaFlag(0x0204, 3, 0x1023))
    SetScenaFlags(ScenaFlag(0x0204, 4, 0x1024))
    NewScene('ED6_DT21/C5600._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_17F2')

    def _loc_17CF(): pass

    label('loc_17CF')

    SetScenaFlags(ScenaFlag(0x0200, 2, 0x1002))
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x0200, 3, 0x1003))
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
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    ClearScenaFlags(ScenaFlag(0x0240, 2, 0x1202))
    ClearScenaFlags(ScenaFlag(0x0240, 3, 0x1203))
    ClearScenaFlags(ScenaFlag(0x0240, 4, 0x1204))
    ClearScenaFlags(ScenaFlag(0x0240, 5, 0x1205))
    ClearScenaFlags(ScenaFlag(0x0240, 6, 0x1206))
    ClearScenaFlags(ScenaFlag(0x0240, 7, 0x1207))
    ClearScenaFlags(ScenaFlag(0x0241, 0, 0x1208))
    ClearScenaFlags(ScenaFlag(0x0241, 1, 0x1209))
    ClearScenaFlags(ScenaFlag(0x0241, 2, 0x120A))
    ClearScenaFlags(ScenaFlag(0x0241, 3, 0x120B))
    ClearScenaFlags(ScenaFlag(0x0241, 4, 0x120C))
    ClearScenaFlags(ScenaFlag(0x0241, 5, 0x120D))
    ClearScenaFlags(ScenaFlag(0x0241, 6, 0x120E))
    ClearScenaFlags(ScenaFlag(0x0241, 7, 0x120F))
    ClearScenaFlags(ScenaFlag(0x0242, 0, 0x1210))
    ClearScenaFlags(ScenaFlag(0x0242, 1, 0x1211))
    ClearScenaFlags(ScenaFlag(0x0242, 2, 0x1212))
    ClearScenaFlags(ScenaFlag(0x0242, 3, 0x1213))
    ClearScenaFlags(ScenaFlag(0x0242, 4, 0x1214))
    ClearScenaFlags(ScenaFlag(0x0242, 5, 0x1215))
    ClearScenaFlags(ScenaFlag(0x0242, 6, 0x1216))
    ClearScenaFlags(ScenaFlag(0x0242, 7, 0x1217))
    ClearScenaFlags(ScenaFlag(0x0243, 0, 0x1218))
    ClearScenaFlags(ScenaFlag(0x0243, 1, 0x1219))
    ClearScenaFlags(ScenaFlag(0x0243, 2, 0x121A))
    ClearScenaFlags(ScenaFlag(0x0243, 3, 0x121B))
    ClearScenaFlags(ScenaFlag(0x0243, 4, 0x121C))
    ClearScenaFlags(ScenaFlag(0x0243, 5, 0x121D))
    ClearScenaFlags(ScenaFlag(0x0243, 6, 0x121E))
    ClearScenaFlags(ScenaFlag(0x0243, 7, 0x121F))
    ClearScenaFlags(ScenaFlag(0x0244, 0, 0x1220))
    ClearScenaFlags(ScenaFlag(0x0244, 1, 0x1221))
    ClearScenaFlags(ScenaFlag(0x0244, 2, 0x1222))
    ClearScenaFlags(ScenaFlag(0x0244, 3, 0x1223))
    ClearScenaFlags(ScenaFlag(0x0244, 4, 0x1224))
    ClearScenaFlags(ScenaFlag(0x0244, 5, 0x1225))
    ClearScenaFlags(ScenaFlag(0x0244, 6, 0x1226))
    ClearScenaFlags(ScenaFlag(0x0244, 7, 0x1227))
    ClearScenaFlags(ScenaFlag(0x0245, 0, 0x1228))
    ClearScenaFlags(ScenaFlag(0x0245, 1, 0x1229))
    ClearScenaFlags(ScenaFlag(0x0245, 2, 0x122A))

    Return()

# id: 0x0007 offset: 0x1896
@scena.Code('func_07_1896')
def func_07_1896():
    SetScenaFlags(ScenaFlag(0x0240, 2, 0x1202))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0240, 3, 0x1203))
    SetScenaFlags(ScenaFlag(0x0240, 4, 0x1204))
    SetScenaFlags(ScenaFlag(0x0240, 5, 0x1205))
    SetScenaFlags(ScenaFlag(0x0240, 6, 0x1206))
    SetScenaFlags(ScenaFlag(0x0241, 6, 0x120E))
    SetScenaFlags(ScenaFlag(0x0241, 7, 0x120F))
    SetScenaFlags(ScenaFlag(0x0242, 0, 0x1210))
    SetScenaFlags(ScenaFlag(0x0242, 1, 0x1211))
    SetScenaFlags(ScenaFlag(0x0242, 2, 0x1212))
    SetScenaFlags(ScenaFlag(0x0242, 3, 0x1213))
    SetScenaFlags(ScenaFlag(0x0242, 4, 0x1214))
    SetScenaFlags(ScenaFlag(0x0242, 5, 0x1215))
    SetScenaFlags(ScenaFlag(0x0242, 6, 0x1216))
    SetScenaFlags(ScenaFlag(0x0242, 7, 0x1217))
    SetScenaFlags(ScenaFlag(0x0243, 0, 0x1218))
    SetScenaFlags(ScenaFlag(0x0243, 1, 0x1219))
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 2, 0x121A))
    FormationDelMember(0x08, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 3, 0x121B))
    SetScenaFlags(ScenaFlag(0x0243, 4, 0x121C))
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['朵洛希'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 5, 0x121D))
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 6, 0x121E))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x26, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 7, 0x121F))
    SetScenaFlags(ScenaFlag(0x0244, 0, 0x1220))
    SetScenaFlags(ScenaFlag(0x0244, 1, 0x1221))
    FormationAddMember(ChrTable['朵洛希'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x0244, 2, 0x1222))
    SetScenaFlags(ScenaFlag(0x0244, 3, 0x1223))
    SetScenaFlags(ScenaFlag(0x0244, 4, 0x1224))
    SetScenaFlags(ScenaFlag(0x0244, 5, 0x1225))
    SetScenaFlags(ScenaFlag(0x0244, 6, 0x1226))
    SetScenaFlags(ScenaFlag(0x0244, 7, 0x1227))
    SetScenaFlags(ScenaFlag(0x0245, 0, 0x1228))
    SetScenaFlags(ScenaFlag(0x0245, 1, 0x1229))
    FormationDelMember(0x26, 0xFF)
    SetScenaFlags(ScenaFlag(0x0245, 2, 0x122A))

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

    SetScenaFlags(ScenaFlag(0x0240, 2, 0x1202))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0240, 3, 0x1203))
    SetScenaFlags(ScenaFlag(0x0240, 4, 0x1204))
    NewScene('ED6_DT21/E0000._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1A7A(): pass

    label('loc_1A7A')

    SetScenaFlags(ScenaFlag(0x0240, 2, 0x1202))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0240, 3, 0x1203))
    SetScenaFlags(ScenaFlag(0x0240, 4, 0x1204))
    SetScenaFlags(ScenaFlag(0x0240, 5, 0x1205))
    SetScenaFlags(ScenaFlag(0x0240, 6, 0x1206))
    NewScene('ED6_DT21/T2130._SN', 108, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1A98(): pass

    label('loc_1A98')

    SetScenaFlags(ScenaFlag(0x0240, 2, 0x1202))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0240, 3, 0x1203))
    SetScenaFlags(ScenaFlag(0x0240, 4, 0x1204))
    SetScenaFlags(ScenaFlag(0x0240, 5, 0x1205))
    SetScenaFlags(ScenaFlag(0x0240, 6, 0x1206))
    SetScenaFlags(ScenaFlag(0x0241, 6, 0x120E))
    SetScenaFlags(ScenaFlag(0x0241, 7, 0x120F))
    SetScenaFlags(ScenaFlag(0x0242, 0, 0x1210))
    NewScene('ED6_DT21/T2700._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1ABF(): pass

    label('loc_1ABF')

    SetScenaFlags(ScenaFlag(0x0240, 2, 0x1202))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0240, 3, 0x1203))
    SetScenaFlags(ScenaFlag(0x0240, 4, 0x1204))
    SetScenaFlags(ScenaFlag(0x0240, 5, 0x1205))
    SetScenaFlags(ScenaFlag(0x0240, 6, 0x1206))
    SetScenaFlags(ScenaFlag(0x0241, 6, 0x120E))
    SetScenaFlags(ScenaFlag(0x0241, 7, 0x120F))
    SetScenaFlags(ScenaFlag(0x0242, 0, 0x1210))
    SetScenaFlags(ScenaFlag(0x0242, 1, 0x1211))
    SetScenaFlags(ScenaFlag(0x0242, 2, 0x1212))
    SetScenaFlags(ScenaFlag(0x0242, 3, 0x1213))
    SetScenaFlags(ScenaFlag(0x0242, 4, 0x1214))
    SetScenaFlags(ScenaFlag(0x0242, 5, 0x1215))
    NewScene('ED6_DT21/T2402._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1AF5(): pass

    label('loc_1AF5')

    SetScenaFlags(ScenaFlag(0x0240, 2, 0x1202))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0240, 3, 0x1203))
    SetScenaFlags(ScenaFlag(0x0240, 4, 0x1204))
    SetScenaFlags(ScenaFlag(0x0240, 5, 0x1205))
    SetScenaFlags(ScenaFlag(0x0240, 6, 0x1206))
    SetScenaFlags(ScenaFlag(0x0241, 6, 0x120E))
    SetScenaFlags(ScenaFlag(0x0241, 7, 0x120F))
    SetScenaFlags(ScenaFlag(0x0242, 0, 0x1210))
    SetScenaFlags(ScenaFlag(0x0242, 1, 0x1211))
    SetScenaFlags(ScenaFlag(0x0242, 2, 0x1212))
    SetScenaFlags(ScenaFlag(0x0242, 3, 0x1213))
    SetScenaFlags(ScenaFlag(0x0242, 4, 0x1214))
    SetScenaFlags(ScenaFlag(0x0242, 5, 0x1215))
    SetScenaFlags(ScenaFlag(0x0242, 6, 0x1216))
    SetScenaFlags(ScenaFlag(0x0242, 7, 0x1217))
    SetScenaFlags(ScenaFlag(0x0243, 0, 0x1218))
    SetScenaFlags(ScenaFlag(0x0243, 1, 0x1219))
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 2, 0x121A))
    FormationDelMember(0x08, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 3, 0x121B))
    NewScene('ED6_DT21/T2120._SN', 105, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1B44(): pass

    label('loc_1B44')

    SetScenaFlags(ScenaFlag(0x0240, 2, 0x1202))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0240, 3, 0x1203))
    SetScenaFlags(ScenaFlag(0x0240, 4, 0x1204))
    SetScenaFlags(ScenaFlag(0x0240, 5, 0x1205))
    SetScenaFlags(ScenaFlag(0x0240, 6, 0x1206))
    SetScenaFlags(ScenaFlag(0x0241, 6, 0x120E))
    SetScenaFlags(ScenaFlag(0x0241, 7, 0x120F))
    SetScenaFlags(ScenaFlag(0x0242, 0, 0x1210))
    SetScenaFlags(ScenaFlag(0x0242, 1, 0x1211))
    SetScenaFlags(ScenaFlag(0x0242, 2, 0x1212))
    SetScenaFlags(ScenaFlag(0x0242, 3, 0x1213))
    SetScenaFlags(ScenaFlag(0x0242, 4, 0x1214))
    SetScenaFlags(ScenaFlag(0x0242, 5, 0x1215))
    SetScenaFlags(ScenaFlag(0x0242, 6, 0x1216))
    SetScenaFlags(ScenaFlag(0x0242, 7, 0x1217))
    SetScenaFlags(ScenaFlag(0x0243, 0, 0x1218))
    SetScenaFlags(ScenaFlag(0x0243, 1, 0x1219))
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 2, 0x121A))
    FormationDelMember(0x08, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 3, 0x121B))
    SetScenaFlags(ScenaFlag(0x0243, 4, 0x121C))
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['朵洛希'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 5, 0x121D))
    NewScene('ED6_DT21/T2500._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1BA1(): pass

    label('loc_1BA1')

    SetScenaFlags(ScenaFlag(0x0240, 2, 0x1202))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0240, 3, 0x1203))
    SetScenaFlags(ScenaFlag(0x0240, 4, 0x1204))
    SetScenaFlags(ScenaFlag(0x0240, 5, 0x1205))
    SetScenaFlags(ScenaFlag(0x0240, 6, 0x1206))
    SetScenaFlags(ScenaFlag(0x0241, 6, 0x120E))
    SetScenaFlags(ScenaFlag(0x0241, 7, 0x120F))
    SetScenaFlags(ScenaFlag(0x0242, 0, 0x1210))
    SetScenaFlags(ScenaFlag(0x0242, 1, 0x1211))
    SetScenaFlags(ScenaFlag(0x0242, 2, 0x1212))
    SetScenaFlags(ScenaFlag(0x0242, 3, 0x1213))
    SetScenaFlags(ScenaFlag(0x0242, 4, 0x1214))
    SetScenaFlags(ScenaFlag(0x0242, 5, 0x1215))
    SetScenaFlags(ScenaFlag(0x0242, 6, 0x1216))
    SetScenaFlags(ScenaFlag(0x0242, 7, 0x1217))
    SetScenaFlags(ScenaFlag(0x0243, 0, 0x1218))
    SetScenaFlags(ScenaFlag(0x0243, 1, 0x1219))
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 2, 0x121A))
    FormationDelMember(0x08, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 3, 0x121B))
    SetScenaFlags(ScenaFlag(0x0243, 4, 0x121C))
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['朵洛希'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 5, 0x121D))
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 6, 0x121E))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x26, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 7, 0x121F))
    SetScenaFlags(ScenaFlag(0x0244, 0, 0x1220))
    SetScenaFlags(ScenaFlag(0x0244, 1, 0x1221))
    FormationAddMember(ChrTable['朵洛希'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x0244, 2, 0x1222))
    NewScene('ED6_DT21/T2800._SN', 120, 0, 0)
    IdleLoop()

    Jump('loc_1CD4')

    def _loc_1C25(): pass

    label('loc_1C25')

    SetScenaFlags(ScenaFlag(0x0240, 2, 0x1202))
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x0240, 3, 0x1203))
    SetScenaFlags(ScenaFlag(0x0240, 4, 0x1204))
    SetScenaFlags(ScenaFlag(0x0240, 5, 0x1205))
    SetScenaFlags(ScenaFlag(0x0240, 6, 0x1206))
    SetScenaFlags(ScenaFlag(0x0241, 6, 0x120E))
    SetScenaFlags(ScenaFlag(0x0241, 7, 0x120F))
    SetScenaFlags(ScenaFlag(0x0242, 0, 0x1210))
    SetScenaFlags(ScenaFlag(0x0242, 1, 0x1211))
    SetScenaFlags(ScenaFlag(0x0242, 2, 0x1212))
    SetScenaFlags(ScenaFlag(0x0242, 3, 0x1213))
    SetScenaFlags(ScenaFlag(0x0242, 4, 0x1214))
    SetScenaFlags(ScenaFlag(0x0242, 5, 0x1215))
    SetScenaFlags(ScenaFlag(0x0242, 6, 0x1216))
    SetScenaFlags(ScenaFlag(0x0242, 7, 0x1217))
    SetScenaFlags(ScenaFlag(0x0243, 0, 0x1218))
    SetScenaFlags(ScenaFlag(0x0243, 1, 0x1219))
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 2, 0x121A))
    FormationDelMember(0x08, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 3, 0x121B))
    SetScenaFlags(ScenaFlag(0x0243, 4, 0x121C))
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['朵洛希'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 5, 0x121D))
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 6, 0x121E))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x26, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 7, 0x121F))
    SetScenaFlags(ScenaFlag(0x0244, 0, 0x1220))
    SetScenaFlags(ScenaFlag(0x0244, 1, 0x1221))
    FormationAddMember(ChrTable['朵洛希'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x0244, 2, 0x1222))
    SetScenaFlags(ScenaFlag(0x0244, 3, 0x1223))
    SetScenaFlags(ScenaFlag(0x0244, 4, 0x1224))
    SetScenaFlags(ScenaFlag(0x0244, 5, 0x1225))
    SetScenaFlags(ScenaFlag(0x0244, 6, 0x1226))
    SetScenaFlags(ScenaFlag(0x0244, 7, 0x1227))
    SetScenaFlags(ScenaFlag(0x0245, 0, 0x1228))
    SetScenaFlags(ScenaFlag(0x0245, 1, 0x1229))
    FormationDelMember(0x26, 0xFF)
    SetScenaFlags(ScenaFlag(0x0245, 2, 0x122A))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
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
    ClearScenaFlags(ScenaFlag(0x0280, 0, 0x1400))
    ClearScenaFlags(ScenaFlag(0x0280, 1, 0x1401))
    ClearScenaFlags(ScenaFlag(0x0280, 2, 0x1402))
    ClearScenaFlags(ScenaFlag(0x0280, 3, 0x1403))
    ClearScenaFlags(ScenaFlag(0x0280, 4, 0x1404))
    ClearScenaFlags(ScenaFlag(0x0280, 5, 0x1405))
    ClearScenaFlags(ScenaFlag(0x0280, 6, 0x1406))
    ClearScenaFlags(ScenaFlag(0x0280, 7, 0x1407))
    ClearScenaFlags(ScenaFlag(0x0281, 0, 0x1408))
    ClearScenaFlags(ScenaFlag(0x0281, 1, 0x1409))
    ClearScenaFlags(ScenaFlag(0x0281, 2, 0x140A))
    ClearScenaFlags(ScenaFlag(0x0281, 3, 0x140B))
    ClearScenaFlags(ScenaFlag(0x0281, 4, 0x140C))
    ClearScenaFlags(ScenaFlag(0x0282, 0, 0x1410))
    ClearScenaFlags(ScenaFlag(0x0281, 5, 0x140D))
    ClearScenaFlags(ScenaFlag(0x0282, 1, 0x1411))
    ClearScenaFlags(ScenaFlag(0x0282, 2, 0x1412))
    ClearScenaFlags(ScenaFlag(0x0281, 6, 0x140E))
    ClearScenaFlags(ScenaFlag(0x0281, 7, 0x140F))
    ClearScenaFlags(ScenaFlag(0x0282, 3, 0x1413))
    ClearScenaFlags(ScenaFlag(0x0282, 4, 0x1414))
    ClearScenaFlags(ScenaFlag(0x0282, 5, 0x1415))
    ClearScenaFlags(ScenaFlag(0x0282, 6, 0x1416))
    ClearScenaFlags(ScenaFlag(0x0282, 7, 0x1417))
    ClearScenaFlags(ScenaFlag(0x0283, 0, 0x1418))
    ClearScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    ClearScenaFlags(ScenaFlag(0x0283, 2, 0x141A))
    ClearScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    ClearScenaFlags(ScenaFlag(0x0283, 4, 0x141C))
    ClearScenaFlags(ScenaFlag(0x0283, 5, 0x141D))
    ClearScenaFlags(ScenaFlag(0x0283, 6, 0x141E))
    ClearScenaFlags(ScenaFlag(0x0283, 7, 0x141F))
    ClearScenaFlags(ScenaFlag(0x0284, 0, 0x1420))
    ClearScenaFlags(ScenaFlag(0x0284, 1, 0x1421))
    ClearScenaFlags(ScenaFlag(0x0284, 2, 0x1422))
    ClearScenaFlags(ScenaFlag(0x0284, 3, 0x1423))
    ClearScenaFlags(ScenaFlag(0x0284, 4, 0x1424))
    ClearScenaFlags(ScenaFlag(0x0290, 0, 0x1480))
    ClearScenaFlags(ScenaFlag(0x0290, 1, 0x1481))
    ClearScenaFlags(ScenaFlag(0x0290, 2, 0x1482))

    Return()

# id: 0x000A offset: 0x1D65
@scena.Code('func_0A_1D65')
def func_0A_1D65():
    SetScenaFlags(ScenaFlag(0x0280, 0, 0x1400))
    SetScenaFlags(ScenaFlag(0x0280, 1, 0x1401))
    SetScenaFlags(ScenaFlag(0x0280, 2, 0x1402))
    SetScenaFlags(ScenaFlag(0x0280, 3, 0x1403))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    SetScenaFlags(ScenaFlag(0x0280, 4, 0x1404))
    SetScenaFlags(ScenaFlag(0x0280, 5, 0x1405))
    SetScenaFlags(ScenaFlag(0x0280, 6, 0x1406))
    SetScenaFlags(ScenaFlag(0x0280, 7, 0x1407))
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0281, 0, 0x1408))
    SetScenaFlags(ScenaFlag(0x0281, 1, 0x1409))
    SetScenaFlags(ScenaFlag(0x0281, 2, 0x140A))
    SetScenaFlags(ScenaFlag(0x0281, 3, 0x140B))
    SetScenaFlags(ScenaFlag(0x0281, 4, 0x140C))
    SetScenaFlags(ScenaFlag(0x0282, 0, 0x1410))
    SetScenaFlags(ScenaFlag(0x0281, 5, 0x140D))
    SetScenaFlags(ScenaFlag(0x0282, 1, 0x1411))
    SetScenaFlags(ScenaFlag(0x0281, 6, 0x140E))
    SetScenaFlags(ScenaFlag(0x0281, 7, 0x140F))
    SetScenaFlags(ScenaFlag(0x0282, 2, 0x1412))
    SetScenaFlags(ScenaFlag(0x0282, 3, 0x1413))
    SetScenaFlags(ScenaFlag(0x0282, 4, 0x1414))
    SetScenaFlags(ScenaFlag(0x0282, 5, 0x1415))
    SetScenaFlags(ScenaFlag(0x0282, 6, 0x1416))
    SetScenaFlags(ScenaFlag(0x0282, 7, 0x1417))
    SetScenaFlags(ScenaFlag(0x0283, 0, 0x1418))
    SetScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    SetScenaFlags(ScenaFlag(0x0283, 2, 0x141A))
    SetScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    SetScenaFlags(ScenaFlag(0x0283, 4, 0x141C))
    SetScenaFlags(ScenaFlag(0x0283, 5, 0x141D))
    SetScenaFlags(ScenaFlag(0x0283, 6, 0x141E))
    SetScenaFlags(ScenaFlag(0x0283, 7, 0x141F))
    SetScenaFlags(ScenaFlag(0x0284, 0, 0x1420))
    SetScenaFlags(ScenaFlag(0x0284, 1, 0x1421))
    SetScenaFlags(ScenaFlag(0x0284, 2, 0x1422))
    SetScenaFlags(ScenaFlag(0x0284, 3, 0x1423))
    SetScenaFlags(ScenaFlag(0x0284, 4, 0x1424))

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

    SetScenaFlags(ScenaFlag(0x0280, 0, 0x1400))
    NewScene('ED6_DT21/T2100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_1F0B(): pass

    label('loc_1F0B')

    SetScenaFlags(ScenaFlag(0x0280, 0, 0x1400))
    SetScenaFlags(ScenaFlag(0x0280, 1, 0x1401))
    SetScenaFlags(ScenaFlag(0x0280, 2, 0x1402))
    SetScenaFlags(ScenaFlag(0x0280, 3, 0x1403))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    NewScene('ED6_DT21/E0011._SN', 114, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_1F2F(): pass

    label('loc_1F2F')

    SetScenaFlags(ScenaFlag(0x0280, 0, 0x1400))
    SetScenaFlags(ScenaFlag(0x0280, 1, 0x1401))
    SetScenaFlags(ScenaFlag(0x0280, 2, 0x1402))
    SetScenaFlags(ScenaFlag(0x0280, 3, 0x1403))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    SetScenaFlags(ScenaFlag(0x0280, 4, 0x1404))
    SetScenaFlags(ScenaFlag(0x0280, 5, 0x1405))
    SetScenaFlags(ScenaFlag(0x0280, 6, 0x1406))
    SetScenaFlags(ScenaFlag(0x0280, 7, 0x1407))
    NewScene('ED6_DT21/E0011._SN', 110, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_1F5F(): pass

    label('loc_1F5F')

    SetScenaFlags(ScenaFlag(0x0280, 0, 0x1400))
    SetScenaFlags(ScenaFlag(0x0280, 1, 0x1401))
    SetScenaFlags(ScenaFlag(0x0280, 2, 0x1402))
    SetScenaFlags(ScenaFlag(0x0280, 3, 0x1403))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    SetScenaFlags(ScenaFlag(0x0280, 4, 0x1404))
    SetScenaFlags(ScenaFlag(0x0280, 5, 0x1405))
    SetScenaFlags(ScenaFlag(0x0280, 6, 0x1406))
    SetScenaFlags(ScenaFlag(0x0280, 7, 0x1407))
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0281, 0, 0x1408))
    SetScenaFlags(ScenaFlag(0x0281, 1, 0x1409))
    SetScenaFlags(ScenaFlag(0x0281, 2, 0x140A))
    NewScene('ED6_DT21/T3300._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_1FA0(): pass

    label('loc_1FA0')

    SetScenaFlags(ScenaFlag(0x0280, 0, 0x1400))
    SetScenaFlags(ScenaFlag(0x0280, 1, 0x1401))
    SetScenaFlags(ScenaFlag(0x0280, 2, 0x1402))
    SetScenaFlags(ScenaFlag(0x0280, 3, 0x1403))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    SetScenaFlags(ScenaFlag(0x0280, 4, 0x1404))
    SetScenaFlags(ScenaFlag(0x0280, 5, 0x1405))
    SetScenaFlags(ScenaFlag(0x0280, 6, 0x1406))
    SetScenaFlags(ScenaFlag(0x0280, 7, 0x1407))
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0281, 0, 0x1408))
    SetScenaFlags(ScenaFlag(0x0281, 1, 0x1409))
    SetScenaFlags(ScenaFlag(0x0281, 2, 0x140A))
    SetScenaFlags(ScenaFlag(0x0281, 3, 0x140B))
    SetScenaFlags(ScenaFlag(0x0281, 4, 0x140C))
    SetScenaFlags(ScenaFlag(0x0282, 0, 0x1410))
    SetScenaFlags(ScenaFlag(0x0281, 5, 0x140D))
    SetScenaFlags(ScenaFlag(0x0282, 1, 0x1411))
    SetScenaFlags(ScenaFlag(0x0281, 6, 0x140E))
    SetScenaFlags(ScenaFlag(0x0281, 7, 0x140F))
    SetScenaFlags(ScenaFlag(0x0282, 2, 0x1412))
    NewScene('ED6_DT21/T3401._SN', 106, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_1FF9(): pass

    label('loc_1FF9')

    SetScenaFlags(ScenaFlag(0x0280, 0, 0x1400))
    SetScenaFlags(ScenaFlag(0x0280, 1, 0x1401))
    SetScenaFlags(ScenaFlag(0x0280, 2, 0x1402))
    SetScenaFlags(ScenaFlag(0x0280, 3, 0x1403))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    SetScenaFlags(ScenaFlag(0x0280, 4, 0x1404))
    SetScenaFlags(ScenaFlag(0x0280, 5, 0x1405))
    SetScenaFlags(ScenaFlag(0x0280, 6, 0x1406))
    SetScenaFlags(ScenaFlag(0x0280, 7, 0x1407))
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0281, 0, 0x1408))
    SetScenaFlags(ScenaFlag(0x0281, 1, 0x1409))
    SetScenaFlags(ScenaFlag(0x0281, 2, 0x140A))
    SetScenaFlags(ScenaFlag(0x0281, 3, 0x140B))
    SetScenaFlags(ScenaFlag(0x0281, 4, 0x140C))
    SetScenaFlags(ScenaFlag(0x0282, 0, 0x1410))
    SetScenaFlags(ScenaFlag(0x0281, 5, 0x140D))
    SetScenaFlags(ScenaFlag(0x0282, 1, 0x1411))
    SetScenaFlags(ScenaFlag(0x0281, 6, 0x140E))
    SetScenaFlags(ScenaFlag(0x0281, 7, 0x140F))
    SetScenaFlags(ScenaFlag(0x0282, 2, 0x1412))
    SetScenaFlags(ScenaFlag(0x0282, 3, 0x1413))
    SetScenaFlags(ScenaFlag(0x0282, 4, 0x1414))
    SetScenaFlags(ScenaFlag(0x0282, 5, 0x1415))
    SetScenaFlags(ScenaFlag(0x0282, 6, 0x1416))
    SetScenaFlags(ScenaFlag(0x0282, 7, 0x1417))
    NewScene('ED6_DT21/T3120._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_2061(): pass

    label('loc_2061')

    SetScenaFlags(ScenaFlag(0x0280, 0, 0x1400))
    SetScenaFlags(ScenaFlag(0x0280, 1, 0x1401))
    SetScenaFlags(ScenaFlag(0x0280, 2, 0x1402))
    SetScenaFlags(ScenaFlag(0x0280, 3, 0x1403))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    SetScenaFlags(ScenaFlag(0x0280, 4, 0x1404))
    SetScenaFlags(ScenaFlag(0x0280, 5, 0x1405))
    SetScenaFlags(ScenaFlag(0x0280, 6, 0x1406))
    SetScenaFlags(ScenaFlag(0x0280, 7, 0x1407))
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0281, 0, 0x1408))
    SetScenaFlags(ScenaFlag(0x0281, 1, 0x1409))
    SetScenaFlags(ScenaFlag(0x0281, 2, 0x140A))
    SetScenaFlags(ScenaFlag(0x0281, 3, 0x140B))
    SetScenaFlags(ScenaFlag(0x0281, 4, 0x140C))
    SetScenaFlags(ScenaFlag(0x0282, 0, 0x1410))
    SetScenaFlags(ScenaFlag(0x0281, 5, 0x140D))
    SetScenaFlags(ScenaFlag(0x0282, 1, 0x1411))
    SetScenaFlags(ScenaFlag(0x0281, 6, 0x140E))
    SetScenaFlags(ScenaFlag(0x0281, 7, 0x140F))
    SetScenaFlags(ScenaFlag(0x0282, 2, 0x1412))
    SetScenaFlags(ScenaFlag(0x0282, 3, 0x1413))
    SetScenaFlags(ScenaFlag(0x0282, 4, 0x1414))
    SetScenaFlags(ScenaFlag(0x0282, 5, 0x1415))
    SetScenaFlags(ScenaFlag(0x0282, 6, 0x1416))
    SetScenaFlags(ScenaFlag(0x0282, 7, 0x1417))
    SetScenaFlags(ScenaFlag(0x0283, 0, 0x1418))
    SetScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    SetScenaFlags(ScenaFlag(0x0283, 2, 0x141A))
    SetScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    SetScenaFlags(ScenaFlag(0x0283, 4, 0x141C))
    SetScenaFlags(ScenaFlag(0x0283, 5, 0x141D))
    SetScenaFlags(ScenaFlag(0x0283, 6, 0x141E))
    SetScenaFlags(ScenaFlag(0x0283, 7, 0x141F))
    SetScenaFlags(ScenaFlag(0x0284, 0, 0x1420))
    NewScene('ED6_DT21/T3200._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2183')

    def _loc_20E4(): pass

    label('loc_20E4')

    SetScenaFlags(ScenaFlag(0x0280, 0, 0x1400))
    SetScenaFlags(ScenaFlag(0x0280, 1, 0x1401))
    SetScenaFlags(ScenaFlag(0x0280, 2, 0x1402))
    SetScenaFlags(ScenaFlag(0x0280, 3, 0x1403))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    SetScenaFlags(ScenaFlag(0x0280, 4, 0x1404))
    SetScenaFlags(ScenaFlag(0x0280, 5, 0x1405))
    SetScenaFlags(ScenaFlag(0x0280, 6, 0x1406))
    SetScenaFlags(ScenaFlag(0x0280, 7, 0x1407))
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0281, 0, 0x1408))
    SetScenaFlags(ScenaFlag(0x0281, 1, 0x1409))
    SetScenaFlags(ScenaFlag(0x0281, 2, 0x140A))
    SetScenaFlags(ScenaFlag(0x0281, 3, 0x140B))
    SetScenaFlags(ScenaFlag(0x0281, 4, 0x140C))
    SetScenaFlags(ScenaFlag(0x0282, 0, 0x1410))
    SetScenaFlags(ScenaFlag(0x0281, 5, 0x140D))
    SetScenaFlags(ScenaFlag(0x0282, 1, 0x1411))
    SetScenaFlags(ScenaFlag(0x0281, 6, 0x140E))
    SetScenaFlags(ScenaFlag(0x0281, 7, 0x140F))
    SetScenaFlags(ScenaFlag(0x0282, 2, 0x1412))
    SetScenaFlags(ScenaFlag(0x0282, 3, 0x1413))
    SetScenaFlags(ScenaFlag(0x0282, 4, 0x1414))
    SetScenaFlags(ScenaFlag(0x0282, 5, 0x1415))
    SetScenaFlags(ScenaFlag(0x0282, 6, 0x1416))
    SetScenaFlags(ScenaFlag(0x0282, 7, 0x1417))
    SetScenaFlags(ScenaFlag(0x0283, 0, 0x1418))
    SetScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    SetScenaFlags(ScenaFlag(0x0283, 2, 0x141A))
    SetScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    SetScenaFlags(ScenaFlag(0x0283, 4, 0x141C))
    SetScenaFlags(ScenaFlag(0x0283, 5, 0x141D))
    SetScenaFlags(ScenaFlag(0x0283, 6, 0x141E))
    SetScenaFlags(ScenaFlag(0x0283, 7, 0x141F))
    SetScenaFlags(ScenaFlag(0x0284, 0, 0x1420))
    SetScenaFlags(ScenaFlag(0x0284, 1, 0x1421))
    SetScenaFlags(ScenaFlag(0x0284, 2, 0x1422))
    SetScenaFlags(ScenaFlag(0x0284, 3, 0x1423))
    SetScenaFlags(ScenaFlag(0x0284, 4, 0x1424))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
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
    ClearScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    ClearScenaFlags(ScenaFlag(0x02C0, 1, 0x1601))
    ClearScenaFlags(ScenaFlag(0x02C0, 2, 0x1602))
    ClearScenaFlags(ScenaFlag(0x02C0, 3, 0x1603))
    ClearScenaFlags(ScenaFlag(0x02C0, 4, 0x1604))
    ClearScenaFlags(ScenaFlag(0x02C0, 5, 0x1605))
    ClearScenaFlags(ScenaFlag(0x02C0, 6, 0x1606))
    ClearScenaFlags(ScenaFlag(0x02C0, 7, 0x1607))
    ClearScenaFlags(ScenaFlag(0x02C1, 0, 0x1608))
    ClearScenaFlags(ScenaFlag(0x02C1, 1, 0x1609))
    ClearScenaFlags(ScenaFlag(0x02C1, 2, 0x160A))
    ClearScenaFlags(ScenaFlag(0x02C1, 3, 0x160B))
    ClearScenaFlags(ScenaFlag(0x02C1, 4, 0x160C))
    ClearScenaFlags(ScenaFlag(0x02C1, 5, 0x160D))
    ClearScenaFlags(ScenaFlag(0x02C1, 6, 0x160E))
    ClearScenaFlags(ScenaFlag(0x02C1, 7, 0x160F))
    ClearScenaFlags(ScenaFlag(0x02C2, 0, 0x1610))
    ClearScenaFlags(ScenaFlag(0x02C2, 1, 0x1611))
    ClearScenaFlags(ScenaFlag(0x02C2, 2, 0x1612))
    ClearScenaFlags(ScenaFlag(0x02C2, 4, 0x1614))
    ClearScenaFlags(ScenaFlag(0x02C2, 5, 0x1615))
    ClearScenaFlags(ScenaFlag(0x02C2, 6, 0x1616))
    ClearScenaFlags(ScenaFlag(0x02C2, 7, 0x1617))
    ClearScenaFlags(ScenaFlag(0x02C2, 3, 0x1613))
    ClearScenaFlags(ScenaFlag(0x02C3, 0, 0x1618))
    ClearScenaFlags(ScenaFlag(0x02C3, 1, 0x1619))
    ClearScenaFlags(ScenaFlag(0x02C3, 2, 0x161A))
    ClearScenaFlags(ScenaFlag(0x02C3, 3, 0x161B))
    ClearScenaFlags(ScenaFlag(0x02C3, 4, 0x161C))
    ClearScenaFlags(ScenaFlag(0x02C3, 5, 0x161D))
    ClearScenaFlags(ScenaFlag(0x02C3, 6, 0x161E))
    ClearScenaFlags(ScenaFlag(0x02C3, 7, 0x161F))
    ClearScenaFlags(ScenaFlag(0x02C4, 0, 0x1620))
    ClearScenaFlags(ScenaFlag(0x02C4, 1, 0x1621))
    ClearScenaFlags(ScenaFlag(0x02C4, 2, 0x1622))
    ClearScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    ClearScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    ClearScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    ClearScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    ClearScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    ClearScenaFlags(ScenaFlag(0x02C5, 0, 0x1628))
    ClearScenaFlags(ScenaFlag(0x02D0, 0, 0x1680))
    ClearScenaFlags(ScenaFlag(0x02C5, 1, 0x1629))
    ClearScenaFlags(ScenaFlag(0x02C5, 2, 0x162A))
    ClearScenaFlags(ScenaFlag(0x02C5, 3, 0x162B))
    ClearScenaFlags(ScenaFlag(0x02C5, 4, 0x162C))
    ClearScenaFlags(ScenaFlag(0x02C5, 5, 0x162D))
    ClearScenaFlags(ScenaFlag(0x02C5, 6, 0x162E))
    ClearScenaFlags(ScenaFlag(0x02C5, 7, 0x162F))
    ClearScenaFlags(ScenaFlag(0x02C6, 0, 0x1630))
    ClearScenaFlags(ScenaFlag(0x02C6, 1, 0x1631))
    ClearScenaFlags(ScenaFlag(0x02C6, 2, 0x1632))
    ClearScenaFlags(ScenaFlag(0x02C6, 3, 0x1633))
    ClearScenaFlags(ScenaFlag(0x02C6, 4, 0x1634))
    ClearScenaFlags(ScenaFlag(0x02C6, 5, 0x1635))
    ClearScenaFlags(ScenaFlag(0x02C6, 6, 0x1636))
    ClearScenaFlags(ScenaFlag(0x02C6, 7, 0x1637))
    ClearScenaFlags(ScenaFlag(0x02C7, 0, 0x1638))
    ClearScenaFlags(ScenaFlag(0x02C7, 1, 0x1639))
    ClearScenaFlags(ScenaFlag(0x02C7, 2, 0x163A))
    ClearScenaFlags(ScenaFlag(0x02C7, 3, 0x163B))
    ClearScenaFlags(ScenaFlag(0x02C7, 4, 0x163C))
    ClearScenaFlags(ScenaFlag(0x02C7, 5, 0x163D))
    ClearScenaFlags(ScenaFlag(0x02C7, 6, 0x163E))

    Return()

# id: 0x000D offset: 0x2257
@scena.Code('func_0D_2257')
def func_0D_2257():
    SetScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    SetScenaFlags(ScenaFlag(0x02C0, 1, 0x1601))
    SetScenaFlags(ScenaFlag(0x02C0, 2, 0x1602))
    SetScenaFlags(ScenaFlag(0x02C0, 3, 0x1603))
    SetScenaFlags(ScenaFlag(0x02C0, 4, 0x1604))
    SetScenaFlags(ScenaFlag(0x02C0, 7, 0x1607))
    SetScenaFlags(ScenaFlag(0x02C0, 5, 0x1605))
    SetScenaFlags(ScenaFlag(0x02C0, 6, 0x1606))
    SetScenaFlags(ScenaFlag(0x02C1, 0, 0x1608))
    SetScenaFlags(ScenaFlag(0x02C1, 1, 0x1609))
    SetScenaFlags(ScenaFlag(0x02C1, 2, 0x160A))
    SetScenaFlags(ScenaFlag(0x02C1, 3, 0x160B))
    SetScenaFlags(ScenaFlag(0x02C1, 4, 0x160C))
    SetScenaFlags(ScenaFlag(0x02C1, 5, 0x160D))
    SetScenaFlags(ScenaFlag(0x02C1, 6, 0x160E))
    SetScenaFlags(ScenaFlag(0x02C1, 7, 0x160F))
    SetScenaFlags(ScenaFlag(0x02C2, 0, 0x1610))
    SetScenaFlags(ScenaFlag(0x02C2, 1, 0x1611))
    SetScenaFlags(ScenaFlag(0x02C2, 2, 0x1612))
    SetScenaFlags(ScenaFlag(0x02C2, 4, 0x1614))
    SetScenaFlags(ScenaFlag(0x02C2, 5, 0x1615))
    SetScenaFlags(ScenaFlag(0x02C2, 6, 0x1616))
    SetScenaFlags(ScenaFlag(0x02C2, 7, 0x1617))
    SetScenaFlags(ScenaFlag(0x02C2, 3, 0x1613))
    SetScenaFlags(ScenaFlag(0x02C3, 0, 0x1618))
    SetScenaFlags(ScenaFlag(0x02C3, 1, 0x1619))
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C3, 2, 0x161A))
    SetScenaFlags(ScenaFlag(0x02C3, 3, 0x161B))
    SetScenaFlags(ScenaFlag(0x02C3, 4, 0x161C))
    SetScenaFlags(ScenaFlag(0x02C3, 5, 0x161D))
    SetScenaFlags(ScenaFlag(0x02C3, 7, 0x161F))
    SetScenaFlags(ScenaFlag(0x02C4, 0, 0x1620))
    SetScenaFlags(ScenaFlag(0x02C4, 1, 0x1621))
    SetScenaFlags(ScenaFlag(0x02C4, 2, 0x1622))
    SetScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    SetScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    SetScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    SetScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    SetScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    SetScenaFlags(ScenaFlag(0x02C5, 0, 0x1628))
    SetScenaFlags(ScenaFlag(0x02C5, 2, 0x162A))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C5, 3, 0x162B))
    SetScenaFlags(ScenaFlag(0x02C5, 4, 0x162C))
    SetScenaFlags(ScenaFlag(0x02C5, 5, 0x162D))
    SetScenaFlags(ScenaFlag(0x02C5, 6, 0x162E))
    SetScenaFlags(ScenaFlag(0x02C6, 0, 0x1630))
    SetScenaFlags(ScenaFlag(0x02C6, 1, 0x1631))
    SetScenaFlags(ScenaFlag(0x02C6, 2, 0x1632))
    SetScenaFlags(ScenaFlag(0x02C6, 3, 0x1633))
    SetScenaFlags(ScenaFlag(0x02C6, 4, 0x1634))
    SetScenaFlags(ScenaFlag(0x02C6, 5, 0x1635))
    SetScenaFlags(ScenaFlag(0x02C6, 6, 0x1636))
    SetScenaFlags(ScenaFlag(0x02C6, 7, 0x1637))
    SetScenaFlags(ScenaFlag(0x02C7, 0, 0x1638))
    SetScenaFlags(ScenaFlag(0x02C7, 1, 0x1639))
    SetScenaFlags(ScenaFlag(0x02C7, 2, 0x163A))
    SetScenaFlags(ScenaFlag(0x02C7, 3, 0x163B))
    SetScenaFlags(ScenaFlag(0x02C7, 4, 0x163C))
    SetScenaFlags(ScenaFlag(0x02C7, 5, 0x163D))
    SetScenaFlags(ScenaFlag(0x02C7, 6, 0x163E))

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

    SetScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T3100._SN', 110, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_245F(): pass

    label('loc_245F')

    SetScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    SetScenaFlags(ScenaFlag(0x02C0, 1, 0x1601))
    SetScenaFlags(ScenaFlag(0x02C0, 2, 0x1602))
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C0, 3, 0x1603))
    SetScenaFlags(ScenaFlag(0x02C0, 4, 0x1604))
    SetScenaFlags(ScenaFlag(0x02C0, 7, 0x1607))
    SetScenaFlags(ScenaFlag(0x02C0, 5, 0x1605))
    SetScenaFlags(ScenaFlag(0x02C0, 6, 0x1606))
    SetScenaFlags(ScenaFlag(0x02C1, 0, 0x1608))
    SetScenaFlags(ScenaFlag(0x02C1, 1, 0x1609))
    SetScenaFlags(ScenaFlag(0x02C1, 2, 0x160A))
    NewScene('ED6_DT21/T4106._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_249E(): pass

    label('loc_249E')

    SetScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    SetScenaFlags(ScenaFlag(0x02C0, 1, 0x1601))
    SetScenaFlags(ScenaFlag(0x02C0, 2, 0x1602))
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C0, 3, 0x1603))
    SetScenaFlags(ScenaFlag(0x02C0, 4, 0x1604))
    SetScenaFlags(ScenaFlag(0x02C0, 7, 0x1607))
    SetScenaFlags(ScenaFlag(0x02C0, 5, 0x1605))
    SetScenaFlags(ScenaFlag(0x02C0, 6, 0x1606))
    SetScenaFlags(ScenaFlag(0x02C1, 0, 0x1608))
    SetScenaFlags(ScenaFlag(0x02C1, 1, 0x1609))
    SetScenaFlags(ScenaFlag(0x02C1, 2, 0x160A))
    SetScenaFlags(ScenaFlag(0x02C1, 3, 0x160B))
    SetScenaFlags(ScenaFlag(0x02C1, 4, 0x160C))
    SetScenaFlags(ScenaFlag(0x02C1, 5, 0x160D))
    SetScenaFlags(ScenaFlag(0x02C1, 6, 0x160E))
    SetScenaFlags(ScenaFlag(0x02C1, 7, 0x160F))
    SetScenaFlags(ScenaFlag(0x02C2, 0, 0x1610))
    SetScenaFlags(ScenaFlag(0x02C2, 1, 0x1611))
    SetScenaFlags(ScenaFlag(0x02C2, 2, 0x1612))
    SetScenaFlags(ScenaFlag(0x02C2, 4, 0x1614))
    SetScenaFlags(ScenaFlag(0x02C2, 5, 0x1615))
    SetScenaFlags(ScenaFlag(0x02C2, 6, 0x1616))
    SetScenaFlags(ScenaFlag(0x02C2, 7, 0x1617))
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C2, 3, 0x1613))
    NewScene('ED6_DT21/R4100._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_2508(): pass

    label('loc_2508')

    SetScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    SetScenaFlags(ScenaFlag(0x02C0, 1, 0x1601))
    SetScenaFlags(ScenaFlag(0x02C0, 2, 0x1602))
    SetScenaFlags(ScenaFlag(0x02C0, 3, 0x1603))
    SetScenaFlags(ScenaFlag(0x02C0, 4, 0x1604))
    SetScenaFlags(ScenaFlag(0x02C0, 7, 0x1607))
    SetScenaFlags(ScenaFlag(0x02C0, 5, 0x1605))
    SetScenaFlags(ScenaFlag(0x02C0, 6, 0x1606))
    SetScenaFlags(ScenaFlag(0x02C1, 0, 0x1608))
    SetScenaFlags(ScenaFlag(0x02C1, 1, 0x1609))
    SetScenaFlags(ScenaFlag(0x02C1, 2, 0x160A))
    SetScenaFlags(ScenaFlag(0x02C1, 3, 0x160B))
    SetScenaFlags(ScenaFlag(0x02C1, 4, 0x160C))
    SetScenaFlags(ScenaFlag(0x02C1, 5, 0x160D))
    SetScenaFlags(ScenaFlag(0x02C1, 6, 0x160E))
    SetScenaFlags(ScenaFlag(0x02C1, 7, 0x160F))
    SetScenaFlags(ScenaFlag(0x02C2, 0, 0x1610))
    SetScenaFlags(ScenaFlag(0x02C2, 1, 0x1611))
    SetScenaFlags(ScenaFlag(0x02C2, 2, 0x1612))
    SetScenaFlags(ScenaFlag(0x02C2, 4, 0x1614))
    SetScenaFlags(ScenaFlag(0x02C2, 5, 0x1615))
    SetScenaFlags(ScenaFlag(0x02C2, 6, 0x1616))
    SetScenaFlags(ScenaFlag(0x02C2, 7, 0x1617))
    SetScenaFlags(ScenaFlag(0x02C2, 3, 0x1613))
    SetScenaFlags(ScenaFlag(0x02C3, 0, 0x1618))
    SetScenaFlags(ScenaFlag(0x02C3, 1, 0x1619))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C3, 2, 0x161A))
    SetScenaFlags(ScenaFlag(0x02C3, 3, 0x161B))
    SetScenaFlags(ScenaFlag(0x02C3, 4, 0x161C))
    SetScenaFlags(ScenaFlag(0x02C3, 5, 0x161D))
    SetScenaFlags(ScenaFlag(0x02C3, 7, 0x161F))
    SetScenaFlags(ScenaFlag(0x02C4, 0, 0x1620))
    SetScenaFlags(ScenaFlag(0x02C4, 1, 0x1621))
    SetScenaFlags(ScenaFlag(0x02C4, 2, 0x1622))
    SetScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    SetScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    SetScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    SetScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    SetScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    SetScenaFlags(ScenaFlag(0x02C5, 0, 0x1628))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/R1504._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_25A1(): pass

    label('loc_25A1')

    SetScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    SetScenaFlags(ScenaFlag(0x02C0, 1, 0x1601))
    SetScenaFlags(ScenaFlag(0x02C0, 2, 0x1602))
    SetScenaFlags(ScenaFlag(0x02C0, 3, 0x1603))
    SetScenaFlags(ScenaFlag(0x02C0, 4, 0x1604))
    SetScenaFlags(ScenaFlag(0x02C0, 7, 0x1607))
    SetScenaFlags(ScenaFlag(0x02C0, 5, 0x1605))
    SetScenaFlags(ScenaFlag(0x02C0, 6, 0x1606))
    SetScenaFlags(ScenaFlag(0x02C1, 0, 0x1608))
    SetScenaFlags(ScenaFlag(0x02C1, 1, 0x1609))
    SetScenaFlags(ScenaFlag(0x02C1, 2, 0x160A))
    SetScenaFlags(ScenaFlag(0x02C1, 3, 0x160B))
    SetScenaFlags(ScenaFlag(0x02C1, 4, 0x160C))
    SetScenaFlags(ScenaFlag(0x02C1, 5, 0x160D))
    SetScenaFlags(ScenaFlag(0x02C1, 6, 0x160E))
    SetScenaFlags(ScenaFlag(0x02C1, 7, 0x160F))
    SetScenaFlags(ScenaFlag(0x02C2, 0, 0x1610))
    SetScenaFlags(ScenaFlag(0x02C2, 1, 0x1611))
    SetScenaFlags(ScenaFlag(0x02C2, 2, 0x1612))
    SetScenaFlags(ScenaFlag(0x02C2, 4, 0x1614))
    SetScenaFlags(ScenaFlag(0x02C2, 5, 0x1615))
    SetScenaFlags(ScenaFlag(0x02C2, 6, 0x1616))
    SetScenaFlags(ScenaFlag(0x02C2, 7, 0x1617))
    SetScenaFlags(ScenaFlag(0x02C2, 3, 0x1613))
    SetScenaFlags(ScenaFlag(0x02C3, 0, 0x1618))
    SetScenaFlags(ScenaFlag(0x02C3, 1, 0x1619))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C3, 2, 0x161A))
    SetScenaFlags(ScenaFlag(0x02C3, 3, 0x161B))
    SetScenaFlags(ScenaFlag(0x02C3, 4, 0x161C))
    SetScenaFlags(ScenaFlag(0x02C3, 5, 0x161D))
    SetScenaFlags(ScenaFlag(0x02C3, 7, 0x161F))
    SetScenaFlags(ScenaFlag(0x02C4, 0, 0x1620))
    SetScenaFlags(ScenaFlag(0x02C4, 1, 0x1621))
    SetScenaFlags(ScenaFlag(0x02C4, 2, 0x1622))
    SetScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    SetScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    SetScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    SetScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    SetScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    SetScenaFlags(ScenaFlag(0x02C5, 0, 0x1628))
    FormationDelMember(0x00, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T4302._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_2641(): pass

    label('loc_2641')

    SetScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    SetScenaFlags(ScenaFlag(0x02C0, 1, 0x1601))
    SetScenaFlags(ScenaFlag(0x02C0, 2, 0x1602))
    SetScenaFlags(ScenaFlag(0x02C0, 3, 0x1603))
    SetScenaFlags(ScenaFlag(0x02C0, 4, 0x1604))
    SetScenaFlags(ScenaFlag(0x02C0, 7, 0x1607))
    SetScenaFlags(ScenaFlag(0x02C0, 5, 0x1605))
    SetScenaFlags(ScenaFlag(0x02C0, 6, 0x1606))
    SetScenaFlags(ScenaFlag(0x02C1, 0, 0x1608))
    SetScenaFlags(ScenaFlag(0x02C1, 1, 0x1609))
    SetScenaFlags(ScenaFlag(0x02C1, 2, 0x160A))
    SetScenaFlags(ScenaFlag(0x02C1, 3, 0x160B))
    SetScenaFlags(ScenaFlag(0x02C1, 4, 0x160C))
    SetScenaFlags(ScenaFlag(0x02C1, 5, 0x160D))
    SetScenaFlags(ScenaFlag(0x02C1, 6, 0x160E))
    SetScenaFlags(ScenaFlag(0x02C1, 7, 0x160F))
    SetScenaFlags(ScenaFlag(0x02C2, 0, 0x1610))
    SetScenaFlags(ScenaFlag(0x02C2, 1, 0x1611))
    SetScenaFlags(ScenaFlag(0x02C2, 2, 0x1612))
    SetScenaFlags(ScenaFlag(0x02C2, 4, 0x1614))
    SetScenaFlags(ScenaFlag(0x02C2, 5, 0x1615))
    SetScenaFlags(ScenaFlag(0x02C2, 6, 0x1616))
    SetScenaFlags(ScenaFlag(0x02C2, 7, 0x1617))
    SetScenaFlags(ScenaFlag(0x02C2, 3, 0x1613))
    SetScenaFlags(ScenaFlag(0x02C3, 0, 0x1618))
    SetScenaFlags(ScenaFlag(0x02C3, 1, 0x1619))
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C3, 2, 0x161A))
    SetScenaFlags(ScenaFlag(0x02C3, 3, 0x161B))
    SetScenaFlags(ScenaFlag(0x02C3, 4, 0x161C))
    SetScenaFlags(ScenaFlag(0x02C3, 5, 0x161D))
    SetScenaFlags(ScenaFlag(0x02C3, 7, 0x161F))
    SetScenaFlags(ScenaFlag(0x02C4, 0, 0x1620))
    SetScenaFlags(ScenaFlag(0x02C4, 1, 0x1621))
    SetScenaFlags(ScenaFlag(0x02C4, 2, 0x1622))
    SetScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    SetScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    SetScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    SetScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    SetScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    SetScenaFlags(ScenaFlag(0x02C5, 0, 0x1628))
    SetScenaFlags(ScenaFlag(0x02C5, 2, 0x162A))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C5, 3, 0x162B))
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C5, 4, 0x162C))
    SetScenaFlags(ScenaFlag(0x02C5, 5, 0x162D))
    NewScene('ED6_DT21/T4101._SN', 108, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_26E7(): pass

    label('loc_26E7')

    SetScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    SetScenaFlags(ScenaFlag(0x02C0, 1, 0x1601))
    SetScenaFlags(ScenaFlag(0x02C0, 2, 0x1602))
    SetScenaFlags(ScenaFlag(0x02C0, 3, 0x1603))
    SetScenaFlags(ScenaFlag(0x02C0, 4, 0x1604))
    SetScenaFlags(ScenaFlag(0x02C0, 7, 0x1607))
    SetScenaFlags(ScenaFlag(0x02C0, 5, 0x1605))
    SetScenaFlags(ScenaFlag(0x02C0, 6, 0x1606))
    SetScenaFlags(ScenaFlag(0x02C1, 0, 0x1608))
    SetScenaFlags(ScenaFlag(0x02C1, 1, 0x1609))
    SetScenaFlags(ScenaFlag(0x02C1, 2, 0x160A))
    SetScenaFlags(ScenaFlag(0x02C1, 3, 0x160B))
    SetScenaFlags(ScenaFlag(0x02C1, 4, 0x160C))
    SetScenaFlags(ScenaFlag(0x02C1, 5, 0x160D))
    SetScenaFlags(ScenaFlag(0x02C1, 6, 0x160E))
    SetScenaFlags(ScenaFlag(0x02C1, 7, 0x160F))
    SetScenaFlags(ScenaFlag(0x02C2, 0, 0x1610))
    SetScenaFlags(ScenaFlag(0x02C2, 1, 0x1611))
    SetScenaFlags(ScenaFlag(0x02C2, 2, 0x1612))
    SetScenaFlags(ScenaFlag(0x02C2, 4, 0x1614))
    SetScenaFlags(ScenaFlag(0x02C2, 5, 0x1615))
    SetScenaFlags(ScenaFlag(0x02C2, 6, 0x1616))
    SetScenaFlags(ScenaFlag(0x02C2, 7, 0x1617))
    SetScenaFlags(ScenaFlag(0x02C2, 3, 0x1613))
    SetScenaFlags(ScenaFlag(0x02C3, 0, 0x1618))
    SetScenaFlags(ScenaFlag(0x02C3, 1, 0x1619))
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C3, 2, 0x161A))
    SetScenaFlags(ScenaFlag(0x02C3, 3, 0x161B))
    SetScenaFlags(ScenaFlag(0x02C3, 4, 0x161C))
    SetScenaFlags(ScenaFlag(0x02C3, 5, 0x161D))
    SetScenaFlags(ScenaFlag(0x02C3, 7, 0x161F))
    SetScenaFlags(ScenaFlag(0x02C4, 0, 0x1620))
    SetScenaFlags(ScenaFlag(0x02C4, 1, 0x1621))
    SetScenaFlags(ScenaFlag(0x02C4, 2, 0x1622))
    SetScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    SetScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    SetScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    SetScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    SetScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    SetScenaFlags(ScenaFlag(0x02C5, 0, 0x1628))
    SetScenaFlags(ScenaFlag(0x02C5, 2, 0x162A))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C5, 3, 0x162B))
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C5, 4, 0x162C))
    SetScenaFlags(ScenaFlag(0x02C5, 5, 0x162D))
    SetScenaFlags(ScenaFlag(0x02C5, 6, 0x162E))
    SetScenaFlags(ScenaFlag(0x02C6, 0, 0x1630))
    SetScenaFlags(ScenaFlag(0x02C6, 1, 0x1631))
    SetScenaFlags(ScenaFlag(0x02C6, 2, 0x1632))
    SetScenaFlags(ScenaFlag(0x02C6, 3, 0x1633))
    SetScenaFlags(ScenaFlag(0x02C6, 4, 0x1634))
    SetScenaFlags(ScenaFlag(0x02C6, 5, 0x1635))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C6, 6, 0x1636))
    NewScene('ED6_DT21/T0600._SN', 107, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_27B4(): pass

    label('loc_27B4')

    SetScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    SetScenaFlags(ScenaFlag(0x02C0, 1, 0x1601))
    SetScenaFlags(ScenaFlag(0x02C0, 2, 0x1602))
    SetScenaFlags(ScenaFlag(0x02C0, 3, 0x1603))
    SetScenaFlags(ScenaFlag(0x02C0, 4, 0x1604))
    SetScenaFlags(ScenaFlag(0x02C0, 7, 0x1607))
    SetScenaFlags(ScenaFlag(0x02C0, 5, 0x1605))
    SetScenaFlags(ScenaFlag(0x02C0, 6, 0x1606))
    SetScenaFlags(ScenaFlag(0x02C1, 0, 0x1608))
    SetScenaFlags(ScenaFlag(0x02C1, 1, 0x1609))
    SetScenaFlags(ScenaFlag(0x02C1, 2, 0x160A))
    SetScenaFlags(ScenaFlag(0x02C1, 3, 0x160B))
    SetScenaFlags(ScenaFlag(0x02C1, 4, 0x160C))
    SetScenaFlags(ScenaFlag(0x02C1, 5, 0x160D))
    SetScenaFlags(ScenaFlag(0x02C1, 6, 0x160E))
    SetScenaFlags(ScenaFlag(0x02C1, 7, 0x160F))
    SetScenaFlags(ScenaFlag(0x02C2, 0, 0x1610))
    SetScenaFlags(ScenaFlag(0x02C2, 1, 0x1611))
    SetScenaFlags(ScenaFlag(0x02C2, 2, 0x1612))
    SetScenaFlags(ScenaFlag(0x02C2, 4, 0x1614))
    SetScenaFlags(ScenaFlag(0x02C2, 5, 0x1615))
    SetScenaFlags(ScenaFlag(0x02C2, 6, 0x1616))
    SetScenaFlags(ScenaFlag(0x02C2, 7, 0x1617))
    SetScenaFlags(ScenaFlag(0x02C2, 3, 0x1613))
    SetScenaFlags(ScenaFlag(0x02C3, 0, 0x1618))
    SetScenaFlags(ScenaFlag(0x02C3, 1, 0x1619))
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C3, 2, 0x161A))
    SetScenaFlags(ScenaFlag(0x02C3, 3, 0x161B))
    SetScenaFlags(ScenaFlag(0x02C3, 4, 0x161C))
    SetScenaFlags(ScenaFlag(0x02C3, 5, 0x161D))
    SetScenaFlags(ScenaFlag(0x02C3, 7, 0x161F))
    SetScenaFlags(ScenaFlag(0x02C4, 0, 0x1620))
    SetScenaFlags(ScenaFlag(0x02C4, 1, 0x1621))
    SetScenaFlags(ScenaFlag(0x02C4, 2, 0x1622))
    SetScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    SetScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    SetScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    SetScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    SetScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    SetScenaFlags(ScenaFlag(0x02C5, 0, 0x1628))
    SetScenaFlags(ScenaFlag(0x02C5, 2, 0x162A))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C5, 3, 0x162B))
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C5, 4, 0x162C))
    SetScenaFlags(ScenaFlag(0x02C5, 5, 0x162D))
    SetScenaFlags(ScenaFlag(0x02C5, 6, 0x162E))
    SetScenaFlags(ScenaFlag(0x02C6, 0, 0x1630))
    SetScenaFlags(ScenaFlag(0x02C6, 1, 0x1631))
    SetScenaFlags(ScenaFlag(0x02C6, 2, 0x1632))
    SetScenaFlags(ScenaFlag(0x02C6, 3, 0x1633))
    SetScenaFlags(ScenaFlag(0x02C6, 4, 0x1634))
    SetScenaFlags(ScenaFlag(0x02C6, 5, 0x1635))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C6, 6, 0x1636))
    SetScenaFlags(ScenaFlag(0x02C6, 7, 0x1637))
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C7, 0, 0x1638))
    NewScene('ED6_DT21/T4150._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_288B(): pass

    label('loc_288B')

    SetScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    SetScenaFlags(ScenaFlag(0x02C0, 1, 0x1601))
    SetScenaFlags(ScenaFlag(0x02C0, 2, 0x1602))
    SetScenaFlags(ScenaFlag(0x02C0, 3, 0x1603))
    SetScenaFlags(ScenaFlag(0x02C0, 4, 0x1604))
    SetScenaFlags(ScenaFlag(0x02C0, 7, 0x1607))
    SetScenaFlags(ScenaFlag(0x02C0, 5, 0x1605))
    SetScenaFlags(ScenaFlag(0x02C0, 6, 0x1606))
    SetScenaFlags(ScenaFlag(0x02C1, 0, 0x1608))
    SetScenaFlags(ScenaFlag(0x02C1, 1, 0x1609))
    SetScenaFlags(ScenaFlag(0x02C1, 2, 0x160A))
    SetScenaFlags(ScenaFlag(0x02C1, 3, 0x160B))
    SetScenaFlags(ScenaFlag(0x02C1, 4, 0x160C))
    SetScenaFlags(ScenaFlag(0x02C1, 5, 0x160D))
    SetScenaFlags(ScenaFlag(0x02C1, 6, 0x160E))
    SetScenaFlags(ScenaFlag(0x02C1, 7, 0x160F))
    SetScenaFlags(ScenaFlag(0x02C2, 0, 0x1610))
    SetScenaFlags(ScenaFlag(0x02C2, 1, 0x1611))
    SetScenaFlags(ScenaFlag(0x02C2, 2, 0x1612))
    SetScenaFlags(ScenaFlag(0x02C2, 4, 0x1614))
    SetScenaFlags(ScenaFlag(0x02C2, 5, 0x1615))
    SetScenaFlags(ScenaFlag(0x02C2, 6, 0x1616))
    SetScenaFlags(ScenaFlag(0x02C2, 7, 0x1617))
    SetScenaFlags(ScenaFlag(0x02C2, 3, 0x1613))
    SetScenaFlags(ScenaFlag(0x02C3, 0, 0x1618))
    SetScenaFlags(ScenaFlag(0x02C3, 1, 0x1619))
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C3, 2, 0x161A))
    SetScenaFlags(ScenaFlag(0x02C3, 3, 0x161B))
    SetScenaFlags(ScenaFlag(0x02C3, 4, 0x161C))
    SetScenaFlags(ScenaFlag(0x02C3, 5, 0x161D))
    SetScenaFlags(ScenaFlag(0x02C3, 7, 0x161F))
    SetScenaFlags(ScenaFlag(0x02C4, 0, 0x1620))
    SetScenaFlags(ScenaFlag(0x02C4, 1, 0x1621))
    SetScenaFlags(ScenaFlag(0x02C4, 2, 0x1622))
    SetScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    SetScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    SetScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    SetScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    SetScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    SetScenaFlags(ScenaFlag(0x02C5, 0, 0x1628))
    SetScenaFlags(ScenaFlag(0x02C5, 2, 0x162A))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C5, 3, 0x162B))
    SetScenaFlags(ScenaFlag(0x02C5, 4, 0x162C))
    SetScenaFlags(ScenaFlag(0x02C5, 5, 0x162D))
    SetScenaFlags(ScenaFlag(0x02C5, 6, 0x162E))
    SetScenaFlags(ScenaFlag(0x02C6, 0, 0x1630))
    SetScenaFlags(ScenaFlag(0x02C6, 1, 0x1631))
    SetScenaFlags(ScenaFlag(0x02C6, 2, 0x1632))
    SetScenaFlags(ScenaFlag(0x02C6, 3, 0x1633))
    SetScenaFlags(ScenaFlag(0x02C6, 4, 0x1634))
    SetScenaFlags(ScenaFlag(0x02C6, 5, 0x1635))
    SetScenaFlags(ScenaFlag(0x02C6, 6, 0x1636))
    SetScenaFlags(ScenaFlag(0x02C6, 7, 0x1637))
    SetScenaFlags(ScenaFlag(0x02C7, 0, 0x1638))
    SetScenaFlags(ScenaFlag(0x02C7, 1, 0x1639))
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C7, 2, 0x163A))
    SetScenaFlags(ScenaFlag(0x02C7, 3, 0x163B))
    SetScenaFlags(ScenaFlag(0x02C7, 4, 0x163C))
    FormationAddMember(ChrTable['尤莉亚上尉'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T4313._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2A46')

    def _loc_2962(): pass

    label('loc_2962')

    SetScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    SetScenaFlags(ScenaFlag(0x02C0, 1, 0x1601))
    SetScenaFlags(ScenaFlag(0x02C0, 2, 0x1602))
    SetScenaFlags(ScenaFlag(0x02C0, 3, 0x1603))
    SetScenaFlags(ScenaFlag(0x02C0, 4, 0x1604))
    SetScenaFlags(ScenaFlag(0x02C0, 7, 0x1607))
    SetScenaFlags(ScenaFlag(0x02C0, 5, 0x1605))
    SetScenaFlags(ScenaFlag(0x02C0, 6, 0x1606))
    SetScenaFlags(ScenaFlag(0x02C1, 0, 0x1608))
    SetScenaFlags(ScenaFlag(0x02C1, 1, 0x1609))
    SetScenaFlags(ScenaFlag(0x02C1, 2, 0x160A))
    SetScenaFlags(ScenaFlag(0x02C1, 3, 0x160B))
    SetScenaFlags(ScenaFlag(0x02C1, 4, 0x160C))
    SetScenaFlags(ScenaFlag(0x02C1, 5, 0x160D))
    SetScenaFlags(ScenaFlag(0x02C1, 6, 0x160E))
    SetScenaFlags(ScenaFlag(0x02C1, 7, 0x160F))
    SetScenaFlags(ScenaFlag(0x02C2, 0, 0x1610))
    SetScenaFlags(ScenaFlag(0x02C2, 1, 0x1611))
    SetScenaFlags(ScenaFlag(0x02C2, 2, 0x1612))
    SetScenaFlags(ScenaFlag(0x02C2, 4, 0x1614))
    SetScenaFlags(ScenaFlag(0x02C2, 5, 0x1615))
    SetScenaFlags(ScenaFlag(0x02C2, 6, 0x1616))
    SetScenaFlags(ScenaFlag(0x02C2, 7, 0x1617))
    SetScenaFlags(ScenaFlag(0x02C2, 3, 0x1613))
    SetScenaFlags(ScenaFlag(0x02C3, 0, 0x1618))
    SetScenaFlags(ScenaFlag(0x02C3, 1, 0x1619))
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C3, 2, 0x161A))
    SetScenaFlags(ScenaFlag(0x02C3, 3, 0x161B))
    SetScenaFlags(ScenaFlag(0x02C3, 4, 0x161C))
    SetScenaFlags(ScenaFlag(0x02C3, 5, 0x161D))
    SetScenaFlags(ScenaFlag(0x02C3, 7, 0x161F))
    SetScenaFlags(ScenaFlag(0x02C4, 0, 0x1620))
    SetScenaFlags(ScenaFlag(0x02C4, 1, 0x1621))
    SetScenaFlags(ScenaFlag(0x02C4, 2, 0x1622))
    SetScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    SetScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    SetScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    SetScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    SetScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    SetScenaFlags(ScenaFlag(0x02C5, 0, 0x1628))
    SetScenaFlags(ScenaFlag(0x02C5, 2, 0x162A))
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C5, 3, 0x162B))
    SetScenaFlags(ScenaFlag(0x02C5, 4, 0x162C))
    SetScenaFlags(ScenaFlag(0x02C5, 5, 0x162D))
    SetScenaFlags(ScenaFlag(0x02C5, 6, 0x162E))
    SetScenaFlags(ScenaFlag(0x02C6, 0, 0x1630))
    SetScenaFlags(ScenaFlag(0x02C6, 1, 0x1631))
    SetScenaFlags(ScenaFlag(0x02C6, 2, 0x1632))
    SetScenaFlags(ScenaFlag(0x02C6, 3, 0x1633))
    SetScenaFlags(ScenaFlag(0x02C6, 4, 0x1634))
    SetScenaFlags(ScenaFlag(0x02C6, 5, 0x1635))
    SetScenaFlags(ScenaFlag(0x02C6, 6, 0x1636))
    SetScenaFlags(ScenaFlag(0x02C6, 7, 0x1637))
    SetScenaFlags(ScenaFlag(0x02C7, 0, 0x1638))
    SetScenaFlags(ScenaFlag(0x02C7, 1, 0x1639))
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    SetScenaFlags(ScenaFlag(0x02C7, 2, 0x163A))
    SetScenaFlags(ScenaFlag(0x02C7, 3, 0x163B))
    SetScenaFlags(ScenaFlag(0x02C7, 4, 0x163C))
    FormationAddMember(ChrTable['尤莉亚上尉'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
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
    ClearScenaFlags(ScenaFlag(0x0300, 0, 0x1800))
    ClearScenaFlags(ScenaFlag(0x0300, 1, 0x1801))
    ClearScenaFlags(ScenaFlag(0x0300, 2, 0x1802))
    ClearScenaFlags(ScenaFlag(0x0300, 3, 0x1803))
    ClearScenaFlags(ScenaFlag(0x0300, 4, 0x1804))
    ClearScenaFlags(ScenaFlag(0x0300, 5, 0x1805))
    ClearScenaFlags(ScenaFlag(0x0300, 6, 0x1806))
    ClearScenaFlags(ScenaFlag(0x0300, 7, 0x1807))
    ClearScenaFlags(ScenaFlag(0x0301, 0, 0x1808))
    ClearScenaFlags(ScenaFlag(0x0301, 1, 0x1809))
    ClearScenaFlags(ScenaFlag(0x0301, 2, 0x180A))
    ClearScenaFlags(ScenaFlag(0x0301, 3, 0x180B))
    ClearScenaFlags(ScenaFlag(0x0301, 4, 0x180C))
    ClearScenaFlags(ScenaFlag(0x0301, 5, 0x180D))
    ClearScenaFlags(ScenaFlag(0x0301, 6, 0x180E))
    ClearScenaFlags(ScenaFlag(0x0301, 7, 0x180F))
    ClearScenaFlags(ScenaFlag(0x0302, 0, 0x1810))
    ClearScenaFlags(ScenaFlag(0x0302, 1, 0x1811))
    ClearScenaFlags(ScenaFlag(0x0302, 2, 0x1812))
    ClearScenaFlags(ScenaFlag(0x0302, 3, 0x1813))
    ClearScenaFlags(ScenaFlag(0x0302, 4, 0x1814))
    ClearScenaFlags(ScenaFlag(0x0302, 5, 0x1815))
    ClearScenaFlags(ScenaFlag(0x0302, 6, 0x1816))
    ClearScenaFlags(ScenaFlag(0x0302, 7, 0x1817))
    ClearScenaFlags(ScenaFlag(0x0303, 0, 0x1818))
    ClearScenaFlags(ScenaFlag(0x0303, 1, 0x1819))
    ClearScenaFlags(ScenaFlag(0x0303, 2, 0x181A))
    ClearScenaFlags(ScenaFlag(0x0303, 3, 0x181B))
    ClearScenaFlags(ScenaFlag(0x0303, 4, 0x181C))
    ClearScenaFlags(ScenaFlag(0x0303, 5, 0x181D))
    ClearScenaFlags(ScenaFlag(0x0303, 6, 0x181E))
    ClearScenaFlags(ScenaFlag(0x0303, 7, 0x181F))
    ClearScenaFlags(ScenaFlag(0x0304, 0, 0x1820))
    ClearScenaFlags(ScenaFlag(0x0304, 1, 0x1821))
    ClearScenaFlags(ScenaFlag(0x0304, 2, 0x1822))
    ClearScenaFlags(ScenaFlag(0x0304, 3, 0x1823))
    ClearScenaFlags(ScenaFlag(0x0304, 4, 0x1824))
    ClearScenaFlags(ScenaFlag(0x0304, 5, 0x1825))
    ClearScenaFlags(ScenaFlag(0x0304, 6, 0x1826))
    ClearScenaFlags(ScenaFlag(0x0304, 7, 0x1827))
    ClearScenaFlags(ScenaFlag(0x0305, 0, 0x1828))
    ClearScenaFlags(ScenaFlag(0x0305, 1, 0x1829))
    ClearScenaFlags(ScenaFlag(0x0305, 2, 0x182A))
    ClearScenaFlags(ScenaFlag(0x0305, 3, 0x182B))
    ClearScenaFlags(ScenaFlag(0x0305, 4, 0x182C))
    ClearScenaFlags(ScenaFlag(0x0305, 5, 0x182D))
    ClearScenaFlags(ScenaFlag(0x0305, 6, 0x182E))
    ClearScenaFlags(ScenaFlag(0x0305, 7, 0x182F))
    ClearScenaFlags(ScenaFlag(0x0306, 0, 0x1830))
    ClearScenaFlags(ScenaFlag(0x0306, 1, 0x1831))
    ClearScenaFlags(ScenaFlag(0x0306, 2, 0x1832))
    ClearScenaFlags(ScenaFlag(0x0306, 3, 0x1833))
    ClearScenaFlags(ScenaFlag(0x0306, 4, 0x1834))
    ClearScenaFlags(ScenaFlag(0x0306, 5, 0x1835))
    ClearScenaFlags(ScenaFlag(0x0306, 6, 0x1836))
    ClearScenaFlags(ScenaFlag(0x0306, 7, 0x1837))
    ClearScenaFlags(ScenaFlag(0x0307, 0, 0x1838))
    ClearScenaFlags(ScenaFlag(0x0307, 1, 0x1839))
    ClearScenaFlags(ScenaFlag(0x0307, 2, 0x183A))
    ClearScenaFlags(ScenaFlag(0x0307, 3, 0x183B))
    ClearScenaFlags(ScenaFlag(0x0307, 4, 0x183C))
    ClearScenaFlags(ScenaFlag(0x0307, 5, 0x183D))
    ClearScenaFlags(ScenaFlag(0x0307, 6, 0x183E))
    ClearScenaFlags(ScenaFlag(0x0307, 7, 0x183F))
    ClearScenaFlags(ScenaFlag(0x0308, 0, 0x1840))
    ClearScenaFlags(ScenaFlag(0x0310, 0, 0x1880))
    ClearScenaFlags(ScenaFlag(0x0310, 1, 0x1881))
    ClearScenaFlags(ScenaFlag(0x0310, 2, 0x1882))
    ClearScenaFlags(ScenaFlag(0x0310, 3, 0x1883))
    ClearScenaFlags(ScenaFlag(0x0310, 5, 0x1885))
    ClearScenaFlags(ScenaFlag(0x0310, 6, 0x1886))

    Return()

# id: 0x0010 offset: 0x2B43
@scena.Code('func_10_2B43')
def func_10_2B43():
    SetScenaFlags(ScenaFlag(0x0300, 0, 0x1800))
    SetScenaFlags(ScenaFlag(0x0300, 1, 0x1801))
    SetScenaFlags(ScenaFlag(0x0300, 2, 0x1802))
    SetScenaFlags(ScenaFlag(0x0300, 3, 0x1803))
    SetScenaFlags(ScenaFlag(0x0300, 4, 0x1804))
    SetScenaFlags(ScenaFlag(0x0300, 5, 0x1805))
    SetScenaFlags(ScenaFlag(0x0300, 6, 0x1806))
    SetScenaFlags(ScenaFlag(0x0300, 7, 0x1807))
    SetScenaFlags(ScenaFlag(0x0301, 0, 0x1808))
    SetScenaFlags(ScenaFlag(0x0301, 1, 0x1809))
    SetScenaFlags(ScenaFlag(0x0301, 2, 0x180A))
    SetScenaFlags(ScenaFlag(0x0301, 3, 0x180B))
    SetScenaFlags(ScenaFlag(0x0301, 4, 0x180C))
    SetScenaFlags(ScenaFlag(0x0301, 5, 0x180D))
    SetScenaFlags(ScenaFlag(0x0301, 6, 0x180E))
    SetScenaFlags(ScenaFlag(0x0301, 7, 0x180F))
    SetScenaFlags(ScenaFlag(0x0302, 0, 0x1810))
    SetScenaFlags(ScenaFlag(0x0302, 1, 0x1811))
    SetScenaFlags(ScenaFlag(0x0302, 2, 0x1812))
    SetScenaFlags(ScenaFlag(0x0302, 3, 0x1813))
    SetScenaFlags(ScenaFlag(0x0302, 4, 0x1814))
    SetScenaFlags(ScenaFlag(0x0302, 5, 0x1815))
    SetScenaFlags(ScenaFlag(0x0302, 6, 0x1816))
    OP_BB(0x00, 0x01, 0x00000043)
    SetScenaFlags(ScenaFlag(0x0302, 7, 0x1817))
    SetScenaFlags(ScenaFlag(0x0303, 0, 0x1818))
    SetScenaFlags(ScenaFlag(0x0303, 1, 0x1819))
    SetScenaFlags(ScenaFlag(0x0303, 2, 0x181A))
    SetScenaFlags(ScenaFlag(0x0303, 3, 0x181B))
    OP_BB(0x00, 0x01, 0x00000000)
    SetScenaFlags(ScenaFlag(0x0303, 4, 0x181C))
    SetScenaFlags(ScenaFlag(0x0303, 5, 0x181D))
    SetScenaFlags(ScenaFlag(0x0303, 6, 0x181E))
    SetScenaFlags(ScenaFlag(0x0303, 7, 0x181F))
    SetScenaFlags(ScenaFlag(0x0304, 0, 0x1820))
    SetScenaFlags(ScenaFlag(0x0304, 1, 0x1821))
    SetScenaFlags(ScenaFlag(0x0304, 2, 0x1822))
    SetScenaFlags(ScenaFlag(0x0304, 3, 0x1823))
    SetScenaFlags(ScenaFlag(0x0304, 4, 0x1824))
    SetScenaFlags(ScenaFlag(0x0304, 5, 0x1825))
    SetScenaFlags(ScenaFlag(0x0304, 6, 0x1826))

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0304, 7, 0x1827))
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

    SetScenaFlags(ScenaFlag(0x0305, 0, 0x1828))
    SetScenaFlags(ScenaFlag(0x0306, 3, 0x1833))
    OP_BB(0x00, 0x01, 0x00000044)
    SetScenaFlags(ScenaFlag(0x0306, 4, 0x1834))
    SetScenaFlags(ScenaFlag(0x0306, 5, 0x1835))
    SetScenaFlags(ScenaFlag(0x0306, 6, 0x1836))
    SetScenaFlags(ScenaFlag(0x0306, 7, 0x1837))
    SetScenaFlags(ScenaFlag(0x0307, 0, 0x1838))
    AddItem(ItemTable['储物室钥匙'], 1)
    SetScenaFlags(ScenaFlag(0x0307, 1, 0x1839))
    SetScenaFlags(ScenaFlag(0x0307, 2, 0x183A))
    AddItem(ItemTable['口琴'], 1)
    SetScenaFlags(ScenaFlag(0x0307, 3, 0x183B))
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

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
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
    SetScenaFlags(ScenaFlag(0x0300, 0, 0x1800))
    SetScenaFlags(ScenaFlag(0x0300, 1, 0x1801))
    SetScenaFlags(ScenaFlag(0x0300, 2, 0x1802))
    SetScenaFlags(ScenaFlag(0x0300, 3, 0x1803))
    SetScenaFlags(ScenaFlag(0x0300, 4, 0x1804))
    SetScenaFlags(ScenaFlag(0x0300, 5, 0x1805))
    NewScene('ED6_DT21/E0001._SN', 104, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_2D7D(): pass

    label('loc_2D7D')

    FormationReset()
    SetScenaFlags(ScenaFlag(0x0300, 0, 0x1800))
    SetScenaFlags(ScenaFlag(0x0300, 1, 0x1801))
    SetScenaFlags(ScenaFlag(0x0300, 2, 0x1802))
    SetScenaFlags(ScenaFlag(0x0300, 3, 0x1803))
    SetScenaFlags(ScenaFlag(0x0300, 4, 0x1804))
    SetScenaFlags(ScenaFlag(0x0300, 5, 0x1805))
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x0300, 6, 0x1806))
    SetScenaFlags(ScenaFlag(0x0300, 7, 0x1807))
    SetScenaFlags(ScenaFlag(0x0301, 0, 0x1808))
    SetScenaFlags(ScenaFlag(0x0301, 1, 0x1809))
    SetScenaFlags(ScenaFlag(0x0301, 2, 0x180A))
    SetScenaFlags(ScenaFlag(0x0301, 3, 0x180B))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T0121._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_2DB5(): pass

    label('loc_2DB5')

    FormationReset()
    SetScenaFlags(ScenaFlag(0x0300, 0, 0x1800))
    SetScenaFlags(ScenaFlag(0x0300, 1, 0x1801))
    SetScenaFlags(ScenaFlag(0x0300, 2, 0x1802))
    SetScenaFlags(ScenaFlag(0x0300, 3, 0x1803))
    SetScenaFlags(ScenaFlag(0x0300, 4, 0x1804))
    SetScenaFlags(ScenaFlag(0x0300, 5, 0x1805))
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x0300, 6, 0x1806))
    SetScenaFlags(ScenaFlag(0x0300, 7, 0x1807))
    SetScenaFlags(ScenaFlag(0x0301, 0, 0x1808))
    SetScenaFlags(ScenaFlag(0x0301, 1, 0x1809))
    SetScenaFlags(ScenaFlag(0x0301, 2, 0x180A))
    SetScenaFlags(ScenaFlag(0x0301, 3, 0x180B))
    SetScenaFlags(ScenaFlag(0x0301, 4, 0x180C))
    SetScenaFlags(ScenaFlag(0x0301, 5, 0x180D))
    SetScenaFlags(ScenaFlag(0x0301, 6, 0x180E))
    SetScenaFlags(ScenaFlag(0x0301, 7, 0x180F))
    SetScenaFlags(ScenaFlag(0x0302, 0, 0x1810))
    SetScenaFlags(ScenaFlag(0x0302, 1, 0x1811))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T0121._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_2DFF(): pass

    label('loc_2DFF')

    FormationReset()
    SetScenaFlags(ScenaFlag(0x0300, 0, 0x1800))
    SetScenaFlags(ScenaFlag(0x0300, 1, 0x1801))
    SetScenaFlags(ScenaFlag(0x0300, 2, 0x1802))
    SetScenaFlags(ScenaFlag(0x0300, 3, 0x1803))
    SetScenaFlags(ScenaFlag(0x0300, 4, 0x1804))
    SetScenaFlags(ScenaFlag(0x0300, 5, 0x1805))
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x0300, 6, 0x1806))
    SetScenaFlags(ScenaFlag(0x0300, 7, 0x1807))
    SetScenaFlags(ScenaFlag(0x0301, 0, 0x1808))
    SetScenaFlags(ScenaFlag(0x0301, 1, 0x1809))
    SetScenaFlags(ScenaFlag(0x0301, 2, 0x180A))
    SetScenaFlags(ScenaFlag(0x0301, 3, 0x180B))
    SetScenaFlags(ScenaFlag(0x0301, 4, 0x180C))
    SetScenaFlags(ScenaFlag(0x0301, 5, 0x180D))
    SetScenaFlags(ScenaFlag(0x0301, 6, 0x180E))
    SetScenaFlags(ScenaFlag(0x0301, 7, 0x180F))
    SetScenaFlags(ScenaFlag(0x0302, 0, 0x1810))
    SetScenaFlags(ScenaFlag(0x0302, 1, 0x1811))
    SetScenaFlags(ScenaFlag(0x0302, 2, 0x1812))
    SetScenaFlags(ScenaFlag(0x0302, 3, 0x1813))
    SetScenaFlags(ScenaFlag(0x0302, 4, 0x1814))
    SetScenaFlags(ScenaFlag(0x0302, 5, 0x1815))
    SetScenaFlags(ScenaFlag(0x0302, 6, 0x1816))
    NewScene('ED6_DT21/T0123._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_2E55(): pass

    label('loc_2E55')

    SetScenaFlags(ScenaFlag(0x0300, 0, 0x1800))
    SetScenaFlags(ScenaFlag(0x0300, 1, 0x1801))
    SetScenaFlags(ScenaFlag(0x0300, 2, 0x1802))
    SetScenaFlags(ScenaFlag(0x0300, 3, 0x1803))
    SetScenaFlags(ScenaFlag(0x0300, 4, 0x1804))
    SetScenaFlags(ScenaFlag(0x0300, 5, 0x1805))
    SetScenaFlags(ScenaFlag(0x0300, 6, 0x1806))
    SetScenaFlags(ScenaFlag(0x0300, 7, 0x1807))
    SetScenaFlags(ScenaFlag(0x0301, 0, 0x1808))
    SetScenaFlags(ScenaFlag(0x0301, 1, 0x1809))
    SetScenaFlags(ScenaFlag(0x0301, 2, 0x180A))
    SetScenaFlags(ScenaFlag(0x0301, 3, 0x180B))
    SetScenaFlags(ScenaFlag(0x0301, 4, 0x180C))
    SetScenaFlags(ScenaFlag(0x0301, 5, 0x180D))
    SetScenaFlags(ScenaFlag(0x0301, 6, 0x180E))
    SetScenaFlags(ScenaFlag(0x0301, 7, 0x180F))
    SetScenaFlags(ScenaFlag(0x0302, 0, 0x1810))
    SetScenaFlags(ScenaFlag(0x0302, 1, 0x1811))
    SetScenaFlags(ScenaFlag(0x0302, 2, 0x1812))
    SetScenaFlags(ScenaFlag(0x0302, 3, 0x1813))
    SetScenaFlags(ScenaFlag(0x0302, 4, 0x1814))
    SetScenaFlags(ScenaFlag(0x0302, 5, 0x1815))
    SetScenaFlags(ScenaFlag(0x0302, 6, 0x1816))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_BB(0x00, 0x01, 0x00000043)
    SetScenaFlags(ScenaFlag(0x0302, 7, 0x1817))
    SetScenaFlags(ScenaFlag(0x0303, 0, 0x1818))
    SetScenaFlags(ScenaFlag(0x0303, 1, 0x1819))
    SetScenaFlags(ScenaFlag(0x0303, 2, 0x181A))
    SetScenaFlags(ScenaFlag(0x0303, 3, 0x181B))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T0300._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_2EC4(): pass

    label('loc_2EC4')

    SetScenaFlags(ScenaFlag(0x0300, 0, 0x1800))
    SetScenaFlags(ScenaFlag(0x0300, 1, 0x1801))
    SetScenaFlags(ScenaFlag(0x0300, 2, 0x1802))
    SetScenaFlags(ScenaFlag(0x0300, 3, 0x1803))
    SetScenaFlags(ScenaFlag(0x0300, 4, 0x1804))
    SetScenaFlags(ScenaFlag(0x0300, 5, 0x1805))
    SetScenaFlags(ScenaFlag(0x0300, 6, 0x1806))
    SetScenaFlags(ScenaFlag(0x0300, 7, 0x1807))
    SetScenaFlags(ScenaFlag(0x0301, 0, 0x1808))
    SetScenaFlags(ScenaFlag(0x0301, 1, 0x1809))
    SetScenaFlags(ScenaFlag(0x0301, 2, 0x180A))
    SetScenaFlags(ScenaFlag(0x0301, 3, 0x180B))
    SetScenaFlags(ScenaFlag(0x0301, 4, 0x180C))
    SetScenaFlags(ScenaFlag(0x0301, 5, 0x180D))
    SetScenaFlags(ScenaFlag(0x0301, 6, 0x180E))
    SetScenaFlags(ScenaFlag(0x0301, 7, 0x180F))
    SetScenaFlags(ScenaFlag(0x0302, 0, 0x1810))
    SetScenaFlags(ScenaFlag(0x0302, 1, 0x1811))
    SetScenaFlags(ScenaFlag(0x0302, 2, 0x1812))
    SetScenaFlags(ScenaFlag(0x0302, 3, 0x1813))
    SetScenaFlags(ScenaFlag(0x0302, 4, 0x1814))
    SetScenaFlags(ScenaFlag(0x0302, 5, 0x1815))
    SetScenaFlags(ScenaFlag(0x0302, 6, 0x1816))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_BB(0x00, 0x01, 0x00000043)
    SetScenaFlags(ScenaFlag(0x0302, 7, 0x1817))
    SetScenaFlags(ScenaFlag(0x0303, 0, 0x1818))
    SetScenaFlags(ScenaFlag(0x0303, 1, 0x1819))
    SetScenaFlags(ScenaFlag(0x0303, 2, 0x181A))
    SetScenaFlags(ScenaFlag(0x0303, 3, 0x181B))
    OP_BB(0x00, 0x01, 0x00000000)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0303, 4, 0x181C))
    SetScenaFlags(ScenaFlag(0x0303, 5, 0x181D))
    SetScenaFlags(ScenaFlag(0x0303, 6, 0x181E))
    SetScenaFlags(ScenaFlag(0x0303, 7, 0x181F))
    SetScenaFlags(ScenaFlag(0x0304, 0, 0x1820))
    SetScenaFlags(ScenaFlag(0x0304, 1, 0x1821))
    SetScenaFlags(ScenaFlag(0x0304, 2, 0x1822))
    SetScenaFlags(ScenaFlag(0x0304, 3, 0x1823))
    NewScene('ED6_DT21/C0300._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_2F5B(): pass

    label('loc_2F5B')

    SetScenaFlags(ScenaFlag(0x0300, 0, 0x1800))
    SetScenaFlags(ScenaFlag(0x0300, 1, 0x1801))
    SetScenaFlags(ScenaFlag(0x0300, 2, 0x1802))
    SetScenaFlags(ScenaFlag(0x0300, 3, 0x1803))
    SetScenaFlags(ScenaFlag(0x0300, 4, 0x1804))
    SetScenaFlags(ScenaFlag(0x0300, 5, 0x1805))
    SetScenaFlags(ScenaFlag(0x0300, 6, 0x1806))
    SetScenaFlags(ScenaFlag(0x0300, 7, 0x1807))
    SetScenaFlags(ScenaFlag(0x0301, 0, 0x1808))
    SetScenaFlags(ScenaFlag(0x0301, 1, 0x1809))
    SetScenaFlags(ScenaFlag(0x0301, 2, 0x180A))
    SetScenaFlags(ScenaFlag(0x0301, 3, 0x180B))
    SetScenaFlags(ScenaFlag(0x0301, 4, 0x180C))
    SetScenaFlags(ScenaFlag(0x0301, 5, 0x180D))
    SetScenaFlags(ScenaFlag(0x0301, 6, 0x180E))
    SetScenaFlags(ScenaFlag(0x0301, 7, 0x180F))
    SetScenaFlags(ScenaFlag(0x0302, 0, 0x1810))
    SetScenaFlags(ScenaFlag(0x0302, 1, 0x1811))
    SetScenaFlags(ScenaFlag(0x0302, 2, 0x1812))
    SetScenaFlags(ScenaFlag(0x0302, 3, 0x1813))
    SetScenaFlags(ScenaFlag(0x0302, 4, 0x1814))
    SetScenaFlags(ScenaFlag(0x0302, 5, 0x1815))
    SetScenaFlags(ScenaFlag(0x0302, 6, 0x1816))
    OP_BB(0x00, 0x01, 0x00000043)
    SetScenaFlags(ScenaFlag(0x0302, 7, 0x1817))
    SetScenaFlags(ScenaFlag(0x0303, 0, 0x1818))
    SetScenaFlags(ScenaFlag(0x0303, 1, 0x1819))
    SetScenaFlags(ScenaFlag(0x0303, 2, 0x181A))
    SetScenaFlags(ScenaFlag(0x0303, 3, 0x181B))
    OP_BB(0x00, 0x01, 0x00000000)
    SetScenaFlags(ScenaFlag(0x0303, 4, 0x181C))
    SetScenaFlags(ScenaFlag(0x0303, 5, 0x181D))
    SetScenaFlags(ScenaFlag(0x0303, 6, 0x181E))
    SetScenaFlags(ScenaFlag(0x0303, 7, 0x181F))
    SetScenaFlags(ScenaFlag(0x0304, 0, 0x1820))
    SetScenaFlags(ScenaFlag(0x0304, 1, 0x1821))
    SetScenaFlags(ScenaFlag(0x0304, 2, 0x1822))
    SetScenaFlags(ScenaFlag(0x0304, 3, 0x1823))
    SetScenaFlags(ScenaFlag(0x0304, 4, 0x1824))
    SetScenaFlags(ScenaFlag(0x0304, 5, 0x1825))
    SetScenaFlags(ScenaFlag(0x0304, 6, 0x1826))

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0304, 7, 0x1827))
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

    SetScenaFlags(ScenaFlag(0x0305, 0, 0x1828))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/T0300._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3141')

    def _loc_300A(): pass

    label('loc_300A')

    SetScenaFlags(ScenaFlag(0x0300, 0, 0x1800))
    SetScenaFlags(ScenaFlag(0x0300, 1, 0x1801))
    SetScenaFlags(ScenaFlag(0x0300, 2, 0x1802))
    SetScenaFlags(ScenaFlag(0x0300, 3, 0x1803))
    SetScenaFlags(ScenaFlag(0x0300, 4, 0x1804))
    SetScenaFlags(ScenaFlag(0x0300, 5, 0x1805))
    SetScenaFlags(ScenaFlag(0x0300, 6, 0x1806))
    SetScenaFlags(ScenaFlag(0x0300, 7, 0x1807))
    SetScenaFlags(ScenaFlag(0x0301, 0, 0x1808))
    SetScenaFlags(ScenaFlag(0x0301, 1, 0x1809))
    SetScenaFlags(ScenaFlag(0x0301, 2, 0x180A))
    SetScenaFlags(ScenaFlag(0x0301, 3, 0x180B))
    SetScenaFlags(ScenaFlag(0x0301, 4, 0x180C))
    SetScenaFlags(ScenaFlag(0x0301, 5, 0x180D))
    SetScenaFlags(ScenaFlag(0x0301, 6, 0x180E))
    SetScenaFlags(ScenaFlag(0x0301, 7, 0x180F))
    SetScenaFlags(ScenaFlag(0x0302, 0, 0x1810))
    SetScenaFlags(ScenaFlag(0x0302, 1, 0x1811))
    SetScenaFlags(ScenaFlag(0x0302, 2, 0x1812))
    SetScenaFlags(ScenaFlag(0x0302, 3, 0x1813))
    SetScenaFlags(ScenaFlag(0x0302, 4, 0x1814))
    SetScenaFlags(ScenaFlag(0x0302, 5, 0x1815))
    SetScenaFlags(ScenaFlag(0x0302, 6, 0x1816))
    OP_BB(0x00, 0x01, 0x00000043)
    SetScenaFlags(ScenaFlag(0x0302, 7, 0x1817))
    SetScenaFlags(ScenaFlag(0x0303, 0, 0x1818))
    SetScenaFlags(ScenaFlag(0x0303, 1, 0x1819))
    SetScenaFlags(ScenaFlag(0x0303, 2, 0x181A))
    SetScenaFlags(ScenaFlag(0x0303, 3, 0x181B))
    OP_BB(0x00, 0x01, 0x00000000)
    SetScenaFlags(ScenaFlag(0x0303, 4, 0x181C))
    SetScenaFlags(ScenaFlag(0x0303, 5, 0x181D))
    SetScenaFlags(ScenaFlag(0x0303, 6, 0x181E))
    SetScenaFlags(ScenaFlag(0x0303, 7, 0x181F))
    SetScenaFlags(ScenaFlag(0x0304, 0, 0x1820))
    SetScenaFlags(ScenaFlag(0x0304, 1, 0x1821))
    SetScenaFlags(ScenaFlag(0x0304, 2, 0x1822))
    SetScenaFlags(ScenaFlag(0x0304, 3, 0x1823))
    SetScenaFlags(ScenaFlag(0x0304, 4, 0x1824))
    SetScenaFlags(ScenaFlag(0x0304, 5, 0x1825))
    SetScenaFlags(ScenaFlag(0x0304, 6, 0x1826))

    OP_CE(
        0x01,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0304, 7, 0x1827))
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

    SetScenaFlags(ScenaFlag(0x0305, 0, 0x1828))
    SetScenaFlags(ScenaFlag(0x0306, 3, 0x1833))
    OP_BB(0x00, 0x01, 0x00000044)
    SetScenaFlags(ScenaFlag(0x0306, 4, 0x1834))
    SetScenaFlags(ScenaFlag(0x0306, 5, 0x1835))
    SetScenaFlags(ScenaFlag(0x0306, 6, 0x1836))
    SetScenaFlags(ScenaFlag(0x0306, 7, 0x1837))
    SetScenaFlags(ScenaFlag(0x0307, 0, 0x1838))
    AddItem(ItemTable['储物室钥匙'], 1)
    SetScenaFlags(ScenaFlag(0x0307, 1, 0x1839))
    SetScenaFlags(ScenaFlag(0x0307, 2, 0x183A))
    AddItem(ItemTable['口琴'], 1)
    SetScenaFlags(ScenaFlag(0x0307, 3, 0x183B))
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/T0100._SN', 119, 0, 0)
    IdleLoop()

    def _loc_30EA(): pass

    label('loc_30EA')

    FormationReset()
    SetScenaFlags(ScenaFlag(0x0300, 0, 0x1800))
    SetScenaFlags(ScenaFlag(0x0300, 1, 0x1801))
    SetScenaFlags(ScenaFlag(0x0300, 2, 0x1802))
    SetScenaFlags(ScenaFlag(0x0300, 3, 0x1803))
    SetScenaFlags(ScenaFlag(0x0300, 4, 0x1804))
    SetScenaFlags(ScenaFlag(0x0300, 5, 0x1805))
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x0300, 6, 0x1806))
    SetScenaFlags(ScenaFlag(0x0300, 7, 0x1807))
    SetScenaFlags(ScenaFlag(0x0301, 0, 0x1808))
    SetScenaFlags(ScenaFlag(0x0301, 1, 0x1809))
    SetScenaFlags(ScenaFlag(0x0301, 2, 0x180A))
    SetScenaFlags(ScenaFlag(0x0301, 3, 0x180B))
    SetScenaFlags(ScenaFlag(0x0301, 4, 0x180C))
    SetScenaFlags(ScenaFlag(0x0301, 5, 0x180D))
    SetScenaFlags(ScenaFlag(0x0301, 6, 0x180E))
    SetScenaFlags(ScenaFlag(0x0301, 7, 0x180F))
    SetScenaFlags(ScenaFlag(0x0302, 0, 0x1810))
    SetScenaFlags(ScenaFlag(0x0302, 1, 0x1811))
    SetScenaFlags(ScenaFlag(0x0302, 2, 0x1812))
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
    ClearScenaFlags(ScenaFlag(0x0340, 0, 0x1A00))
    ClearScenaFlags(ScenaFlag(0x0340, 1, 0x1A01))
    ClearScenaFlags(ScenaFlag(0x0340, 2, 0x1A02))
    ClearScenaFlags(ScenaFlag(0x0340, 3, 0x1A03))
    ClearScenaFlags(ScenaFlag(0x0340, 4, 0x1A04))
    ClearScenaFlags(ScenaFlag(0x0340, 5, 0x1A05))
    ClearScenaFlags(ScenaFlag(0x0340, 6, 0x1A06))
    ClearScenaFlags(ScenaFlag(0x0340, 7, 0x1A07))
    ClearScenaFlags(ScenaFlag(0x0341, 0, 0x1A08))
    ClearScenaFlags(ScenaFlag(0x0341, 1, 0x1A09))
    ClearScenaFlags(ScenaFlag(0x0341, 2, 0x1A0A))
    ClearScenaFlags(ScenaFlag(0x0341, 3, 0x1A0B))
    ClearScenaFlags(ScenaFlag(0x0341, 4, 0x1A0C))
    ClearScenaFlags(ScenaFlag(0x0341, 5, 0x1A0D))
    ClearScenaFlags(ScenaFlag(0x0341, 6, 0x1A0E))
    ClearScenaFlags(ScenaFlag(0x0341, 7, 0x1A0F))
    ClearScenaFlags(ScenaFlag(0x0342, 0, 0x1A10))
    ClearScenaFlags(ScenaFlag(0x0342, 1, 0x1A11))
    ClearScenaFlags(ScenaFlag(0x0342, 2, 0x1A12))
    ClearScenaFlags(ScenaFlag(0x0342, 3, 0x1A13))
    ClearScenaFlags(ScenaFlag(0x0342, 4, 0x1A14))
    ClearScenaFlags(ScenaFlag(0x0342, 5, 0x1A15))
    ClearScenaFlags(ScenaFlag(0x0342, 6, 0x1A16))
    ClearScenaFlags(ScenaFlag(0x0342, 7, 0x1A17))
    ClearScenaFlags(ScenaFlag(0x0343, 0, 0x1A18))
    ClearScenaFlags(ScenaFlag(0x0343, 1, 0x1A19))
    ClearScenaFlags(ScenaFlag(0x0343, 2, 0x1A1A))
    ClearScenaFlags(ScenaFlag(0x0350, 3, 0x1A83))
    ClearScenaFlags(ScenaFlag(0x0343, 3, 0x1A1B))
    ClearScenaFlags(ScenaFlag(0x0343, 4, 0x1A1C))
    ClearScenaFlags(ScenaFlag(0x0343, 5, 0x1A1D))
    ClearScenaFlags(ScenaFlag(0x0343, 6, 0x1A1E))
    ClearScenaFlags(ScenaFlag(0x0343, 7, 0x1A1F))
    ClearScenaFlags(ScenaFlag(0x0344, 0, 0x1A20))
    ClearScenaFlags(ScenaFlag(0x0344, 1, 0x1A21))
    ClearScenaFlags(ScenaFlag(0x0344, 2, 0x1A22))
    ClearScenaFlags(ScenaFlag(0x0344, 3, 0x1A23))
    ClearScenaFlags(ScenaFlag(0x0344, 4, 0x1A24))
    ClearScenaFlags(ScenaFlag(0x0344, 5, 0x1A25))
    ClearScenaFlags(ScenaFlag(0x0344, 6, 0x1A26))
    ClearScenaFlags(ScenaFlag(0x0344, 7, 0x1A27))
    ClearScenaFlags(ScenaFlag(0x0345, 0, 0x1A28))
    ClearScenaFlags(ScenaFlag(0x0345, 1, 0x1A29))
    ClearScenaFlags(ScenaFlag(0x034F, 1, 0x1A79))

    Return()

# id: 0x0013 offset: 0x31D9
@scena.Code('func_13_31D9')
def func_13_31D9():
    SetScenaFlags(ScenaFlag(0x0340, 0, 0x1A00))
    SetScenaFlags(ScenaFlag(0x0340, 1, 0x1A01))
    SetScenaFlags(ScenaFlag(0x0340, 2, 0x1A02))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x0340, 3, 0x1A03))
    SetScenaFlags(ScenaFlag(0x0340, 4, 0x1A04))
    SetScenaFlags(ScenaFlag(0x0340, 5, 0x1A05))
    SetScenaFlags(ScenaFlag(0x0340, 7, 0x1A07))
    SetScenaFlags(ScenaFlag(0x0341, 0, 0x1A08))
    SetScenaFlags(ScenaFlag(0x0341, 1, 0x1A09))
    SetScenaFlags(ScenaFlag(0x0341, 2, 0x1A0A))
    SetScenaFlags(ScenaFlag(0x0341, 3, 0x1A0B))
    SetScenaFlags(ScenaFlag(0x0341, 4, 0x1A0C))
    SetScenaFlags(ScenaFlag(0x0340, 6, 0x1A06))
    SetScenaFlags(ScenaFlag(0x0341, 5, 0x1A0D))
    SetScenaFlags(ScenaFlag(0x0341, 6, 0x1A0E))
    SetScenaFlags(ScenaFlag(0x0341, 7, 0x1A0F))
    SetScenaFlags(ScenaFlag(0x0342, 0, 0x1A10))
    SetScenaFlags(ScenaFlag(0x0342, 1, 0x1A11))
    SetScenaFlags(ScenaFlag(0x0342, 2, 0x1A12))
    SetScenaFlags(ScenaFlag(0x0342, 3, 0x1A13))
    SetScenaFlags(ScenaFlag(0x0342, 4, 0x1A14))
    SetScenaFlags(ScenaFlag(0x0342, 5, 0x1A15))
    SetScenaFlags(ScenaFlag(0x0342, 6, 0x1A16))
    SetScenaFlags(ScenaFlag(0x0342, 7, 0x1A17))
    SetScenaFlags(ScenaFlag(0x0343, 0, 0x1A18))
    SetScenaFlags(ScenaFlag(0x0343, 1, 0x1A19))
    SetScenaFlags(ScenaFlag(0x0343, 2, 0x1A1A))
    SetScenaFlags(ScenaFlag(0x0350, 3, 0x1A83))
    SetScenaFlags(ScenaFlag(0x0343, 3, 0x1A1B))
    SetScenaFlags(ScenaFlag(0x0343, 4, 0x1A1C))
    SetScenaFlags(ScenaFlag(0x0343, 5, 0x1A1D))
    SetScenaFlags(ScenaFlag(0x0343, 6, 0x1A1E))
    SetScenaFlags(ScenaFlag(0x0343, 7, 0x1A1F))
    SetScenaFlags(ScenaFlag(0x0344, 0, 0x1A20))
    SetScenaFlags(ScenaFlag(0x0344, 1, 0x1A21))
    SetScenaFlags(ScenaFlag(0x0344, 2, 0x1A22))
    SetScenaFlags(ScenaFlag(0x0344, 3, 0x1A23))
    SetScenaFlags(ScenaFlag(0x0344, 4, 0x1A24))
    SetScenaFlags(ScenaFlag(0x0344, 5, 0x1A25))
    SetScenaFlags(ScenaFlag(0x0344, 6, 0x1A26))
    SetScenaFlags(ScenaFlag(0x0344, 7, 0x1A27))
    SetScenaFlags(ScenaFlag(0x0345, 0, 0x1A28))
    SetScenaFlags(ScenaFlag(0x0345, 1, 0x1A29))
    SetScenaFlags(ScenaFlag(0x034F, 1, 0x1A79))

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

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C0705._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_33CD(): pass

    label('loc_33CD')

    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    SetScenaFlags(ScenaFlag(0x0340, 0, 0x1A00))
    NewScene('ED6_DT21/T0100._SN', 110, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_33DF(): pass

    label('loc_33DF')

    SetScenaFlags(ScenaFlag(0x0340, 0, 0x1A00))
    SetScenaFlags(ScenaFlag(0x0340, 1, 0x1A01))
    SetScenaFlags(ScenaFlag(0x0340, 2, 0x1A02))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x0340, 3, 0x1A03))
    SetScenaFlags(ScenaFlag(0x0340, 4, 0x1A04))
    SetScenaFlags(ScenaFlag(0x0340, 5, 0x1A05))
    SetScenaFlags(ScenaFlag(0x0340, 7, 0x1A07))
    SetScenaFlags(ScenaFlag(0x0341, 0, 0x1A08))
    SetScenaFlags(ScenaFlag(0x0341, 1, 0x1A09))
    SetScenaFlags(ScenaFlag(0x0341, 2, 0x1A0A))
    SetScenaFlags(ScenaFlag(0x0341, 3, 0x1A0B))
    SetScenaFlags(ScenaFlag(0x0341, 4, 0x1A0C))
    SetScenaFlags(ScenaFlag(0x0340, 6, 0x1A06))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1121._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_3427(): pass

    label('loc_3427')

    SetScenaFlags(ScenaFlag(0x0340, 0, 0x1A00))
    SetScenaFlags(ScenaFlag(0x0340, 1, 0x1A01))
    SetScenaFlags(ScenaFlag(0x0340, 2, 0x1A02))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x0340, 3, 0x1A03))
    SetScenaFlags(ScenaFlag(0x0340, 4, 0x1A04))
    SetScenaFlags(ScenaFlag(0x0340, 5, 0x1A05))
    SetScenaFlags(ScenaFlag(0x0340, 7, 0x1A07))
    SetScenaFlags(ScenaFlag(0x0341, 0, 0x1A08))
    SetScenaFlags(ScenaFlag(0x0341, 1, 0x1A09))
    SetScenaFlags(ScenaFlag(0x0341, 2, 0x1A0A))
    SetScenaFlags(ScenaFlag(0x0341, 3, 0x1A0B))
    SetScenaFlags(ScenaFlag(0x0341, 4, 0x1A0C))
    SetScenaFlags(ScenaFlag(0x0340, 6, 0x1A06))
    SetScenaFlags(ScenaFlag(0x0341, 5, 0x1A0D))
    SetScenaFlags(ScenaFlag(0x0341, 6, 0x1A0E))
    SetScenaFlags(ScenaFlag(0x0341, 7, 0x1A0F))
    SetScenaFlags(ScenaFlag(0x0342, 0, 0x1A10))
    SetScenaFlags(ScenaFlag(0x0342, 1, 0x1A11))
    SetScenaFlags(ScenaFlag(0x0342, 2, 0x1A12))
    SetScenaFlags(ScenaFlag(0x0342, 3, 0x1A13))
    NewScene('ED6_DT21/T1201._SN', 108, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_3481(): pass

    label('loc_3481')

    SetScenaFlags(ScenaFlag(0x0340, 0, 0x1A00))
    SetScenaFlags(ScenaFlag(0x0340, 1, 0x1A01))
    SetScenaFlags(ScenaFlag(0x0340, 2, 0x1A02))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x0340, 3, 0x1A03))
    SetScenaFlags(ScenaFlag(0x0340, 4, 0x1A04))
    SetScenaFlags(ScenaFlag(0x0340, 5, 0x1A05))
    SetScenaFlags(ScenaFlag(0x0340, 7, 0x1A07))
    SetScenaFlags(ScenaFlag(0x0341, 0, 0x1A08))
    SetScenaFlags(ScenaFlag(0x0341, 1, 0x1A09))
    SetScenaFlags(ScenaFlag(0x0341, 2, 0x1A0A))
    SetScenaFlags(ScenaFlag(0x0341, 3, 0x1A0B))
    SetScenaFlags(ScenaFlag(0x0341, 4, 0x1A0C))
    SetScenaFlags(ScenaFlag(0x0340, 6, 0x1A06))
    SetScenaFlags(ScenaFlag(0x0341, 5, 0x1A0D))
    SetScenaFlags(ScenaFlag(0x0341, 6, 0x1A0E))
    SetScenaFlags(ScenaFlag(0x0341, 7, 0x1A0F))
    SetScenaFlags(ScenaFlag(0x0342, 0, 0x1A10))
    SetScenaFlags(ScenaFlag(0x0342, 1, 0x1A11))
    SetScenaFlags(ScenaFlag(0x0342, 2, 0x1A12))
    SetScenaFlags(ScenaFlag(0x0342, 3, 0x1A13))
    SetScenaFlags(ScenaFlag(0x0342, 4, 0x1A14))
    SetScenaFlags(ScenaFlag(0x0342, 5, 0x1A15))
    SetScenaFlags(ScenaFlag(0x0342, 6, 0x1A16))
    SetScenaFlags(ScenaFlag(0x0342, 7, 0x1A17))
    SetScenaFlags(ScenaFlag(0x0343, 0, 0x1A18))
    SetScenaFlags(ScenaFlag(0x0343, 1, 0x1A19))
    SetScenaFlags(ScenaFlag(0x0350, 3, 0x1A83))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1201._SN', 108, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_34F3(): pass

    label('loc_34F3')

    SetScenaFlags(ScenaFlag(0x0340, 0, 0x1A00))
    SetScenaFlags(ScenaFlag(0x0340, 1, 0x1A01))
    SetScenaFlags(ScenaFlag(0x0340, 2, 0x1A02))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x0340, 3, 0x1A03))
    SetScenaFlags(ScenaFlag(0x0340, 4, 0x1A04))
    SetScenaFlags(ScenaFlag(0x0340, 5, 0x1A05))
    SetScenaFlags(ScenaFlag(0x0340, 7, 0x1A07))
    SetScenaFlags(ScenaFlag(0x0341, 0, 0x1A08))
    SetScenaFlags(ScenaFlag(0x0341, 1, 0x1A09))
    SetScenaFlags(ScenaFlag(0x0341, 2, 0x1A0A))
    SetScenaFlags(ScenaFlag(0x0341, 3, 0x1A0B))
    SetScenaFlags(ScenaFlag(0x0341, 4, 0x1A0C))
    SetScenaFlags(ScenaFlag(0x0340, 6, 0x1A06))
    SetScenaFlags(ScenaFlag(0x0341, 5, 0x1A0D))
    SetScenaFlags(ScenaFlag(0x0341, 6, 0x1A0E))
    SetScenaFlags(ScenaFlag(0x0341, 7, 0x1A0F))
    SetScenaFlags(ScenaFlag(0x0342, 0, 0x1A10))
    SetScenaFlags(ScenaFlag(0x0342, 1, 0x1A11))
    SetScenaFlags(ScenaFlag(0x0342, 2, 0x1A12))
    SetScenaFlags(ScenaFlag(0x0342, 3, 0x1A13))
    SetScenaFlags(ScenaFlag(0x0342, 4, 0x1A14))
    SetScenaFlags(ScenaFlag(0x0342, 5, 0x1A15))
    SetScenaFlags(ScenaFlag(0x0342, 6, 0x1A16))
    SetScenaFlags(ScenaFlag(0x0342, 7, 0x1A17))
    SetScenaFlags(ScenaFlag(0x0343, 0, 0x1A18))
    SetScenaFlags(ScenaFlag(0x0343, 1, 0x1A19))
    SetScenaFlags(ScenaFlag(0x0350, 3, 0x1A83))
    SetScenaFlags(ScenaFlag(0x0343, 2, 0x1A1A))
    SetScenaFlags(ScenaFlag(0x0343, 3, 0x1A1B))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T1103._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_356B(): pass

    label('loc_356B')

    SetScenaFlags(ScenaFlag(0x0340, 0, 0x1A00))
    SetScenaFlags(ScenaFlag(0x0340, 1, 0x1A01))
    SetScenaFlags(ScenaFlag(0x0340, 2, 0x1A02))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x0340, 3, 0x1A03))
    SetScenaFlags(ScenaFlag(0x0340, 4, 0x1A04))
    SetScenaFlags(ScenaFlag(0x0340, 5, 0x1A05))
    SetScenaFlags(ScenaFlag(0x0340, 7, 0x1A07))
    SetScenaFlags(ScenaFlag(0x0341, 0, 0x1A08))
    SetScenaFlags(ScenaFlag(0x0341, 1, 0x1A09))
    SetScenaFlags(ScenaFlag(0x0341, 2, 0x1A0A))
    SetScenaFlags(ScenaFlag(0x0341, 3, 0x1A0B))
    SetScenaFlags(ScenaFlag(0x0341, 4, 0x1A0C))
    SetScenaFlags(ScenaFlag(0x0340, 6, 0x1A06))
    SetScenaFlags(ScenaFlag(0x0341, 5, 0x1A0D))
    SetScenaFlags(ScenaFlag(0x0341, 6, 0x1A0E))
    SetScenaFlags(ScenaFlag(0x0341, 7, 0x1A0F))
    SetScenaFlags(ScenaFlag(0x0342, 0, 0x1A10))
    SetScenaFlags(ScenaFlag(0x0342, 1, 0x1A11))
    SetScenaFlags(ScenaFlag(0x0342, 2, 0x1A12))
    SetScenaFlags(ScenaFlag(0x0342, 3, 0x1A13))
    SetScenaFlags(ScenaFlag(0x0342, 4, 0x1A14))
    SetScenaFlags(ScenaFlag(0x0342, 5, 0x1A15))
    SetScenaFlags(ScenaFlag(0x0342, 6, 0x1A16))
    SetScenaFlags(ScenaFlag(0x0342, 7, 0x1A17))
    SetScenaFlags(ScenaFlag(0x0343, 0, 0x1A18))
    SetScenaFlags(ScenaFlag(0x0343, 1, 0x1A19))
    SetScenaFlags(ScenaFlag(0x0350, 3, 0x1A83))
    SetScenaFlags(ScenaFlag(0x0343, 2, 0x1A1A))
    SetScenaFlags(ScenaFlag(0x0343, 3, 0x1A1B))
    SetScenaFlags(ScenaFlag(0x0343, 4, 0x1A1C))
    SetScenaFlags(ScenaFlag(0x0343, 5, 0x1A1D))
    SetScenaFlags(ScenaFlag(0x0343, 6, 0x1A1E))
    SetScenaFlags(ScenaFlag(0x0343, 7, 0x1A1F))
    SetScenaFlags(ScenaFlag(0x0344, 0, 0x1A20))
    SetScenaFlags(ScenaFlag(0x0344, 1, 0x1A21))
    SetScenaFlags(ScenaFlag(0x0344, 2, 0x1A22))
    SetScenaFlags(ScenaFlag(0x0344, 3, 0x1A23))
    FormationAddMember(ChrTable['科洛丝'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF9, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFA, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/T1102._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_360B(): pass

    label('loc_360B')

    SetScenaFlags(ScenaFlag(0x0340, 0, 0x1A00))
    SetScenaFlags(ScenaFlag(0x0340, 1, 0x1A01))
    SetScenaFlags(ScenaFlag(0x0340, 2, 0x1A02))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x0340, 3, 0x1A03))
    SetScenaFlags(ScenaFlag(0x0340, 4, 0x1A04))
    SetScenaFlags(ScenaFlag(0x0340, 5, 0x1A05))
    SetScenaFlags(ScenaFlag(0x0340, 7, 0x1A07))
    SetScenaFlags(ScenaFlag(0x0341, 0, 0x1A08))
    SetScenaFlags(ScenaFlag(0x0341, 1, 0x1A09))
    SetScenaFlags(ScenaFlag(0x0341, 2, 0x1A0A))
    SetScenaFlags(ScenaFlag(0x0341, 3, 0x1A0B))
    SetScenaFlags(ScenaFlag(0x0341, 4, 0x1A0C))
    SetScenaFlags(ScenaFlag(0x0340, 6, 0x1A06))
    SetScenaFlags(ScenaFlag(0x0341, 5, 0x1A0D))
    SetScenaFlags(ScenaFlag(0x0341, 6, 0x1A0E))
    SetScenaFlags(ScenaFlag(0x0341, 7, 0x1A0F))
    SetScenaFlags(ScenaFlag(0x0342, 0, 0x1A10))
    SetScenaFlags(ScenaFlag(0x0342, 1, 0x1A11))
    SetScenaFlags(ScenaFlag(0x0342, 2, 0x1A12))
    SetScenaFlags(ScenaFlag(0x0342, 3, 0x1A13))
    SetScenaFlags(ScenaFlag(0x0342, 4, 0x1A14))
    SetScenaFlags(ScenaFlag(0x0342, 5, 0x1A15))
    SetScenaFlags(ScenaFlag(0x0342, 6, 0x1A16))
    SetScenaFlags(ScenaFlag(0x0342, 7, 0x1A17))
    SetScenaFlags(ScenaFlag(0x0343, 0, 0x1A18))
    SetScenaFlags(ScenaFlag(0x0343, 1, 0x1A19))
    SetScenaFlags(ScenaFlag(0x0343, 2, 0x1A1A))
    SetScenaFlags(ScenaFlag(0x0350, 3, 0x1A83))
    SetScenaFlags(ScenaFlag(0x0343, 3, 0x1A1B))
    SetScenaFlags(ScenaFlag(0x0343, 4, 0x1A1C))
    SetScenaFlags(ScenaFlag(0x0343, 5, 0x1A1D))
    SetScenaFlags(ScenaFlag(0x0343, 6, 0x1A1E))
    SetScenaFlags(ScenaFlag(0x0343, 7, 0x1A1F))
    SetScenaFlags(ScenaFlag(0x0344, 0, 0x1A20))
    SetScenaFlags(ScenaFlag(0x0344, 1, 0x1A21))
    SetScenaFlags(ScenaFlag(0x0344, 2, 0x1A22))
    SetScenaFlags(ScenaFlag(0x0344, 3, 0x1A23))
    SetScenaFlags(ScenaFlag(0x0344, 4, 0x1A24))
    SetScenaFlags(ScenaFlag(0x0344, 5, 0x1A25))
    SetScenaFlags(ScenaFlag(0x0344, 6, 0x1A26))
    SetScenaFlags(ScenaFlag(0x0344, 7, 0x1A27))
    SetScenaFlags(ScenaFlag(0x0345, 0, 0x1A28))
    SetScenaFlags(ScenaFlag(0x0345, 1, 0x1A29))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1202._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_36AD(): pass

    label('loc_36AD')

    SetScenaFlags(ScenaFlag(0x0340, 0, 0x1A00))
    SetScenaFlags(ScenaFlag(0x0340, 1, 0x1A01))
    SetScenaFlags(ScenaFlag(0x0340, 2, 0x1A02))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x0340, 3, 0x1A03))
    SetScenaFlags(ScenaFlag(0x0340, 4, 0x1A04))
    SetScenaFlags(ScenaFlag(0x0340, 5, 0x1A05))
    SetScenaFlags(ScenaFlag(0x0340, 7, 0x1A07))
    SetScenaFlags(ScenaFlag(0x0341, 0, 0x1A08))
    SetScenaFlags(ScenaFlag(0x0341, 1, 0x1A09))
    SetScenaFlags(ScenaFlag(0x0341, 2, 0x1A0A))
    SetScenaFlags(ScenaFlag(0x0341, 3, 0x1A0B))
    SetScenaFlags(ScenaFlag(0x0341, 4, 0x1A0C))
    SetScenaFlags(ScenaFlag(0x0340, 6, 0x1A06))
    SetScenaFlags(ScenaFlag(0x0341, 5, 0x1A0D))
    SetScenaFlags(ScenaFlag(0x0341, 6, 0x1A0E))
    SetScenaFlags(ScenaFlag(0x0341, 7, 0x1A0F))
    SetScenaFlags(ScenaFlag(0x0342, 0, 0x1A10))
    SetScenaFlags(ScenaFlag(0x0342, 1, 0x1A11))
    NewScene('ED6_DT21/T1121._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_371D')

    def _loc_3701(): pass

    label('loc_3701')

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
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
    ClearScenaFlags(ScenaFlag(0x0380, 0, 0x1C00))
    ClearScenaFlags(ScenaFlag(0x0380, 1, 0x1C01))
    ClearScenaFlags(ScenaFlag(0x0380, 2, 0x1C02))
    ClearScenaFlags(ScenaFlag(0x0380, 3, 0x1C03))
    ClearScenaFlags(ScenaFlag(0x0390, 0, 0x1C80))
    ClearScenaFlags(ScenaFlag(0x0380, 4, 0x1C04))
    ClearScenaFlags(ScenaFlag(0x0380, 5, 0x1C05))
    ClearScenaFlags(ScenaFlag(0x0380, 6, 0x1C06))
    ClearScenaFlags(ScenaFlag(0x0380, 7, 0x1C07))
    ClearScenaFlags(ScenaFlag(0x0381, 0, 0x1C08))
    ClearScenaFlags(ScenaFlag(0x0381, 1, 0x1C09))
    ClearScenaFlags(ScenaFlag(0x0381, 2, 0x1C0A))
    ClearScenaFlags(ScenaFlag(0x0381, 3, 0x1C0B))
    ClearScenaFlags(ScenaFlag(0x0381, 4, 0x1C0C))
    ClearScenaFlags(ScenaFlag(0x0381, 5, 0x1C0D))
    ClearScenaFlags(ScenaFlag(0x0381, 6, 0x1C0E))
    ClearScenaFlags(ScenaFlag(0x0381, 7, 0x1C0F))
    ClearScenaFlags(ScenaFlag(0x0382, 0, 0x1C10))
    ClearScenaFlags(ScenaFlag(0x0382, 1, 0x1C11))
    ClearScenaFlags(ScenaFlag(0x0382, 2, 0x1C12))
    ClearScenaFlags(ScenaFlag(0x0382, 3, 0x1C13))
    ClearScenaFlags(ScenaFlag(0x0382, 4, 0x1C14))
    ClearScenaFlags(ScenaFlag(0x0382, 5, 0x1C15))
    ClearScenaFlags(ScenaFlag(0x0382, 6, 0x1C16))
    ClearScenaFlags(ScenaFlag(0x0382, 7, 0x1C17))
    ClearScenaFlags(ScenaFlag(0x0383, 0, 0x1C18))
    ClearScenaFlags(ScenaFlag(0x0383, 1, 0x1C19))
    ClearScenaFlags(ScenaFlag(0x0383, 2, 0x1C1A))
    ClearScenaFlags(ScenaFlag(0x0383, 3, 0x1C1B))
    ClearScenaFlags(ScenaFlag(0x0383, 4, 0x1C1C))
    ClearScenaFlags(ScenaFlag(0x0390, 1, 0x1C81))
    ClearScenaFlags(ScenaFlag(0x0390, 2, 0x1C82))
    ClearScenaFlags(ScenaFlag(0x0390, 3, 0x1C83))
    ClearScenaFlags(ScenaFlag(0x0390, 4, 0x1C84))
    ClearScenaFlags(ScenaFlag(0x0390, 5, 0x1C85))
    ClearScenaFlags(ScenaFlag(0x0390, 6, 0x1C86))
    ClearScenaFlags(ScenaFlag(0x0390, 7, 0x1C87))
    ClearScenaFlags(ScenaFlag(0x0391, 0, 0x1C88))
    ClearScenaFlags(ScenaFlag(0x0383, 5, 0x1C1D))
    ClearScenaFlags(ScenaFlag(0x0383, 6, 0x1C1E))
    ClearScenaFlags(ScenaFlag(0x0383, 7, 0x1C1F))
    ClearScenaFlags(ScenaFlag(0x0384, 0, 0x1C20))
    ClearScenaFlags(ScenaFlag(0x0384, 1, 0x1C21))
    ClearScenaFlags(ScenaFlag(0x0384, 2, 0x1C22))
    ClearScenaFlags(ScenaFlag(0x0384, 3, 0x1C23))
    ClearScenaFlags(ScenaFlag(0x0384, 4, 0x1C24))
    ClearScenaFlags(ScenaFlag(0x0384, 5, 0x1C25))
    ClearScenaFlags(ScenaFlag(0x0384, 6, 0x1C26))
    ClearScenaFlags(ScenaFlag(0x0384, 7, 0x1C27))
    ClearScenaFlags(ScenaFlag(0x0385, 0, 0x1C28))
    ClearScenaFlags(ScenaFlag(0x0394, 5, 0x1CA5))

    Return()

# id: 0x0016 offset: 0x37D9
@scena.Code('func_16_37D9')
def func_16_37D9():
    SetScenaFlags(ScenaFlag(0x0380, 0, 0x1C00))
    SetScenaFlags(ScenaFlag(0x0380, 1, 0x1C01))
    SetScenaFlags(ScenaFlag(0x0380, 2, 0x1C02))
    SetScenaFlags(ScenaFlag(0x0380, 3, 0x1C03))
    SetScenaFlags(ScenaFlag(0x0380, 4, 0x1C04))
    SetScenaFlags(ScenaFlag(0x0380, 5, 0x1C05))
    SetScenaFlags(ScenaFlag(0x0380, 6, 0x1C06))
    SetScenaFlags(ScenaFlag(0x0383, 2, 0x1C1A))
    SetScenaFlags(ScenaFlag(0x0380, 7, 0x1C07))
    SetScenaFlags(ScenaFlag(0x0381, 0, 0x1C08))
    AddItem(ItemTable['红色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 1, 0x1C09))
    SetScenaFlags(ScenaFlag(0x0381, 2, 0x1C0A))
    SetScenaFlags(ScenaFlag(0x0381, 3, 0x1C0B))
    AddItem(ItemTable['绿色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 4, 0x1C0C))
    SetScenaFlags(ScenaFlag(0x0381, 5, 0x1C0D))
    AddItem(ItemTable['蓝色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 6, 0x1C0E))
    SetScenaFlags(ScenaFlag(0x0381, 7, 0x1C0F))
    SetScenaFlags(ScenaFlag(0x0382, 0, 0x1C10))
    SetScenaFlags(ScenaFlag(0x0382, 1, 0x1C11))
    SetScenaFlags(ScenaFlag(0x0382, 2, 0x1C12))
    SetScenaFlags(ScenaFlag(0x0382, 3, 0x1C13))
    SetScenaFlags(ScenaFlag(0x0382, 4, 0x1C14))
    SetScenaFlags(ScenaFlag(0x0382, 5, 0x1C15))
    SetScenaFlags(ScenaFlag(0x0382, 6, 0x1C16))
    SetScenaFlags(ScenaFlag(0x0382, 7, 0x1C17))
    SetScenaFlags(ScenaFlag(0x0383, 0, 0x1C18))
    SetScenaFlags(ScenaFlag(0x0383, 1, 0x1C19))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x0383, 3, 0x1C1B))
    SetScenaFlags(ScenaFlag(0x0383, 4, 0x1C1C))
    SetScenaFlags(ScenaFlag(0x0383, 5, 0x1C1D))
    SetScenaFlags(ScenaFlag(0x0384, 6, 0x1C26))
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    OP_BB(0x01, 0x00, 0x00200033)
    OP_BB(0x01, 0x01, 0x00000001)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x0384, 7, 0x1C27))
    SetScenaFlags(ScenaFlag(0x0385, 0, 0x1C28))
    SetScenaFlags(ScenaFlag(0x0394, 5, 0x1CA5))

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

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0101._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3B3D')

    def _loc_3955(): pass

    label('loc_3955')

    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x0380, 0, 0x1C00))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/T1121._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3B3D')

    def _loc_396C(): pass

    label('loc_396C')

    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x0380, 0, 0x1C00))
    SetScenaFlags(ScenaFlag(0x0380, 1, 0x1C01))
    SetScenaFlags(ScenaFlag(0x0380, 2, 0x1C02))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1510._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3B3D')

    def _loc_3989(): pass

    label('loc_3989')

    SetScenaFlags(ScenaFlag(0x0380, 0, 0x1C00))
    SetScenaFlags(ScenaFlag(0x0380, 1, 0x1C01))
    SetScenaFlags(ScenaFlag(0x0380, 2, 0x1C02))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x0380, 3, 0x1C03))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0901._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3B3D')

    def _loc_39A9(): pass

    label('loc_39A9')

    SetScenaFlags(ScenaFlag(0x0380, 0, 0x1C00))
    SetScenaFlags(ScenaFlag(0x0380, 1, 0x1C01))
    SetScenaFlags(ScenaFlag(0x0380, 2, 0x1C02))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x0380, 3, 0x1C03))
    SetScenaFlags(ScenaFlag(0x0380, 4, 0x1C04))
    SetScenaFlags(ScenaFlag(0x0380, 5, 0x1C05))
    SetScenaFlags(ScenaFlag(0x0380, 6, 0x1C06))
    SetScenaFlags(ScenaFlag(0x0383, 2, 0x1C1A))
    SetScenaFlags(ScenaFlag(0x0380, 7, 0x1C07))
    SetScenaFlags(ScenaFlag(0x0381, 0, 0x1C08))
    AddItem(ItemTable['红色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 1, 0x1C09))
    SetScenaFlags(ScenaFlag(0x0381, 2, 0x1C0A))
    SetScenaFlags(ScenaFlag(0x0381, 3, 0x1C0B))
    AddItem(ItemTable['绿色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 4, 0x1C0C))
    SetScenaFlags(ScenaFlag(0x0381, 5, 0x1C0D))
    AddItem(ItemTable['蓝色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 6, 0x1C0E))
    SetScenaFlags(ScenaFlag(0x0381, 7, 0x1C0F))
    SetScenaFlags(ScenaFlag(0x0382, 0, 0x1C10))
    SetScenaFlags(ScenaFlag(0x0382, 1, 0x1C11))
    SetScenaFlags(ScenaFlag(0x0382, 2, 0x1C12))
    SetScenaFlags(ScenaFlag(0x0382, 3, 0x1C13))
    SetScenaFlags(ScenaFlag(0x0382, 4, 0x1C14))
    SetScenaFlags(ScenaFlag(0x0382, 5, 0x1C15))
    SetScenaFlags(ScenaFlag(0x0382, 6, 0x1C16))
    SetScenaFlags(ScenaFlag(0x0382, 7, 0x1C17))
    SetScenaFlags(ScenaFlag(0x0383, 0, 0x1C18))
    SetScenaFlags(ScenaFlag(0x0383, 1, 0x1C19))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5400._SN', 111, 0, 0)
    IdleLoop()

    Jump('loc_3B3D')

    def _loc_3A1D(): pass

    label('loc_3A1D')

    SetScenaFlags(ScenaFlag(0x0380, 0, 0x1C00))
    SetScenaFlags(ScenaFlag(0x0380, 1, 0x1C01))
    SetScenaFlags(ScenaFlag(0x0380, 2, 0x1C02))
    SetScenaFlags(ScenaFlag(0x0380, 3, 0x1C03))
    SetScenaFlags(ScenaFlag(0x0380, 4, 0x1C04))
    SetScenaFlags(ScenaFlag(0x0380, 5, 0x1C05))
    SetScenaFlags(ScenaFlag(0x0380, 6, 0x1C06))
    SetScenaFlags(ScenaFlag(0x0383, 2, 0x1C1A))
    SetScenaFlags(ScenaFlag(0x0380, 7, 0x1C07))
    SetScenaFlags(ScenaFlag(0x0381, 0, 0x1C08))
    AddItem(ItemTable['红色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 1, 0x1C09))
    SetScenaFlags(ScenaFlag(0x0381, 2, 0x1C0A))
    SetScenaFlags(ScenaFlag(0x0381, 3, 0x1C0B))
    AddItem(ItemTable['绿色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 4, 0x1C0C))
    SetScenaFlags(ScenaFlag(0x0381, 5, 0x1C0D))
    AddItem(ItemTable['蓝色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 6, 0x1C0E))
    SetScenaFlags(ScenaFlag(0x0381, 7, 0x1C0F))
    SetScenaFlags(ScenaFlag(0x0382, 0, 0x1C10))
    SetScenaFlags(ScenaFlag(0x0382, 1, 0x1C11))
    SetScenaFlags(ScenaFlag(0x0382, 2, 0x1C12))
    SetScenaFlags(ScenaFlag(0x0382, 3, 0x1C13))
    SetScenaFlags(ScenaFlag(0x0382, 4, 0x1C14))
    SetScenaFlags(ScenaFlag(0x0382, 5, 0x1C15))
    SetScenaFlags(ScenaFlag(0x0382, 6, 0x1C16))
    SetScenaFlags(ScenaFlag(0x0382, 7, 0x1C17))
    SetScenaFlags(ScenaFlag(0x0383, 0, 0x1C18))
    SetScenaFlags(ScenaFlag(0x0383, 1, 0x1C19))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x0383, 3, 0x1C1B))
    SetScenaFlags(ScenaFlag(0x0383, 4, 0x1C1C))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    NewScene('ED6_DT21/C5400._SN', 110, 0, 0)
    IdleLoop()

    Jump('loc_3B3D')

    def _loc_3A97(): pass

    label('loc_3A97')

    SetScenaFlags(ScenaFlag(0x0380, 0, 0x1C00))
    SetScenaFlags(ScenaFlag(0x0380, 1, 0x1C01))
    SetScenaFlags(ScenaFlag(0x0380, 2, 0x1C02))
    SetScenaFlags(ScenaFlag(0x0380, 3, 0x1C03))
    SetScenaFlags(ScenaFlag(0x0380, 4, 0x1C04))
    SetScenaFlags(ScenaFlag(0x0380, 5, 0x1C05))
    SetScenaFlags(ScenaFlag(0x0380, 6, 0x1C06))
    SetScenaFlags(ScenaFlag(0x0383, 2, 0x1C1A))
    SetScenaFlags(ScenaFlag(0x0380, 7, 0x1C07))
    SetScenaFlags(ScenaFlag(0x0381, 0, 0x1C08))
    AddItem(ItemTable['红色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 1, 0x1C09))
    SetScenaFlags(ScenaFlag(0x0381, 2, 0x1C0A))
    SetScenaFlags(ScenaFlag(0x0381, 3, 0x1C0B))
    AddItem(ItemTable['绿色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 4, 0x1C0C))
    SetScenaFlags(ScenaFlag(0x0381, 5, 0x1C0D))
    AddItem(ItemTable['蓝色密码卡'], 1)
    SetScenaFlags(ScenaFlag(0x0381, 6, 0x1C0E))
    SetScenaFlags(ScenaFlag(0x0381, 7, 0x1C0F))
    SetScenaFlags(ScenaFlag(0x0382, 0, 0x1C10))
    SetScenaFlags(ScenaFlag(0x0382, 1, 0x1C11))
    SetScenaFlags(ScenaFlag(0x0382, 2, 0x1C12))
    SetScenaFlags(ScenaFlag(0x0382, 3, 0x1C13))
    SetScenaFlags(ScenaFlag(0x0382, 4, 0x1C14))
    SetScenaFlags(ScenaFlag(0x0382, 5, 0x1C15))
    SetScenaFlags(ScenaFlag(0x0382, 6, 0x1C16))
    SetScenaFlags(ScenaFlag(0x0382, 7, 0x1C17))
    SetScenaFlags(ScenaFlag(0x0383, 0, 0x1C18))
    SetScenaFlags(ScenaFlag(0x0383, 1, 0x1C19))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    SetScenaFlags(ScenaFlag(0x0383, 3, 0x1C1B))
    SetScenaFlags(ScenaFlag(0x0383, 4, 0x1C1C))
    SetScenaFlags(ScenaFlag(0x0383, 5, 0x1C1D))
    SetScenaFlags(ScenaFlag(0x0384, 6, 0x1C26))
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    OP_BB(0x01, 0x00, 0x00200033)
    OP_BB(0x01, 0x01, 0x00000001)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x0384, 7, 0x1C27))
    SetScenaFlags(ScenaFlag(0x0385, 0, 0x1C28))
    SetScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
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
    ClearScenaFlags(ScenaFlag(0x03C0, 0, 0x1E00))
    ClearScenaFlags(ScenaFlag(0x03C0, 1, 0x1E01))
    ClearScenaFlags(ScenaFlag(0x03C0, 2, 0x1E02))
    ClearScenaFlags(ScenaFlag(0x03C0, 3, 0x1E03))
    ClearScenaFlags(ScenaFlag(0x03C0, 4, 0x1E04))
    ClearScenaFlags(ScenaFlag(0x03C0, 5, 0x1E05))
    ClearScenaFlags(ScenaFlag(0x03C0, 6, 0x1E06))
    ClearScenaFlags(ScenaFlag(0x03C6, 1, 0x1E31))
    ClearScenaFlags(ScenaFlag(0x03C0, 7, 0x1E07))
    ClearScenaFlags(ScenaFlag(0x03C1, 0, 0x1E08))
    ClearScenaFlags(ScenaFlag(0x03C1, 1, 0x1E09))
    ClearScenaFlags(ScenaFlag(0x03C1, 2, 0x1E0A))
    ClearScenaFlags(ScenaFlag(0x03C1, 3, 0x1E0B))
    ClearScenaFlags(ScenaFlag(0x03C1, 4, 0x1E0C))
    ClearScenaFlags(ScenaFlag(0x03C1, 5, 0x1E0D))
    ClearScenaFlags(ScenaFlag(0x03C1, 6, 0x1E0E))
    ClearScenaFlags(ScenaFlag(0x03C1, 7, 0x1E0F))
    ClearScenaFlags(ScenaFlag(0x03C2, 0, 0x1E10))
    ClearScenaFlags(ScenaFlag(0x03C3, 2, 0x1E1A))
    ClearScenaFlags(ScenaFlag(0x03C2, 1, 0x1E11))
    ClearScenaFlags(ScenaFlag(0x03C2, 2, 0x1E12))
    ClearScenaFlags(ScenaFlag(0x03C2, 3, 0x1E13))
    ClearScenaFlags(ScenaFlag(0x03C2, 4, 0x1E14))
    ClearScenaFlags(ScenaFlag(0x03C2, 5, 0x1E15))
    ClearScenaFlags(ScenaFlag(0x03C2, 6, 0x1E16))
    ClearScenaFlags(ScenaFlag(0x03C2, 7, 0x1E17))
    ClearScenaFlags(ScenaFlag(0x03C3, 0, 0x1E18))
    ClearScenaFlags(ScenaFlag(0x03C3, 1, 0x1E19))
    ClearScenaFlags(ScenaFlag(0x03C3, 3, 0x1E1B))
    ClearScenaFlags(ScenaFlag(0x03C3, 4, 0x1E1C))
    ClearScenaFlags(ScenaFlag(0x03C4, 1, 0x1E21))
    ClearScenaFlags(ScenaFlag(0x03C4, 2, 0x1E22))
    ClearScenaFlags(ScenaFlag(0x03C3, 5, 0x1E1D))
    ClearScenaFlags(ScenaFlag(0x03C3, 6, 0x1E1E))
    ClearScenaFlags(ScenaFlag(0x03C3, 7, 0x1E1F))
    ClearScenaFlags(ScenaFlag(0x03C4, 0, 0x1E20))
    ClearScenaFlags(ScenaFlag(0x03C4, 3, 0x1E23))
    ClearScenaFlags(ScenaFlag(0x03C6, 2, 0x1E32))
    ClearScenaFlags(ScenaFlag(0x03C6, 3, 0x1E33))
    ClearScenaFlags(ScenaFlag(0x03C6, 4, 0x1E34))
    ClearScenaFlags(ScenaFlag(0x03C4, 4, 0x1E24))

    Return()

# id: 0x0019 offset: 0x3C1C
@scena.Code('func_19_3C1C')
def func_19_3C1C():
    SetScenaFlags(ScenaFlag(0x03C0, 0, 0x1E00))
    SetScenaFlags(ScenaFlag(0x03C0, 1, 0x1E01))
    SetScenaFlags(ScenaFlag(0x03C0, 2, 0x1E02))
    SetScenaFlags(ScenaFlag(0x03C0, 3, 0x1E03))
    SetScenaFlags(ScenaFlag(0x03C0, 4, 0x1E04))
    SetScenaFlags(ScenaFlag(0x03C0, 5, 0x1E05))
    SetScenaFlags(ScenaFlag(0x03C0, 6, 0x1E06))
    SetScenaFlags(ScenaFlag(0x03C6, 1, 0x1E31))
    SetScenaFlags(ScenaFlag(0x03C0, 7, 0x1E07))
    SetScenaFlags(ScenaFlag(0x03C1, 0, 0x1E08))
    SetScenaFlags(ScenaFlag(0x03C1, 1, 0x1E09))
    AddItem(ItemTable['数据水晶０'], 1)
    AddItem(ItemTable['数据水晶１'], 1)
    AddItem(ItemTable['数据水晶２'], 1)
    AddItem(ItemTable['数据水晶３'], 1)
    SetScenaFlags(ScenaFlag(0x03C1, 2, 0x1E0A))
    SetScenaFlags(ScenaFlag(0x03C1, 3, 0x1E0B))
    SetScenaFlags(ScenaFlag(0x03C1, 4, 0x1E0C))
    SetScenaFlags(ScenaFlag(0x03C1, 5, 0x1E0D))
    SetScenaFlags(ScenaFlag(0x03C1, 6, 0x1E0E))
    SetScenaFlags(ScenaFlag(0x03C1, 7, 0x1E0F))
    SetScenaFlags(ScenaFlag(0x03C2, 0, 0x1E10))
    SetScenaFlags(ScenaFlag(0x03C3, 2, 0x1E1A))
    AddItem(ItemTable['数据水晶４'], 1)
    AddItem(ItemTable['数据水晶５'], 1)
    AddItem(ItemTable['数据水晶６'], 1)
    AddItem(ItemTable['数据水晶７'], 1)
    SetScenaFlags(ScenaFlag(0x03C2, 1, 0x1E11))
    SetScenaFlags(ScenaFlag(0x03C2, 2, 0x1E12))
    SetScenaFlags(ScenaFlag(0x03C2, 3, 0x1E13))
    SetScenaFlags(ScenaFlag(0x03C2, 4, 0x1E14))
    SetScenaFlags(ScenaFlag(0x03C2, 5, 0x1E15))
    AddItem(ItemTable['数据水晶８'], 1)
    SetScenaFlags(ScenaFlag(0x03C3, 3, 0x1E1B))
    SetScenaFlags(ScenaFlag(0x03C2, 6, 0x1E16))
    SetScenaFlags(ScenaFlag(0x03C2, 7, 0x1E17))
    AddItem(ItemTable['数据水晶９'], 1)
    SetScenaFlags(ScenaFlag(0x03C3, 4, 0x1E1C))
    SetScenaFlags(ScenaFlag(0x03C3, 0, 0x1E18))
    SetScenaFlags(ScenaFlag(0x03C3, 1, 0x1E19))
    AddItem(ItemTable['数据水晶１０'], 1)
    SetScenaFlags(ScenaFlag(0x03C4, 1, 0x1E21))
    AddItem(ItemTable['数据水晶１１'], 1)
    SetScenaFlags(ScenaFlag(0x03C4, 2, 0x1E22))
    SetScenaFlags(ScenaFlag(0x03C3, 5, 0x1E1D))
    SetScenaFlags(ScenaFlag(0x03C3, 6, 0x1E1E))
    SetScenaFlags(ScenaFlag(0x03C3, 7, 0x1E1F))
    SetScenaFlags(ScenaFlag(0x03C4, 0, 0x1E20))
    SetScenaFlags(ScenaFlag(0x03C4, 3, 0x1E23))
    SetScenaFlags(ScenaFlag(0x03C6, 2, 0x1E32))
    SetScenaFlags(ScenaFlag(0x03C6, 3, 0x1E33))
    SetScenaFlags(ScenaFlag(0x03C6, 4, 0x1E34))
    AddItem(ItemTable['数据水晶１２'], 1)
    AddItem(ItemTable['数据水晶１３'], 1)
    AddItem(ItemTable['数据水晶１４'], 1)
    AddItem(ItemTable['数据水晶１５'], 1)
    SetScenaFlags(ScenaFlag(0x03C4, 4, 0x1E24))

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

    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C0705._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_402B')

    def _loc_3DBE(): pass

    label('loc_3DBE')

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T4201._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_402B')

    def _loc_3DCD(): pass

    label('loc_3DCD')

    SetScenaFlags(ScenaFlag(0x03C0, 0, 0x1E00))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_402B')

    def _loc_3DE2(): pass

    label('loc_3DE2')

    SetScenaFlags(ScenaFlag(0x03C0, 0, 0x1E00))
    SetScenaFlags(ScenaFlag(0x03C0, 1, 0x1E01))
    SetScenaFlags(ScenaFlag(0x03C0, 2, 0x1E02))
    SetScenaFlags(ScenaFlag(0x03C0, 3, 0x1E03))
    SetScenaFlags(ScenaFlag(0x03C0, 4, 0x1E04))
    SetScenaFlags(ScenaFlag(0x03C0, 5, 0x1E05))
    SetScenaFlags(ScenaFlag(0x03C0, 6, 0x1E06))
    AddItem(ItemTable['数据水晶０'], 1)
    AddItem(ItemTable['数据水晶１'], 1)
    AddItem(ItemTable['数据水晶２'], 1)
    AddItem(ItemTable['数据水晶３'], 1)
    SetScenaFlags(ScenaFlag(0x03C6, 1, 0x1E31))
    SetScenaFlags(ScenaFlag(0x03C0, 7, 0x1E07))
    SetScenaFlags(ScenaFlag(0x03C1, 0, 0x1E08))
    SetScenaFlags(ScenaFlag(0x03C1, 1, 0x1E09))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/R3100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_402B')

    def _loc_3E26(): pass

    label('loc_3E26')

    SetScenaFlags(ScenaFlag(0x03C0, 0, 0x1E00))
    SetScenaFlags(ScenaFlag(0x03C0, 1, 0x1E01))
    SetScenaFlags(ScenaFlag(0x03C0, 2, 0x1E02))
    SetScenaFlags(ScenaFlag(0x03C0, 3, 0x1E03))
    SetScenaFlags(ScenaFlag(0x03C0, 4, 0x1E04))
    SetScenaFlags(ScenaFlag(0x03C0, 5, 0x1E05))
    SetScenaFlags(ScenaFlag(0x03C0, 6, 0x1E06))
    AddItem(ItemTable['数据水晶０'], 1)
    AddItem(ItemTable['数据水晶１'], 1)
    AddItem(ItemTable['数据水晶２'], 1)
    AddItem(ItemTable['数据水晶３'], 1)
    SetScenaFlags(ScenaFlag(0x03C6, 1, 0x1E31))
    SetScenaFlags(ScenaFlag(0x03C0, 7, 0x1E07))
    SetScenaFlags(ScenaFlag(0x03C1, 0, 0x1E08))
    SetScenaFlags(ScenaFlag(0x03C1, 1, 0x1E09))
    SetScenaFlags(ScenaFlag(0x03C1, 2, 0x1E0A))
    SetScenaFlags(ScenaFlag(0x03C1, 3, 0x1E0B))
    SetScenaFlags(ScenaFlag(0x03C1, 4, 0x1E0C))
    SetScenaFlags(ScenaFlag(0x03C1, 5, 0x1E0D))
    AddItem(ItemTable['数据水晶４'], 1)
    AddItem(ItemTable['数据水晶５'], 1)
    AddItem(ItemTable['数据水晶６'], 1)
    AddItem(ItemTable['数据水晶７'], 1)
    SetScenaFlags(ScenaFlag(0x03C1, 6, 0x1E0E))
    SetScenaFlags(ScenaFlag(0x03C1, 7, 0x1E0F))
    SetScenaFlags(ScenaFlag(0x03C2, 0, 0x1E10))
    SetScenaFlags(ScenaFlag(0x03C3, 2, 0x1E1A))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/R2200._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_402B')

    def _loc_3E96(): pass

    label('loc_3E96')

    SetScenaFlags(ScenaFlag(0x03C0, 0, 0x1E00))
    SetScenaFlags(ScenaFlag(0x03C0, 1, 0x1E01))
    SetScenaFlags(ScenaFlag(0x03C0, 2, 0x1E02))
    SetScenaFlags(ScenaFlag(0x03C0, 3, 0x1E03))
    SetScenaFlags(ScenaFlag(0x03C0, 4, 0x1E04))
    SetScenaFlags(ScenaFlag(0x03C0, 5, 0x1E05))
    SetScenaFlags(ScenaFlag(0x03C0, 6, 0x1E06))
    AddItem(ItemTable['数据水晶０'], 1)
    AddItem(ItemTable['数据水晶１'], 1)
    AddItem(ItemTable['数据水晶２'], 1)
    AddItem(ItemTable['数据水晶３'], 1)
    SetScenaFlags(ScenaFlag(0x03C6, 1, 0x1E31))
    SetScenaFlags(ScenaFlag(0x03C0, 7, 0x1E07))
    SetScenaFlags(ScenaFlag(0x03C1, 0, 0x1E08))
    SetScenaFlags(ScenaFlag(0x03C1, 1, 0x1E09))
    SetScenaFlags(ScenaFlag(0x03C1, 2, 0x1E0A))
    SetScenaFlags(ScenaFlag(0x03C1, 3, 0x1E0B))
    SetScenaFlags(ScenaFlag(0x03C1, 4, 0x1E0C))
    SetScenaFlags(ScenaFlag(0x03C1, 5, 0x1E0D))
    AddItem(ItemTable['数据水晶４'], 1)
    AddItem(ItemTable['数据水晶５'], 1)
    AddItem(ItemTable['数据水晶６'], 1)
    AddItem(ItemTable['数据水晶７'], 1)
    SetScenaFlags(ScenaFlag(0x03C1, 6, 0x1E0E))
    SetScenaFlags(ScenaFlag(0x03C1, 7, 0x1E0F))
    SetScenaFlags(ScenaFlag(0x03C2, 0, 0x1E10))
    SetScenaFlags(ScenaFlag(0x03C3, 2, 0x1E1A))
    SetScenaFlags(ScenaFlag(0x03C2, 1, 0x1E11))
    SetScenaFlags(ScenaFlag(0x03C2, 2, 0x1E12))
    SetScenaFlags(ScenaFlag(0x03C2, 3, 0x1E13))
    SetScenaFlags(ScenaFlag(0x03C2, 4, 0x1E14))
    SetScenaFlags(ScenaFlag(0x03C2, 5, 0x1E15))
    AddItem(ItemTable['数据水晶８'], 1)
    SetScenaFlags(ScenaFlag(0x03C3, 3, 0x1E1B))
    SetScenaFlags(ScenaFlag(0x03C2, 6, 0x1E16))
    SetScenaFlags(ScenaFlag(0x03C2, 7, 0x1E17))
    AddItem(ItemTable['数据水晶９'], 1)
    SetScenaFlags(ScenaFlag(0x03C3, 4, 0x1E1C))
    SetScenaFlags(ScenaFlag(0x03C3, 0, 0x1E18))
    SetScenaFlags(ScenaFlag(0x03C3, 1, 0x1E19))
    AddItem(ItemTable['数据水晶１０'], 1)
    SetScenaFlags(ScenaFlag(0x03C4, 1, 0x1E21))
    AddItem(ItemTable['数据水晶１１'], 1)
    SetScenaFlags(ScenaFlag(0x03C4, 2, 0x1E22))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_402B')

    def _loc_3F44(): pass

    label('loc_3F44')

    SetScenaFlags(ScenaFlag(0x03C0, 0, 0x1E00))
    SetScenaFlags(ScenaFlag(0x03C0, 1, 0x1E01))
    SetScenaFlags(ScenaFlag(0x03C0, 2, 0x1E02))
    SetScenaFlags(ScenaFlag(0x03C0, 3, 0x1E03))
    SetScenaFlags(ScenaFlag(0x03C0, 4, 0x1E04))
    SetScenaFlags(ScenaFlag(0x03C0, 5, 0x1E05))
    SetScenaFlags(ScenaFlag(0x03C0, 6, 0x1E06))
    AddItem(ItemTable['数据水晶０'], 1)
    AddItem(ItemTable['数据水晶１'], 1)
    AddItem(ItemTable['数据水晶２'], 1)
    AddItem(ItemTable['数据水晶３'], 1)
    SetScenaFlags(ScenaFlag(0x03C6, 1, 0x1E31))
    SetScenaFlags(ScenaFlag(0x03C0, 7, 0x1E07))
    SetScenaFlags(ScenaFlag(0x03C1, 0, 0x1E08))
    SetScenaFlags(ScenaFlag(0x03C1, 1, 0x1E09))
    SetScenaFlags(ScenaFlag(0x03C1, 2, 0x1E0A))
    SetScenaFlags(ScenaFlag(0x03C1, 3, 0x1E0B))
    SetScenaFlags(ScenaFlag(0x03C1, 4, 0x1E0C))
    SetScenaFlags(ScenaFlag(0x03C1, 5, 0x1E0D))
    AddItem(ItemTable['数据水晶４'], 1)
    AddItem(ItemTable['数据水晶５'], 1)
    AddItem(ItemTable['数据水晶６'], 1)
    AddItem(ItemTable['数据水晶７'], 1)
    SetScenaFlags(ScenaFlag(0x03C1, 6, 0x1E0E))
    SetScenaFlags(ScenaFlag(0x03C1, 7, 0x1E0F))
    SetScenaFlags(ScenaFlag(0x03C2, 0, 0x1E10))
    SetScenaFlags(ScenaFlag(0x03C3, 2, 0x1E1A))
    SetScenaFlags(ScenaFlag(0x03C2, 1, 0x1E11))
    SetScenaFlags(ScenaFlag(0x03C2, 2, 0x1E12))
    SetScenaFlags(ScenaFlag(0x03C2, 3, 0x1E13))
    SetScenaFlags(ScenaFlag(0x03C2, 4, 0x1E14))
    SetScenaFlags(ScenaFlag(0x03C2, 5, 0x1E15))
    AddItem(ItemTable['数据水晶８'], 1)
    SetScenaFlags(ScenaFlag(0x03C3, 3, 0x1E1B))
    SetScenaFlags(ScenaFlag(0x03C2, 6, 0x1E16))
    SetScenaFlags(ScenaFlag(0x03C2, 7, 0x1E17))
    AddItem(ItemTable['数据水晶９'], 1)
    SetScenaFlags(ScenaFlag(0x03C3, 4, 0x1E1C))
    SetScenaFlags(ScenaFlag(0x03C3, 0, 0x1E18))
    SetScenaFlags(ScenaFlag(0x03C3, 1, 0x1E19))
    AddItem(ItemTable['数据水晶１０'], 1)
    SetScenaFlags(ScenaFlag(0x03C4, 1, 0x1E21))
    AddItem(ItemTable['数据水晶１１'], 1)
    SetScenaFlags(ScenaFlag(0x03C4, 2, 0x1E22))
    SetScenaFlags(ScenaFlag(0x03C3, 5, 0x1E1D))
    SetScenaFlags(ScenaFlag(0x03C3, 6, 0x1E1E))
    SetScenaFlags(ScenaFlag(0x03C3, 7, 0x1E1F))
    SetScenaFlags(ScenaFlag(0x03C4, 0, 0x1E20))
    AddItem(ItemTable['数据水晶１１'], 1)
    AddItem(ItemTable['数据水晶１３'], 1)
    AddItem(ItemTable['数据水晶１４'], 1)
    AddItem(ItemTable['数据水晶１５'], 1)
    SetScenaFlags(ScenaFlag(0x03C4, 3, 0x1E23))
    SetScenaFlags(ScenaFlag(0x03C6, 2, 0x1E32))
    SetScenaFlags(ScenaFlag(0x03C6, 3, 0x1E33))
    SetScenaFlags(ScenaFlag(0x03C6, 4, 0x1E34))
    SetScenaFlags(ScenaFlag(0x03C4, 4, 0x1E24))
    SetScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
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
    ClearScenaFlags(ScenaFlag(0x0400, 0, 0x2000))
    ClearScenaFlags(ScenaFlag(0x0400, 1, 0x2001))
    ClearScenaFlags(ScenaFlag(0x0400, 2, 0x2002))
    ClearScenaFlags(ScenaFlag(0x0400, 3, 0x2003))
    ClearScenaFlags(ScenaFlag(0x0400, 4, 0x2004))
    ClearScenaFlags(ScenaFlag(0x0400, 5, 0x2005))
    ClearScenaFlags(ScenaFlag(0x0400, 6, 0x2006))
    ClearScenaFlags(ScenaFlag(0x0400, 7, 0x2007))
    ClearScenaFlags(ScenaFlag(0x0401, 0, 0x2008))
    ClearScenaFlags(ScenaFlag(0x0401, 1, 0x2009))
    ClearScenaFlags(ScenaFlag(0x0401, 2, 0x200A))
    ClearScenaFlags(ScenaFlag(0x0401, 3, 0x200B))
    ClearScenaFlags(ScenaFlag(0x0401, 4, 0x200C))
    ClearScenaFlags(ScenaFlag(0x0401, 5, 0x200D))
    ClearScenaFlags(ScenaFlag(0x0401, 6, 0x200E))
    ClearScenaFlags(ScenaFlag(0x0401, 7, 0x200F))
    ClearScenaFlags(ScenaFlag(0x0402, 0, 0x2010))
    ClearScenaFlags(ScenaFlag(0x0402, 1, 0x2011))
    ClearScenaFlags(ScenaFlag(0x0402, 2, 0x2012))
    ClearScenaFlags(ScenaFlag(0x0402, 3, 0x2013))
    ClearScenaFlags(ScenaFlag(0x0402, 4, 0x2014))
    ClearScenaFlags(ScenaFlag(0x0402, 5, 0x2015))
    ClearScenaFlags(ScenaFlag(0x0402, 6, 0x2016))
    ClearScenaFlags(ScenaFlag(0x0402, 7, 0x2017))
    ClearScenaFlags(ScenaFlag(0x0403, 0, 0x2018))
    ClearScenaFlags(ScenaFlag(0x0403, 1, 0x2019))
    ClearScenaFlags(ScenaFlag(0x0403, 2, 0x201A))
    ClearScenaFlags(ScenaFlag(0x0403, 3, 0x201B))
    ClearScenaFlags(ScenaFlag(0x0403, 4, 0x201C))
    ClearScenaFlags(ScenaFlag(0x0403, 5, 0x201D))
    ClearScenaFlags(ScenaFlag(0x0403, 6, 0x201E))
    ClearScenaFlags(ScenaFlag(0x0403, 7, 0x201F))
    ClearScenaFlags(ScenaFlag(0x0404, 0, 0x2020))
    ClearScenaFlags(ScenaFlag(0x0404, 1, 0x2021))
    ClearScenaFlags(ScenaFlag(0x0404, 2, 0x2022))
    ClearScenaFlags(ScenaFlag(0x0404, 3, 0x2023))
    ClearScenaFlags(ScenaFlag(0x0404, 4, 0x2024))
    ClearScenaFlags(ScenaFlag(0x0404, 5, 0x2025))
    ClearScenaFlags(ScenaFlag(0x0404, 6, 0x2026))
    ClearScenaFlags(ScenaFlag(0x0404, 7, 0x2027))
    ClearScenaFlags(ScenaFlag(0x0405, 0, 0x2028))
    ClearScenaFlags(ScenaFlag(0x0405, 1, 0x2029))
    ClearScenaFlags(ScenaFlag(0x0405, 2, 0x202A))
    ClearScenaFlags(ScenaFlag(0x0405, 3, 0x202B))
    ClearScenaFlags(ScenaFlag(0x0405, 4, 0x202C))
    ClearScenaFlags(ScenaFlag(0x0405, 5, 0x202D))
    ClearScenaFlags(ScenaFlag(0x0405, 6, 0x202E))
    ClearScenaFlags(ScenaFlag(0x0405, 7, 0x202F))
    ClearScenaFlags(ScenaFlag(0x0406, 0, 0x2030))
    ClearScenaFlags(ScenaFlag(0x0406, 1, 0x2031))
    ClearScenaFlags(ScenaFlag(0x0406, 2, 0x2032))
    ClearScenaFlags(ScenaFlag(0x0406, 3, 0x2033))
    ClearScenaFlags(ScenaFlag(0x0406, 4, 0x2034))
    ClearScenaFlags(ScenaFlag(0x0406, 5, 0x2035))
    ClearScenaFlags(ScenaFlag(0x0406, 6, 0x2036))
    ClearScenaFlags(ScenaFlag(0x0406, 7, 0x2037))
    ClearScenaFlags(ScenaFlag(0x0407, 0, 0x2038))
    ClearScenaFlags(ScenaFlag(0x0407, 1, 0x2039))
    ClearScenaFlags(ScenaFlag(0x0407, 2, 0x203A))
    ClearScenaFlags(ScenaFlag(0x0407, 3, 0x203B))
    ClearScenaFlags(ScenaFlag(0x0407, 4, 0x203C))
    ClearScenaFlags(ScenaFlag(0x0407, 5, 0x203D))
    ClearScenaFlags(ScenaFlag(0x0407, 6, 0x203E))
    ClearScenaFlags(ScenaFlag(0x0407, 7, 0x203F))
    ClearScenaFlags(ScenaFlag(0x0410, 0, 0x2080))
    ClearScenaFlags(ScenaFlag(0x0410, 1, 0x2081))
    ClearScenaFlags(ScenaFlag(0x0410, 2, 0x2082))
    ClearScenaFlags(ScenaFlag(0x0410, 3, 0x2083))
    ClearScenaFlags(ScenaFlag(0x0410, 4, 0x2084))
    ClearScenaFlags(ScenaFlag(0x0412, 0, 0x2090))
    ClearScenaFlags(ScenaFlag(0x0412, 1, 0x2091))
    ClearScenaFlags(ScenaFlag(0x0416, 7, 0x20B7))
    ClearScenaFlags(ScenaFlag(0x0417, 0, 0x20B8))
    ClearScenaFlags(ScenaFlag(0x0417, 1, 0x20B9))

    Return()

# id: 0x001C offset: 0x413B
@scena.Code('func_1C_413B')
def func_1C_413B():
    SetScenaFlags(ScenaFlag(0x0400, 0, 0x2000))

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
    SetScenaFlags(ScenaFlag(0x0400, 1, 0x2001))
    SetScenaFlags(ScenaFlag(0x0400, 2, 0x2002))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 3, 0x2003))
    SetScenaFlags(ScenaFlag(0x0412, 1, 0x2091))
    SetScenaFlags(ScenaFlag(0x0400, 4, 0x2004))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 5, 0x2005))
    SetScenaFlags(ScenaFlag(0x0400, 6, 0x2006))
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 7, 0x2007))
    SetScenaFlags(ScenaFlag(0x0401, 0, 0x2008))
    SetScenaFlags(ScenaFlag(0x0401, 1, 0x2009))
    SetScenaFlags(ScenaFlag(0x0401, 2, 0x200A))
    SetScenaFlags(ScenaFlag(0x0401, 3, 0x200B))
    SetScenaFlags(ScenaFlag(0x0401, 5, 0x200D))
    ClearScenaFlags(ScenaFlag(0x0401, 6, 0x200E))
    SetScenaFlags(ScenaFlag(0x0401, 7, 0x200F))
    AddItem(ItemTable['工房长的介绍信'], 1)
    SetScenaFlags(ScenaFlag(0x0402, 0, 0x2010))
    SetScenaFlags(ScenaFlag(0x0402, 1, 0x2011))
    SetScenaFlags(ScenaFlag(0x0402, 2, 0x2012))
    SetScenaFlags(ScenaFlag(0x0402, 3, 0x2013))
    SetScenaFlags(ScenaFlag(0x0402, 4, 0x2014))
    SetScenaFlags(ScenaFlag(0x0402, 5, 0x2015))
    SetScenaFlags(ScenaFlag(0x0402, 6, 0x2016))
    SetScenaFlags(ScenaFlag(0x0402, 7, 0x2017))
    SetScenaFlags(ScenaFlag(0x0403, 0, 0x2018))
    SetScenaFlags(ScenaFlag(0x0403, 1, 0x2019))
    SetScenaFlags(ScenaFlag(0x0403, 2, 0x201A))
    SetScenaFlags(ScenaFlag(0x0403, 3, 0x201B))
    AddItem(ItemTable['人质名单'], 1)
    SetScenaFlags(ScenaFlag(0x0403, 4, 0x201C))
    SetScenaFlags(ScenaFlag(0x0403, 5, 0x201D))
    SetScenaFlags(ScenaFlag(0x0403, 6, 0x201E))
    SetScenaFlags(ScenaFlag(0x0403, 7, 0x201F))
    SetScenaFlags(ScenaFlag(0x0404, 0, 0x2020))
    SetScenaFlags(ScenaFlag(0x0404, 1, 0x2021))
    SetScenaFlags(ScenaFlag(0x0404, 2, 0x2022))
    SetScenaFlags(ScenaFlag(0x0404, 3, 0x2023))
    SetScenaFlags(ScenaFlag(0x0404, 4, 0x2024))
    SetScenaFlags(ScenaFlag(0x0404, 5, 0x2025))
    SetScenaFlags(ScenaFlag(0x0404, 6, 0x2026))
    SetScenaFlags(ScenaFlag(0x0404, 7, 0x2027))
    SetScenaFlags(ScenaFlag(0x0405, 0, 0x2028))
    SetScenaFlags(ScenaFlag(0x0405, 1, 0x2029))
    SetScenaFlags(ScenaFlag(0x0405, 2, 0x202A))
    SetScenaFlags(ScenaFlag(0x0405, 3, 0x202B))
    SetScenaFlags(ScenaFlag(0x0405, 4, 0x202C))
    SetScenaFlags(ScenaFlag(0x0405, 5, 0x202D))
    SetScenaFlags(ScenaFlag(0x0405, 6, 0x202E))
    SetScenaFlags(ScenaFlag(0x0405, 7, 0x202F))
    SetScenaFlags(ScenaFlag(0x0407, 0, 0x2038))
    SetScenaFlags(ScenaFlag(0x0407, 1, 0x2039))
    SetScenaFlags(ScenaFlag(0x0407, 2, 0x203A))
    SetScenaFlags(ScenaFlag(0x0407, 3, 0x203B))
    SetScenaFlags(ScenaFlag(0x0407, 4, 0x203C))
    SetScenaFlags(ScenaFlag(0x0407, 5, 0x203D))
    SetScenaFlags(ScenaFlag(0x0407, 6, 0x203E))
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

    SetScenaFlags(ScenaFlag(0x021F, 5, 0x10FD))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_43DB(): pass

    label('loc_43DB')

    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T2100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_43EA(): pass

    label('loc_43EA')

    SetScenaFlags(ScenaFlag(0x0400, 0, 0x2000))

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
    SetScenaFlags(ScenaFlag(0x0400, 1, 0x2001))
    SetScenaFlags(ScenaFlag(0x0400, 2, 0x2002))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 3, 0x2003))
    SetScenaFlags(ScenaFlag(0x0412, 1, 0x2091))
    SetScenaFlags(ScenaFlag(0x0400, 4, 0x2004))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 5, 0x2005))
    SetScenaFlags(ScenaFlag(0x0400, 6, 0x2006))
    NewScene('ED6_DT21/T3221._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_442B(): pass

    label('loc_442B')

    SetScenaFlags(ScenaFlag(0x0400, 0, 0x2000))

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
    SetScenaFlags(ScenaFlag(0x0400, 1, 0x2001))
    SetScenaFlags(ScenaFlag(0x0400, 2, 0x2002))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 3, 0x2003))
    SetScenaFlags(ScenaFlag(0x0412, 1, 0x2091))
    SetScenaFlags(ScenaFlag(0x0400, 4, 0x2004))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 5, 0x2005))
    SetScenaFlags(ScenaFlag(0x0400, 6, 0x2006))
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 7, 0x2007))
    SetScenaFlags(ScenaFlag(0x0401, 0, 0x2008))
    SetScenaFlags(ScenaFlag(0x0401, 1, 0x2009))
    SetScenaFlags(ScenaFlag(0x0401, 2, 0x200A))
    SetScenaFlags(ScenaFlag(0x0401, 3, 0x200B))
    SetScenaFlags(ScenaFlag(0x0401, 5, 0x200D))
    ClearScenaFlags(ScenaFlag(0x0401, 6, 0x200E))
    SetScenaFlags(ScenaFlag(0x0401, 7, 0x200F))
    AddItem(ItemTable['工房长的介绍信'], 1)
    SetScenaFlags(ScenaFlag(0x0402, 0, 0x2010))
    SetScenaFlags(ScenaFlag(0x0402, 1, 0x2011))
    SetScenaFlags(ScenaFlag(0x0402, 2, 0x2012))
    NewScene('ED6_DT21/R2300._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_4497(): pass

    label('loc_4497')

    SetScenaFlags(ScenaFlag(0x0400, 0, 0x2000))

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
    SetScenaFlags(ScenaFlag(0x0400, 1, 0x2001))
    SetScenaFlags(ScenaFlag(0x0400, 2, 0x2002))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 3, 0x2003))
    SetScenaFlags(ScenaFlag(0x0412, 1, 0x2091))
    SetScenaFlags(ScenaFlag(0x0400, 4, 0x2004))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 5, 0x2005))
    SetScenaFlags(ScenaFlag(0x0400, 6, 0x2006))
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 7, 0x2007))
    SetScenaFlags(ScenaFlag(0x0401, 0, 0x2008))
    SetScenaFlags(ScenaFlag(0x0401, 1, 0x2009))
    SetScenaFlags(ScenaFlag(0x0401, 2, 0x200A))
    SetScenaFlags(ScenaFlag(0x0401, 3, 0x200B))
    SetScenaFlags(ScenaFlag(0x0401, 5, 0x200D))
    ClearScenaFlags(ScenaFlag(0x0401, 6, 0x200E))
    SetScenaFlags(ScenaFlag(0x0401, 7, 0x200F))
    AddItem(ItemTable['工房长的介绍信'], 1)
    SetScenaFlags(ScenaFlag(0x0402, 0, 0x2010))
    SetScenaFlags(ScenaFlag(0x0402, 1, 0x2011))
    SetScenaFlags(ScenaFlag(0x0402, 2, 0x2012))
    SetScenaFlags(ScenaFlag(0x0402, 3, 0x2013))
    SetScenaFlags(ScenaFlag(0x0402, 4, 0x2014))
    SetScenaFlags(ScenaFlag(0x0402, 5, 0x2015))
    SetScenaFlags(ScenaFlag(0x0402, 6, 0x2016))
    SetScenaFlags(ScenaFlag(0x0402, 7, 0x2017))
    SetScenaFlags(ScenaFlag(0x0403, 0, 0x2018))
    SetScenaFlags(ScenaFlag(0x0403, 1, 0x2019))
    SetScenaFlags(ScenaFlag(0x0403, 2, 0x201A))
    SetScenaFlags(ScenaFlag(0x0403, 3, 0x201B))
    AddItem(ItemTable['人质名单'], 1)
    SetScenaFlags(ScenaFlag(0x0403, 4, 0x201C))
    SetScenaFlags(ScenaFlag(0x0403, 5, 0x201D))
    SetScenaFlags(ScenaFlag(0x0403, 6, 0x201E))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['克鲁茨'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0403, 7, 0x201F))
    SetScenaFlags(ScenaFlag(0x0404, 0, 0x2020))
    SetScenaFlags(ScenaFlag(0x0404, 1, 0x2021))
    SetScenaFlags(ScenaFlag(0x0404, 2, 0x2022))
    SetScenaFlags(ScenaFlag(0x0404, 3, 0x2023))
    SetScenaFlags(ScenaFlag(0x0404, 4, 0x2024))
    SetScenaFlags(ScenaFlag(0x0404, 5, 0x2025))
    SetScenaFlags(ScenaFlag(0x0404, 6, 0x2026))
    SetScenaFlags(ScenaFlag(0x0404, 7, 0x2027))
    SetScenaFlags(ScenaFlag(0x0405, 0, 0x2028))
    SetScenaFlags(ScenaFlag(0x0405, 1, 0x2029))
    SetScenaFlags(ScenaFlag(0x0405, 2, 0x202A))
    SetScenaFlags(ScenaFlag(0x0405, 3, 0x202B))
    SetScenaFlags(ScenaFlag(0x0405, 4, 0x202C))
    SetScenaFlags(ScenaFlag(0x0405, 5, 0x202D))
    SetScenaFlags(ScenaFlag(0x0405, 6, 0x202E))
    SetScenaFlags(ScenaFlag(0x0405, 7, 0x202F))
    NewScene('ED6_DT21/T2100._SN', 105, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_4570(): pass

    label('loc_4570')

    SetScenaFlags(ScenaFlag(0x0400, 0, 0x2000))

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
    SetScenaFlags(ScenaFlag(0x0400, 1, 0x2001))
    SetScenaFlags(ScenaFlag(0x0400, 2, 0x2002))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 3, 0x2003))
    SetScenaFlags(ScenaFlag(0x0412, 1, 0x2091))
    SetScenaFlags(ScenaFlag(0x0400, 4, 0x2004))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 5, 0x2005))
    SetScenaFlags(ScenaFlag(0x0400, 6, 0x2006))
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 7, 0x2007))
    SetScenaFlags(ScenaFlag(0x0401, 0, 0x2008))
    SetScenaFlags(ScenaFlag(0x0401, 1, 0x2009))
    SetScenaFlags(ScenaFlag(0x0401, 2, 0x200A))
    SetScenaFlags(ScenaFlag(0x0401, 3, 0x200B))
    SetScenaFlags(ScenaFlag(0x0401, 5, 0x200D))
    ClearScenaFlags(ScenaFlag(0x0401, 6, 0x200E))
    SetScenaFlags(ScenaFlag(0x0401, 7, 0x200F))
    AddItem(ItemTable['工房长的介绍信'], 1)
    SetScenaFlags(ScenaFlag(0x0402, 0, 0x2010))
    SetScenaFlags(ScenaFlag(0x0402, 1, 0x2011))
    SetScenaFlags(ScenaFlag(0x0402, 2, 0x2012))
    SetScenaFlags(ScenaFlag(0x0402, 3, 0x2013))
    SetScenaFlags(ScenaFlag(0x0402, 4, 0x2014))
    SetScenaFlags(ScenaFlag(0x0402, 5, 0x2015))
    SetScenaFlags(ScenaFlag(0x0402, 6, 0x2016))
    SetScenaFlags(ScenaFlag(0x0402, 7, 0x2017))
    SetScenaFlags(ScenaFlag(0x0403, 0, 0x2018))
    SetScenaFlags(ScenaFlag(0x0403, 1, 0x2019))
    SetScenaFlags(ScenaFlag(0x0403, 2, 0x201A))
    SetScenaFlags(ScenaFlag(0x0403, 3, 0x201B))
    AddItem(ItemTable['人质名单'], 1)
    SetScenaFlags(ScenaFlag(0x0403, 4, 0x201C))
    SetScenaFlags(ScenaFlag(0x0403, 5, 0x201D))
    SetScenaFlags(ScenaFlag(0x0403, 6, 0x201E))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['克鲁茨'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0403, 7, 0x201F))
    SetScenaFlags(ScenaFlag(0x0404, 0, 0x2020))
    SetScenaFlags(ScenaFlag(0x0404, 1, 0x2021))
    SetScenaFlags(ScenaFlag(0x0404, 2, 0x2022))
    SetScenaFlags(ScenaFlag(0x0404, 3, 0x2023))
    SetScenaFlags(ScenaFlag(0x0404, 4, 0x2024))
    SetScenaFlags(ScenaFlag(0x0404, 5, 0x2025))
    SetScenaFlags(ScenaFlag(0x0404, 6, 0x2026))
    SetScenaFlags(ScenaFlag(0x0404, 7, 0x2027))
    SetScenaFlags(ScenaFlag(0x0405, 0, 0x2028))
    SetScenaFlags(ScenaFlag(0x0405, 1, 0x2029))
    SetScenaFlags(ScenaFlag(0x0405, 2, 0x202A))
    SetScenaFlags(ScenaFlag(0x0405, 3, 0x202B))
    SetScenaFlags(ScenaFlag(0x0405, 4, 0x202C))
    SetScenaFlags(ScenaFlag(0x0405, 5, 0x202D))
    SetScenaFlags(ScenaFlag(0x0405, 6, 0x202E))
    SetScenaFlags(ScenaFlag(0x0405, 7, 0x202F))
    NewScene('ED6_DT21/R4100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_4649(): pass

    label('loc_4649')

    SetScenaFlags(ScenaFlag(0x0400, 0, 0x2000))

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
    SetScenaFlags(ScenaFlag(0x0400, 1, 0x2001))
    SetScenaFlags(ScenaFlag(0x0400, 2, 0x2002))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 3, 0x2003))
    SetScenaFlags(ScenaFlag(0x0412, 1, 0x2091))
    SetScenaFlags(ScenaFlag(0x0400, 4, 0x2004))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 5, 0x2005))
    SetScenaFlags(ScenaFlag(0x0400, 6, 0x2006))
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 7, 0x2007))
    SetScenaFlags(ScenaFlag(0x0401, 0, 0x2008))
    SetScenaFlags(ScenaFlag(0x0401, 1, 0x2009))
    SetScenaFlags(ScenaFlag(0x0401, 2, 0x200A))
    SetScenaFlags(ScenaFlag(0x0401, 3, 0x200B))
    SetScenaFlags(ScenaFlag(0x0401, 5, 0x200D))
    ClearScenaFlags(ScenaFlag(0x0401, 6, 0x200E))
    SetScenaFlags(ScenaFlag(0x0401, 7, 0x200F))
    AddItem(ItemTable['工房长的介绍信'], 1)
    SetScenaFlags(ScenaFlag(0x0402, 0, 0x2010))
    SetScenaFlags(ScenaFlag(0x0402, 1, 0x2011))
    SetScenaFlags(ScenaFlag(0x0402, 2, 0x2012))
    SetScenaFlags(ScenaFlag(0x0402, 3, 0x2013))
    SetScenaFlags(ScenaFlag(0x0402, 4, 0x2014))
    SetScenaFlags(ScenaFlag(0x0402, 5, 0x2015))
    SetScenaFlags(ScenaFlag(0x0402, 6, 0x2016))
    SetScenaFlags(ScenaFlag(0x0402, 7, 0x2017))
    SetScenaFlags(ScenaFlag(0x0403, 0, 0x2018))
    SetScenaFlags(ScenaFlag(0x0403, 1, 0x2019))
    SetScenaFlags(ScenaFlag(0x0403, 2, 0x201A))
    SetScenaFlags(ScenaFlag(0x0403, 3, 0x201B))
    AddItem(ItemTable['人质名单'], 1)
    SetScenaFlags(ScenaFlag(0x0403, 4, 0x201C))
    SetScenaFlags(ScenaFlag(0x0403, 5, 0x201D))
    SetScenaFlags(ScenaFlag(0x0403, 6, 0x201E))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['克鲁茨'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0403, 7, 0x201F))
    SetScenaFlags(ScenaFlag(0x0404, 0, 0x2020))
    SetScenaFlags(ScenaFlag(0x0404, 1, 0x2021))
    SetScenaFlags(ScenaFlag(0x0404, 2, 0x2022))
    SetScenaFlags(ScenaFlag(0x0404, 3, 0x2023))
    SetScenaFlags(ScenaFlag(0x0404, 4, 0x2024))
    SetScenaFlags(ScenaFlag(0x0404, 5, 0x2025))
    SetScenaFlags(ScenaFlag(0x0404, 6, 0x2026))
    SetScenaFlags(ScenaFlag(0x0404, 7, 0x2027))
    SetScenaFlags(ScenaFlag(0x0405, 0, 0x2028))
    SetScenaFlags(ScenaFlag(0x0405, 1, 0x2029))
    SetScenaFlags(ScenaFlag(0x0405, 2, 0x202A))
    SetScenaFlags(ScenaFlag(0x0405, 3, 0x202B))
    SetScenaFlags(ScenaFlag(0x0405, 4, 0x202C))
    SetScenaFlags(ScenaFlag(0x0405, 5, 0x202D))
    SetScenaFlags(ScenaFlag(0x0405, 6, 0x202E))
    SetScenaFlags(ScenaFlag(0x0405, 7, 0x202F))
    SetScenaFlags(ScenaFlag(0x0407, 0, 0x2038))
    SetScenaFlags(ScenaFlag(0x0407, 1, 0x2039))
    SetScenaFlags(ScenaFlag(0x0407, 2, 0x203A))
    SetScenaFlags(ScenaFlag(0x0407, 3, 0x203B))
    SetScenaFlags(ScenaFlag(0x0407, 4, 0x203C))
    SetScenaFlags(ScenaFlag(0x0407, 5, 0x203D))
    SetScenaFlags(ScenaFlag(0x0407, 6, 0x203E))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1400._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_473A(): pass

    label('loc_473A')

    SetScenaFlags(ScenaFlag(0x0400, 0, 0x2000))

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AddItem(ItemTable['零力场发生器'], 4)
    ClearScenaFlags(ScenaFlag(0x0412, 1, 0x2091))
    SetScenaFlags(ScenaFlag(0x0410, 5, 0x2085))
    ClearScenaFlags(ScenaFlag(0x0410, 6, 0x2086))
    NewScene('ED6_DT21/T0130._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_4760(): pass

    label('loc_4760')

    SetScenaFlags(ScenaFlag(0x0400, 0, 0x2000))

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
    SetScenaFlags(ScenaFlag(0x0400, 3, 0x2003))
    ClearScenaFlags(ScenaFlag(0x0410, 7, 0x2087))
    ClearScenaFlags(ScenaFlag(0x0411, 0, 0x2088))
    ClearScenaFlags(ScenaFlag(0x0411, 1, 0x2089))
    ClearScenaFlags(ScenaFlag(0x0411, 2, 0x208A))
    ClearScenaFlags(ScenaFlag(0x0411, 3, 0x208B))
    ClearScenaFlags(ScenaFlag(0x0411, 4, 0x208C))
    ClearScenaFlags(ScenaFlag(0x0411, 5, 0x208D))
    ClearScenaFlags(ScenaFlag(0x0410, 5, 0x2085))
    ClearScenaFlags(ScenaFlag(0x0411, 6, 0x208E))
    NewScene('ED6_DT21/C0101._SN', 102, 0, 0)
    IdleLoop()

    Jump('loc_489E')

    def _loc_47A0(): pass

    label('loc_47A0')

    SetScenaFlags(ScenaFlag(0x0400, 0, 0x2000))

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
    SetScenaFlags(ScenaFlag(0x0400, 1, 0x2001))
    SetScenaFlags(ScenaFlag(0x0400, 2, 0x2002))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 3, 0x2003))
    SetScenaFlags(ScenaFlag(0x0412, 1, 0x2091))
    SetScenaFlags(ScenaFlag(0x0400, 4, 0x2004))
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 5, 0x2005))
    SetScenaFlags(ScenaFlag(0x0400, 6, 0x2006))
    AddItem(ItemTable['水泵小屋的钥匙'], 1)
    SetScenaFlags(ScenaFlag(0x0400, 7, 0x2007))
    SetScenaFlags(ScenaFlag(0x0401, 0, 0x2008))
    SetScenaFlags(ScenaFlag(0x0401, 1, 0x2009))
    SetScenaFlags(ScenaFlag(0x0401, 2, 0x200A))
    SetScenaFlags(ScenaFlag(0x0401, 3, 0x200B))
    SetScenaFlags(ScenaFlag(0x0401, 5, 0x200D))
    ClearScenaFlags(ScenaFlag(0x0401, 6, 0x200E))
    SetScenaFlags(ScenaFlag(0x0401, 7, 0x200F))
    AddItem(ItemTable['工房长的介绍信'], 1)
    SetScenaFlags(ScenaFlag(0x0402, 0, 0x2010))
    SetScenaFlags(ScenaFlag(0x0402, 1, 0x2011))
    SetScenaFlags(ScenaFlag(0x0402, 2, 0x2012))
    SetScenaFlags(ScenaFlag(0x0402, 3, 0x2013))
    SetScenaFlags(ScenaFlag(0x0402, 4, 0x2014))
    SetScenaFlags(ScenaFlag(0x0402, 5, 0x2015))
    SetScenaFlags(ScenaFlag(0x0402, 6, 0x2016))
    SetScenaFlags(ScenaFlag(0x0402, 7, 0x2017))
    SetScenaFlags(ScenaFlag(0x0403, 0, 0x2018))
    SetScenaFlags(ScenaFlag(0x0403, 1, 0x2019))
    SetScenaFlags(ScenaFlag(0x0403, 2, 0x201A))
    SetScenaFlags(ScenaFlag(0x0403, 3, 0x201B))
    AddItem(ItemTable['人质名单'], 1)
    SetScenaFlags(ScenaFlag(0x0403, 4, 0x201C))
    SetScenaFlags(ScenaFlag(0x0403, 5, 0x201D))
    SetScenaFlags(ScenaFlag(0x0403, 6, 0x201E))
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['克鲁茨'], 0xF9, 0xFF)
    SetScenaFlags(ScenaFlag(0x0403, 7, 0x201F))
    SetScenaFlags(ScenaFlag(0x0404, 0, 0x2020))
    SetScenaFlags(ScenaFlag(0x0404, 1, 0x2021))
    SetScenaFlags(ScenaFlag(0x0404, 2, 0x2022))
    SetScenaFlags(ScenaFlag(0x0404, 3, 0x2023))
    SetScenaFlags(ScenaFlag(0x0404, 4, 0x2024))
    SetScenaFlags(ScenaFlag(0x0404, 5, 0x2025))
    SetScenaFlags(ScenaFlag(0x0404, 6, 0x2026))
    SetScenaFlags(ScenaFlag(0x0404, 7, 0x2027))
    SetScenaFlags(ScenaFlag(0x0405, 0, 0x2028))
    SetScenaFlags(ScenaFlag(0x0405, 1, 0x2029))
    SetScenaFlags(ScenaFlag(0x0405, 2, 0x202A))
    SetScenaFlags(ScenaFlag(0x0405, 3, 0x202B))
    SetScenaFlags(ScenaFlag(0x0405, 4, 0x202C))
    SetScenaFlags(ScenaFlag(0x0405, 5, 0x202D))
    SetScenaFlags(ScenaFlag(0x0405, 6, 0x202E))
    SetScenaFlags(ScenaFlag(0x0405, 7, 0x202F))
    SetScenaFlags(ScenaFlag(0x0407, 0, 0x2038))
    SetScenaFlags(ScenaFlag(0x0407, 1, 0x2039))
    SetScenaFlags(ScenaFlag(0x0407, 2, 0x203A))
    SetScenaFlags(ScenaFlag(0x0407, 3, 0x203B))
    SetScenaFlags(ScenaFlag(0x0407, 4, 0x203C))
    SetScenaFlags(ScenaFlag(0x0407, 5, 0x203D))
    SetScenaFlags(ScenaFlag(0x0407, 6, 0x203E))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
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
    ClearScenaFlags(ScenaFlag(0x0440, 0, 0x2200))
    ClearScenaFlags(ScenaFlag(0x0455, 7, 0x22AF))
    ClearScenaFlags(ScenaFlag(0x0440, 1, 0x2201))
    ClearScenaFlags(ScenaFlag(0x0440, 2, 0x2202))
    ClearScenaFlags(ScenaFlag(0x0440, 3, 0x2203))
    ClearScenaFlags(ScenaFlag(0x0440, 4, 0x2204))
    ClearScenaFlags(ScenaFlag(0x0440, 5, 0x2205))
    ClearScenaFlags(ScenaFlag(0x0440, 7, 0x2207))
    ClearScenaFlags(ScenaFlag(0x0441, 0, 0x2208))
    ClearScenaFlags(ScenaFlag(0x0441, 1, 0x2209))
    ClearScenaFlags(ScenaFlag(0x0441, 2, 0x220A))
    ClearScenaFlags(ScenaFlag(0x0441, 3, 0x220B))
    ClearScenaFlags(ScenaFlag(0x0441, 4, 0x220C))
    ClearScenaFlags(ScenaFlag(0x0440, 6, 0x2206))
    ClearScenaFlags(ScenaFlag(0x0441, 5, 0x220D))
    ClearScenaFlags(ScenaFlag(0x0441, 6, 0x220E))
    ClearScenaFlags(ScenaFlag(0x0441, 7, 0x220F))
    ClearScenaFlags(ScenaFlag(0x0443, 0, 0x2218))
    ClearScenaFlags(ScenaFlag(0x0443, 1, 0x2219))
    ClearScenaFlags(ScenaFlag(0x0443, 2, 0x221A))
    ClearScenaFlags(ScenaFlag(0x0443, 3, 0x221B))
    ClearScenaFlags(ScenaFlag(0x0443, 4, 0x221C))
    ClearScenaFlags(ScenaFlag(0x0443, 5, 0x221D))
    ClearScenaFlags(ScenaFlag(0x0443, 6, 0x221E))
    ClearScenaFlags(ScenaFlag(0x0443, 7, 0x221F))
    ClearScenaFlags(ScenaFlag(0x0444, 0, 0x2220))
    ClearScenaFlags(ScenaFlag(0x0444, 1, 0x2221))
    ClearScenaFlags(ScenaFlag(0x0444, 2, 0x2222))
    ClearScenaFlags(ScenaFlag(0x0444, 3, 0x2223))
    ClearScenaFlags(ScenaFlag(0x0444, 4, 0x2224))
    ClearScenaFlags(ScenaFlag(0x0456, 2, 0x22B2))
    ClearScenaFlags(ScenaFlag(0x0444, 5, 0x2225))
    ClearScenaFlags(ScenaFlag(0x0444, 6, 0x2226))
    ClearScenaFlags(ScenaFlag(0x0444, 7, 0x2227))
    ClearScenaFlags(ScenaFlag(0x0445, 0, 0x2228))
    ClearScenaFlags(ScenaFlag(0x0445, 1, 0x2229))
    ClearScenaFlags(ScenaFlag(0x0445, 2, 0x222A))
    ClearScenaFlags(ScenaFlag(0x0445, 3, 0x222B))
    ClearScenaFlags(ScenaFlag(0x0445, 4, 0x222C))
    ClearScenaFlags(ScenaFlag(0x0445, 5, 0x222D))
    ClearScenaFlags(ScenaFlag(0x0445, 6, 0x222E))
    ClearScenaFlags(ScenaFlag(0x0445, 7, 0x222F))
    ClearScenaFlags(ScenaFlag(0x0446, 0, 0x2230))
    ClearScenaFlags(ScenaFlag(0x0446, 1, 0x2231))
    ClearScenaFlags(ScenaFlag(0x0446, 2, 0x2232))
    ClearScenaFlags(ScenaFlag(0x0446, 3, 0x2233))
    ClearScenaFlags(ScenaFlag(0x0446, 4, 0x2234))
    ClearScenaFlags(ScenaFlag(0x0446, 5, 0x2235))
    ClearScenaFlags(ScenaFlag(0x0446, 6, 0x2236))
    ClearScenaFlags(ScenaFlag(0x0446, 7, 0x2237))
    ClearScenaFlags(ScenaFlag(0x0447, 0, 0x2238))
    ClearScenaFlags(ScenaFlag(0x0447, 1, 0x2239))
    ClearScenaFlags(ScenaFlag(0x0447, 2, 0x223A))
    ClearScenaFlags(ScenaFlag(0x0447, 3, 0x223B))
    ClearScenaFlags(ScenaFlag(0x0447, 4, 0x223C))
    ClearScenaFlags(ScenaFlag(0x0447, 6, 0x223E))
    ClearScenaFlags(ScenaFlag(0x0447, 5, 0x223D))
    ClearScenaFlags(ScenaFlag(0x0450, 1, 0x2281))
    ClearScenaFlags(ScenaFlag(0x0450, 2, 0x2282))
    ClearScenaFlags(ScenaFlag(0x0450, 3, 0x2283))
    ClearScenaFlags(ScenaFlag(0x0450, 4, 0x2284))
    ClearScenaFlags(ScenaFlag(0x0450, 5, 0x2285))
    ClearScenaFlags(ScenaFlag(0x0450, 6, 0x2286))
    ClearScenaFlags(ScenaFlag(0x0450, 7, 0x2287))
    ClearScenaFlags(ScenaFlag(0x0451, 0, 0x2288))
    ClearScenaFlags(ScenaFlag(0x0451, 1, 0x2289))
    ClearScenaFlags(ScenaFlag(0x0451, 2, 0x228A))
    ClearScenaFlags(ScenaFlag(0x0451, 3, 0x228B))
    ClearScenaFlags(ScenaFlag(0x044E, 6, 0x2276))

    Return()

# id: 0x001F offset: 0x4986
@scena.Code('func_1F_4986')
def func_1F_4986():
    SetScenaFlags(ScenaFlag(0x0440, 0, 0x2200))
    SetScenaFlags(ScenaFlag(0x0455, 7, 0x22AF))
    SetScenaFlags(ScenaFlag(0x0440, 1, 0x2201))
    SetScenaFlags(ScenaFlag(0x0440, 2, 0x2202))
    SetScenaFlags(ScenaFlag(0x0440, 3, 0x2203))
    SetScenaFlags(ScenaFlag(0x0440, 4, 0x2204))
    SetScenaFlags(ScenaFlag(0x0441, 5, 0x220D))
    ClearScenaFlags(ScenaFlag(0x0442, 0, 0x2210))
    ClearScenaFlags(ScenaFlag(0x0442, 1, 0x2211))
    ClearScenaFlags(ScenaFlag(0x0442, 2, 0x2212))
    ClearScenaFlags(ScenaFlag(0x0442, 3, 0x2213))
    ClearScenaFlags(ScenaFlag(0x0442, 4, 0x2214))
    ClearScenaFlags(ScenaFlag(0x0442, 5, 0x2215))
    ClearScenaFlags(ScenaFlag(0x0442, 6, 0x2216))
    ClearScenaFlags(ScenaFlag(0x0442, 7, 0x2217))
    SetScenaFlags(ScenaFlag(0x0443, 0, 0x2218))
    SetScenaFlags(ScenaFlag(0x0443, 1, 0x2219))
    SetScenaFlags(ScenaFlag(0x0443, 2, 0x221A))
    SetScenaFlags(ScenaFlag(0x0443, 3, 0x221B))
    AddItem(ItemTable['原福音'], 1)
    SetScenaFlags(ScenaFlag(0x0443, 4, 0x221C))
    SetScenaFlags(ScenaFlag(0x0443, 6, 0x221E))
    SetScenaFlags(ScenaFlag(0x0445, 7, 0x222F))
    SetScenaFlags(ScenaFlag(0x0443, 7, 0x221F))
    SetScenaFlags(ScenaFlag(0x0444, 0, 0x2220))
    SetScenaFlags(ScenaFlag(0x0444, 1, 0x2221))
    SetScenaFlags(ScenaFlag(0x0444, 2, 0x2222))
    SetScenaFlags(ScenaFlag(0x0444, 3, 0x2223))
    SetScenaFlags(ScenaFlag(0x0444, 4, 0x2224))
    SetScenaFlags(ScenaFlag(0x0456, 2, 0x22B2))
    AddItem(ItemTable['安全卡片'], 1)
    SetScenaFlags(ScenaFlag(0x0444, 5, 0x2225))
    SetScenaFlags(ScenaFlag(0x0444, 6, 0x2226))
    SetScenaFlags(ScenaFlag(0x0444, 7, 0x2227))
    SetScenaFlags(ScenaFlag(0x0445, 0, 0x2228))
    SetScenaFlags(ScenaFlag(0x0445, 1, 0x2229))
    SetScenaFlags(ScenaFlag(0x0445, 2, 0x222A))
    SetScenaFlags(ScenaFlag(0x0445, 3, 0x222B))
    SetScenaFlags(ScenaFlag(0x0445, 4, 0x222C))
    SetScenaFlags(ScenaFlag(0x0445, 5, 0x222D))
    SetScenaFlags(ScenaFlag(0x0445, 6, 0x222E))
    SetScenaFlags(ScenaFlag(0x0446, 0, 0x2230))
    SetScenaFlags(ScenaFlag(0x0446, 1, 0x2231))
    SetScenaFlags(ScenaFlag(0x0447, 4, 0x223C))
    SetScenaFlags(ScenaFlag(0x0446, 2, 0x2232))
    SetScenaFlags(ScenaFlag(0x0446, 3, 0x2233))
    SetScenaFlags(ScenaFlag(0x0446, 4, 0x2234))
    SetScenaFlags(ScenaFlag(0x0446, 5, 0x2235))
    SetScenaFlags(ScenaFlag(0x0446, 6, 0x2236))
    SetScenaFlags(ScenaFlag(0x0446, 7, 0x2237))
    SetScenaFlags(ScenaFlag(0x0447, 0, 0x2238))
    SetScenaFlags(ScenaFlag(0x0447, 1, 0x2239))
    SetScenaFlags(ScenaFlag(0x0447, 2, 0x223A))
    SetScenaFlags(ScenaFlag(0x0447, 3, 0x223B))
    SetScenaFlags(ScenaFlag(0x0447, 5, 0x223D))
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
    SetScenaFlags(ScenaFlag(0x0447, 6, 0x223E))

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

    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    NewScene('ED6_DT21/E0800._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4C92(): pass

    label('loc_4C92')

    SetScenaFlags(ScenaFlag(0x0440, 0, 0x2200))
    SetScenaFlags(ScenaFlag(0x0455, 7, 0x22AF))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4CAA(): pass

    label('loc_4CAA')

    SetScenaFlags(ScenaFlag(0x0440, 0, 0x2200))
    SetScenaFlags(ScenaFlag(0x0455, 7, 0x22AF))
    SetScenaFlags(ScenaFlag(0x0440, 1, 0x2201))
    SetScenaFlags(ScenaFlag(0x0440, 2, 0x2202))
    SetScenaFlags(ScenaFlag(0x0440, 3, 0x2203))
    SetScenaFlags(ScenaFlag(0x0440, 4, 0x2204))
    SetScenaFlags(ScenaFlag(0x0441, 5, 0x220D))
    ClearScenaFlags(ScenaFlag(0x0442, 0, 0x2210))
    ClearScenaFlags(ScenaFlag(0x0442, 1, 0x2211))
    ClearScenaFlags(ScenaFlag(0x0442, 2, 0x2212))
    ClearScenaFlags(ScenaFlag(0x0442, 3, 0x2213))
    ClearScenaFlags(ScenaFlag(0x0442, 4, 0x2214))
    ClearScenaFlags(ScenaFlag(0x0442, 5, 0x2215))
    ClearScenaFlags(ScenaFlag(0x0442, 6, 0x2216))
    ClearScenaFlags(ScenaFlag(0x0442, 7, 0x2217))
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    NewScene('ED6_DT21/C5800._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4CEB(): pass

    label('loc_4CEB')

    SetScenaFlags(ScenaFlag(0x0440, 0, 0x2200))
    SetScenaFlags(ScenaFlag(0x0455, 7, 0x22AF))
    SetScenaFlags(ScenaFlag(0x0440, 1, 0x2201))
    SetScenaFlags(ScenaFlag(0x0440, 2, 0x2202))
    SetScenaFlags(ScenaFlag(0x0440, 3, 0x2203))
    SetScenaFlags(ScenaFlag(0x0440, 4, 0x2204))
    SetScenaFlags(ScenaFlag(0x0441, 5, 0x220D))
    ClearScenaFlags(ScenaFlag(0x0442, 0, 0x2210))
    ClearScenaFlags(ScenaFlag(0x0442, 1, 0x2211))
    ClearScenaFlags(ScenaFlag(0x0442, 2, 0x2212))
    ClearScenaFlags(ScenaFlag(0x0442, 3, 0x2213))
    ClearScenaFlags(ScenaFlag(0x0442, 4, 0x2214))
    ClearScenaFlags(ScenaFlag(0x0442, 5, 0x2215))
    ClearScenaFlags(ScenaFlag(0x0442, 6, 0x2216))
    ClearScenaFlags(ScenaFlag(0x0442, 7, 0x2217))
    SetScenaFlags(ScenaFlag(0x0443, 0, 0x2218))
    SetScenaFlags(ScenaFlag(0x0443, 1, 0x2219))
    SetScenaFlags(ScenaFlag(0x0443, 2, 0x221A))
    SetScenaFlags(ScenaFlag(0x0443, 3, 0x221B))
    AddItem(ItemTable['原福音'], 1)
    SetScenaFlags(ScenaFlag(0x0443, 4, 0x221C))
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    NewScene('ED6_DT21/C5700._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4D40(): pass

    label('loc_4D40')

    SetScenaFlags(ScenaFlag(0x0440, 0, 0x2200))
    SetScenaFlags(ScenaFlag(0x0455, 7, 0x22AF))
    SetScenaFlags(ScenaFlag(0x0440, 1, 0x2201))
    SetScenaFlags(ScenaFlag(0x0440, 2, 0x2202))
    SetScenaFlags(ScenaFlag(0x0440, 3, 0x2203))
    SetScenaFlags(ScenaFlag(0x0440, 4, 0x2204))
    SetScenaFlags(ScenaFlag(0x0441, 5, 0x220D))
    ClearScenaFlags(ScenaFlag(0x0442, 0, 0x2210))
    ClearScenaFlags(ScenaFlag(0x0442, 1, 0x2211))
    ClearScenaFlags(ScenaFlag(0x0442, 2, 0x2212))
    ClearScenaFlags(ScenaFlag(0x0442, 3, 0x2213))
    ClearScenaFlags(ScenaFlag(0x0442, 4, 0x2214))
    ClearScenaFlags(ScenaFlag(0x0442, 5, 0x2215))
    ClearScenaFlags(ScenaFlag(0x0442, 6, 0x2216))
    ClearScenaFlags(ScenaFlag(0x0442, 7, 0x2217))
    SetScenaFlags(ScenaFlag(0x0443, 0, 0x2218))
    SetScenaFlags(ScenaFlag(0x0443, 1, 0x2219))
    SetScenaFlags(ScenaFlag(0x0443, 2, 0x221A))
    SetScenaFlags(ScenaFlag(0x0443, 3, 0x221B))
    AddItem(ItemTable['原福音'], 1)
    SetScenaFlags(ScenaFlag(0x0443, 4, 0x221C))
    SetScenaFlags(ScenaFlag(0x0443, 6, 0x221E))
    SetScenaFlags(ScenaFlag(0x0445, 7, 0x222F))
    SetScenaFlags(ScenaFlag(0x0443, 7, 0x221F))
    SetScenaFlags(ScenaFlag(0x0444, 0, 0x2220))
    SetScenaFlags(ScenaFlag(0x0444, 1, 0x2221))
    SetScenaFlags(ScenaFlag(0x0444, 2, 0x2222))
    SetScenaFlags(ScenaFlag(0x0444, 3, 0x2223))
    SetScenaFlags(ScenaFlag(0x0444, 4, 0x2224))
    SetScenaFlags(ScenaFlag(0x0456, 2, 0x22B2))
    AddItem(ItemTable['安全卡片'], 1)
    SetScenaFlags(ScenaFlag(0x0444, 5, 0x2225))
    SetScenaFlags(ScenaFlag(0x0444, 6, 0x2226))
    SetScenaFlags(ScenaFlag(0x0444, 7, 0x2227))
    SetScenaFlags(ScenaFlag(0x0445, 0, 0x2228))
    SetScenaFlags(ScenaFlag(0x0445, 1, 0x2229))
    SetScenaFlags(ScenaFlag(0x0445, 2, 0x222A))
    SetScenaFlags(ScenaFlag(0x0445, 3, 0x222B))
    SetScenaFlags(ScenaFlag(0x0445, 4, 0x222C))
    SetScenaFlags(ScenaFlag(0x0445, 5, 0x222D))
    SetScenaFlags(ScenaFlag(0x0445, 6, 0x222E))
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    NewScene('ED6_DT21/C5100._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4DD3(): pass

    label('loc_4DD3')

    SetScenaFlags(ScenaFlag(0x0440, 0, 0x2200))
    SetScenaFlags(ScenaFlag(0x0455, 7, 0x22AF))
    SetScenaFlags(ScenaFlag(0x0440, 1, 0x2201))
    SetScenaFlags(ScenaFlag(0x0440, 2, 0x2202))
    SetScenaFlags(ScenaFlag(0x0440, 3, 0x2203))
    SetScenaFlags(ScenaFlag(0x0440, 4, 0x2204))
    SetScenaFlags(ScenaFlag(0x0441, 5, 0x220D))
    ClearScenaFlags(ScenaFlag(0x0442, 0, 0x2210))
    ClearScenaFlags(ScenaFlag(0x0442, 1, 0x2211))
    ClearScenaFlags(ScenaFlag(0x0442, 2, 0x2212))
    ClearScenaFlags(ScenaFlag(0x0442, 3, 0x2213))
    ClearScenaFlags(ScenaFlag(0x0442, 4, 0x2214))
    ClearScenaFlags(ScenaFlag(0x0442, 5, 0x2215))
    ClearScenaFlags(ScenaFlag(0x0442, 6, 0x2216))
    ClearScenaFlags(ScenaFlag(0x0442, 7, 0x2217))
    SetScenaFlags(ScenaFlag(0x0443, 0, 0x2218))
    SetScenaFlags(ScenaFlag(0x0443, 1, 0x2219))
    SetScenaFlags(ScenaFlag(0x0443, 2, 0x221A))
    SetScenaFlags(ScenaFlag(0x0443, 3, 0x221B))
    AddItem(ItemTable['原福音'], 1)
    SetScenaFlags(ScenaFlag(0x0443, 4, 0x221C))
    SetScenaFlags(ScenaFlag(0x0443, 6, 0x221E))
    SetScenaFlags(ScenaFlag(0x0445, 7, 0x222F))
    SetScenaFlags(ScenaFlag(0x0443, 7, 0x221F))
    SetScenaFlags(ScenaFlag(0x0444, 0, 0x2220))
    SetScenaFlags(ScenaFlag(0x0444, 1, 0x2221))
    SetScenaFlags(ScenaFlag(0x0444, 2, 0x2222))
    SetScenaFlags(ScenaFlag(0x0444, 3, 0x2223))
    SetScenaFlags(ScenaFlag(0x0444, 4, 0x2224))
    SetScenaFlags(ScenaFlag(0x0456, 2, 0x22B2))
    AddItem(ItemTable['安全卡片'], 1)
    SetScenaFlags(ScenaFlag(0x0444, 5, 0x2225))
    SetScenaFlags(ScenaFlag(0x0444, 6, 0x2226))
    SetScenaFlags(ScenaFlag(0x0444, 7, 0x2227))
    SetScenaFlags(ScenaFlag(0x0445, 0, 0x2228))
    SetScenaFlags(ScenaFlag(0x0445, 1, 0x2229))
    SetScenaFlags(ScenaFlag(0x0445, 2, 0x222A))
    SetScenaFlags(ScenaFlag(0x0445, 3, 0x222B))
    SetScenaFlags(ScenaFlag(0x0445, 4, 0x222C))
    SetScenaFlags(ScenaFlag(0x0445, 5, 0x222D))
    SetScenaFlags(ScenaFlag(0x0445, 6, 0x222E))
    SetScenaFlags(ScenaFlag(0x0446, 0, 0x2230))
    SetScenaFlags(ScenaFlag(0x0446, 1, 0x2231))
    SetScenaFlags(ScenaFlag(0x0447, 4, 0x223C))
    SetScenaFlags(ScenaFlag(0x0446, 2, 0x2232))
    SetScenaFlags(ScenaFlag(0x0446, 3, 0x2233))
    SetScenaFlags(ScenaFlag(0x0446, 4, 0x2234))
    SetScenaFlags(ScenaFlag(0x0446, 5, 0x2235))
    SetScenaFlags(ScenaFlag(0x0446, 6, 0x2236))
    SetScenaFlags(ScenaFlag(0x0446, 7, 0x2237))
    SetScenaFlags(ScenaFlag(0x0447, 0, 0x2238))
    SetScenaFlags(ScenaFlag(0x0447, 1, 0x2239))
    SetScenaFlags(ScenaFlag(0x0447, 2, 0x223A))
    SetScenaFlags(ScenaFlag(0x0447, 3, 0x223B))
    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5315._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4E93(): pass

    label('loc_4E93')

    SetScenaFlags(ScenaFlag(0x0440, 0, 0x2200))
    SetScenaFlags(ScenaFlag(0x0455, 7, 0x22AF))
    SetScenaFlags(ScenaFlag(0x0440, 1, 0x2201))
    SetScenaFlags(ScenaFlag(0x0440, 2, 0x2202))
    SetScenaFlags(ScenaFlag(0x0440, 3, 0x2203))
    SetScenaFlags(ScenaFlag(0x0440, 4, 0x2204))
    SetScenaFlags(ScenaFlag(0x0441, 5, 0x220D))
    ClearScenaFlags(ScenaFlag(0x0442, 0, 0x2210))
    ClearScenaFlags(ScenaFlag(0x0442, 1, 0x2211))
    ClearScenaFlags(ScenaFlag(0x0442, 2, 0x2212))
    ClearScenaFlags(ScenaFlag(0x0442, 3, 0x2213))
    ClearScenaFlags(ScenaFlag(0x0442, 4, 0x2214))
    ClearScenaFlags(ScenaFlag(0x0442, 5, 0x2215))
    ClearScenaFlags(ScenaFlag(0x0442, 6, 0x2216))
    ClearScenaFlags(ScenaFlag(0x0442, 7, 0x2217))
    SetScenaFlags(ScenaFlag(0x0443, 0, 0x2218))
    SetScenaFlags(ScenaFlag(0x0443, 1, 0x2219))
    SetScenaFlags(ScenaFlag(0x0443, 2, 0x221A))
    SetScenaFlags(ScenaFlag(0x0443, 3, 0x221B))
    AddItem(ItemTable['原福音'], 1)
    SetScenaFlags(ScenaFlag(0x0443, 4, 0x221C))
    SetScenaFlags(ScenaFlag(0x0443, 6, 0x221E))
    SetScenaFlags(ScenaFlag(0x0445, 7, 0x222F))
    SetScenaFlags(ScenaFlag(0x0443, 7, 0x221F))
    SetScenaFlags(ScenaFlag(0x0444, 0, 0x2220))
    SetScenaFlags(ScenaFlag(0x0444, 1, 0x2221))
    SetScenaFlags(ScenaFlag(0x0444, 2, 0x2222))
    SetScenaFlags(ScenaFlag(0x0444, 3, 0x2223))
    SetScenaFlags(ScenaFlag(0x0444, 4, 0x2224))
    SetScenaFlags(ScenaFlag(0x0456, 2, 0x22B2))
    AddItem(ItemTable['安全卡片'], 1)
    SetScenaFlags(ScenaFlag(0x0444, 5, 0x2225))
    SetScenaFlags(ScenaFlag(0x0444, 6, 0x2226))
    SetScenaFlags(ScenaFlag(0x0444, 7, 0x2227))
    SetScenaFlags(ScenaFlag(0x0445, 0, 0x2228))
    SetScenaFlags(ScenaFlag(0x0445, 1, 0x2229))
    SetScenaFlags(ScenaFlag(0x0445, 2, 0x222A))
    SetScenaFlags(ScenaFlag(0x0445, 3, 0x222B))
    SetScenaFlags(ScenaFlag(0x0445, 4, 0x222C))
    SetScenaFlags(ScenaFlag(0x0445, 5, 0x222D))
    SetScenaFlags(ScenaFlag(0x0445, 6, 0x222E))
    SetScenaFlags(ScenaFlag(0x0446, 0, 0x2230))
    SetScenaFlags(ScenaFlag(0x0446, 1, 0x2231))
    SetScenaFlags(ScenaFlag(0x0447, 4, 0x223C))
    SetScenaFlags(ScenaFlag(0x0446, 2, 0x2232))
    SetScenaFlags(ScenaFlag(0x0446, 3, 0x2233))
    SetScenaFlags(ScenaFlag(0x0446, 4, 0x2234))
    SetScenaFlags(ScenaFlag(0x0446, 5, 0x2235))
    SetScenaFlags(ScenaFlag(0x0446, 6, 0x2236))
    SetScenaFlags(ScenaFlag(0x0446, 7, 0x2237))
    SetScenaFlags(ScenaFlag(0x0447, 0, 0x2238))
    SetScenaFlags(ScenaFlag(0x0447, 1, 0x2239))
    SetScenaFlags(ScenaFlag(0x0447, 2, 0x223A))
    SetScenaFlags(ScenaFlag(0x0447, 3, 0x223B))
    SetScenaFlags(ScenaFlag(0x0447, 5, 0x223D))
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
    SetScenaFlags(ScenaFlag(0x0447, 6, 0x223E))
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T5200._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_4F7D(): pass

    label('loc_4F7D')

    SetScenaFlags(ScenaFlag(0x0440, 0, 0x2200))
    SetScenaFlags(ScenaFlag(0x0455, 7, 0x22AF))
    SetScenaFlags(ScenaFlag(0x0440, 1, 0x2201))
    SetScenaFlags(ScenaFlag(0x0440, 2, 0x2202))
    SetScenaFlags(ScenaFlag(0x0440, 3, 0x2203))
    SetScenaFlags(ScenaFlag(0x0440, 4, 0x2204))
    SetScenaFlags(ScenaFlag(0x0441, 5, 0x220D))
    ClearScenaFlags(ScenaFlag(0x0442, 0, 0x2210))
    ClearScenaFlags(ScenaFlag(0x0442, 1, 0x2211))
    ClearScenaFlags(ScenaFlag(0x0442, 2, 0x2212))
    ClearScenaFlags(ScenaFlag(0x0442, 3, 0x2213))
    ClearScenaFlags(ScenaFlag(0x0442, 4, 0x2214))
    ClearScenaFlags(ScenaFlag(0x0442, 5, 0x2215))
    ClearScenaFlags(ScenaFlag(0x0442, 6, 0x2216))
    ClearScenaFlags(ScenaFlag(0x0442, 7, 0x2217))
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
    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            ChrTable['尤莉亚上尉'],
            ChrTable['穆拉'],
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

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5313._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_505F(): pass

    label('loc_505F')

    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            ChrTable['尤莉亚上尉'],
            ChrTable['穆拉'],
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
    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            ChrTable['尤莉亚上尉'],
            ChrTable['穆拉'],
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

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5318._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_50F7(): pass

    label('loc_50F7')

    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            ChrTable['尤莉亚上尉'],
            ChrTable['穆拉'],
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

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5317._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_5143(): pass

    label('loc_5143')

    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            ChrTable['尤莉亚上尉'],
            ChrTable['穆拉'],
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

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5300._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5244')

    def _loc_518F(): pass

    label('loc_518F')

    FormationDelMember(0x01, 0xFF)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            ChrTable['尤莉亚上尉'],
            ChrTable['穆拉'],
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

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
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
    SetScenaFlags(ScenaFlag(0x0447, 6, 0x223E))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
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
