import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0001_2_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0001_2 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x32F9
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
            '请选择',
            TxtCtl.Enter,
        ),
    )

    def _loc_B2(): pass

    label('loc_B2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14C',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '洛连特\n'),
            TXT(0x01, '柏斯\n'),
            TXT(0x02, '卢安\n'),
            TXT(0x03, '蔡斯\n'),
            TXT(0x04, '格兰赛尔\n'),
            TXT(0x05, '其它\n'),
            TXT(0x06, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_115'),
        (0x00000001, 'loc_11C'),
        (0x00000002, 'loc_123'),
        (0x00000003, 'loc_12A'),
        (0x00000004, 'loc_131'),
        (0x00000005, 'loc_138'),
        (-1, 'loc_13F'),
    )

    def _loc_115(): pass

    label('loc_115')

    Call(2, 0x0001)

    Jump('loc_149')

    def _loc_11C(): pass

    label('loc_11C')

    Call(2, 0x0009)

    Jump('loc_149')

    def _loc_123(): pass

    label('loc_123')

    Call(2, 0x0014)

    Jump('loc_149')

    def _loc_12A(): pass

    label('loc_12A')

    Call(2, 0x001B)

    Jump('loc_149')

    def _loc_131(): pass

    label('loc_131')

    Call(2, 0x0023)

    Jump('loc_149')

    def _loc_138(): pass

    label('loc_138')

    Call(2, 0x002E)

    Jump('loc_149')

    def _loc_13F(): pass

    label('loc_13F')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_149(): pass

    label('loc_149')

    Jump('loc_B2')

    def _loc_14C(): pass

    label('loc_14C')

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

# id: 0x0001 offset: 0x15C
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27A',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        80,
        1,
        (
            TXT(0x00, '玛鲁加矿山\n'),
            TXT(0x01, '神秘森林\n'),
            TXT(0x02, '翡翠之塔\n'),
            TXT(0x03, '艾利兹街道\n'),
            TXT(0x04, '米尔西街道\n'),
            TXT(0x05, '玛鲁加山道\n'),
            TXT(0x06, '地下水路\n'),
            TXT(0x07, '帕赛尔农场（夜晚）\n'),
            TXT(0x08, '威尔特桥关所外部\n'),
            TXT(0x09, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_21C'),
        (0x00000001, 'loc_223'),
        (0x00000002, 'loc_22A'),
        (0x00000003, 'loc_231'),
        (0x00000004, 'loc_238'),
        (0x00000005, 'loc_23F'),
        (0x00000006, 'loc_246'),
        (0x00000007, 'loc_24D'),
        (0x00000008, 'loc_25D'),
        (-1, 'loc_26D'),
    )

    def _loc_21C(): pass

    label('loc_21C')

    Call(2, 0x0002)

    Jump('loc_277')

    def _loc_223(): pass

    label('loc_223')

    Call(2, 0x0003)

    Jump('loc_277')

    def _loc_22A(): pass

    label('loc_22A')

    Call(2, 0x0004)

    Jump('loc_277')

    def _loc_231(): pass

    label('loc_231')

    Call(2, 0x0005)

    Jump('loc_277')

    def _loc_238(): pass

    label('loc_238')

    Call(2, 0x0006)

    Jump('loc_277')

    def _loc_23F(): pass

    label('loc_23F')

    Call(2, 0x0007)

    Jump('loc_277')

    def _loc_246(): pass

    label('loc_246')

    Call(2, 0x0008)

    Jump('loc_277')

    def _loc_24D(): pass

    label('loc_24D')

    Battle(0x00000393, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_277')

    def _loc_25D(): pass

    label('loc_25D')

    Battle(0x000003ED, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_277')

    def _loc_26D(): pass

    label('loc_26D')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_277(): pass

    label('loc_277')

    Jump('Init')

    def _loc_27A(): pass

    label('loc_27A')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x288
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_318',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C0100_01\n'),
            TXT(0x01, 'C0100_02\n'),
            TXT(0x02, 'C0100_03\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2DB'),
        (0x00000001, 'loc_2EB'),
        (0x00000002, 'loc_2FB'),
        (-1, 'loc_30B'),
    )

    def _loc_2DB(): pass

    label('loc_2DB')

    Battle(0x00000056, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_315')

    def _loc_2EB(): pass

    label('loc_2EB')

    Battle(0x00000057, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_315')

    def _loc_2FB(): pass

    label('loc_2FB')

    Battle(0x00000058, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_315')

    def _loc_30B(): pass

    label('loc_30B')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_315(): pass

    label('loc_315')

    Jump('ReInit')

    def _loc_318(): pass

    label('loc_318')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0003 offset: 0x326
@scena.Code('func_03_326')
def func_03_326():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_411',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C0100_01\n'),
            TXT(0x01, 'C0100_02\n'),
            TXT(0x02, 'C0100_03\n'),
            TXT(0x03, 'C0100_20\n'),
            TXT(0x04, 'C0100_11\n'),
            TXT(0x05, 'BTL_EVENT001\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3A4'),
        (0x00000001, 'loc_3B4'),
        (0x00000002, 'loc_3C4'),
        (0x00000003, 'loc_3D4'),
        (0x00000004, 'loc_3E4'),
        (0x00000005, 'loc_3F4'),
        (-1, 'loc_404'),
    )

    def _loc_3A4(): pass

    label('loc_3A4')

    Battle(0x0000003E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_40E')

    def _loc_3B4(): pass

    label('loc_3B4')

    Battle(0x0000003F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_40E')

    def _loc_3C4(): pass

    label('loc_3C4')

    Battle(0x00000040, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_40E')

    def _loc_3D4(): pass

    label('loc_3D4')

    Battle(0x00000051, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_40E')

    def _loc_3E4(): pass

    label('loc_3E4')

    Battle(0x00000048, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_40E')

    def _loc_3F4(): pass

    label('loc_3F4')

    Battle(0x00000385, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_40E')

    def _loc_404(): pass

    label('loc_404')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_40E(): pass

    label('loc_40E')

    Jump('func_03_326')

    def _loc_411(): pass

    label('loc_411')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0004 offset: 0x41F
@scena.Code('func_04_41F')
def func_04_41F():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F6',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C0400_01\n'),
            TXT(0x01, 'C0400_02\n'),
            TXT(0x02, 'C0400_07\n'),
            TXT(0x03, 'C0400_13\n'),
            TXT(0x04, 'C0400_10\n'),
            TXT(0x05, 'BTL_EVENT002\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_499'),
        (0x00000001, 'loc_4A9'),
        (0x00000002, 'loc_4B9'),
        (0x00000003, 'loc_4C9'),
        (0x00000004, 'loc_4D9'),
        (-1, 'loc_4E9'),
    )

    def _loc_499(): pass

    label('loc_499')

    Battle(0x00000031, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_4F3')

    def _loc_4A9(): pass

    label('loc_4A9')

    Battle(0x00000032, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_4F3')

    def _loc_4B9(): pass

    label('loc_4B9')

    Battle(0x00000037, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_4F3')

    def _loc_4C9(): pass

    label('loc_4C9')

    Battle(0x0000003D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_4F3')

    def _loc_4D9(): pass

    label('loc_4D9')

    Battle(0x0000003A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_4F3')

    def _loc_4E9(): pass

    label('loc_4E9')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_4F3(): pass

    label('loc_4F3')

    Jump('func_04_41F')

    def _loc_4F6(): pass

    label('loc_4F6')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0005 offset: 0x504
@scena.Code('func_05_504')
def func_05_504():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5CE',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R0100_02\n'),
            TXT(0x01, 'R0100_05\n'),
            TXT(0x02, 'R0100_09\n'),
            TXT(0x03, 'R0100_11\n'),
            TXT(0x04, 'R0100_14\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_571'),
        (0x00000001, 'loc_581'),
        (0x00000002, 'loc_591'),
        (0x00000003, 'loc_5A1'),
        (0x00000004, 'loc_5B1'),
        (-1, 'loc_5C1'),
    )

    def _loc_571(): pass

    label('loc_571')

    Battle(0x00000015, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_5CB')

    def _loc_581(): pass

    label('loc_581')

    Battle(0x00000018, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_5CB')

    def _loc_591(): pass

    label('loc_591')

    Battle(0x0000001C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_5CB')

    def _loc_5A1(): pass

    label('loc_5A1')

    Battle(0x0000001E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_5CB')

    def _loc_5B1(): pass

    label('loc_5B1')

    Battle(0x00000021, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_5CB')

    def _loc_5C1(): pass

    label('loc_5C1')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5CB(): pass

    label('loc_5CB')

    Jump('func_05_504')

    def _loc_5CE(): pass

    label('loc_5CE')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0006 offset: 0x5DC
@scena.Code('func_06_5DC')
def func_06_5DC():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6E8',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R0200_02\n'),
            TXT(0x01, 'R0200_06\n'),
            TXT(0x02, 'R0200_09\n'),
            TXT(0x03, 'R0200_11\n'),
            TXT(0x04, 'R0200_17\n'),
            TXT(0x05, 'BTL_QUEST003\n'),
            TXT(0x06, 'BTL_QUEST004\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_66B'),
        (0x00000001, 'loc_67B'),
        (0x00000002, 'loc_68B'),
        (0x00000003, 'loc_69B'),
        (0x00000004, 'loc_6AB'),
        (0x00000005, 'loc_6BB'),
        (0x00000006, 'loc_6CB'),
        (-1, 'loc_6DB'),
    )

    def _loc_66B(): pass

    label('loc_66B')

    Battle(0x0000007A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_6E5')

    def _loc_67B(): pass

    label('loc_67B')

    Battle(0x0000007E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_6E5')

    def _loc_68B(): pass

    label('loc_68B')

    Battle(0x00000081, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_6E5')

    def _loc_69B(): pass

    label('loc_69B')

    Battle(0x00000083, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_6E5')

    def _loc_6AB(): pass

    label('loc_6AB')

    Battle(0x00000089, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_6E5')

    def _loc_6BB(): pass

    label('loc_6BB')

    Battle(0x000003EB, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_6E5')

    def _loc_6CB(): pass

    label('loc_6CB')

    Battle(0x000003EC, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_6E5')

    def _loc_6DB(): pass

    label('loc_6DB')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6E5(): pass

    label('loc_6E5')

    Jump('func_06_5DC')

    def _loc_6E8(): pass

    label('loc_6E8')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0007 offset: 0x6F6
@scena.Code('func_07_6F6')
def func_07_6F6():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7C0',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R0300_02\n'),
            TXT(0x01, 'R0300_06\n'),
            TXT(0x02, 'R0300_09\n'),
            TXT(0x03, 'R0300_12\n'),
            TXT(0x04, 'R0300_17\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_763'),
        (0x00000001, 'loc_773'),
        (0x00000002, 'loc_783'),
        (0x00000003, 'loc_793'),
        (0x00000004, 'loc_7A3'),
        (-1, 'loc_7B3'),
    )

    def _loc_763(): pass

    label('loc_763')

    Battle(0x00000065, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_7BD')

    def _loc_773(): pass

    label('loc_773')

    Battle(0x00000069, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_7BD')

    def _loc_783(): pass

    label('loc_783')

    Battle(0x0000006C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_7BD')

    def _loc_793(): pass

    label('loc_793')

    Battle(0x0000006F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_7BD')

    def _loc_7A3(): pass

    label('loc_7A3')

    Battle(0x00000074, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_7BD')

    def _loc_7B3(): pass

    label('loc_7B3')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_7BD(): pass

    label('loc_7BD')

    Jump('func_07_6F6')

    def _loc_7C0(): pass

    label('loc_7C0')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0008 offset: 0x7CE
@scena.Code('func_08_7CE')
def func_08_7CE():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_898',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C0500_01\n'),
            TXT(0x01, 'C0500_02\n'),
            TXT(0x02, 'C0500_03\n'),
            TXT(0x03, 'C0500_04\n'),
            TXT(0x04, 'C0500_07\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_83B'),
        (0x00000001, 'loc_84B'),
        (0x00000002, 'loc_85B'),
        (0x00000003, 'loc_86B'),
        (0x00000004, 'loc_87B'),
        (-1, 'loc_88B'),
    )

    def _loc_83B(): pass

    label('loc_83B')

    Battle(0x0000002A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_895')

    def _loc_84B(): pass

    label('loc_84B')

    Battle(0x0000002B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_895')

    def _loc_85B(): pass

    label('loc_85B')

    Battle(0x0000002C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_895')

    def _loc_86B(): pass

    label('loc_86B')

    Battle(0x0000002D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_895')

    def _loc_87B(): pass

    label('loc_87B')

    Battle(0x00000030, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_895')

    def _loc_88B(): pass

    label('loc_88B')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_895(): pass

    label('loc_895')

    Jump('func_08_7CE')

    def _loc_898(): pass

    label('loc_898')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0009 offset: 0x8A6
@scena.Code('func_09_8A6')
def func_09_8A6():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A35',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        60,
        1,
        (
            TXT(0x00, '琥珀之塔\n'),
            TXT(0x01, '空贼要塞\n'),
            TXT(0x02, '迷雾峡谷\n'),
            TXT(0x03, '古罗尼山顶\n'),
            TXT(0x04, '东柏斯街道\n'),
            TXT(0x05, '西柏斯街道\n'),
            TXT(0x06, '钢壁之路\n'),
            TXT(0x07, '安塞尔新街\n'),
            TXT(0x08, '拉文努山道\n'),
            TXT(0x09, '拉文努废坑\n'),
            TXT(0x0A, '拉文努废坑中央广场（吉尔）\n'),
            TXT(0x0B, '空贼要塞（多伦）\n'),
            TXT(0x0C, '古罗尼关所外部（犬）\n'),
            TXT(0x0D, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_9B2'),
        (0x00000001, 'loc_9B9'),
        (0x00000002, 'loc_9C0'),
        (0x00000003, 'loc_9C7'),
        (0x00000004, 'loc_9CE'),
        (0x00000005, 'loc_9D5'),
        (0x00000006, 'loc_9DC'),
        (0x00000007, 'loc_9E3'),
        (0x00000008, 'loc_9EA'),
        (0x00000009, 'loc_9F1'),
        (0x0000000A, 'loc_9F8'),
        (0x0000000B, 'loc_A08'),
        (0x0000000C, 'loc_A18'),
        (-1, 'loc_A28'),
    )

    def _loc_9B2(): pass

    label('loc_9B2')

    Call(2, 0x000A)

    Jump('loc_A32')

    def _loc_9B9(): pass

    label('loc_9B9')

    Call(2, 0x000B)

    Jump('loc_A32')

    def _loc_9C0(): pass

    label('loc_9C0')

    Call(2, 0x000C)

    Jump('loc_A32')

    def _loc_9C7(): pass

    label('loc_9C7')

    Call(2, 0x000D)

    Jump('loc_A32')

    def _loc_9CE(): pass

    label('loc_9CE')

    Call(2, 0x000E)

    Jump('loc_A32')

    def _loc_9D5(): pass

    label('loc_9D5')

    Call(2, 0x000F)

    Jump('loc_A32')

    def _loc_9DC(): pass

    label('loc_9DC')

    Call(2, 0x0010)

    Jump('loc_A32')

    def _loc_9E3(): pass

    label('loc_9E3')

    Call(2, 0x0011)

    Jump('loc_A32')

    def _loc_9EA(): pass

    label('loc_9EA')

    Call(2, 0x0012)

    Jump('loc_A32')

    def _loc_9F1(): pass

    label('loc_9F1')

    Call(2, 0x0013)

    Jump('loc_A32')

    def _loc_9F8(): pass

    label('loc_9F8')

    Battle(0x00000387, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_A32')

    def _loc_A08(): pass

    label('loc_A08')

    Battle(0x00000389, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_A32')

    def _loc_A18(): pass

    label('loc_A18')

    Battle(0x00000396, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_A32')

    def _loc_A28(): pass

    label('loc_A28')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_A32(): pass

    label('loc_A32')

    Jump('func_09_8A6')

    def _loc_A35(): pass

    label('loc_A35')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000A offset: 0xA43
@scena.Code('func_0A_A43')
def func_0A_A43():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B11',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C1211_01\n'),
            TXT(0x01, 'C1211_02\n'),
            TXT(0x02, 'C1211_03\n'),
            TXT(0x03, 'C1211_04\n'),
            TXT(0x04, 'BTL_QUEST007\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_AB4'),
        (0x00000001, 'loc_AC4'),
        (0x00000002, 'loc_AD4'),
        (0x00000003, 'loc_AE4'),
        (0x00000004, 'loc_AF4'),
        (-1, 'loc_B04'),
    )

    def _loc_AB4(): pass

    label('loc_AB4')

    Battle(0x0000008E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_B0E')

    def _loc_AC4(): pass

    label('loc_AC4')

    Battle(0x0000008F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_B0E')

    def _loc_AD4(): pass

    label('loc_AD4')

    Battle(0x00000090, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_B0E')

    def _loc_AE4(): pass

    label('loc_AE4')

    Battle(0x00000091, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_B0E')

    def _loc_AF4(): pass

    label('loc_AF4')

    Battle(0x000003EF, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_B0E')

    def _loc_B04(): pass

    label('loc_B04')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B0E(): pass

    label('loc_B0E')

    Jump('func_0A_A43')

    def _loc_B11(): pass

    label('loc_B11')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000B offset: 0xB1F
@scena.Code('func_0B_B1F')
def func_0B_B1F():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BE9',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C1300_01\n'),
            TXT(0x01, 'C1300_02\n'),
            TXT(0x02, 'C1300_03\n'),
            TXT(0x03, 'C1300_04\n'),
            TXT(0x04, 'C1300_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_B8C'),
        (0x00000001, 'loc_B9C'),
        (0x00000002, 'loc_BAC'),
        (0x00000003, 'loc_BBC'),
        (0x00000004, 'loc_BCC'),
        (-1, 'loc_BDC'),
    )

    def _loc_B8C(): pass

    label('loc_B8C')

    Battle(0x000000A1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_BE6')

    def _loc_B9C(): pass

    label('loc_B9C')

    Battle(0x000000A2, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_BE6')

    def _loc_BAC(): pass

    label('loc_BAC')

    Battle(0x000000A3, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_BE6')

    def _loc_BBC(): pass

    label('loc_BBC')

    Battle(0x000000A4, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_BE6')

    def _loc_BCC(): pass

    label('loc_BCC')

    Battle(0x000000A5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_BE6')

    def _loc_BDC(): pass

    label('loc_BDC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_BE6(): pass

    label('loc_BE6')

    Jump('func_0B_B1F')

    def _loc_BE9(): pass

    label('loc_BE9')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000C offset: 0xBF7
@scena.Code('func_0C_BF7')
def func_0C_BF7():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CC1',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C1400_01\n'),
            TXT(0x01, 'C1400_02\n'),
            TXT(0x02, 'C1400_03\n'),
            TXT(0x03, 'C1400_04\n'),
            TXT(0x04, 'C1400_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_C64'),
        (0x00000001, 'loc_C74'),
        (0x00000002, 'loc_C84'),
        (0x00000003, 'loc_C94'),
        (0x00000004, 'loc_CA4'),
        (-1, 'loc_CB4'),
    )

    def _loc_C64(): pass

    label('loc_C64')

    Battle(0x000000B5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_CBE')

    def _loc_C74(): pass

    label('loc_C74')

    Battle(0x000000B6, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_CBE')

    def _loc_C84(): pass

    label('loc_C84')

    Battle(0x000000B7, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_CBE')

    def _loc_C94(): pass

    label('loc_C94')

    Battle(0x000000B8, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_CBE')

    def _loc_CA4(): pass

    label('loc_CA4')

    Battle(0x000000B9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_CBE')

    def _loc_CB4(): pass

    label('loc_CB4')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CBE(): pass

    label('loc_CBE')

    Jump('func_0C_BF7')

    def _loc_CC1(): pass

    label('loc_CC1')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000D offset: 0xCCF
@scena.Code('func_0D_CCF')
def func_0D_CCF():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D99',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C1500_01\n'),
            TXT(0x01, 'C1500_02\n'),
            TXT(0x02, 'C1500_03\n'),
            TXT(0x03, 'C1500_04\n'),
            TXT(0x04, 'C1500_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_D3C'),
        (0x00000001, 'loc_D4C'),
        (0x00000002, 'loc_D5C'),
        (0x00000003, 'loc_D6C'),
        (0x00000004, 'loc_D7C'),
        (-1, 'loc_D8C'),
    )

    def _loc_D3C(): pass

    label('loc_D3C')

    Battle(0x000000C9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_D96')

    def _loc_D4C(): pass

    label('loc_D4C')

    Battle(0x000000CA, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_D96')

    def _loc_D5C(): pass

    label('loc_D5C')

    Battle(0x000000CB, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_D96')

    def _loc_D6C(): pass

    label('loc_D6C')

    Battle(0x000000CC, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_D96')

    def _loc_D7C(): pass

    label('loc_D7C')

    Battle(0x000000CD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_D96')

    def _loc_D8C(): pass

    label('loc_D8C')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_D96(): pass

    label('loc_D96')

    Jump('func_0D_CCF')

    def _loc_D99(): pass

    label('loc_D99')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000E offset: 0xDA7
@scena.Code('func_0E_DA7')
def func_0E_DA7():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E71',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R1100_01\n'),
            TXT(0x01, 'R1100_02\n'),
            TXT(0x02, 'R1100_20\n'),
            TXT(0x03, 'R1100_04\n'),
            TXT(0x04, 'R1100_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_E14'),
        (0x00000001, 'loc_E24'),
        (0x00000002, 'loc_E34'),
        (0x00000003, 'loc_E44'),
        (0x00000004, 'loc_E54'),
        (-1, 'loc_E64'),
    )

    def _loc_E14(): pass

    label('loc_E14')

    Battle(0x000000DD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_E6E')

    def _loc_E24(): pass

    label('loc_E24')

    Battle(0x000000DE, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_E6E')

    def _loc_E34(): pass

    label('loc_E34')

    Battle(0x000000F0, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_E6E')

    def _loc_E44(): pass

    label('loc_E44')

    Battle(0x000000E0, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_E6E')

    def _loc_E54(): pass

    label('loc_E54')

    Battle(0x000000E1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_E6E')

    def _loc_E64(): pass

    label('loc_E64')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_E6E(): pass

    label('loc_E6E')

    Jump('func_0E_DA7')

    def _loc_E71(): pass

    label('loc_E71')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000F offset: 0xE7F
@scena.Code('func_0F_E7F')
def func_0F_E7F():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F49',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R1200_01\n'),
            TXT(0x01, 'R1200_02\n'),
            TXT(0x02, 'R1200_03\n'),
            TXT(0x03, 'R1200_04\n'),
            TXT(0x04, 'R1200_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_EEC'),
        (0x00000001, 'loc_EFC'),
        (0x00000002, 'loc_F0C'),
        (0x00000003, 'loc_F1C'),
        (0x00000004, 'loc_F2C'),
        (-1, 'loc_F3C'),
    )

    def _loc_EEC(): pass

    label('loc_EEC')

    Battle(0x000000F1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F46')

    def _loc_EFC(): pass

    label('loc_EFC')

    Battle(0x000000F2, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F46')

    def _loc_F0C(): pass

    label('loc_F0C')

    Battle(0x000000F3, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F46')

    def _loc_F1C(): pass

    label('loc_F1C')

    Battle(0x000000F4, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F46')

    def _loc_F2C(): pass

    label('loc_F2C')

    Battle(0x000000F5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_F46')

    def _loc_F3C(): pass

    label('loc_F3C')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_F46(): pass

    label('loc_F46')

    Jump('func_0F_E7F')

    def _loc_F49(): pass

    label('loc_F49')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0010 offset: 0xF57
@scena.Code('func_10_F57')
def func_10_F57():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1021',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R1300_01\n'),
            TXT(0x01, 'R1300_02\n'),
            TXT(0x02, 'R1300_03\n'),
            TXT(0x03, 'R1300_04\n'),
            TXT(0x04, 'R1300_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_FC4'),
        (0x00000001, 'loc_FD4'),
        (0x00000002, 'loc_FE4'),
        (0x00000003, 'loc_FF4'),
        (0x00000004, 'loc_1004'),
        (-1, 'loc_1014'),
    )

    def _loc_FC4(): pass

    label('loc_FC4')

    Battle(0x00000105, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_101E')

    def _loc_FD4(): pass

    label('loc_FD4')

    Battle(0x00000106, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_101E')

    def _loc_FE4(): pass

    label('loc_FE4')

    Battle(0x00000107, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_101E')

    def _loc_FF4(): pass

    label('loc_FF4')

    Battle(0x00000108, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_101E')

    def _loc_1004(): pass

    label('loc_1004')

    Battle(0x00000109, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_101E')

    def _loc_1014(): pass

    label('loc_1014')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_101E(): pass

    label('loc_101E')

    Jump('func_10_F57')

    def _loc_1021(): pass

    label('loc_1021')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0011 offset: 0x102F
@scena.Code('func_11_102F')
def func_11_102F():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10F9',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R1400_01\n'),
            TXT(0x01, 'R1400_02\n'),
            TXT(0x02, 'R1400_03\n'),
            TXT(0x03, 'R1400_04\n'),
            TXT(0x04, 'R1400_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_109C'),
        (0x00000001, 'loc_10AC'),
        (0x00000002, 'loc_10BC'),
        (0x00000003, 'loc_10CC'),
        (0x00000004, 'loc_10DC'),
        (-1, 'loc_10EC'),
    )

    def _loc_109C(): pass

    label('loc_109C')

    Battle(0x00000119, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_10F6')

    def _loc_10AC(): pass

    label('loc_10AC')

    Battle(0x0000011A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_10F6')

    def _loc_10BC(): pass

    label('loc_10BC')

    Battle(0x0000011B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_10F6')

    def _loc_10CC(): pass

    label('loc_10CC')

    Battle(0x0000011C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_10F6')

    def _loc_10DC(): pass

    label('loc_10DC')

    Battle(0x0000011D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_10F6')

    def _loc_10EC(): pass

    label('loc_10EC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_10F6(): pass

    label('loc_10F6')

    Jump('func_11_102F')

    def _loc_10F9(): pass

    label('loc_10F9')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0012 offset: 0x1107
@scena.Code('func_12_1107')
def func_12_1107():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11D5',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R1500_01\n'),
            TXT(0x01, 'R1500_02\n'),
            TXT(0x02, 'R1500_03\n'),
            TXT(0x03, 'R1500_04\n'),
            TXT(0x04, 'BTL_QUEST006\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1178'),
        (0x00000001, 'loc_1188'),
        (0x00000002, 'loc_1198'),
        (0x00000003, 'loc_11A8'),
        (0x00000004, 'loc_11B8'),
        (-1, 'loc_11C8'),
    )

    def _loc_1178(): pass

    label('loc_1178')

    Battle(0x0000012D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_11D2')

    def _loc_1188(): pass

    label('loc_1188')

    Battle(0x0000012E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_11D2')

    def _loc_1198(): pass

    label('loc_1198')

    Battle(0x0000012F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_11D2')

    def _loc_11A8(): pass

    label('loc_11A8')

    Battle(0x00000130, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_11D2')

    def _loc_11B8(): pass

    label('loc_11B8')

    Battle(0x000003EE, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_11D2')

    def _loc_11C8(): pass

    label('loc_11C8')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11D2(): pass

    label('loc_11D2')

    Jump('func_12_1107')

    def _loc_11D5(): pass

    label('loc_11D5')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0013 offset: 0x11E3
@scena.Code('func_13_11E3')
def func_13_11E3():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12AD',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C1100_01\n'),
            TXT(0x01, 'C1100_02\n'),
            TXT(0x02, 'C1100_03\n'),
            TXT(0x03, 'C1100_04\n'),
            TXT(0x04, 'C1100_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1250'),
        (0x00000001, 'loc_1260'),
        (0x00000002, 'loc_1270'),
        (0x00000003, 'loc_1280'),
        (0x00000004, 'loc_1290'),
        (-1, 'loc_12A0'),
    )

    def _loc_1250(): pass

    label('loc_1250')

    Battle(0x00000141, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12AA')

    def _loc_1260(): pass

    label('loc_1260')

    Battle(0x00000142, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12AA')

    def _loc_1270(): pass

    label('loc_1270')

    Battle(0x00000143, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12AA')

    def _loc_1280(): pass

    label('loc_1280')

    Battle(0x00000144, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12AA')

    def _loc_1290(): pass

    label('loc_1290')

    Battle(0x00000145, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_12AA')

    def _loc_12A0(): pass

    label('loc_12A0')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_12AA(): pass

    label('loc_12AA')

    Jump('func_13_11E3')

    def _loc_12AD(): pass

    label('loc_12AD')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0014 offset: 0x12BB
@scena.Code('func_14_12BB')
def func_14_12BB():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_142F',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        60,
        1,
        (
            TXT(0x00, '玛诺利亚间道\n'),
            TXT(0x01, '梅威海道\n'),
            TXT(0x02, '街景林道\n'),
            TXT(0x03, '阿伊纳街道\n'),
            TXT(0x04, '绀碧之塔\n'),
            TXT(0x05, '卢安市长官邸内部（事件）\n'),
            TXT(0x06, '巴伦诺灯塔夜晚（事件）\n'),
            TXT(0x07, '卢安仓库内部（渡鸦帮）\n'),
            TXT(0x08, '旧校舍内部（事件）\n'),
            TXT(0x09, '巴伦诺灯塔白天（任务）\n'),
            TXT(0x0A, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_13B8'),
        (0x00000001, 'loc_13BF'),
        (0x00000002, 'loc_13C6'),
        (0x00000003, 'loc_13CD'),
        (0x00000004, 'loc_13D4'),
        (0x00000005, 'loc_13DB'),
        (0x00000006, 'loc_13EB'),
        (0x00000007, 'loc_13F2'),
        (0x00000008, 'loc_1402'),
        (0x00000009, 'loc_1412'),
        (-1, 'loc_1422'),
    )

    def _loc_13B8(): pass

    label('loc_13B8')

    Call(2, 0x0015)

    Jump('loc_142C')

    def _loc_13BF(): pass

    label('loc_13BF')

    Call(2, 0x0016)

    Jump('loc_142C')

    def _loc_13C6(): pass

    label('loc_13C6')

    Call(2, 0x0017)

    Jump('loc_142C')

    def _loc_13CD(): pass

    label('loc_13CD')

    Call(2, 0x0018)

    Jump('loc_142C')

    def _loc_13D4(): pass

    label('loc_13D4')

    Call(2, 0x0019)

    Jump('loc_142C')

    def _loc_13DB(): pass

    label('loc_13DB')

    Battle(0x00000394, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_142C')

    def _loc_13EB(): pass

    label('loc_13EB')

    Call(2, 0x001A)

    Jump('loc_142C')

    def _loc_13F2(): pass

    label('loc_13F2')

    Battle(0x00000397, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_142C')

    def _loc_1402(): pass

    label('loc_1402')

    Battle(0x00000399, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_142C')

    def _loc_1412(): pass

    label('loc_1412')

    Battle(0x000003F2, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_142C')

    def _loc_1422(): pass

    label('loc_1422')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_142C(): pass

    label('loc_142C')

    Jump('func_14_12BB')

    def _loc_142F(): pass

    label('loc_142F')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0015 offset: 0x143D
@scena.Code('func_15_143D')
def func_15_143D():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1507',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R2100_01\n'),
            TXT(0x01, 'R2100_02\n'),
            TXT(0x02, 'R2100_03\n'),
            TXT(0x03, 'R2100_04\n'),
            TXT(0x04, 'R2100_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_14AA'),
        (0x00000001, 'loc_14BA'),
        (0x00000002, 'loc_14CA'),
        (0x00000003, 'loc_14DA'),
        (0x00000004, 'loc_14EA'),
        (-1, 'loc_14FA'),
    )

    def _loc_14AA(): pass

    label('loc_14AA')

    Battle(0x00000169, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1504')

    def _loc_14BA(): pass

    label('loc_14BA')

    Battle(0x0000016A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1504')

    def _loc_14CA(): pass

    label('loc_14CA')

    Battle(0x0000016B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1504')

    def _loc_14DA(): pass

    label('loc_14DA')

    Battle(0x0000016C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1504')

    def _loc_14EA(): pass

    label('loc_14EA')

    Battle(0x0000016D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1504')

    def _loc_14FA(): pass

    label('loc_14FA')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1504(): pass

    label('loc_1504')

    Jump('func_15_143D')

    def _loc_1507(): pass

    label('loc_1507')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0016 offset: 0x1515
@scena.Code('func_16_1515')
def func_16_1515():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1652',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R2200_01主要\n'),
            TXT(0x01, 'R2200_02\n'),
            TXT(0x02, 'R2201_01沙滩\n'),
            TXT(0x03, 'R2201_02\n'),
            TXT(0x04, 'R2202_01主要(傍晚)\n'),
            TXT(0x05, 'R2202_02\n'),
            TXT(0x06, 'R2203_01沙滩(傍晚)\n'),
            TXT(0x07, 'R2203_02\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_15C5'),
        (0x00000001, 'loc_15D5'),
        (0x00000002, 'loc_15E5'),
        (0x00000003, 'loc_15F5'),
        (0x00000004, 'loc_1605'),
        (0x00000005, 'loc_1615'),
        (0x00000006, 'loc_1625'),
        (0x00000007, 'loc_1635'),
        (-1, 'loc_1645'),
    )

    def _loc_15C5(): pass

    label('loc_15C5')

    Battle(0x0000017D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_164F')

    def _loc_15D5(): pass

    label('loc_15D5')

    Battle(0x0000017E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_164F')

    def _loc_15E5(): pass

    label('loc_15E5')

    Battle(0x00000187, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_164F')

    def _loc_15F5(): pass

    label('loc_15F5')

    Battle(0x00000188, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_164F')

    def _loc_1605(): pass

    label('loc_1605')

    Battle(0x00000321, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_164F')

    def _loc_1615(): pass

    label('loc_1615')

    Battle(0x00000322, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_164F')

    def _loc_1625(): pass

    label('loc_1625')

    Battle(0x0000032B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_164F')

    def _loc_1635(): pass

    label('loc_1635')

    Battle(0x0000032C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_164F')

    def _loc_1645(): pass

    label('loc_1645')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_164F(): pass

    label('loc_164F')

    Jump('func_16_1515')

    def _loc_1652(): pass

    label('loc_1652')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0017 offset: 0x1660
@scena.Code('func_17_1660')
def func_17_1660():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17D9',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R2300_01\n'),
            TXT(0x01, 'R2300_02\n'),
            TXT(0x02, 'R2300_03\n'),
            TXT(0x03, 'R2300_04\n'),
            TXT(0x04, 'R2300_05\n'),
            TXT(0x05, 'R2301_01(傍晚)\n'),
            TXT(0x06, 'R2301_02(傍晚)\n'),
            TXT(0x07, 'R2301_03(傍晚)\n'),
            TXT(0x08, 'R2301_04(傍晚)\n'),
            TXT(0x09, 'R2301_05(傍晚)\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_172C'),
        (0x00000001, 'loc_173C'),
        (0x00000002, 'loc_174C'),
        (0x00000003, 'loc_175C'),
        (0x00000004, 'loc_176C'),
        (0x00000005, 'loc_177C'),
        (0x00000006, 'loc_178C'),
        (0x00000007, 'loc_179C'),
        (0x00000008, 'loc_17AC'),
        (0x00000009, 'loc_17BC'),
        (-1, 'loc_17CC'),
    )

    def _loc_172C(): pass

    label('loc_172C')

    Battle(0x00000191, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17D6')

    def _loc_173C(): pass

    label('loc_173C')

    Battle(0x00000192, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17D6')

    def _loc_174C(): pass

    label('loc_174C')

    Battle(0x00000193, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17D6')

    def _loc_175C(): pass

    label('loc_175C')

    Battle(0x00000194, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17D6')

    def _loc_176C(): pass

    label('loc_176C')

    Battle(0x00000195, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17D6')

    def _loc_177C(): pass

    label('loc_177C')

    Battle(0x00000335, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17D6')

    def _loc_178C(): pass

    label('loc_178C')

    Battle(0x00000336, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17D6')

    def _loc_179C(): pass

    label('loc_179C')

    Battle(0x00000337, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17D6')

    def _loc_17AC(): pass

    label('loc_17AC')

    Battle(0x00000338, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17D6')

    def _loc_17BC(): pass

    label('loc_17BC')

    Battle(0x00000339, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_17D6')

    def _loc_17CC(): pass

    label('loc_17CC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_17D6(): pass

    label('loc_17D6')

    Jump('func_17_1660')

    def _loc_17D9(): pass

    label('loc_17D9')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0018 offset: 0x17E7
@scena.Code('func_18_17E7')
def func_18_17E7():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18B1',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R2400_01\n'),
            TXT(0x01, 'R2400_02\n'),
            TXT(0x02, 'R2400_03\n'),
            TXT(0x03, 'R2400_04\n'),
            TXT(0x04, 'R2400_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1854'),
        (0x00000001, 'loc_1864'),
        (0x00000002, 'loc_1874'),
        (0x00000003, 'loc_1884'),
        (0x00000004, 'loc_1894'),
        (-1, 'loc_18A4'),
    )

    def _loc_1854(): pass

    label('loc_1854')

    Battle(0x000001A5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18AE')

    def _loc_1864(): pass

    label('loc_1864')

    Battle(0x000001A6, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18AE')

    def _loc_1874(): pass

    label('loc_1874')

    Battle(0x000001A7, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18AE')

    def _loc_1884(): pass

    label('loc_1884')

    Battle(0x000001A8, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18AE')

    def _loc_1894(): pass

    label('loc_1894')

    Battle(0x000001A9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_18AE')

    def _loc_18A4(): pass

    label('loc_18A4')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_18AE(): pass

    label('loc_18AE')

    Jump('func_18_17E7')

    def _loc_18B1(): pass

    label('loc_18B1')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0019 offset: 0x18BF
@scena.Code('func_19_18BF')
def func_19_18BF():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1989',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C2111_01\n'),
            TXT(0x01, 'C2111_02\n'),
            TXT(0x02, 'C2111_03\n'),
            TXT(0x03, 'C2111_04\n'),
            TXT(0x04, 'C2111_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_192C'),
        (0x00000001, 'loc_193C'),
        (0x00000002, 'loc_194C'),
        (0x00000003, 'loc_195C'),
        (0x00000004, 'loc_196C'),
        (-1, 'loc_197C'),
    )

    def _loc_192C(): pass

    label('loc_192C')

    Battle(0x000001B9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1986')

    def _loc_193C(): pass

    label('loc_193C')

    Battle(0x000001BA, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1986')

    def _loc_194C(): pass

    label('loc_194C')

    Battle(0x000001BB, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1986')

    def _loc_195C(): pass

    label('loc_195C')

    Battle(0x000001BC, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1986')

    def _loc_196C(): pass

    label('loc_196C')

    Battle(0x000001BD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1986')

    def _loc_197C(): pass

    label('loc_197C')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1986(): pass

    label('loc_1986')

    Jump('func_19_18BF')

    def _loc_1989(): pass

    label('loc_1989')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001A offset: 0x1997
@scena.Code('func_1A_1997')
def func_1A_1997():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A70',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'BTL_EVENT011(迪恩)\n'),
            TXT(0x01, 'BTL_EVENT012(雷斯)\n'),
            TXT(0x02, 'BTL_EVENT013(洛克)\n'),
            TXT(0x03, 'BTL_EVENT014(黑衣男子)\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1A23'),
        (0x00000001, 'loc_1A33'),
        (0x00000002, 'loc_1A43'),
        (0x00000003, 'loc_1A53'),
        (-1, 'loc_1A63'),
    )

    def _loc_1A23(): pass

    label('loc_1A23')

    Battle(0x0000038F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1A6D')

    def _loc_1A33(): pass

    label('loc_1A33')

    Battle(0x00000390, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1A6D')

    def _loc_1A43(): pass

    label('loc_1A43')

    Battle(0x00000391, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1A6D')

    def _loc_1A53(): pass

    label('loc_1A53')

    Battle(0x00000392, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1A6D')

    def _loc_1A63(): pass

    label('loc_1A63')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1A6D(): pass

    label('loc_1A6D')

    Jump('func_1A_1997')

    def _loc_1A70(): pass

    label('loc_1A70')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001B offset: 0x1A7E
@scena.Code('func_1B_1A7E')
def func_1B_1A7E():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B87',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        80,
        1,
        (
            TXT(0x00, '卡鲁迪亚隧道\n'),
            TXT(0x01, '卡鲁迪亚大钟乳洞\n'),
            TXT(0x02, '红莲之塔\n'),
            TXT(0x03, '托兰特平原道\n'),
            TXT(0x04, '利塔街道\n'),
            TXT(0x05, '佐达特军用道\n'),
            TXT(0x06, '雷斯顿水上要塞\n'),
            TXT(0x07, '红莲之塔（事件）\n'),
            TXT(0x08, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1B39'),
        (0x00000001, 'loc_1B40'),
        (0x00000002, 'loc_1B47'),
        (0x00000003, 'loc_1B4E'),
        (0x00000004, 'loc_1B55'),
        (0x00000005, 'loc_1B5C'),
        (0x00000006, 'loc_1B63'),
        (0x00000007, 'loc_1B6A'),
        (-1, 'loc_1B7A'),
    )

    def _loc_1B39(): pass

    label('loc_1B39')

    Call(2, 0x001C)

    Jump('loc_1B84')

    def _loc_1B40(): pass

    label('loc_1B40')

    Call(2, 0x001D)

    Jump('loc_1B84')

    def _loc_1B47(): pass

    label('loc_1B47')

    Call(2, 0x001E)

    Jump('loc_1B84')

    def _loc_1B4E(): pass

    label('loc_1B4E')

    Call(2, 0x001F)

    Jump('loc_1B84')

    def _loc_1B55(): pass

    label('loc_1B55')

    Call(2, 0x0020)

    Jump('loc_1B84')

    def _loc_1B5C(): pass

    label('loc_1B5C')

    Call(2, 0x0021)

    Jump('loc_1B84')

    def _loc_1B63(): pass

    label('loc_1B63')

    Call(2, 0x0022)

    Jump('loc_1B84')

    def _loc_1B6A(): pass

    label('loc_1B6A')

    Battle(0x000003A0, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1B84')

    def _loc_1B7A(): pass

    label('loc_1B7A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B84(): pass

    label('loc_1B84')

    Jump('func_1B_1A7E')

    def _loc_1B87(): pass

    label('loc_1B87')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001C offset: 0x1B95
@scena.Code('func_1C_1B95')
def func_1C_1B95():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C5F',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R3400_01\n'),
            TXT(0x01, 'R3400_02\n'),
            TXT(0x02, 'R3400_03\n'),
            TXT(0x03, 'R3400_04\n'),
            TXT(0x04, 'R3400_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1C02'),
        (0x00000001, 'loc_1C12'),
        (0x00000002, 'loc_1C22'),
        (0x00000003, 'loc_1C32'),
        (0x00000004, 'loc_1C42'),
        (-1, 'loc_1C52'),
    )

    def _loc_1C02(): pass

    label('loc_1C02')

    Battle(0x000001CD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1C5C')

    def _loc_1C12(): pass

    label('loc_1C12')

    Battle(0x000001CE, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1C5C')

    def _loc_1C22(): pass

    label('loc_1C22')

    Battle(0x000001CF, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1C5C')

    def _loc_1C32(): pass

    label('loc_1C32')

    Battle(0x000001D0, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1C5C')

    def _loc_1C42(): pass

    label('loc_1C42')

    Battle(0x000001D1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1C5C')

    def _loc_1C52(): pass

    label('loc_1C52')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1C5C(): pass

    label('loc_1C5C')

    Jump('func_1C_1B95')

    def _loc_1C5F(): pass

    label('loc_1C5F')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001D offset: 0x1C6D
@scena.Code('func_1D_1C6D')
def func_1D_1C6D():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D92',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C3300_01\n'),
            TXT(0x01, 'C3300_02\n'),
            TXT(0x02, 'C3300_03\n'),
            TXT(0x03, 'C3300_04\n'),
            TXT(0x04, 'C3300_05\n'),
            TXT(0x05, 'C3300_06\n'),
            TXT(0x06, 'C3300_07\n'),
            TXT(0x07, 'BTL_EVENT020\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1D05'),
        (0x00000001, 'loc_1D15'),
        (0x00000002, 'loc_1D25'),
        (0x00000003, 'loc_1D35'),
        (0x00000004, 'loc_1D45'),
        (0x00000005, 'loc_1D55'),
        (0x00000006, 'loc_1D65'),
        (0x00000007, 'loc_1D75'),
        (-1, 'loc_1D85'),
    )

    def _loc_1D05(): pass

    label('loc_1D05')

    Battle(0x000001E1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1D8F')

    def _loc_1D15(): pass

    label('loc_1D15')

    Battle(0x000001E2, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1D8F')

    def _loc_1D25(): pass

    label('loc_1D25')

    Battle(0x000001E3, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1D8F')

    def _loc_1D35(): pass

    label('loc_1D35')

    Battle(0x000001E4, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1D8F')

    def _loc_1D45(): pass

    label('loc_1D45')

    Battle(0x000001E5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1D8F')

    def _loc_1D55(): pass

    label('loc_1D55')

    Battle(0x000001E6, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1D8F')

    def _loc_1D65(): pass

    label('loc_1D65')

    Battle(0x000001E7, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1D8F')

    def _loc_1D75(): pass

    label('loc_1D75')

    Battle(0x00000398, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1D8F')

    def _loc_1D85(): pass

    label('loc_1D85')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1D8F(): pass

    label('loc_1D8F')

    Jump('func_1D_1C6D')

    def _loc_1D92(): pass

    label('loc_1D92')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001E offset: 0x1DA0
@scena.Code('func_1E_1DA0')
def func_1E_1DA0():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E6A',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C3511_01\n'),
            TXT(0x01, 'C3511_02\n'),
            TXT(0x02, 'C3511_03\n'),
            TXT(0x03, 'C3511_04\n'),
            TXT(0x04, 'C3511_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1E0D'),
        (0x00000001, 'loc_1E1D'),
        (0x00000002, 'loc_1E2D'),
        (0x00000003, 'loc_1E3D'),
        (0x00000004, 'loc_1E4D'),
        (-1, 'loc_1E5D'),
    )

    def _loc_1E0D(): pass

    label('loc_1E0D')

    Battle(0x000001F5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1E67')

    def _loc_1E1D(): pass

    label('loc_1E1D')

    Battle(0x000001F6, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1E67')

    def _loc_1E2D(): pass

    label('loc_1E2D')

    Battle(0x000001F7, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1E67')

    def _loc_1E3D(): pass

    label('loc_1E3D')

    Battle(0x000001F8, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1E67')

    def _loc_1E4D(): pass

    label('loc_1E4D')

    Battle(0x000001F9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1E67')

    def _loc_1E5D(): pass

    label('loc_1E5D')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1E67(): pass

    label('loc_1E67')

    Jump('func_1E_1DA0')

    def _loc_1E6A(): pass

    label('loc_1E6A')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001F offset: 0x1E78
@scena.Code('func_1F_1E78')
def func_1F_1E78():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FD3',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R3100_01\n'),
            TXT(0x01, 'R3100_02\n'),
            TXT(0x02, 'R3100_03\n'),
            TXT(0x03, 'R3100_04\n'),
            TXT(0x04, 'R3101_05\n'),
            TXT(0x05, 'R3101_01\n'),
            TXT(0x06, 'R3101_02\n'),
            TXT(0x07, 'R3101_03\n'),
            TXT(0x08, 'R3101_04\n'),
            TXT(0x09, 'R3101_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1F26'),
        (0x00000001, 'loc_1F36'),
        (0x00000002, 'loc_1F46'),
        (0x00000003, 'loc_1F56'),
        (0x00000004, 'loc_1F66'),
        (0x00000005, 'loc_1F76'),
        (0x00000006, 'loc_1F86'),
        (0x00000007, 'loc_1F96'),
        (0x00000008, 'loc_1FA6'),
        (0x00000009, 'loc_1FB6'),
        (-1, 'loc_1FC6'),
    )

    def _loc_1F26(): pass

    label('loc_1F26')

    Battle(0x00000209, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1FD0')

    def _loc_1F36(): pass

    label('loc_1F36')

    Battle(0x0000020A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1FD0')

    def _loc_1F46(): pass

    label('loc_1F46')

    Battle(0x0000020B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1FD0')

    def _loc_1F56(): pass

    label('loc_1F56')

    Battle(0x0000020C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1FD0')

    def _loc_1F66(): pass

    label('loc_1F66')

    Battle(0x0000020D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1FD0')

    def _loc_1F76(): pass

    label('loc_1F76')

    Battle(0x00000349, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1FD0')

    def _loc_1F86(): pass

    label('loc_1F86')

    Battle(0x0000034A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1FD0')

    def _loc_1F96(): pass

    label('loc_1F96')

    Battle(0x0000034B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1FD0')

    def _loc_1FA6(): pass

    label('loc_1FA6')

    Battle(0x0000034C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1FD0')

    def _loc_1FB6(): pass

    label('loc_1FB6')

    Battle(0x0000034D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1FD0')

    def _loc_1FC6(): pass

    label('loc_1FC6')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1FD0(): pass

    label('loc_1FD0')

    Jump('func_1F_1E78')

    def _loc_1FD3(): pass

    label('loc_1FD3')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0020 offset: 0x1FE1
@scena.Code('func_20_1FE1')
def func_20_1FE1():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20AB',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R3200_01\n'),
            TXT(0x01, 'R3200_02\n'),
            TXT(0x02, 'R3200_03\n'),
            TXT(0x03, 'R3200_04\n'),
            TXT(0x04, 'R3200_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_204E'),
        (0x00000001, 'loc_205E'),
        (0x00000002, 'loc_206E'),
        (0x00000003, 'loc_207E'),
        (0x00000004, 'loc_208E'),
        (-1, 'loc_209E'),
    )

    def _loc_204E(): pass

    label('loc_204E')

    Battle(0x0000021D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_20A8')

    def _loc_205E(): pass

    label('loc_205E')

    Battle(0x0000021E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_20A8')

    def _loc_206E(): pass

    label('loc_206E')

    Battle(0x0000021F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_20A8')

    def _loc_207E(): pass

    label('loc_207E')

    Battle(0x00000220, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_20A8')

    def _loc_208E(): pass

    label('loc_208E')

    Battle(0x00000221, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_20A8')

    def _loc_209E(): pass

    label('loc_209E')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_20A8(): pass

    label('loc_20A8')

    Jump('func_20_1FE1')

    def _loc_20AB(): pass

    label('loc_20AB')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0021 offset: 0x20B9
@scena.Code('func_21_20B9')
def func_21_20B9():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2183',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R3300_01\n'),
            TXT(0x01, 'R3300_02\n'),
            TXT(0x02, 'R3300_03\n'),
            TXT(0x03, 'R3300_04\n'),
            TXT(0x04, 'R3300_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2126'),
        (0x00000001, 'loc_2136'),
        (0x00000002, 'loc_2146'),
        (0x00000003, 'loc_2156'),
        (0x00000004, 'loc_2166'),
        (-1, 'loc_2176'),
    )

    def _loc_2126(): pass

    label('loc_2126')

    Battle(0x00000231, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2180')

    def _loc_2136(): pass

    label('loc_2136')

    Battle(0x00000232, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2180')

    def _loc_2146(): pass

    label('loc_2146')

    Battle(0x00000233, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2180')

    def _loc_2156(): pass

    label('loc_2156')

    Battle(0x00000234, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2180')

    def _loc_2166(): pass

    label('loc_2166')

    Battle(0x00000235, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2180')

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

    def _loc_2180(): pass

    label('loc_2180')

    Jump('func_21_20B9')

    def _loc_2183(): pass

    label('loc_2183')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0022 offset: 0x2191
@scena.Code('func_22_2191')
def func_22_2191():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2280',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C3107_01\n'),
            TXT(0x01, 'C3107_02\n'),
            TXT(0x02, 'C3107_10\n'),
            TXT(0x03, 'C3107_11\n'),
            TXT(0x04, 'C3107_12\n'),
            TXT(0x05, 'C3107_14特务兵Ｃ\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2213'),
        (0x00000001, 'loc_2223'),
        (0x00000002, 'loc_2233'),
        (0x00000003, 'loc_2243'),
        (0x00000004, 'loc_2253'),
        (0x00000005, 'loc_2263'),
        (-1, 'loc_2273'),
    )

    def _loc_2213(): pass

    label('loc_2213')

    Battle(0x00000245, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_227D')

    def _loc_2223(): pass

    label('loc_2223')

    Battle(0x00000246, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_227D')

    def _loc_2233(): pass

    label('loc_2233')

    Battle(0x0000024E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_227D')

    def _loc_2243(): pass

    label('loc_2243')

    Battle(0x0000024F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_227D')

    def _loc_2253(): pass

    label('loc_2253')

    Battle(0x00000250, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_227D')

    def _loc_2263(): pass

    label('loc_2263')

    Battle(0x00000252, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_227D')

    def _loc_2273(): pass

    label('loc_2273')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_227D(): pass

    label('loc_227D')

    Jump('func_22_2191')

    def _loc_2280(): pass

    label('loc_2280')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0023 offset: 0x228E
@scena.Code('func_23_228E')
def func_23_228E():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2424',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        2,
        10,
        80,
        1,
        (
            TXT(0x00, '艾尔贝周游道\n'),
            TXT(0x01, '地下水路\n'),
            TXT(0x02, '封印区域\n'),
            TXT(0x03, '庭园大道\n'),
            TXT(0x04, '艾尔贝离宫外部　中庭、回廊（夜晚）\n'),
            TXT(0x05, '艾尔贝离宫外部　内部（夜晚）\n'),
            TXT(0x06, '格兰赛尔城内部、中庭、女王宫内\n'),
            TXT(0x07, '格兰赛尔城内部、空中庭园\n'),
            TXT(0x08, '封印区域BOSS其它（凯诺娜、理查德、洛伦斯）\n'),
            TXT(0x09, '王都格兰赛尔外部（竞技场内部）\n'),
            TXT(0x0A, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_23D1'),
        (0x00000001, 'loc_23D8'),
        (0x00000002, 'loc_23DF'),
        (0x00000003, 'loc_23E6'),
        (0x00000004, 'loc_23ED'),
        (0x00000005, 'loc_23F4'),
        (0x00000006, 'loc_23FB'),
        (0x00000007, 'loc_2402'),
        (0x00000008, 'loc_2409'),
        (0x00000009, 'loc_2410'),
        (-1, 'loc_2417'),
    )

    def _loc_23D1(): pass

    label('loc_23D1')

    Call(2, 0x0024)

    Jump('loc_2421')

    def _loc_23D8(): pass

    label('loc_23D8')

    Call(2, 0x0025)

    Jump('loc_2421')

    def _loc_23DF(): pass

    label('loc_23DF')

    Call(2, 0x0026)

    Jump('loc_2421')

    def _loc_23E6(): pass

    label('loc_23E6')

    Call(2, 0x0027)

    Jump('loc_2421')

    def _loc_23ED(): pass

    label('loc_23ED')

    Call(2, 0x0028)

    Jump('loc_2421')

    def _loc_23F4(): pass

    label('loc_23F4')

    Call(2, 0x0029)

    Jump('loc_2421')

    def _loc_23FB(): pass

    label('loc_23FB')

    Call(2, 0x002A)

    Jump('loc_2421')

    def _loc_2402(): pass

    label('loc_2402')

    Call(2, 0x002B)

    Jump('loc_2421')

    def _loc_2409(): pass

    label('loc_2409')

    Call(2, 0x002C)

    Jump('loc_2421')

    def _loc_2410(): pass

    label('loc_2410')

    Call(2, 0x002D)

    Jump('loc_2421')

    def _loc_2417(): pass

    label('loc_2417')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2421(): pass

    label('loc_2421')

    Jump('func_23_228E')

    def _loc_2424(): pass

    label('loc_2424')

    OP_5F(0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0024 offset: 0x2432
@scena.Code('func_24_2432')
def func_24_2432():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24FC',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C4100_01\n'),
            TXT(0x01, 'C4100_02\n'),
            TXT(0x02, 'C4100_03\n'),
            TXT(0x03, 'C4100_04\n'),
            TXT(0x04, 'C4100_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_249F'),
        (0x00000001, 'loc_24AF'),
        (0x00000002, 'loc_24BF'),
        (0x00000003, 'loc_24CF'),
        (0x00000004, 'loc_24DF'),
        (-1, 'loc_24EF'),
    )

    def _loc_249F(): pass

    label('loc_249F')

    Battle(0x00000259, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_24F9')

    def _loc_24AF(): pass

    label('loc_24AF')

    Battle(0x0000025A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_24F9')

    def _loc_24BF(): pass

    label('loc_24BF')

    Battle(0x0000025B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_24F9')

    def _loc_24CF(): pass

    label('loc_24CF')

    Battle(0x0000025C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_24F9')

    def _loc_24DF(): pass

    label('loc_24DF')

    Battle(0x0000025D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_24F9')

    def _loc_24EF(): pass

    label('loc_24EF')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_24F9(): pass

    label('loc_24F9')

    Jump('func_24_2432')

    def _loc_24FC(): pass

    label('loc_24FC')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0025 offset: 0x250A
@scena.Code('func_25_250A')
def func_25_250A():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2648',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C4200_01\n'),
            TXT(0x01, 'C4200_02\n'),
            TXT(0x02, 'C4200_03\n'),
            TXT(0x03, 'C4200_04\n'),
            TXT(0x04, 'C4200_05\n'),
            TXT(0x05, 'C4200_06\n'),
            TXT(0x06, 'C4200_07\n'),
            TXT(0x07, 'C4200_08\n'),
            TXT(0x08, 'C4200_09\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_25AB'),
        (0x00000001, 'loc_25BB'),
        (0x00000002, 'loc_25CB'),
        (0x00000003, 'loc_25DB'),
        (0x00000004, 'loc_25EB'),
        (0x00000005, 'loc_25FB'),
        (0x00000006, 'loc_260B'),
        (0x00000007, 'loc_261B'),
        (0x00000008, 'loc_262B'),
        (-1, 'loc_263B'),
    )

    def _loc_25AB(): pass

    label('loc_25AB')

    Battle(0x0000026D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2645')

    def _loc_25BB(): pass

    label('loc_25BB')

    Battle(0x0000026E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2645')

    def _loc_25CB(): pass

    label('loc_25CB')

    Battle(0x0000026F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2645')

    def _loc_25DB(): pass

    label('loc_25DB')

    Battle(0x00000270, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2645')

    def _loc_25EB(): pass

    label('loc_25EB')

    Battle(0x00000271, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2645')

    def _loc_25FB(): pass

    label('loc_25FB')

    Battle(0x00000272, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2645')

    def _loc_260B(): pass

    label('loc_260B')

    Battle(0x00000273, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2645')

    def _loc_261B(): pass

    label('loc_261B')

    Battle(0x00000274, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2645')

    def _loc_262B(): pass

    label('loc_262B')

    Battle(0x00000275, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2645')

    def _loc_263B(): pass

    label('loc_263B')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2645(): pass

    label('loc_2645')

    Jump('func_25_250A')

    def _loc_2648(): pass

    label('loc_2648')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0026 offset: 0x2656
@scena.Code('func_26_2656')
def func_26_2656():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27B1',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C4300_01\n'),
            TXT(0x01, 'C4300_02\n'),
            TXT(0x02, 'C4300_03\n'),
            TXT(0x03, 'C4300_04\n'),
            TXT(0x04, 'C4300_05\n'),
            TXT(0x05, 'C4300_06\n'),
            TXT(0x06, 'C4300_07\n'),
            TXT(0x07, 'C4300_08\n'),
            TXT(0x08, 'C4300_09\n'),
            TXT(0x09, 'C4300_10\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2704'),
        (0x00000001, 'loc_2714'),
        (0x00000002, 'loc_2724'),
        (0x00000003, 'loc_2734'),
        (0x00000004, 'loc_2744'),
        (0x00000005, 'loc_2754'),
        (0x00000006, 'loc_2764'),
        (0x00000007, 'loc_2774'),
        (0x00000008, 'loc_2784'),
        (0x00000009, 'loc_2794'),
        (-1, 'loc_27A4'),
    )

    def _loc_2704(): pass

    label('loc_2704')

    Battle(0x00000281, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_27AE')

    def _loc_2714(): pass

    label('loc_2714')

    Battle(0x00000282, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_27AE')

    def _loc_2724(): pass

    label('loc_2724')

    Battle(0x00000283, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_27AE')

    def _loc_2734(): pass

    label('loc_2734')

    Battle(0x00000284, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_27AE')

    def _loc_2744(): pass

    label('loc_2744')

    Battle(0x00000285, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_27AE')

    def _loc_2754(): pass

    label('loc_2754')

    Battle(0x00000286, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_27AE')

    def _loc_2764(): pass

    label('loc_2764')

    Battle(0x00000287, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_27AE')

    def _loc_2774(): pass

    label('loc_2774')

    Battle(0x00000288, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_27AE')

    def _loc_2784(): pass

    label('loc_2784')

    Battle(0x00000289, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_27AE')

    def _loc_2794(): pass

    label('loc_2794')

    Battle(0x0000028A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_27AE')

    def _loc_27A4(): pass

    label('loc_27A4')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_27AE(): pass

    label('loc_27AE')

    Jump('func_26_2656')

    def _loc_27B1(): pass

    label('loc_27B1')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0027 offset: 0x27BF
@scena.Code('func_27_27BF')
def func_27_27BF():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2889',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R4100_01\n'),
            TXT(0x01, 'R4100_02\n'),
            TXT(0x02, 'R4100_03\n'),
            TXT(0x03, 'R4100_04\n'),
            TXT(0x04, 'R4100_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_282C'),
        (0x00000001, 'loc_283C'),
        (0x00000002, 'loc_284C'),
        (0x00000003, 'loc_285C'),
        (0x00000004, 'loc_286C'),
        (-1, 'loc_287C'),
    )

    def _loc_282C(): pass

    label('loc_282C')

    Battle(0x00000295, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2886')

    def _loc_283C(): pass

    label('loc_283C')

    Battle(0x00000296, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2886')

    def _loc_284C(): pass

    label('loc_284C')

    Battle(0x00000297, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2886')

    def _loc_285C(): pass

    label('loc_285C')

    Battle(0x00000298, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2886')

    def _loc_286C(): pass

    label('loc_286C')

    Battle(0x00000299, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2886')

    def _loc_287C(): pass

    label('loc_287C')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2886(): pass

    label('loc_2886')

    Jump('func_27_27BF')

    def _loc_2889(): pass

    label('loc_2889')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0028 offset: 0x2897
@scena.Code('func_28_2897')
def func_28_2897():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2961',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'T4301_01\n'),
            TXT(0x01, 'T4301_02\n'),
            TXT(0x02, 'T4301_03\n'),
            TXT(0x03, 'T4301_04\n'),
            TXT(0x04, 'T4301_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2904'),
        (0x00000001, 'loc_2914'),
        (0x00000002, 'loc_2924'),
        (0x00000003, 'loc_2934'),
        (0x00000004, 'loc_2944'),
        (-1, 'loc_2954'),
    )

    def _loc_2904(): pass

    label('loc_2904')

    Battle(0x000002BD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_295E')

    def _loc_2914(): pass

    label('loc_2914')

    Battle(0x000002BE, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_295E')

    def _loc_2924(): pass

    label('loc_2924')

    Battle(0x000002BF, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_295E')

    def _loc_2934(): pass

    label('loc_2934')

    Battle(0x000002C0, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_295E')

    def _loc_2944(): pass

    label('loc_2944')

    Battle(0x000002C1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_295E')

    def _loc_2954(): pass

    label('loc_2954')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_295E(): pass

    label('loc_295E')

    Jump('func_28_2897')

    def _loc_2961(): pass

    label('loc_2961')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0029 offset: 0x296F
@scena.Code('func_29_296F')
def func_29_296F():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A39',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'T4310_01\n'),
            TXT(0x01, 'T4310_02\n'),
            TXT(0x02, 'T4310_03\n'),
            TXT(0x03, 'T4310_04\n'),
            TXT(0x04, 'T4310_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_29DC'),
        (0x00000001, 'loc_29EC'),
        (0x00000002, 'loc_29FC'),
        (0x00000003, 'loc_2A0C'),
        (0x00000004, 'loc_2A1C'),
        (-1, 'loc_2A2C'),
    )

    def _loc_29DC(): pass

    label('loc_29DC')

    Battle(0x000002D1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2A36')

    def _loc_29EC(): pass

    label('loc_29EC')

    Battle(0x000002D2, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2A36')

    def _loc_29FC(): pass

    label('loc_29FC')

    Battle(0x000002D3, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2A36')

    def _loc_2A0C(): pass

    label('loc_2A0C')

    Battle(0x000002D4, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2A36')

    def _loc_2A1C(): pass

    label('loc_2A1C')

    Battle(0x000002D5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2A36')

    def _loc_2A2C(): pass

    label('loc_2A2C')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2A36(): pass

    label('loc_2A36')

    Jump('func_29_296F')

    def _loc_2A39(): pass

    label('loc_2A39')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x002A offset: 0x2A47
@scena.Code('func_2A_2A47')
def func_2A_2A47():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B11',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'T4210_01\n'),
            TXT(0x01, 'T4210_02\n'),
            TXT(0x02, 'T4210_03\n'),
            TXT(0x03, 'T4210_04\n'),
            TXT(0x04, 'T4210_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2AB4'),
        (0x00000001, 'loc_2AC4'),
        (0x00000002, 'loc_2AD4'),
        (0x00000003, 'loc_2AE4'),
        (0x00000004, 'loc_2AF4'),
        (-1, 'loc_2B04'),
    )

    def _loc_2AB4(): pass

    label('loc_2AB4')

    Battle(0x000002E5, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B0E')

    def _loc_2AC4(): pass

    label('loc_2AC4')

    Battle(0x000002E6, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B0E')

    def _loc_2AD4(): pass

    label('loc_2AD4')

    Battle(0x000002E7, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B0E')

    def _loc_2AE4(): pass

    label('loc_2AE4')

    Battle(0x000002E8, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B0E')

    def _loc_2AF4(): pass

    label('loc_2AF4')

    Battle(0x000002E9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B0E')

    def _loc_2B04(): pass

    label('loc_2B04')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2B0E(): pass

    label('loc_2B0E')

    Jump('func_2A_2A47')

    def _loc_2B11(): pass

    label('loc_2B11')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x002B offset: 0x2B1F
@scena.Code('func_2B_2B1F')
def func_2B_2B1F():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BE9',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'T4201_01\n'),
            TXT(0x01, 'T4201_02\n'),
            TXT(0x02, 'T4201_03\n'),
            TXT(0x03, 'T4201_04\n'),
            TXT(0x04, 'T4201_05\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2B8C'),
        (0x00000001, 'loc_2B9C'),
        (0x00000002, 'loc_2BAC'),
        (0x00000003, 'loc_2BBC'),
        (0x00000004, 'loc_2BCC'),
        (-1, 'loc_2BDC'),
    )

    def _loc_2B8C(): pass

    label('loc_2B8C')

    Battle(0x000002F9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2BE6')

    def _loc_2B9C(): pass

    label('loc_2B9C')

    Battle(0x000002FA, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2BE6')

    def _loc_2BAC(): pass

    label('loc_2BAC')

    Battle(0x000002FB, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2BE6')

    def _loc_2BBC(): pass

    label('loc_2BBC')

    Battle(0x000002FC, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2BE6')

    def _loc_2BCC(): pass

    label('loc_2BCC')

    Battle(0x000002FD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2BE6')

    def _loc_2BDC(): pass

    label('loc_2BDC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2BE6(): pass

    label('loc_2BE6')

    Jump('func_2B_2B1F')

    def _loc_2BE9(): pass

    label('loc_2BE9')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x002C offset: 0x2BF7
@scena.Code('func_2C_2BF7')
def func_2C_2BF7():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CD3',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '洛伦斯\n'),
            TXT(0x01, '凯诺娜\n'),
            TXT(0x02, '理查德\n'),
            TXT(0x03, '最终BOSS第一形态\n'),
            TXT(0x04, '最终BOSS第二形态\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2C6E'),
        (0x00000001, 'loc_2C7E'),
        (0x00000002, 'loc_2C8E'),
        (0x00000003, 'loc_2C9E'),
        (0x00000004, 'loc_2CB2'),
        (-1, 'loc_2CC6'),
    )

    def _loc_2C6E(): pass

    label('loc_2C6E')

    Battle(0x0000039A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2CD0')

    def _loc_2C7E(): pass

    label('loc_2C7E')

    Battle(0x0000039B, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2CD0')

    def _loc_2C8E(): pass

    label('loc_2C8E')

    Battle(0x0000039C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2CD0')

    def _loc_2C9E(): pass

    label('loc_2C9E')

    Call(2, 0x0030)
    Battle(0x000003A1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2CD0')

    def _loc_2CB2(): pass

    label('loc_2CB2')

    Call(2, 0x0030)
    Battle(0x000003A2, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2CD0')

    def _loc_2CC6(): pass

    label('loc_2CC6')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2CD0(): pass

    label('loc_2CD0')

    Jump('func_2C_2BF7')

    def _loc_2CD3(): pass

    label('loc_2CD3')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x002D offset: 0x2CE1
@scena.Code('func_2D_2CE1')
def func_2D_2CE1():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DAD',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '迪恩、雷斯、洛克、杂鱼\n'),
            TXT(0x01, '克鲁茨、库拉茨、卡露娜、亚妮拉丝\n'),
            TXT(0x02, '洛伦斯、特务兵、特务兵、特务兵\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2D70'),
        (0x00000001, 'loc_2D80'),
        (0x00000002, 'loc_2D90'),
        (-1, 'loc_2DA0'),
    )

    def _loc_2D70(): pass

    label('loc_2D70')

    Battle(0x0000039D, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2DAA')

    def _loc_2D80(): pass

    label('loc_2D80')

    Battle(0x0000039E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2DAA')

    def _loc_2D90(): pass

    label('loc_2D90')

    Battle(0x0000039F, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2DAA')

    def _loc_2DA0(): pass

    label('loc_2DA0')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2DAA(): pass

    label('loc_2DAA')

    Jump('func_2D_2CE1')

    def _loc_2DAD(): pass

    label('loc_2DAD')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x002E offset: 0x2DBB
@scena.Code('func_2E_2DBB')
def func_2E_2DBB():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E85',
    )

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'R4100_21\n'),
            TXT(0x01, 'R4100_22\n'),
            TXT(0x02, 'R4100_23\n'),
            TXT(0x03, 'R4100_24\n'),
            TXT(0x04, 'R4100_25\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2E28'),
        (0x00000001, 'loc_2E38'),
        (0x00000002, 'loc_2E48'),
        (0x00000003, 'loc_2E58'),
        (0x00000004, 'loc_2E68'),
        (-1, 'loc_2E78'),
    )

    def _loc_2E28(): pass

    label('loc_2E28')

    Battle(0x000002A9, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2E82')

    def _loc_2E38(): pass

    label('loc_2E38')

    Battle(0x000002AA, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2E82')

    def _loc_2E48(): pass

    label('loc_2E48')

    Battle(0x000002AB, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2E82')

    def _loc_2E58(): pass

    label('loc_2E58')

    Battle(0x000002AC, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2E82')

    def _loc_2E68(): pass

    label('loc_2E68')

    Battle(0x000002AD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2E82')

    def _loc_2E78(): pass

    label('loc_2E78')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2E82(): pass

    label('loc_2E82')

    Jump('func_2E_2DBB')

    def _loc_2E85(): pass

    label('loc_2E85')

    OP_5F(0x0003)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x002F offset: 0x2E93
@scena.Code('func_2F_2E93')
def func_2F_2E93():
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0000, 0x05, 0)
    SetChrStatus(0x0001, 0x05, 0)

    Talk(
        (
            TxtCtl.ShowAll,
            '请选择',
            TxtCtl.Enter,
        ),
    )

    def _loc_2EB1(): pass

    label('loc_2EB1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30E2',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '杂鱼中的杂鱼\n'),
            TXT(0x01, '爆种铃兰\n'),
            TXT(0x02, '事件战斗、田鼠\n'),
            TXT(0x03, '波波＋食人鲨\n'),
            TXT(0x04, '有NPC的战斗\n'),
            TXT(0x05, '空贼战\n'),
            TXT(0x06, '自动战斗１\n'),
            TXT(0x07, '竞技场①\n'),
            TXT(0x08, '竞技场②\n'),
            TXT(0x09, '竞技场③\n'),
            TXT(0x0A, '竞技场④\n'),
            TXT(0x0B, '竞技场⑤\n'),
            TXT(0x0C, '竞技场⑥\n'),
            TXT(0x0D, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2F92'),
        (0x00000001, 'loc_2FA2'),
        (0x00000002, 'loc_2FB2'),
        (0x00000003, 'loc_2FE6'),
        (0x00000004, 'loc_2FF6'),
        (0x00000005, 'loc_300C'),
        (0x00000006, 'loc_301C'),
        (0x00000007, 'loc_3035'),
        (0x00000008, 'loc_304E'),
        (0x00000009, 'loc_3067'),
        (0x0000000A, 'loc_3080'),
        (0x0000000B, 'loc_3099'),
        (0x0000000C, 'loc_30B2'),
        (-1, 'loc_30CB'),
    )

    def _loc_2F92(): pass

    label('loc_2F92')

    Battle(0x0000007A, 0x00000000, 0x00, 0x0002, 0xFF)

    Jump('loc_30D5')

    def _loc_2FA2(): pass

    label('loc_2FA2')

    Battle(0x00000018, 0x00000000, 0x00, 0x0002, 0xFF)

    Jump('loc_30D5')

    def _loc_2FB2(): pass

    label('loc_2FB2')

    Talk(
        (
            '这是事件战斗，请打倒所有的敌人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Battle(0x00000393, 0x00000000, 0x00, 0x0002, 0xFF)

    Jump('loc_30D5')

    def _loc_2FE6(): pass

    label('loc_2FE6')

    Battle(0x00000038, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_30D5')

    def _loc_2FF6(): pass

    label('loc_2FF6')

    FormationAddMember(0x0E, 0xFF)
    FormationAddMember(0x0F, 0xFF)
    Battle(0x0000007A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_30D5')

    def _loc_300C(): pass

    label('loc_300C')

    Battle(0x00000387, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_30D5')

    def _loc_301C(): pass

    label('loc_301C')

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BB8, 0x00100001, 0x00, 0x0200, 0xFF)

    Jump('loc_30D5')

    def _loc_3035(): pass

    label('loc_3035')

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BB9, 0x00100002, 0x00, 0x0200, 0xFF)

    Jump('loc_30D5')

    def _loc_304E(): pass

    label('loc_304E')

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBA, 0x00100003, 0x00, 0x0200, 0xFF)

    Jump('loc_30D5')

    def _loc_3067(): pass

    label('loc_3067')

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBB, 0x00100004, 0x00, 0x0200, 0xFF)

    Jump('loc_30D5')

    def _loc_3080(): pass

    label('loc_3080')

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBC, 0x00100005, 0x00, 0x0200, 0xFF)

    Jump('loc_30D5')

    def _loc_3099(): pass

    label('loc_3099')

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBD, 0x00100006, 0x00, 0x0200, 0xFF)

    Jump('loc_30D5')

    def _loc_30B2(): pass

    label('loc_30B2')

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBE, 0x00100007, 0x00, 0x0200, 0xFF)

    Jump('loc_30D5')

    def _loc_30CB(): pass

    label('loc_30CB')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_30D5(): pass

    label('loc_30D5')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2EB1')

    def _loc_30E2(): pass

    label('loc_30E2')

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

# id: 0x0030 offset: 0x30F2
@scena.Code('func_30_30F2')
def func_30_30F2():
    SetChrStatus(0x0000, 0x00, 39)
    SetChrStatus(0x0001, 0x00, 39)
    SetChrStatus(0x0002, 0x00, 39)
    SetChrStatus(0x0003, 0x00, 39)
    SetChrStatus(0x0006, 0x00, 39)
    SetChrStatus(0x0004, 0x00, 39)
    SetChrStatus(0x0005, 0x00, 39)
    SetChrStatus(0x0007, 0x00, 39)
    SetChrStatus(0x0000, 0x05, 100)
    SetChrStatus(0x0001, 0x05, 100)
    SetChrStatus(0x0002, 0x05, 100)
    SetChrStatus(0x0003, 0x05, 100)
    SetChrStatus(0x0006, 0x05, 100)
    SetChrStatus(0x0004, 0x05, 100)
    SetChrStatus(0x0005, 0x05, 100)
    SetChrStatus(0x0007, 0x05, 100)
    AddItem(0x01F5, 99)
    AddItem(0x01F6, 99)
    AddItem(0x01F7, 99)
    AddItem(0x01FB, 99)
    AddItem(0x01FC, 99)
    AddItem(0x01FD, 10)
    AddItem(0x01FF, 99)
    AddItem(0x01FF, 99)
    OP_34(0x01, 0x003C)
    OP_34(0x01, 0x003E)
    OP_34(0x01, 0x0041)
    OP_34(0x01, 0x003F)
    OP_34(0x01, 0x005F)
    OP_34(0x01, 0x0060)
    OP_34(0x01, 0x0069)
    OP_34(0x01, 0x006A)
    OP_34(0x00, 0x001E)
    OP_34(0x00, 0x001F)
    OP_34(0x00, 0x0020)
    OP_34(0x00, 0x0023)
    OP_34(0x00, 0x0025)
    OP_34(0x00, 0x006E)
    OP_34(0x00, 0x006F)
    OP_34(0x00, 0x0070)
    OP_34(0x00, 0x0076)
    OP_34(0x00, 0x0077)
    OP_34(0x00, 0x0078)
    OP_34(0x02, 0x0032)
    OP_34(0x02, 0x0033)
    OP_34(0x02, 0x0034)
    OP_34(0x02, 0x0036)
    OP_34(0x02, 0x0037)
    OP_34(0x03, 0x0064)
    OP_34(0x03, 0x0069)
    OP_34(0x03, 0x0069)
    OP_34(0x03, 0x004B)
    OP_34(0x03, 0x004C)
    OP_34(0x04, 0x006E)
    OP_34(0x04, 0x006F)
    OP_34(0x04, 0x0070)
    OP_34(0x04, 0x0072)
    OP_34(0x04, 0x0073)
    OP_34(0x04, 0x0076)
    OP_34(0x04, 0x0077)
    OP_34(0x04, 0x0078)
    OP_34(0x05, 0x001E)
    OP_34(0x05, 0x001F)
    OP_34(0x05, 0x0020)
    OP_34(0x06, 0x0056)
    OP_34(0x06, 0x0057)
    OP_34(0x06, 0x0058)
    OP_34(0x06, 0x006E)
    OP_34(0x06, 0x006F)
    OP_34(0x06, 0x0076)
    OP_34(0x07, 0x000B)
    OP_34(0x07, 0x000D)
    OP_34(0x07, 0x0010)
    OP_34(0x07, 0x004B)
    OP_34(0x07, 0x004C)
    EquipCmd(0x00, 0x000A)
    EquipCmd(0x00, 0x00FE)
    EquipCmd(0x00, 0x0119)
    EquipCmd(0x01, 0x0029)
    EquipCmd(0x01, 0x00FD)
    EquipCmd(0x01, 0x011A)
    EquipCmd(0x02, 0x0041)
    EquipCmd(0x02, 0x00FE)
    EquipCmd(0x02, 0x0119)
    EquipCmd(0x03, 0x0062)
    EquipCmd(0x03, 0x00FD)
    EquipCmd(0x03, 0x011A)
    EquipCmd(0x04, 0x0080)
    EquipCmd(0x04, 0x00FE)
    EquipCmd(0x04, 0x0119)
    EquipCmd(0x05, 0x009D)
    EquipCmd(0x05, 0x00FD)
    EquipCmd(0x05, 0x011A)
    EquipCmd(0x06, 0x00BB)
    EquipCmd(0x06, 0x00FE)
    EquipCmd(0x06, 0x0119)
    EquipCmd(0x07, 0x00D9)
    EquipCmd(0x07, 0x00FD)
    EquipCmd(0x07, 0x011A)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
