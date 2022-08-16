import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0001_3_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0001_3 ._SN')

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
            '哪个？',
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
        'loc_101',
    )

    Menu(
        1,
        10,
        32,
        1,
        (
            TXT(0x00, '后篇\n'),
            TXT(0x01, '前篇\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_E6'),
        (0x00000001, 'loc_ED'),
        (-1, 'loc_F4'),
    )

    def _loc_E6(): pass

    label('loc_E6')

    Call(3, 0x0001)

    Jump('loc_FE')

    def _loc_ED(): pass

    label('loc_ED')

    Call(3, 0x0002)

    Jump('loc_FE')

    def _loc_F4(): pass

    label('loc_F4')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_FE(): pass

    label('loc_FE')

    Jump('loc_B2')

    def _loc_101(): pass

    label('loc_101')

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

# id: 0x0001 offset: 0x111
@scena.Code('func_01_111')
def func_01_111():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪个？',
            TxtCtl.Enter,
        ),
    )

    def _loc_11B(): pass

    label('loc_11B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31C',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, 'A0020 队伍与专用ＮＰＬ\n'),
            TXT(0x01, 'A0021战斗艾丝蒂尔 约修亚 金 阿加特 奥利维尔\n'),
            TXT(0x02, 'A0022 战斗雪拉、提妲、科洛丝、科洛丝礼服\n'),
            TXT(0x03, 'A0023 战斗凯文，亚尼拉丝，乔丝特，克鲁茨\n'),
            TXT(0x04, 'A0024 战斗尤莉亚，穆拉，基德，凯诺娜\n'),
            TXT(0x05, 'A0025 战斗瓦鲁特，玲，露茜奥拉，布卢布兰\n'),
            TXT(0x06, 'A0026 战斗莱恩哈特，怀斯曼，猎兵约修亚、乌猫蝶\n'),
            TXT(0x07, 'A0027 战斗猎兵Ａ，猎兵Ｂ，克鲁茨，卡露娜，基尔巴特\n'),
            TXT(0x08, 'A0039 后篇座位一览\n'),
            TXT(0x09, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2BE'),
        (0x00000001, 'loc_2C7'),
        (0x00000002, 'loc_2D0'),
        (0x00000003, 'loc_2D9'),
        (0x00000004, 'loc_2E2'),
        (0x00000005, 'loc_2EB'),
        (0x00000006, 'loc_2F4'),
        (0x00000007, 'loc_2FD'),
        (0x00000008, 'loc_306'),
        (-1, 'loc_30F'),
    )

    def _loc_2BE(): pass

    label('loc_2BE')

    NewScene('ED6_DT21/A0020._SN', 0, 0, 0)
    IdleLoop()

    def _loc_2C7(): pass

    label('loc_2C7')

    NewScene('ED6_DT21/A0021._SN', 0, 0, 0)
    IdleLoop()

    def _loc_2D0(): pass

    label('loc_2D0')

    NewScene('ED6_DT21/A0022._SN', 0, 0, 0)
    IdleLoop()

    def _loc_2D9(): pass

    label('loc_2D9')

    NewScene('ED6_DT21/A0023._SN', 0, 0, 0)
    IdleLoop()

    def _loc_2E2(): pass

    label('loc_2E2')

    NewScene('ED6_DT21/A0024._SN', 0, 0, 0)
    IdleLoop()

    def _loc_2EB(): pass

    label('loc_2EB')

    NewScene('ED6_DT21/A0025._SN', 0, 0, 0)
    IdleLoop()

    def _loc_2F4(): pass

    label('loc_2F4')

    NewScene('ED6_DT21/A0026._SN', 0, 0, 0)
    IdleLoop()

    def _loc_2FD(): pass

    label('loc_2FD')

    NewScene('ED6_DT21/A0027._SN', 0, 0, 0)
    IdleLoop()

    def _loc_306(): pass

    label('loc_306')

    NewScene('ED6_DT21/A0039._SN', 0, 0, 0)
    IdleLoop()

    def _loc_30F(): pass

    label('loc_30F')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_11B')

    def _loc_31C(): pass

    label('loc_31C')

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

# id: 0x0002 offset: 0x32C
@scena.Code('func_02_32C')
def func_02_32C():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪个？',
            TxtCtl.Enter,
        ),
    )

    def _loc_336(): pass

    label('loc_336')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_501',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '30泛用ＮＰＬ\n'),
            TXT(0x01, '31队伍与专用ＮＰＬ\n'),
            TXT(0x02, '32泛用ＮＰＬ与专用ＮＰＬ２＿ＡＰＬ\n'),
            TXT(0x03, '33PT战斗艾丝蒂尔、约修亚、金、阿加特、奥利维尔\n'),
            TXT(0x04, '34PT战斗约修亚、雪拉扎德、提妲、科洛丝\n'),
            TXT(0x05, '35NPC战斗男女游击士、小流氓、空贼们\n'),
            TXT(0x06, '36NPC战斗小流氓团伙、男女游击士２\n'),
            TXT(0x07, '37NPC战斗王国兵士、士官、特务兵、洛伦斯、理查德、凯诺娜\n'),
            TXT(0x08, '39座位角色\n'),
            TXT(0x09, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4A3'),
        (0x00000001, 'loc_4AC'),
        (0x00000002, 'loc_4B5'),
        (0x00000003, 'loc_4BE'),
        (0x00000004, 'loc_4C7'),
        (0x00000005, 'loc_4D0'),
        (0x00000006, 'loc_4D9'),
        (0x00000007, 'loc_4E2'),
        (0x00000008, 'loc_4EB'),
        (-1, 'loc_4F4'),
    )

    def _loc_4A3(): pass

    label('loc_4A3')

    NewScene('ED6_DT21/T0030._SN', 0, 0, 0)
    IdleLoop()

    def _loc_4AC(): pass

    label('loc_4AC')

    NewScene('ED6_DT21/T0031._SN', 0, 0, 0)
    IdleLoop()

    def _loc_4B5(): pass

    label('loc_4B5')

    NewScene('ED6_DT21/T0032._SN', 0, 0, 0)
    IdleLoop()

    def _loc_4BE(): pass

    label('loc_4BE')

    NewScene('ED6_DT21/T0033._SN', 0, 0, 0)
    IdleLoop()

    def _loc_4C7(): pass

    label('loc_4C7')

    NewScene('ED6_DT21/T0034._SN', 0, 0, 0)
    IdleLoop()

    def _loc_4D0(): pass

    label('loc_4D0')

    NewScene('ED6_DT21/T0035._SN', 0, 0, 0)
    IdleLoop()

    def _loc_4D9(): pass

    label('loc_4D9')

    NewScene('ED6_DT21/T0036._SN', 0, 0, 0)
    IdleLoop()

    def _loc_4E2(): pass

    label('loc_4E2')

    NewScene('ED6_DT21/T0037._SN', 0, 0, 0)
    IdleLoop()

    def _loc_4EB(): pass

    label('loc_4EB')

    NewScene('ED6_DT21/T0039._SN', 0, 0, 0)
    IdleLoop()

    def _loc_4F4(): pass

    label('loc_4F4')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_336')

    def _loc_501(): pass

    label('loc_501')

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

# id: 0x0003 offset: 0x511
@scena.Code('func_03_511')
def func_03_511():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪个？',
            TxtCtl.Enter,
        ),
    )

    def _loc_51B(): pass

    label('loc_51B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56A',
    )

    Menu(
        1,
        10,
        32,
        1,
        (
            TXT(0x00, '后篇\n'),
            TXT(0x01, '前篇\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_54F'),
        (0x00000001, 'loc_556'),
        (-1, 'loc_55D'),
    )

    def _loc_54F(): pass

    label('loc_54F')

    Call(3, 0x0005)

    Jump('loc_567')

    def _loc_556(): pass

    label('loc_556')

    Call(3, 0x0004)

    Jump('loc_567')

    def _loc_55D(): pass

    label('loc_55D')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_567(): pass

    label('loc_567')

    Jump('loc_51B')

    def _loc_56A(): pass

    label('loc_56A')

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

# id: 0x0004 offset: 0x57A
@scena.Code('func_04_57A')
def func_04_57A():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪个？',
            TxtCtl.Enter,
        ),
    )

    def _loc_584(): pass

    label('loc_584')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_92C',
    )

    Menu(
        2,
        10,
        32,
        1,
        (
            TXT(0x00, '40魔兽列表（10000-10290）\n'),
            TXT(0x01, '41魔兽列表（10300-10590）\n'),
            TXT(0x02, '42魔兽列表（10600-10890）\n'),
            TXT(0x03, '57魔兽列表（10900-11040）\n'),
            TXT(0x04, '60魔兽列表（11050-11190）\n'),
            TXT(0x05, '43魔兽动作（10000-10050）\n'),
            TXT(0x06, '44魔兽动作（10060-10140）\n'),
            TXT(0x07, '45魔兽动作（10150-10210）\n'),
            TXT(0x08, '46魔兽动作（10220-10290）\n'),
            TXT(0x09, '47魔兽动作（10300-10380）\n'),
            TXT(0x0A, '48魔兽动作（10390-10450）\n'),
            TXT(0x0B, '49魔兽动作（10460-10530）\n'),
            TXT(0x0C, '50魔兽动作（10540-10610）\n'),
            TXT(0x0D, '51魔兽动作（10620-10690）\n'),
            TXT(0x0E, '52魔兽动作（10700-10770）\n'),
            TXT(0x0F, '53魔兽动作（10780-10850）\n'),
            TXT(0x10, '54魔兽动作（10860-10900）\n'),
            TXT(0x11, '55魔兽动作（10910-10940）\n'),
            TXT(0x12, '56魔兽动作（10950-10990）\n'),
            TXT(0x13, '58魔兽动作（11000-11060）\n'),
            TXT(0x14, '59魔兽动作（11070-11110）\n'),
            TXT(0x15, '61魔兽动作（11120-11150）\n'),
            TXT(0x16, '62魔兽动作（11160-11190）\n'),
            TXT(0x17, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_859'),
        (0x00000001, 'loc_862'),
        (0x00000002, 'loc_86B'),
        (0x00000003, 'loc_874'),
        (0x00000004, 'loc_87D'),
        (0x00000005, 'loc_886'),
        (0x00000006, 'loc_88F'),
        (0x00000007, 'loc_898'),
        (0x00000008, 'loc_8A1'),
        (0x00000009, 'loc_8AA'),
        (0x0000000A, 'loc_8B3'),
        (0x0000000B, 'loc_8BC'),
        (0x0000000C, 'loc_8C5'),
        (0x0000000D, 'loc_8CE'),
        (0x0000000E, 'loc_8D7'),
        (0x0000000F, 'loc_8E0'),
        (0x00000010, 'loc_8E9'),
        (0x00000011, 'loc_8F2'),
        (0x00000012, 'loc_8FB'),
        (0x00000013, 'loc_904'),
        (0x00000014, 'loc_90D'),
        (0x00000015, 'loc_916'),
        (-1, 'loc_91F'),
    )

    def _loc_859(): pass

    label('loc_859')

    NewScene('ED6_DT21/T0040._SN', 0, 0, 0)
    IdleLoop()

    def _loc_862(): pass

    label('loc_862')

    NewScene('ED6_DT21/T0041._SN', 0, 0, 0)
    IdleLoop()

    def _loc_86B(): pass

    label('loc_86B')

    NewScene('ED6_DT21/T0042._SN', 0, 0, 0)
    IdleLoop()

    def _loc_874(): pass

    label('loc_874')

    NewScene('ED6_DT21/T0057._SN', 0, 0, 0)
    IdleLoop()

    def _loc_87D(): pass

    label('loc_87D')

    NewScene('ED6_DT21/T0060._SN', 0, 0, 0)
    IdleLoop()

    def _loc_886(): pass

    label('loc_886')

    NewScene('ED6_DT21/T0043._SN', 0, 0, 0)
    IdleLoop()

    def _loc_88F(): pass

    label('loc_88F')

    NewScene('ED6_DT21/T0044._SN', 0, 0, 0)
    IdleLoop()

    def _loc_898(): pass

    label('loc_898')

    NewScene('ED6_DT21/T0045._SN', 0, 0, 0)
    IdleLoop()

    def _loc_8A1(): pass

    label('loc_8A1')

    NewScene('ED6_DT21/T0046._SN', 0, 0, 0)
    IdleLoop()

    def _loc_8AA(): pass

    label('loc_8AA')

    NewScene('ED6_DT21/T0047._SN', 0, 0, 0)
    IdleLoop()

    def _loc_8B3(): pass

    label('loc_8B3')

    NewScene('ED6_DT21/T0048._SN', 0, 0, 0)
    IdleLoop()

    def _loc_8BC(): pass

    label('loc_8BC')

    NewScene('ED6_DT21/T0049._SN', 0, 0, 0)
    IdleLoop()

    def _loc_8C5(): pass

    label('loc_8C5')

    NewScene('ED6_DT21/T0050._SN', 0, 0, 0)
    IdleLoop()

    def _loc_8CE(): pass

    label('loc_8CE')

    NewScene('ED6_DT21/T0051._SN', 0, 0, 0)
    IdleLoop()

    def _loc_8D7(): pass

    label('loc_8D7')

    NewScene('ED6_DT21/T0052._SN', 0, 0, 0)
    IdleLoop()

    def _loc_8E0(): pass

    label('loc_8E0')

    NewScene('ED6_DT21/T0053._SN', 0, 0, 0)
    IdleLoop()

    def _loc_8E9(): pass

    label('loc_8E9')

    NewScene('ED6_DT21/T0054._SN', 0, 0, 0)
    IdleLoop()

    def _loc_8F2(): pass

    label('loc_8F2')

    NewScene('ED6_DT21/T0055._SN', 0, 0, 0)
    IdleLoop()

    def _loc_8FB(): pass

    label('loc_8FB')

    NewScene('ED6_DT21/T0056._SN', 0, 0, 0)
    IdleLoop()

    def _loc_904(): pass

    label('loc_904')

    NewScene('ED6_DT21/T0058._SN', 0, 0, 0)
    IdleLoop()

    def _loc_90D(): pass

    label('loc_90D')

    NewScene('ED6_DT21/T0059._SN', 0, 0, 0)
    IdleLoop()

    def _loc_916(): pass

    label('loc_916')

    NewScene('ED6_DT21/T0061._SN', 0, 0, 0)
    IdleLoop()

    def _loc_91F(): pass

    label('loc_91F')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_584')

    def _loc_92C(): pass

    label('loc_92C')

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

# id: 0x0005 offset: 0x93C
@scena.Code('func_05_93C')
def func_05_93C():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪个？',
            TxtCtl.Enter,
        ),
    )

    def _loc_946(): pass

    label('loc_946')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B7E',
    )

    Menu(
        2,
        10,
        32,
        1,
        (
            TXT(0x00, 'A0000 魔兽列表（12000-12040）\n'),
            TXT(0x01, 'A0001 魔兽列表（12050-12090）\n'),
            TXT(0x02, 'A0002 魔兽列表（12100-12140）\n'),
            TXT(0x03, 'A0003 魔兽列表（12150-12190）\n'),
            TXT(0x04, 'A0004 魔兽列表（12200-12240）\n'),
            TXT(0x05, 'A0005 魔兽列表（12250-12290）\n'),
            TXT(0x06, 'A0006 魔兽列表（12300-12340）\n'),
            TXT(0x07, 'A0007 魔兽列表（12350-12390）\n'),
            TXT(0x08, 'A0008 魔兽列表（12400-12440）\n'),
            TXT(0x09, 'A0009 魔兽列表（12450-12490）\n'),
            TXT(0x0A, 'A0010 魔兽列表（12500-12520）\n'),
            TXT(0x0B, 'A0011 魔兽列表（12530-12540）\n'),
            TXT(0x0C, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_B05'),
        (0x00000001, 'loc_B0E'),
        (0x00000002, 'loc_B17'),
        (0x00000003, 'loc_B20'),
        (0x00000004, 'loc_B29'),
        (0x00000005, 'loc_B32'),
        (0x00000006, 'loc_B3B'),
        (0x00000007, 'loc_B44'),
        (0x00000008, 'loc_B4D'),
        (0x00000009, 'loc_B56'),
        (0x0000000A, 'loc_B5F'),
        (0x0000000B, 'loc_B68'),
        (-1, 'loc_B71'),
    )

    def _loc_B05(): pass

    label('loc_B05')

    NewScene('ED6_DT21/A0000._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B0E(): pass

    label('loc_B0E')

    NewScene('ED6_DT21/A0001._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B17(): pass

    label('loc_B17')

    NewScene('ED6_DT21/A0002._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B20(): pass

    label('loc_B20')

    NewScene('ED6_DT21/A0003._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B29(): pass

    label('loc_B29')

    NewScene('ED6_DT21/A0004._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B32(): pass

    label('loc_B32')

    NewScene('ED6_DT21/A0005._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B3B(): pass

    label('loc_B3B')

    NewScene('ED6_DT21/A0006._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B44(): pass

    label('loc_B44')

    NewScene('ED6_DT21/A0007._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B4D(): pass

    label('loc_B4D')

    NewScene('ED6_DT21/A0008._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B56(): pass

    label('loc_B56')

    NewScene('ED6_DT21/A0009._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B5F(): pass

    label('loc_B5F')

    NewScene('ED6_DT21/A0010._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B68(): pass

    label('loc_B68')

    NewScene('ED6_DT21/A0011._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B71(): pass

    label('loc_B71')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_946')

    def _loc_B7E(): pass

    label('loc_B7E')

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

# id: 0x0006 offset: 0xB8E
@scena.Code('func_06_B8E')
def func_06_B8E():
    Talk(
        (
            TxtCtl.ShowAll,
            '这是地图。请选择。',
            TxtCtl.Enter,
        ),
    )

    def _loc_BA4(): pass

    label('loc_BA4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C98',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '洛连特地区\n'),
            TXT(0x01, '柏斯地区\n'),
            TXT(0x02, '卢安地区\n'),
            TXT(0x03, '蔡斯地区\n'),
            TXT(0x04, '格兰赛尔地区\n'),
            TXT(0x05, '辉之环、训练所、古罗力亚斯内部等\n'),
            TXT(0x06, '事件，飞船\n'),
            TXT(0x07, '看动画。\n'),
            TXT(0x08, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_C53'),
        (0x00000001, 'loc_C5A'),
        (0x00000002, 'loc_C61'),
        (0x00000003, 'loc_C68'),
        (0x00000004, 'loc_C6F'),
        (0x00000005, 'loc_C76'),
        (0x00000006, 'loc_C7D'),
        (0x00000007, 'loc_C84'),
        (-1, 'loc_C8B'),
    )

    def _loc_C53(): pass

    label('loc_C53')

    Call(3, 0x0007)

    Jump('loc_C95')

    def _loc_C5A(): pass

    label('loc_C5A')

    Call(3, 0x0008)

    Jump('loc_C95')

    def _loc_C61(): pass

    label('loc_C61')

    Call(3, 0x0009)

    Jump('loc_C95')

    def _loc_C68(): pass

    label('loc_C68')

    Call(3, 0x000A)

    Jump('loc_C95')

    def _loc_C6F(): pass

    label('loc_C6F')

    Call(3, 0x000B)

    Jump('loc_C95')

    def _loc_C76(): pass

    label('loc_C76')

    Call(3, 0x000C)

    Jump('loc_C95')

    def _loc_C7D(): pass

    label('loc_C7D')

    Call(3, 0x000D)

    Jump('loc_C95')

    def _loc_C84(): pass

    label('loc_C84')

    Call(3, 0x000E)

    Jump('loc_C95')

    def _loc_C8B(): pass

    label('loc_C8B')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C95(): pass

    label('loc_C95')

    Jump('loc_BA4')

    def _loc_C98(): pass

    label('loc_C98')

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

# id: 0x0007 offset: 0xCA8
@scena.Code('func_07_CA8')
def func_07_CA8():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    def _loc_CB2(): pass

    label('loc_CB2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11D0',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '城里\n'),
            TXT(0x01, '迷宫\n'),
            TXT(0x02, '大道\n'),
            TXT(0x03, '夜\n'),
            TXT(0x04, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_CFB'),
        (0x00000001, 'loc_E4A'),
        (0x00000002, 'loc_10D8'),
        (0x00000003, 'loc_1177'),
        (-1, 'loc_11C3'),
    )

    def _loc_CFB(): pass

    label('loc_CFB')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        120,
        1,
        (
            TXT(0x00, '洛连特\n'),
            TXT(0x01, '市长邸\n'),
            TXT(0x02, '布莱特家\n'),
            TXT(0x03, '帕赛尔农场\n'),
            TXT(0x04, '帕赛尔农场（夜晚）\n'),
            TXT(0x05, '威尔特关所\n'),
            TXT(0x06, '飞船坪\n'),
            TXT(0x07, '布莱特家\n'),
            TXT(0x08, '格鲁纳门\n'),
            TXT(0x09, '洛连特（夜晚）\n'),
            TXT(0x0A, '市长邸（夜晚）\n'),
            TXT(0x0B, '飞船坪（夜晚）\n'),
            TXT(0x0C, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_DD5'),
        (0x00000001, 'loc_DDE'),
        (0x00000002, 'loc_DE7'),
        (0x00000003, 'loc_DF0'),
        (0x00000004, 'loc_DF9'),
        (0x00000005, 'loc_E02'),
        (0x00000006, 'loc_E0B'),
        (0x00000007, 'loc_E14'),
        (0x00000008, 'loc_E1D'),
        (0x00000009, 'loc_E26'),
        (0x0000000A, 'loc_E2F'),
        (0x0000000B, 'loc_E38'),
        (-1, 'loc_E41'),
    )

    def _loc_DD5(): pass

    label('loc_DD5')

    NewScene('ED6_DT21/T0100._SN', 119, 0, 0)
    IdleLoop()

    def _loc_DDE(): pass

    label('loc_DDE')

    NewScene('ED6_DT21/T0200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_DE7(): pass

    label('loc_DE7')

    NewScene('ED6_DT21/T0300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_DF0(): pass

    label('loc_DF0')

    NewScene('ED6_DT21/T0400._SN', 100, 0, 0)
    IdleLoop()

    def _loc_DF9(): pass

    label('loc_DF9')

    NewScene('ED6_DT21/T0401._SN', 100, 0, 0)
    IdleLoop()

    def _loc_E02(): pass

    label('loc_E02')

    NewScene('ED6_DT21/T0500._SN', 100, 0, 0)
    IdleLoop()

    def _loc_E0B(): pass

    label('loc_E0B')

    NewScene('ED6_DT21/T0700._SN', 100, 0, 0)
    IdleLoop()

    def _loc_E14(): pass

    label('loc_E14')

    NewScene('ED6_DT21/T0300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_E1D(): pass

    label('loc_E1D')

    NewScene('ED6_DT21/T0600._SN', 100, 0, 0)
    IdleLoop()

    def _loc_E26(): pass

    label('loc_E26')

    NewScene('ED6_DT21/T0101._SN', 119, 0, 0)
    IdleLoop()

    def _loc_E2F(): pass

    label('loc_E2F')

    NewScene('ED6_DT21/T0201._SN', 100, 0, 0)
    IdleLoop()

    def _loc_E38(): pass

    label('loc_E38')

    NewScene('ED6_DT21/T0701._SN', 100, 0, 0)
    IdleLoop()

    def _loc_E41(): pass

    label('loc_E41')

    OP_5F(0x0003)

    Jump('loc_E47')

    def _loc_E47(): pass

    label('loc_E47')

    Jump('loc_11CD')

    def _loc_E4A(): pass

    label('loc_E4A')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        120,
        1,
        (
            TXT(0x00, '玛鲁加矿山（前篇）\n'),
            TXT(0x01, '玛鲁加矿山（后篇８章任务用）\n'),
            TXT(0x02, '神秘森林\n'),
            TXT(0x03, '神秘森林圈\n'),
            TXT(0x04, '地下水路\n'),
            TXT(0x05, '翡翠之塔1F（前半）\n'),
            TXT(0x06, '翡翠之塔2F（前半）\n'),
            TXT(0x07, '翡翠之塔3F（前半）\n'),
            TXT(0x08, '翡翠之塔4F（前半）\n'),
            TXT(0x09, '翡翠之塔5F（前半）\n'),
            TXT(0x0A, '翡翠之塔1F（后半）\n'),
            TXT(0x0B, '翡翠之塔2F（后半）\n'),
            TXT(0x0C, '翡翠之塔3F（后半）\n'),
            TXT(0x0D, '翡翠之塔4F（后半）\n'),
            TXT(0x0E, '翡翠之塔5F（后半）\n'),
            TXT(0x0F, '翡翠之塔屋顶（后半 异次元背景）\n'),
            TXT(0x10, '翡翠之塔屋顶（后半 异次元背景，埃尔赛尤视点）\n'),
            TXT(0x11, '翡翠之塔屋顶（后半 一般背景）\n'),
            TXT(0x12, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_102D'),
        (0x00000001, 'loc_1036'),
        (0x00000002, 'loc_103F'),
        (0x00000003, 'loc_1048'),
        (0x00000004, 'loc_1051'),
        (0x00000005, 'loc_105A'),
        (0x00000006, 'loc_1063'),
        (0x00000007, 'loc_106C'),
        (0x00000008, 'loc_1075'),
        (0x00000009, 'loc_107E'),
        (0x0000000A, 'loc_1087'),
        (0x0000000B, 'loc_1090'),
        (0x0000000C, 'loc_1099'),
        (0x0000000D, 'loc_10A2'),
        (0x0000000E, 'loc_10AB'),
        (0x0000000F, 'loc_10B4'),
        (0x00000010, 'loc_10BD'),
        (0x00000011, 'loc_10C6'),
        (-1, 'loc_10CF'),
    )

    def _loc_102D(): pass

    label('loc_102D')

    NewScene('ED6_DT21/C0100._SN', 103, 0, 0)
    IdleLoop()

    def _loc_1036(): pass

    label('loc_1036')

    NewScene('ED6_DT21/C0101._SN', 103, 0, 0)
    IdleLoop()

    def _loc_103F(): pass

    label('loc_103F')

    NewScene('ED6_DT21/C0300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1048(): pass

    label('loc_1048')

    NewScene('ED6_DT21/C0304._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1051(): pass

    label('loc_1051')

    NewScene('ED6_DT21/C0500._SN', 100, 0, 0)
    IdleLoop()

    def _loc_105A(): pass

    label('loc_105A')

    NewScene('ED6_DT21/C0411._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1063(): pass

    label('loc_1063')

    NewScene('ED6_DT21/C0412._SN', 100, 0, 0)
    IdleLoop()

    def _loc_106C(): pass

    label('loc_106C')

    NewScene('ED6_DT21/C0413._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1075(): pass

    label('loc_1075')

    NewScene('ED6_DT21/C0414._SN', 100, 0, 0)
    IdleLoop()

    def _loc_107E(): pass

    label('loc_107E')

    NewScene('ED6_DT21/C0415._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1087(): pass

    label('loc_1087')

    NewScene('ED6_DT21/C0700._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1090(): pass

    label('loc_1090')

    NewScene('ED6_DT21/C0701._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1099(): pass

    label('loc_1099')

    NewScene('ED6_DT21/C0702._SN', 100, 0, 0)
    IdleLoop()

    def _loc_10A2(): pass

    label('loc_10A2')

    NewScene('ED6_DT21/C0703._SN', 100, 0, 0)
    IdleLoop()

    def _loc_10AB(): pass

    label('loc_10AB')

    NewScene('ED6_DT21/C0704._SN', 100, 0, 0)
    IdleLoop()

    def _loc_10B4(): pass

    label('loc_10B4')

    NewScene('ED6_DT21/C0705._SN', 100, 0, 0)
    IdleLoop()

    def _loc_10BD(): pass

    label('loc_10BD')

    NewScene('ED6_DT21/C0706._SN', 100, 0, 0)
    IdleLoop()

    def _loc_10C6(): pass

    label('loc_10C6')

    NewScene('ED6_DT21/C0707._SN', 100, 0, 0)
    IdleLoop()

    def _loc_10CF(): pass

    label('loc_10CF')

    OP_5F(0x0003)

    Jump('loc_10D5')

    def _loc_10D5(): pass

    label('loc_10D5')

    Jump('loc_11CD')

    def _loc_10D8(): pass

    label('loc_10D8')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        120,
        1,
        (
            TXT(0x00, '艾利兹街道\n'),
            TXT(0x01, '米尔西街道\n'),
            TXT(0x02, '玛鲁加山道\n'),
            TXT(0x03, '米尔西街道军用艇\n'),
            TXT(0x04, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_113E'),
        (0x00000001, 'loc_114A'),
        (0x00000002, 'loc_1156'),
        (0x00000003, 'loc_1162'),
        (-1, 'loc_116E'),
    )

    def _loc_113E(): pass

    label('loc_113E')

    NewScene('ED6_DT21/R0100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1174')

    def _loc_114A(): pass

    label('loc_114A')

    NewScene('ED6_DT21/R0200._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1174')

    def _loc_1156(): pass

    label('loc_1156')

    NewScene('ED6_DT21/R0300._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1174')

    def _loc_1162(): pass

    label('loc_1162')

    NewScene('ED6_DT21/R0203._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1174')

    def _loc_116E(): pass

    label('loc_116E')

    OP_5F(0x0003)

    Jump('loc_1174')

    def _loc_1174(): pass

    label('loc_1174')

    Jump('loc_11CD')

    def _loc_1177(): pass

    label('loc_1177')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        120,
        1,
        (
            TXT(0x00, '布莱特家·外观\n'),
            TXT(0x01, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_11AE'),
        (-1, 'loc_11BA'),
    )

    def _loc_11AE(): pass

    label('loc_11AE')

    NewScene('ED6_DT21/T0311._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_11C0')

    def _loc_11BA(): pass

    label('loc_11BA')

    OP_5F(0x0003)

    Jump('loc_11C0')

    def _loc_11C0(): pass

    label('loc_11C0')

    Jump('loc_11CD')

    def _loc_11C3(): pass

    label('loc_11C3')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11CD(): pass

    label('loc_11CD')

    Jump('loc_CB2')

    def _loc_11D0(): pass

    label('loc_11D0')

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

# id: 0x0008 offset: 0x11E0
@scena.Code('func_08_11E0')
def func_08_11E0():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    def _loc_11EA(): pass

    label('loc_11EA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1774',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '城里\n'),
            TXT(0x01, '迷宫\n'),
            TXT(0x02, '大道\n'),
            TXT(0x03, '夜\n'),
            TXT(0x04, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1233'),
        (0x00000001, 'loc_1380'),
        (0x00000002, 'loc_15E0'),
        (0x00000003, 'loc_16BB'),
        (-1, 'loc_1764'),
    )

    def _loc_1233(): pass

    label('loc_1233')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '柏斯城，南门\n'),
            TXT(0x01, '柏斯城，民房\n'),
            TXT(0x02, '古罗尼关所\n'),
            TXT(0x03, '古罗尼关所（夜晚）\n'),
            TXT(0x04, '柏斯国际空港\n'),
            TXT(0x05, '拉文努村\n'),
            TXT(0x06, '拉文努村（夜晚）\n'),
            TXT(0x07, '哈肯大门\n'),
            TXT(0x08, '哈肯大门北部平原\n'),
            TXT(0x09, '湖畔旅馆\n'),
            TXT(0x0A, '柏斯城北，破坏\n'),
            TXT(0x0B, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1314'),
        (0x00000001, 'loc_131D'),
        (0x00000002, 'loc_1326'),
        (0x00000003, 'loc_132F'),
        (0x00000004, 'loc_1338'),
        (0x00000005, 'loc_1341'),
        (0x00000006, 'loc_134A'),
        (0x00000007, 'loc_1353'),
        (0x00000008, 'loc_135C'),
        (0x00000009, 'loc_1365'),
        (0x0000000A, 'loc_136E'),
        (-1, 'loc_1377'),
    )

    def _loc_1314(): pass

    label('loc_1314')

    NewScene('ED6_DT21/T1100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_131D(): pass

    label('loc_131D')

    NewScene('ED6_DT21/T1110._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1326(): pass

    label('loc_1326')

    NewScene('ED6_DT21/T1300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_132F(): pass

    label('loc_132F')

    NewScene('ED6_DT21/T1301._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1338(): pass

    label('loc_1338')

    NewScene('ED6_DT21/T1102._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1341(): pass

    label('loc_1341')

    NewScene('ED6_DT21/T1200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_134A(): pass

    label('loc_134A')

    NewScene('ED6_DT21/T1211._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1353(): pass

    label('loc_1353')

    NewScene('ED6_DT21/T1400._SN', 100, 0, 0)
    IdleLoop()

    def _loc_135C(): pass

    label('loc_135C')

    NewScene('ED6_DT21/T1402._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1365(): pass

    label('loc_1365')

    NewScene('ED6_DT21/T1500._SN', 100, 0, 0)
    IdleLoop()

    def _loc_136E(): pass

    label('loc_136E')

    NewScene('ED6_DT21/T1103._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1377(): pass

    label('loc_1377')

    OP_5F(0x0003)

    Jump('loc_137D')

    def _loc_137D(): pass

    label('loc_137D')

    Jump('loc_1771')

    def _loc_1380(): pass

    label('loc_1380')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '迷雾峡谷\n'),
            TXT(0x01, '拉文努废坑后篇\n'),
            TXT(0x02, '空贼城寨\n'),
            TXT(0x03, '古龙的住处\n'),
            TXT(0x04, '琥珀之塔1F（前半）\n'),
            TXT(0x05, '琥珀之塔2F（前半）\n'),
            TXT(0x06, '琥珀之塔3F（前半）\n'),
            TXT(0x07, '琥珀之塔4F（前半）\n'),
            TXT(0x08, '琥珀之塔5F（前半）\n'),
            TXT(0x09, '琥珀之塔1F（后半）\n'),
            TXT(0x0A, '琥珀之塔2F（后半）\n'),
            TXT(0x0B, '琥珀之塔3F（后半）\n'),
            TXT(0x0C, '琥珀之塔4F（后半）\n'),
            TXT(0x0D, '琥珀之塔5F（后半）\n'),
            TXT(0x0E, '琥珀之塔屋顶（后半 异次元背景）\n'),
            TXT(0x0F, '琥珀之塔屋顶（后半 异次元背景，埃尔赛尤视点）\n'),
            TXT(0x10, '琥珀之塔屋顶（后半 一般背景）\n'),
            TXT(0x11, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_153E'),
        (0x00000001, 'loc_1547'),
        (0x00000002, 'loc_1550'),
        (0x00000003, 'loc_1559'),
        (0x00000004, 'loc_1562'),
        (0x00000005, 'loc_156B'),
        (0x00000006, 'loc_1574'),
        (0x00000007, 'loc_157D'),
        (0x00000008, 'loc_1586'),
        (0x00000009, 'loc_158F'),
        (0x0000000A, 'loc_1598'),
        (0x0000000B, 'loc_15A1'),
        (0x0000000C, 'loc_15AA'),
        (0x0000000D, 'loc_15B3'),
        (0x0000000E, 'loc_15BC'),
        (0x0000000F, 'loc_15C5'),
        (0x00000010, 'loc_15CE'),
        (-1, 'loc_15D7'),
    )

    def _loc_153E(): pass

    label('loc_153E')

    NewScene('ED6_DT21/C1400._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1547(): pass

    label('loc_1547')

    NewScene('ED6_DT21/C1102._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1550(): pass

    label('loc_1550')

    NewScene('ED6_DT21/C1300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1559(): pass

    label('loc_1559')

    NewScene('ED6_DT21/C1600._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1562(): pass

    label('loc_1562')

    NewScene('ED6_DT21/C1211._SN', 100, 0, 0)
    IdleLoop()

    def _loc_156B(): pass

    label('loc_156B')

    NewScene('ED6_DT21/C1212._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1574(): pass

    label('loc_1574')

    NewScene('ED6_DT21/C1213._SN', 100, 0, 0)
    IdleLoop()

    def _loc_157D(): pass

    label('loc_157D')

    NewScene('ED6_DT21/C1214._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1586(): pass

    label('loc_1586')

    NewScene('ED6_DT21/C1215._SN', 100, 0, 0)
    IdleLoop()

    def _loc_158F(): pass

    label('loc_158F')

    NewScene('ED6_DT21/C1700._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1598(): pass

    label('loc_1598')

    NewScene('ED6_DT21/C1701._SN', 100, 0, 0)
    IdleLoop()

    def _loc_15A1(): pass

    label('loc_15A1')

    NewScene('ED6_DT21/C1702._SN', 100, 0, 0)
    IdleLoop()

    def _loc_15AA(): pass

    label('loc_15AA')

    NewScene('ED6_DT21/C1703._SN', 100, 0, 0)
    IdleLoop()

    def _loc_15B3(): pass

    label('loc_15B3')

    NewScene('ED6_DT21/C1704._SN', 100, 0, 0)
    IdleLoop()

    def _loc_15BC(): pass

    label('loc_15BC')

    NewScene('ED6_DT21/C1705._SN', 100, 0, 0)
    IdleLoop()

    def _loc_15C5(): pass

    label('loc_15C5')

    NewScene('ED6_DT21/C1706._SN', 100, 0, 0)
    IdleLoop()

    def _loc_15CE(): pass

    label('loc_15CE')

    NewScene('ED6_DT21/C1707._SN', 100, 0, 0)
    IdleLoop()

    def _loc_15D7(): pass

    label('loc_15D7')

    OP_5F(0x0003)

    Jump('loc_15DD')

    def _loc_15DD(): pass

    label('loc_15DD')

    Jump('loc_1771')

    def _loc_15E0(): pass

    label('loc_15E0')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '古罗尼山道\n'),
            TXT(0x01, '钢壁之路\n'),
            TXT(0x02, '东柏斯街道\n'),
            TXT(0x03, '西柏斯街道\n'),
            TXT(0x04, '安塞尔新街\n'),
            TXT(0x05, '安塞尔新街（夜晚）\n'),
            TXT(0x06, '拉文努山道\n'),
            TXT(0x07, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1673'),
        (0x00000001, 'loc_167C'),
        (0x00000002, 'loc_1685'),
        (0x00000003, 'loc_168E'),
        (0x00000004, 'loc_1697'),
        (0x00000005, 'loc_16A0'),
        (0x00000006, 'loc_16A9'),
        (-1, 'loc_16B2'),
    )

    def _loc_1673(): pass

    label('loc_1673')

    NewScene('ED6_DT21/C1500._SN', 100, 0, 0)
    IdleLoop()

    def _loc_167C(): pass

    label('loc_167C')

    NewScene('ED6_DT21/R1300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1685(): pass

    label('loc_1685')

    NewScene('ED6_DT21/R1100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_168E(): pass

    label('loc_168E')

    NewScene('ED6_DT21/R1200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1697(): pass

    label('loc_1697')

    NewScene('ED6_DT21/R1400._SN', 100, 0, 0)
    IdleLoop()

    def _loc_16A0(): pass

    label('loc_16A0')

    NewScene('ED6_DT21/R1403._SN', 100, 0, 0)
    IdleLoop()

    def _loc_16A9(): pass

    label('loc_16A9')

    NewScene('ED6_DT21/R1500._SN', 100, 0, 0)
    IdleLoop()

    def _loc_16B2(): pass

    label('loc_16B2')

    OP_5F(0x0003)

    Jump('loc_16B8')

    def _loc_16B8(): pass

    label('loc_16B8')

    Jump('loc_1771')

    def _loc_16BB(): pass

    label('loc_16BB')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        120,
        1,
        (
            TXT(0x00, '哈肯门\n'),
            TXT(0x01, '古罗尼关所\n'),
            TXT(0x02, '迷雾峡谷\n'),
            TXT(0x03, '西柏斯街道\n'),
            TXT(0x04, '拉文努废坑\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_171F'),
        (0x00000001, 'loc_172B'),
        (0x00000002, 'loc_1737'),
        (0x00000003, 'loc_1743'),
        (0x00000004, 'loc_174F'),
        (-1, 'loc_175B'),
    )

    def _loc_171F(): pass

    label('loc_171F')

    NewScene('ED6_DT21/T1401._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1761')

    def _loc_172B(): pass

    label('loc_172B')

    NewScene('ED6_DT21/T1311._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1761')

    def _loc_1737(): pass

    label('loc_1737')

    NewScene('ED6_DT21/C1402._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1761')

    def _loc_1743(): pass

    label('loc_1743')

    NewScene('ED6_DT21/R1203._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1761')

    def _loc_174F(): pass

    label('loc_174F')

    NewScene('ED6_DT21/C1104._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1761')

    def _loc_175B(): pass

    label('loc_175B')

    OP_5F(0x0003)

    Jump('loc_1761')

    def _loc_1761(): pass

    label('loc_1761')

    Jump('loc_1771')

    def _loc_1764(): pass

    label('loc_1764')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1771')

    def _loc_1771(): pass

    label('loc_1771')

    Jump('loc_11EA')

    def _loc_1774(): pass

    label('loc_1774')

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

# id: 0x0009 offset: 0x1784
@scena.Code('func_09_1784')
def func_09_1784():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    def _loc_178E(): pass

    label('loc_178E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E6C',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '城里\n'),
            TXT(0x01, '迷宫\n'),
            TXT(0x02, '大道\n'),
            TXT(0x03, '夜\n'),
            TXT(0x04, '其他\n'),
            TXT(0x05, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_17E0'),
        (0x00000001, 'loc_1A3B'),
        (0x00000002, 'loc_1C8F'),
        (0x00000003, 'loc_1D4E'),
        (0x00000004, 'loc_1DFB'),
        (-1, 'loc_1E5C'),
    )

    def _loc_17E0(): pass

    label('loc_17E0')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '卢安城\n'),
            TXT(0x01, '飞船坪\n'),
            TXT(0x02, '市长官邸\n'),
            TXT(0x03, '王立学院 旧校舍\n'),
            TXT(0x04, '王立学院 本馆\n'),
            TXT(0x05, '王立学院 本馆 上课时\n'),
            TXT(0x06, '王立学院 本馆 准备上课时\n'),
            TXT(0x07, '玛西亚孤儿院\n'),
            TXT(0x08, '玛西亚孤儿院（火灾后）\n'),
            TXT(0x09, '玛西亚孤儿院（重建后）\n'),
            TXT(0x0A, '民房\n'),
            TXT(0x0B, '店\n'),
            TXT(0x0C, '教会\n'),
            TXT(0x0D, '酒馆，娱乐场\n'),
            TXT(0x0E, '艾尔·雷登关所\n'),
            TXT(0x0F, '玛诺利亚村\n'),
            TXT(0x10, '玛西亚孤儿院内部（火灾中）\n'),
            TXT(0x11, '王立学院 （夜晚）旧校舍\n'),
            TXT(0x12, '王立学院 （夜晚）本馆\n'),
            TXT(0x13, '卢安城（夜晚）\n'),
            TXT(0x14, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_197E'),
        (0x00000001, 'loc_1987'),
        (0x00000002, 'loc_1990'),
        (0x00000003, 'loc_1999'),
        (0x00000004, 'loc_19A2'),
        (0x00000005, 'loc_19AB'),
        (0x00000006, 'loc_19B4'),
        (0x00000007, 'loc_19BD'),
        (0x00000008, 'loc_19C6'),
        (0x00000009, 'loc_19CF'),
        (0x0000000A, 'loc_19D8'),
        (0x0000000B, 'loc_19E1'),
        (0x0000000C, 'loc_19EA'),
        (0x0000000D, 'loc_19F3'),
        (0x0000000E, 'loc_19FC'),
        (0x0000000F, 'loc_1A05'),
        (0x00000010, 'loc_1A0E'),
        (0x00000011, 'loc_1A17'),
        (0x00000012, 'loc_1A20'),
        (0x00000013, 'loc_1A29'),
        (-1, 'loc_1A32'),
    )

    def _loc_197E(): pass

    label('loc_197E')

    NewScene('ED6_DT21/T2100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1987(): pass

    label('loc_1987')

    NewScene('ED6_DT21/T2102._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1990(): pass

    label('loc_1990')

    NewScene('ED6_DT21/T2200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1999(): pass

    label('loc_1999')

    NewScene('ED6_DT21/T2600._SN', 100, 0, 0)
    IdleLoop()

    def _loc_19A2(): pass

    label('loc_19A2')

    NewScene('ED6_DT21/T2510._SN', 100, 0, 0)
    IdleLoop()

    def _loc_19AB(): pass

    label('loc_19AB')

    NewScene('ED6_DT21/T2520._SN', 100, 0, 0)
    IdleLoop()

    def _loc_19B4(): pass

    label('loc_19B4')

    NewScene('ED6_DT21/T2530._SN', 100, 0, 0)
    IdleLoop()

    def _loc_19BD(): pass

    label('loc_19BD')

    NewScene('ED6_DT21/T2400._SN', 100, 0, 0)
    IdleLoop()

    def _loc_19C6(): pass

    label('loc_19C6')

    NewScene('ED6_DT21/T2401._SN', 100, 0, 0)
    IdleLoop()

    def _loc_19CF(): pass

    label('loc_19CF')

    NewScene('ED6_DT21/T2402._SN', 100, 0, 0)
    IdleLoop()

    def _loc_19D8(): pass

    label('loc_19D8')

    NewScene('ED6_DT21/T2110._SN', 100, 0, 0)
    IdleLoop()

    def _loc_19E1(): pass

    label('loc_19E1')

    NewScene('ED6_DT21/T2120._SN', 100, 0, 0)
    IdleLoop()

    def _loc_19EA(): pass

    label('loc_19EA')

    NewScene('ED6_DT21/T2130._SN', 100, 0, 0)
    IdleLoop()

    def _loc_19F3(): pass

    label('loc_19F3')

    NewScene('ED6_DT21/T2131._SN', 100, 0, 0)
    IdleLoop()

    def _loc_19FC(): pass

    label('loc_19FC')

    NewScene('ED6_DT21/T2700._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1A05(): pass

    label('loc_1A05')

    NewScene('ED6_DT21/T2300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1A0E(): pass

    label('loc_1A0E')

    NewScene('ED6_DT21/T2411._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1A17(): pass

    label('loc_1A17')

    NewScene('ED6_DT21/T2601._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1A20(): pass

    label('loc_1A20')

    NewScene('ED6_DT21/T2810._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1A29(): pass

    label('loc_1A29')

    NewScene('ED6_DT21/T2105._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1A32(): pass

    label('loc_1A32')

    OP_5F(0x0003)

    Jump('loc_1A38')

    def _loc_1A38(): pass

    label('loc_1A38')

    Jump('loc_1E69')

    def _loc_1A3B(): pass

    label('loc_1A3B')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '巴伦诺灯塔\n'),
            TXT(0x01, '巴伦诺灯塔（夜晚）\n'),
            TXT(0x02, '旧校舍地下遗迹\n'),
            TXT(0x03, '绀碧之塔1F（前半）\n'),
            TXT(0x04, '绀碧之塔2F（前半）\n'),
            TXT(0x05, '绀碧之塔3F（前半）\n'),
            TXT(0x06, '绀碧之塔4F（前半）\n'),
            TXT(0x07, '绀碧之塔5F（前半）\n'),
            TXT(0x08, '绀碧之塔1F（后半）\n'),
            TXT(0x09, '绀碧之塔2F（后半）\n'),
            TXT(0x0A, '绀碧之塔3F（后半）\n'),
            TXT(0x0B, '绀碧之塔4F（后半）\n'),
            TXT(0x0C, '绀碧之塔5F（后半）\n'),
            TXT(0x0D, '绀碧之塔屋顶（后半 异次元背景）\n'),
            TXT(0x0E, '绀碧之塔屋顶（后半 异次元背景，埃尔赛尤视点）\n'),
            TXT(0x0F, '绀碧之塔屋顶（后半 一般背景）\n'),
            TXT(0x10, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1BF6'),
        (0x00000001, 'loc_1BFF'),
        (0x00000002, 'loc_1C08'),
        (0x00000003, 'loc_1C11'),
        (0x00000004, 'loc_1C1A'),
        (0x00000005, 'loc_1C23'),
        (0x00000006, 'loc_1C2C'),
        (0x00000007, 'loc_1C35'),
        (0x00000008, 'loc_1C3E'),
        (0x00000009, 'loc_1C47'),
        (0x0000000A, 'loc_1C50'),
        (0x0000000B, 'loc_1C59'),
        (0x0000000C, 'loc_1C62'),
        (0x0000000D, 'loc_1C6B'),
        (0x0000000E, 'loc_1C74'),
        (0x0000000F, 'loc_1C7D'),
        (-1, 'loc_1C86'),
    )

    def _loc_1BF6(): pass

    label('loc_1BF6')

    NewScene('ED6_DT21/C2209._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1BFF(): pass

    label('loc_1BFF')

    NewScene('ED6_DT21/C2200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C08(): pass

    label('loc_1C08')

    NewScene('ED6_DT21/C2400._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C11(): pass

    label('loc_1C11')

    NewScene('ED6_DT21/C2111._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C1A(): pass

    label('loc_1C1A')

    NewScene('ED6_DT21/C2112._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C23(): pass

    label('loc_1C23')

    NewScene('ED6_DT21/C2113._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C2C(): pass

    label('loc_1C2C')

    NewScene('ED6_DT21/C2114._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C35(): pass

    label('loc_1C35')

    NewScene('ED6_DT21/C2115._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C3E(): pass

    label('loc_1C3E')

    NewScene('ED6_DT21/C2300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C47(): pass

    label('loc_1C47')

    NewScene('ED6_DT21/C2301._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C50(): pass

    label('loc_1C50')

    NewScene('ED6_DT21/C2302._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C59(): pass

    label('loc_1C59')

    NewScene('ED6_DT21/C2303._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C62(): pass

    label('loc_1C62')

    NewScene('ED6_DT21/C2304._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C6B(): pass

    label('loc_1C6B')

    NewScene('ED6_DT21/C2305._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C74(): pass

    label('loc_1C74')

    NewScene('ED6_DT21/C2306._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C7D(): pass

    label('loc_1C7D')

    NewScene('ED6_DT21/C2307._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1C86(): pass

    label('loc_1C86')

    OP_5F(0x0003)

    Jump('loc_1C8C')

    def _loc_1C8C(): pass

    label('loc_1C8C')

    Jump('loc_1E69')

    def _loc_1C8F(): pass

    label('loc_1C8F')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '古罗尼山道\n'),
            TXT(0x01, '玛诺利亚间道\n'),
            TXT(0x02, '阿伊纳街道\n'),
            TXT(0x03, '梅威海道\n'),
            TXT(0x04, '街景林道\n'),
            TXT(0x05, '梅威海道军用艇\n'),
            TXT(0x06, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1D0F'),
        (0x00000001, 'loc_1D18'),
        (0x00000002, 'loc_1D21'),
        (0x00000003, 'loc_1D2A'),
        (0x00000004, 'loc_1D33'),
        (0x00000005, 'loc_1D3C'),
        (-1, 'loc_1D45'),
    )

    def _loc_1D0F(): pass

    label('loc_1D0F')

    NewScene('ED6_DT21/C1501._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1D18(): pass

    label('loc_1D18')

    NewScene('ED6_DT21/R2100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1D21(): pass

    label('loc_1D21')

    NewScene('ED6_DT21/R2400._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1D2A(): pass

    label('loc_1D2A')

    NewScene('ED6_DT21/R2200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1D33(): pass

    label('loc_1D33')

    NewScene('ED6_DT21/R2300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1D3C(): pass

    label('loc_1D3C')

    NewScene('ED6_DT21/R2203._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1D45(): pass

    label('loc_1D45')

    OP_5F(0x0003)

    Jump('loc_1D4B')

    def _loc_1D4B(): pass

    label('loc_1D4B')

    Jump('loc_1E69')

    def _loc_1D4E(): pass

    label('loc_1D4E')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        120,
        1,
        (
            TXT(0x00, 'T2301 玛诺利亚\n'),
            TXT(0x01, 'R2111 玛诺利亚海岸\n'),
            TXT(0x02, 'T2403 孤儿院\n'),
            TXT(0x03, 'R2412 阿伊纳街道\n'),
            TXT(0x04, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1DC2'),
        (0x00000001, 'loc_1DCE'),
        (0x00000002, 'loc_1DDA'),
        (0x00000003, 'loc_1DE6'),
        (-1, 'loc_1DF2'),
    )

    def _loc_1DC2(): pass

    label('loc_1DC2')

    NewScene('ED6_DT21/T2301._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1DF8')

    def _loc_1DCE(): pass

    label('loc_1DCE')

    NewScene('ED6_DT21/R2111._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1DF8')

    def _loc_1DDA(): pass

    label('loc_1DDA')

    NewScene('ED6_DT21/T2403._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1DF8')

    def _loc_1DE6(): pass

    label('loc_1DE6')

    NewScene('ED6_DT21/R2412._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1DF8')

    def _loc_1DF2(): pass

    label('loc_1DF2')

    OP_5F(0x0003)

    Jump('loc_1DF8')

    def _loc_1DF8(): pass

    label('loc_1DF8')

    Jump('loc_1E69')

    def _loc_1DFB(): pass

    label('loc_1DFB')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        120,
        1,
        (
            TXT(0x00, 'T2103 海卷\n'),
            TXT(0x01, 'T2104 海\n'),
            TXT(0x02, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1E3B'),
        (0x00000001, 'loc_1E47'),
        (-1, 'loc_1E53'),
    )

    def _loc_1E3B(): pass

    label('loc_1E3B')

    NewScene('ED6_DT21/T2103._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1E59')

    def _loc_1E47(): pass

    label('loc_1E47')

    NewScene('ED6_DT21/T2104._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1E59')

    def _loc_1E53(): pass

    label('loc_1E53')

    OP_5F(0x0003)

    Jump('loc_1E59')

    def _loc_1E59(): pass

    label('loc_1E59')

    Jump('loc_1E69')

    def _loc_1E5C(): pass

    label('loc_1E5C')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E69')

    def _loc_1E69(): pass

    label('loc_1E69')

    Jump('loc_178E')

    def _loc_1E6C(): pass

    label('loc_1E6C')

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

# id: 0x000A offset: 0x1E7C
@scena.Code('func_0A_1E7C')
def func_0A_1E7C():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    def _loc_1E86(): pass

    label('loc_1E86')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2488',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '城里\n'),
            TXT(0x01, '迷宫\n'),
            TXT(0x02, '大道\n'),
            TXT(0x03, '夜\n'),
            TXT(0x04, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1ECF'),
        (0x00000001, 'loc_204E'),
        (0x00000002, 'loc_2356'),
        (0x00000003, 'loc_2411'),
        (-1, 'loc_2478'),
    )

    def _loc_1ECF(): pass

    label('loc_1ECF')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '蔡斯城\n'),
            TXT(0x01, '蔡斯民房1～3室内\n'),
            TXT(0x02, '中央工房 室内\n'),
            TXT(0x03, '沃尔费堡垒\n'),
            TXT(0x04, '蔡斯教会\n'),
            TXT(0x05, '武器点\n'),
            TXT(0x06, '拉赛尔工房\n'),
            TXT(0x07, '亚尔摩村外部\n'),
            TXT(0x08, '亚尔摩村外部（夜晚）\n'),
            TXT(0x09, '圣海姆门\n'),
            TXT(0x0A, '圣海姆门 地震后\n'),
            TXT(0x0B, '蔡斯城（夜晚）\n'),
            TXT(0x0C, '蔡斯城（停电事件）\n'),
            TXT(0x0D, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1FD0'),
        (0x00000001, 'loc_1FD9'),
        (0x00000002, 'loc_1FE2'),
        (0x00000003, 'loc_1FEB'),
        (0x00000004, 'loc_1FF4'),
        (0x00000005, 'loc_1FFD'),
        (0x00000006, 'loc_2006'),
        (0x00000007, 'loc_200F'),
        (0x00000008, 'loc_2018'),
        (0x00000009, 'loc_2021'),
        (0x0000000A, 'loc_202A'),
        (0x0000000B, 'loc_2033'),
        (0x0000000C, 'loc_203C'),
        (-1, 'loc_2045'),
    )

    def _loc_1FD0(): pass

    label('loc_1FD0')

    NewScene('ED6_DT21/T3100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1FD9(): pass

    label('loc_1FD9')

    NewScene('ED6_DT21/T3110._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1FE2(): pass

    label('loc_1FE2')

    NewScene('ED6_DT21/T3111._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1FEB(): pass

    label('loc_1FEB')

    NewScene('ED6_DT21/T3300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1FF4(): pass

    label('loc_1FF4')

    NewScene('ED6_DT21/T3130._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1FFD(): pass

    label('loc_1FFD')

    NewScene('ED6_DT21/T3120._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2006(): pass

    label('loc_2006')

    NewScene('ED6_DT21/T3133._SN', 100, 0, 0)
    IdleLoop()

    def _loc_200F(): pass

    label('loc_200F')

    NewScene('ED6_DT21/T3200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2018(): pass

    label('loc_2018')

    NewScene('ED6_DT21/T3201._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2021(): pass

    label('loc_2021')

    NewScene('ED6_DT21/T3400._SN', 100, 0, 0)
    IdleLoop()

    def _loc_202A(): pass

    label('loc_202A')

    NewScene('ED6_DT21/T3401._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2033(): pass

    label('loc_2033')

    NewScene('ED6_DT21/T3103._SN', 100, 0, 0)
    IdleLoop()

    def _loc_203C(): pass

    label('loc_203C')

    NewScene('ED6_DT21/T3106._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2045(): pass

    label('loc_2045')

    OP_5F(0x0003)

    Jump('loc_204B')

    def _loc_204B(): pass

    label('loc_204B')

    Jump('loc_2485')

    def _loc_204E(): pass

    label('loc_204E')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '雷斯顿水上要塞外\n'),
            TXT(0x01, '雷斯顿水上要塞中\n'),
            TXT(0x02, '雷斯顿水上要塞外（夜晚）\n'),
            TXT(0x03, '雷斯顿水上要塞（飞船坪无军用艇）\n'),
            TXT(0x04, '卡鲁迪亚钟乳洞\n'),
            TXT(0x05, '卡鲁迪亚大钟乳洞　Boss房间\n'),
            TXT(0x06, '温泉源流地图入口\n'),
            TXT(0x07, '温泉源流\n'),
            TXT(0x08, '红莲之塔1F（前半）\n'),
            TXT(0x09, '红莲之塔2F（前半）\n'),
            TXT(0x0A, '红莲之塔3F（前半）\n'),
            TXT(0x0B, '红莲之塔4F（前半）\n'),
            TXT(0x0C, '红莲之塔5F（前半）\n'),
            TXT(0x0D, '红莲之塔1F（后半）\n'),
            TXT(0x0E, '红莲之塔2F（后半）\n'),
            TXT(0x0F, '红莲之塔3F（后半）\n'),
            TXT(0x10, '红莲之塔4F（后半）\n'),
            TXT(0x11, '红莲之塔5F（后半）\n'),
            TXT(0x12, '红莲之塔屋顶（后半 异次元背景）\n'),
            TXT(0x13, '红莲之塔屋顶（后半 异次元背景，埃尔赛尤视点）\n'),
            TXT(0x14, '红莲之塔屋顶（后半 一般背景）\n'),
            TXT(0x15, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2290'),
        (0x00000001, 'loc_2299'),
        (0x00000002, 'loc_22A2'),
        (0x00000003, 'loc_22AB'),
        (0x00000004, 'loc_22B4'),
        (0x00000005, 'loc_22BD'),
        (0x00000006, 'loc_22C6'),
        (0x00000007, 'loc_22CF'),
        (0x00000008, 'loc_22D8'),
        (0x00000009, 'loc_22E1'),
        (0x0000000A, 'loc_22EA'),
        (0x0000000B, 'loc_22F3'),
        (0x0000000C, 'loc_22FC'),
        (0x0000000D, 'loc_2305'),
        (0x0000000E, 'loc_230E'),
        (0x0000000F, 'loc_2317'),
        (0x00000010, 'loc_2320'),
        (0x00000011, 'loc_2329'),
        (0x00000012, 'loc_2332'),
        (0x00000013, 'loc_233B'),
        (0x00000014, 'loc_2344'),
        (-1, 'loc_234D'),
    )

    def _loc_2290(): pass

    label('loc_2290')

    NewScene('ED6_DT21/C3100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2299(): pass

    label('loc_2299')

    NewScene('ED6_DT21/C3110._SN', 100, 0, 0)
    IdleLoop()

    def _loc_22A2(): pass

    label('loc_22A2')

    NewScene('ED6_DT21/C3104._SN', 100, 0, 0)
    IdleLoop()

    def _loc_22AB(): pass

    label('loc_22AB')

    NewScene('ED6_DT21/C3108._SN', 100, 0, 0)
    IdleLoop()

    def _loc_22B4(): pass

    label('loc_22B4')

    NewScene('ED6_DT21/C3300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_22BD(): pass

    label('loc_22BD')

    NewScene('ED6_DT21/C3303._SN', 100, 0, 0)
    IdleLoop()

    def _loc_22C6(): pass

    label('loc_22C6')

    NewScene('ED6_DT21/C3400._SN', 100, 0, 0)
    IdleLoop()

    def _loc_22CF(): pass

    label('loc_22CF')

    NewScene('ED6_DT21/C3401._SN', 100, 0, 0)
    IdleLoop()

    def _loc_22D8(): pass

    label('loc_22D8')

    NewScene('ED6_DT21/C3511._SN', 100, 0, 0)
    IdleLoop()

    def _loc_22E1(): pass

    label('loc_22E1')

    NewScene('ED6_DT21/C3512._SN', 100, 0, 0)
    IdleLoop()

    def _loc_22EA(): pass

    label('loc_22EA')

    NewScene('ED6_DT21/C3513._SN', 100, 0, 0)
    IdleLoop()

    def _loc_22F3(): pass

    label('loc_22F3')

    NewScene('ED6_DT21/C3514._SN', 100, 0, 0)
    IdleLoop()

    def _loc_22FC(): pass

    label('loc_22FC')

    NewScene('ED6_DT21/C3515._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2305(): pass

    label('loc_2305')

    NewScene('ED6_DT21/C3600._SN', 100, 0, 0)
    IdleLoop()

    def _loc_230E(): pass

    label('loc_230E')

    NewScene('ED6_DT21/C3601._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2317(): pass

    label('loc_2317')

    NewScene('ED6_DT21/C3602._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2320(): pass

    label('loc_2320')

    NewScene('ED6_DT21/C3603._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2329(): pass

    label('loc_2329')

    NewScene('ED6_DT21/C3604._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2332(): pass

    label('loc_2332')

    NewScene('ED6_DT21/C3605._SN', 100, 0, 0)
    IdleLoop()

    def _loc_233B(): pass

    label('loc_233B')

    NewScene('ED6_DT21/C3606._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2344(): pass

    label('loc_2344')

    NewScene('ED6_DT21/C3607._SN', 100, 0, 0)
    IdleLoop()

    def _loc_234D(): pass

    label('loc_234D')

    OP_5F(0x0003)

    Jump('loc_2353')

    def _loc_2353(): pass

    label('loc_2353')

    Jump('loc_2485')

    def _loc_2356(): pass

    label('loc_2356')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '佐达特军用道\n'),
            TXT(0x01, '卡鲁迪亚隧道（suidou）\n'),
            TXT(0x02, '托兰特平原道\n'),
            TXT(0x03, '利塔街道\n'),
            TXT(0x04, '托兰特平原道军用舰\n'),
            TXT(0x05, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_23DB'),
        (0x00000001, 'loc_23E4'),
        (0x00000002, 'loc_23ED'),
        (0x00000003, 'loc_23F6'),
        (0x00000004, 'loc_23FF'),
        (-1, 'loc_2408'),
    )

    def _loc_23DB(): pass

    label('loc_23DB')

    NewScene('ED6_DT21/R3300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_23E4(): pass

    label('loc_23E4')

    NewScene('ED6_DT21/R3400._SN', 100, 0, 0)
    IdleLoop()

    def _loc_23ED(): pass

    label('loc_23ED')

    NewScene('ED6_DT21/R3100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_23F6(): pass

    label('loc_23F6')

    NewScene('ED6_DT21/R3200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_23FF(): pass

    label('loc_23FF')

    NewScene('ED6_DT21/R3105._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2408(): pass

    label('loc_2408')

    OP_5F(0x0003)

    Jump('loc_240E')

    def _loc_240E(): pass

    label('loc_240E')

    Jump('loc_2485')

    def _loc_2411(): pass

    label('loc_2411')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        120,
        1,
        (
            TXT(0x00, 'T3103 蔡斯\n'),
            TXT(0x01, 'T3104 中央工房\n'),
            TXT(0x02, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2457'),
        (0x00000001, 'loc_2463'),
        (-1, 'loc_246F'),
    )

    def _loc_2457(): pass

    label('loc_2457')

    NewScene('ED6_DT21/T3103._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2475')

    def _loc_2463(): pass

    label('loc_2463')

    NewScene('ED6_DT21/T3104._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2475')

    def _loc_246F(): pass

    label('loc_246F')

    OP_5F(0x0003)

    Jump('loc_2475')

    def _loc_2475(): pass

    label('loc_2475')

    Jump('loc_2485')

    def _loc_2478(): pass

    label('loc_2478')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2485')

    def _loc_2485(): pass

    label('loc_2485')

    Jump('loc_1E86')

    def _loc_2488(): pass

    label('loc_2488')

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

# id: 0x000B offset: 0x2498
@scena.Code('func_0B_2498')
def func_0B_2498():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    def _loc_24A2(): pass

    label('loc_24A2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BC7',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '城里\n'),
            TXT(0x01, '迷宫\n'),
            TXT(0x02, '大道\n'),
            TXT(0x03, '夜\n'),
            TXT(0x04, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_24EB'),
        (0x00000001, 'loc_282F'),
        (0x00000002, 'loc_28F0'),
        (0x00000003, 'loc_296B'),
        (-1, 'loc_2BB7'),
    )

    def _loc_24EB(): pass

    label('loc_24EB')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '----- 格兰赛尔\n'),
            TXT(0x01, 'T4200 格兰赛尔城\n'),
            TXT(0x02, 'T4300 艾尔贝离宫（夜晚）\n'),
            TXT(0x03, 'T4133 酒店室内（夜晚）\n'),
            TXT(0x04, 'T4134 大圣堂室内（夜晚）\n'),
            TXT(0x05, 'T4135 历史资料馆室内\n'),
            TXT(0x06, 'T4136 竞技场室内\n'),
            TXT(0x07, 'T4400 码头\n'),
            TXT(0x08, 'T4138 帝国大使馆内部 内部\n'),
            TXT(0x09, 'T4139 共和国大使馆 内部\n'),
            TXT(0x0A, 'T4140 武器屋、工房（夜晚）\n'),
            TXT(0x0B, 'T4141 艾德尔百货店（夜晚）\n'),
            TXT(0x0C, 'T4142 酒廊（夜晚）\n'),
            TXT(0x0D, 'T4143 黑市商店 内部\n'),
            TXT(0x0E, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2670'),
        (0x00000001, 'loc_27B1'),
        (0x00000002, 'loc_27BA'),
        (0x00000003, 'loc_27C3'),
        (0x00000004, 'loc_27CC'),
        (0x00000005, 'loc_27D5'),
        (0x00000006, 'loc_27DE'),
        (0x00000007, 'loc_27E7'),
        (0x00000008, 'loc_27F0'),
        (0x00000009, 'loc_27F9'),
        (0x0000000A, 'loc_2802'),
        (0x0000000B, 'loc_280B'),
        (0x0000000C, 'loc_2814'),
        (0x0000000D, 'loc_281D'),
        (-1, 'loc_2826'),
    )

    def _loc_2670(): pass

    label('loc_2670')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        4,
        10,
        100,
        1,
        (
            TXT(0x00, 'T4100 格兰赛尔（南街区）\n'),
            TXT(0x01, 'T4101 格兰赛尔（东街区）\n'),
            TXT(0x02, 'T4102 格兰赛尔（西街区）\n'),
            TXT(0x03, 'T4103 格兰赛尔（北街区）\n'),
            TXT(0x04, 'T4104 格兰赛尔（竞技场内侧）\n'),
            TXT(0x05, 'T4105 格兰赛尔（空港）\n'),
            TXT(0x06, 'T4106 格兰赛尔（空港无埃尔赛尤）\n'),
            TXT(0x07, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2769'),
        (0x00000001, 'loc_2772'),
        (0x00000002, 'loc_277B'),
        (0x00000003, 'loc_2784'),
        (0x00000004, 'loc_278D'),
        (0x00000005, 'loc_2796'),
        (0x00000006, 'loc_279F'),
        (-1, 'loc_27A8'),
    )

    def _loc_2769(): pass

    label('loc_2769')

    NewScene('ED6_DT21/T4100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2772(): pass

    label('loc_2772')

    NewScene('ED6_DT21/T4101._SN', 100, 0, 0)
    IdleLoop()

    def _loc_277B(): pass

    label('loc_277B')

    NewScene('ED6_DT21/T4102._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2784(): pass

    label('loc_2784')

    NewScene('ED6_DT21/T4103._SN', 100, 0, 0)
    IdleLoop()

    def _loc_278D(): pass

    label('loc_278D')

    NewScene('ED6_DT21/T4104._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2796(): pass

    label('loc_2796')

    NewScene('ED6_DT21/T4105._SN', 100, 0, 0)
    IdleLoop()

    def _loc_279F(): pass

    label('loc_279F')

    NewScene('ED6_DT21/T4106._SN', 100, 0, 0)
    IdleLoop()

    def _loc_27A8(): pass

    label('loc_27A8')

    OP_5F(0x0004)
    OP_5F(0x0003)

    Jump('loc_282C')

    def _loc_27B1(): pass

    label('loc_27B1')

    NewScene('ED6_DT21/T4200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_27BA(): pass

    label('loc_27BA')

    NewScene('ED6_DT21/T4300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_27C3(): pass

    label('loc_27C3')

    NewScene('ED6_DT21/T4133._SN', 100, 0, 0)
    IdleLoop()

    def _loc_27CC(): pass

    label('loc_27CC')

    NewScene('ED6_DT21/T4134._SN', 100, 0, 0)
    IdleLoop()

    def _loc_27D5(): pass

    label('loc_27D5')

    NewScene('ED6_DT21/T4135._SN', 100, 0, 0)
    IdleLoop()

    def _loc_27DE(): pass

    label('loc_27DE')

    NewScene('ED6_DT21/T4136._SN', 100, 0, 0)
    IdleLoop()

    def _loc_27E7(): pass

    label('loc_27E7')

    NewScene('ED6_DT21/T4400._SN', 100, 0, 0)
    IdleLoop()

    def _loc_27F0(): pass

    label('loc_27F0')

    NewScene('ED6_DT21/T4138._SN', 100, 0, 0)
    IdleLoop()

    def _loc_27F9(): pass

    label('loc_27F9')

    NewScene('ED6_DT21/T4139._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2802(): pass

    label('loc_2802')

    NewScene('ED6_DT21/T4140._SN', 100, 0, 0)
    IdleLoop()

    def _loc_280B(): pass

    label('loc_280B')

    NewScene('ED6_DT21/T4141._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2814(): pass

    label('loc_2814')

    NewScene('ED6_DT21/T4142._SN', 100, 0, 0)
    IdleLoop()

    def _loc_281D(): pass

    label('loc_281D')

    NewScene('ED6_DT21/T4143._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2826(): pass

    label('loc_2826')

    OP_5F(0x0003)

    Jump('loc_282C')

    def _loc_282C(): pass

    label('loc_282C')

    Jump('loc_2BC4')

    def _loc_282F(): pass

    label('loc_282F')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '下水道Ａ\n'),
            TXT(0x01, '下水道Ｂ\n'),
            TXT(0x02, '下水道Ｃ\n'),
            TXT(0x03, '封印区域最上层\n'),
            TXT(0x04, '封印区域中层\n'),
            TXT(0x05, '封印区域最下层\n'),
            TXT(0x06, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_28B1'),
        (0x00000001, 'loc_28BA'),
        (0x00000002, 'loc_28C3'),
        (0x00000003, 'loc_28CC'),
        (0x00000004, 'loc_28D5'),
        (0x00000005, 'loc_28DE'),
        (-1, 'loc_28E7'),
    )

    def _loc_28B1(): pass

    label('loc_28B1')

    NewScene('ED6_DT21/C4200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_28BA(): pass

    label('loc_28BA')

    NewScene('ED6_DT21/C4202._SN', 100, 0, 0)
    IdleLoop()

    def _loc_28C3(): pass

    label('loc_28C3')

    NewScene('ED6_DT21/C4204._SN', 100, 0, 0)
    IdleLoop()

    def _loc_28CC(): pass

    label('loc_28CC')

    NewScene('ED6_DT21/C4300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_28D5(): pass

    label('loc_28D5')

    NewScene('ED6_DT21/C4301._SN', 100, 0, 0)
    IdleLoop()

    def _loc_28DE(): pass

    label('loc_28DE')

    NewScene('ED6_DT21/C4302._SN', 100, 0, 0)
    IdleLoop()

    def _loc_28E7(): pass

    label('loc_28E7')

    OP_5F(0x0003)

    Jump('loc_28ED')

    def _loc_28ED(): pass

    label('loc_28ED')

    Jump('loc_2BC4')

    def _loc_28F0(): pass

    label('loc_28F0')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '艾尔贝周游道\n'),
            TXT(0x01, '庭园大道\n'),
            TXT(0x02, '艾尔贝周游道·湖\n'),
            TXT(0x03, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2947'),
        (0x00000001, 'loc_2950'),
        (0x00000002, 'loc_2959'),
        (-1, 'loc_2962'),
    )

    def _loc_2947(): pass

    label('loc_2947')

    NewScene('ED6_DT21/C4100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2950(): pass

    label('loc_2950')

    NewScene('ED6_DT21/R4100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2959(): pass

    label('loc_2959')

    NewScene('ED6_DT21/C4103._SN', 101, 0, 0)
    IdleLoop()

    def _loc_2962(): pass

    label('loc_2962')

    OP_5F(0x0003)

    Jump('loc_2968')

    def _loc_2968(): pass

    label('loc_2968')

    Jump('loc_2BC4')

    def _loc_296B(): pass

    label('loc_296B')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        120,
        1,
        (
            TXT(0x00, 'C4111 艾尔贝周游道\n'),
            TXT(0x01, 'C4113 艾尔贝周游道\n'),
            TXT(0x02, 'T4302 艾尔贝离宫 入口庭园（白天）\n'),
            TXT(0x03, 'T4303 艾尔贝离宫 中庭，回廊\n'),
            TXT(0x04, 'T4312 艾尔贝离宫 大厅～\n'),
            TXT(0x05, 'T4313 艾尔贝离宫 客房～\n'),
            TXT(0x06, 'T4150 格兰赛尔 南街区\n'),
            TXT(0x07, 'T4151 格兰赛尔 東街区\n'),
            TXT(0x08, 'T4152 格兰赛尔 西街区\n'),
            TXT(0x09, 'T4153 格兰赛尔 北街区\n'),
            TXT(0x0A, 'T4156 格兰赛尔（空港无埃尔赛尤）\n'),
            TXT(0x0B, 'T4203 格兰赛尔城\n'),
            TXT(0x0C, 'T4250 格兰赛尔城 室内\n'),
            TXT(0x0D, 'T4403 码头\n'),
            TXT(0x0E, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2B06'),
        (0x00000001, 'loc_2B12'),
        (0x00000002, 'loc_2B1E'),
        (0x00000003, 'loc_2B2A'),
        (0x00000004, 'loc_2B36'),
        (0x00000005, 'loc_2B42'),
        (0x00000006, 'loc_2B4E'),
        (0x00000007, 'loc_2B5A'),
        (0x00000008, 'loc_2B66'),
        (0x00000009, 'loc_2B72'),
        (0x0000000A, 'loc_2B7E'),
        (0x0000000B, 'loc_2B8A'),
        (0x0000000C, 'loc_2B96'),
        (0x0000000D, 'loc_2BA2'),
        (-1, 'loc_2BAE'),
    )

    def _loc_2B06(): pass

    label('loc_2B06')

    NewScene('ED6_DT21/C4111._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2B12(): pass

    label('loc_2B12')

    NewScene('ED6_DT21/C4113._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2B1E(): pass

    label('loc_2B1E')

    NewScene('ED6_DT21/T4302._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2B2A(): pass

    label('loc_2B2A')

    NewScene('ED6_DT21/T4303._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2B36(): pass

    label('loc_2B36')

    NewScene('ED6_DT21/T4312._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2B42(): pass

    label('loc_2B42')

    NewScene('ED6_DT21/T4313._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2B4E(): pass

    label('loc_2B4E')

    NewScene('ED6_DT21/T4150._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2B5A(): pass

    label('loc_2B5A')

    NewScene('ED6_DT21/T4151._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2B66(): pass

    label('loc_2B66')

    NewScene('ED6_DT21/T4152._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2B72(): pass

    label('loc_2B72')

    NewScene('ED6_DT21/T4153._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2B7E(): pass

    label('loc_2B7E')

    NewScene('ED6_DT21/T4156._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2B8A(): pass

    label('loc_2B8A')

    NewScene('ED6_DT21/T4203._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2B96(): pass

    label('loc_2B96')

    NewScene('ED6_DT21/T4250._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2BA2(): pass

    label('loc_2BA2')

    NewScene('ED6_DT21/T4403._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_2BB4')

    def _loc_2BAE(): pass

    label('loc_2BAE')

    OP_5F(0x0003)

    Jump('loc_2BB4')

    def _loc_2BB4(): pass

    label('loc_2BB4')

    Jump('loc_2BC4')

    def _loc_2BB7(): pass

    label('loc_2BB7')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2BC4')

    def _loc_2BC4(): pass

    label('loc_2BC4')

    Jump('loc_24A2')

    def _loc_2BC7(): pass

    label('loc_2BC7')

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

# id: 0x000C offset: 0x2BD7
@scena.Code('func_0C_2BD7')
def func_0C_2BD7():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    def _loc_2BE1(): pass

    label('loc_2BE1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3979',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '卢·洛克尔\n'),
            TXT(0x01, '研究所\n'),
            TXT(0x02, '辉之环\n'),
            TXT(0x03, '哈梅尔村\n'),
            TXT(0x04, '古罗力亚斯内部\n'),
            TXT(0x05, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2C4D'),
        (0x00000001, 'loc_2D3D'),
        (0x00000002, 'loc_2EB4'),
        (0x00000003, 'loc_35E5'),
        (0x00000004, 'loc_363A'),
        (-1, 'loc_3969'),
    )

    def _loc_2C4D(): pass

    label('loc_2C4D')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'T5100 训练场外观\n'),
            TXT(0x01, 'C5503 训练场１ 巴斯塔尔水道\n'),
            TXT(0x02, 'C5504 训练场２ 圣科洛瓦森林\n'),
            TXT(0x03, 'C5508 训练场３ 格林姆瑟尔小要塞\n'),
            TXT(0x04, 'T5101 训练场外观（夜晚）\n'),
            TXT(0x05, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2D07'),
        (0x00000001, 'loc_2D10'),
        (0x00000002, 'loc_2D19'),
        (0x00000003, 'loc_2D22'),
        (0x00000004, 'loc_2D2B'),
        (-1, 'loc_2D34'),
    )

    def _loc_2D07(): pass

    label('loc_2D07')

    NewScene('ED6_DT21/T5100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2D10(): pass

    label('loc_2D10')

    NewScene('ED6_DT21/C5503._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2D19(): pass

    label('loc_2D19')

    NewScene('ED6_DT21/C5504._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2D22(): pass

    label('loc_2D22')

    NewScene('ED6_DT21/C5508._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2D2B(): pass

    label('loc_2D2B')

    NewScene('ED6_DT21/T5101._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2D34(): pass

    label('loc_2D34')

    OP_5F(0x0003)

    Jump('loc_2D3A')

    def _loc_2D3A(): pass

    label('loc_2D3A')

    Jump('loc_3976')

    def _loc_2D3D(): pass

    label('loc_2D3D')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？\n',
            '室内与夜晚地图连接。\n',
            '侵入事件只在夜晚进行。白天使用事件专用。',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C5600 研究所外观（入口）\n'),
            TXT(0x01, 'C5601 研究所外观（入口）夜晚\n'),
            TXT(0x02, 'C5610 研究所内部（１楼）\n'),
            TXT(0x03, 'C5611 研究所内部（２楼）\n'),
            TXT(0x04, 'C5612 研究所内部（３楼）\n'),
            TXT(0x05, 'C5613 研究所内部（４楼）\n'),
            TXT(0x06, 'C5614 研究所内部升降梯\n'),
            TXT(0x07, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2E6C'),
        (0x00000001, 'loc_2E75'),
        (0x00000002, 'loc_2E7E'),
        (0x00000003, 'loc_2E87'),
        (0x00000004, 'loc_2E90'),
        (0x00000005, 'loc_2E99'),
        (0x00000006, 'loc_2EA2'),
        (-1, 'loc_2EAB'),
    )

    def _loc_2E6C(): pass

    label('loc_2E6C')

    NewScene('ED6_DT21/C5600._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2E75(): pass

    label('loc_2E75')

    NewScene('ED6_DT21/C5601._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2E7E(): pass

    label('loc_2E7E')

    NewScene('ED6_DT21/C5610._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2E87(): pass

    label('loc_2E87')

    NewScene('ED6_DT21/C5611._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2E90(): pass

    label('loc_2E90')

    NewScene('ED6_DT21/C5612._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2E99(): pass

    label('loc_2E99')

    NewScene('ED6_DT21/C5613._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2EA2(): pass

    label('loc_2EA2')

    NewScene('ED6_DT21/C5614._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2EAB(): pass

    label('loc_2EAB')

    OP_5F(0x0003)

    Jump('loc_2EB1')

    def _loc_2EB1(): pass

    label('loc_2EB1')

    Jump('loc_3976')

    def _loc_2EB4(): pass

    label('loc_2EB4')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C5100中枢塔前通路\n'),
            TXT(0x01, 'C5101中枢塔入口\n'),
            TXT(0x02, 'C5700工业区域法克特里亚\n'),
            TXT(0x03, 'C5800居住区域克雷德尔\n'),
            TXT(0x04, 'C5900公园区域卡尔玛丽\n'),
            TXT(0x05, '-----辉之环内部（地下道、车站）\n'),
            TXT(0x06, '-----中央中枢塔内部\n'),
            TXT(0x07, '-----车站\n'),
            TXT(0x08, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2F9C'),
        (0x00000001, 'loc_2FA5'),
        (0x00000002, 'loc_2FAE'),
        (0x00000003, 'loc_2FB7'),
        (0x00000004, 'loc_2FC0'),
        (0x00000005, 'loc_2FC9'),
        (0x00000006, 'loc_31F3'),
        (0x00000007, 'loc_34FE'),
        (-1, 'loc_35DC'),
    )

    def _loc_2F9C(): pass

    label('loc_2F9C')

    NewScene('ED6_DT21/C5100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2FA5(): pass

    label('loc_2FA5')

    NewScene('ED6_DT21/C5101._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2FAE(): pass

    label('loc_2FAE')

    NewScene('ED6_DT21/C5700._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2FB7(): pass

    label('loc_2FB7')

    NewScene('ED6_DT21/C5800._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2FC0(): pass

    label('loc_2FC0')

    NewScene('ED6_DT21/C5900._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2FC9(): pass

    label('loc_2FC9')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        4,
        10,
        100,
        1,
        (
            TXT(0x00, '地下道5200（公园～居住区①）\n'),
            TXT(0x01, '地下道5201（公园～居住区②）\n'),
            TXT(0x02, '地下道5202（居住区域～工业区域①）\n'),
            TXT(0x03, '地下道5203（居住区域～工业区域②）\n'),
            TXT(0x04, '地下道5204（工业区域～中枢塔①）\n'),
            TXT(0x05, '地下道5205（工业区域～中枢塔②）\n'),
            TXT(0x06, '地下道5206（中枢塔～公园区域①）\n'),
            TXT(0x07, '地下道5207（中枢塔ー～公园区域②）\n'),
            TXT(0x08, 'C6000 西卡尔玛丽车站\n'),
            TXT(0x09, 'C6001 第３５克雷德尔车站\n'),
            TXT(0x0A, 'C6002 第７法克特里亚车站\n'),
            TXT(0x0B, 'C6003 中枢塔车站\n'),
            TXT(0x0C, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_317B'),
        (0x00000001, 'loc_3184'),
        (0x00000002, 'loc_318D'),
        (0x00000003, 'loc_3196'),
        (0x00000004, 'loc_319F'),
        (0x00000005, 'loc_31A8'),
        (0x00000006, 'loc_31B1'),
        (0x00000007, 'loc_31BA'),
        (0x00000008, 'loc_31C3'),
        (0x00000009, 'loc_31CC'),
        (0x0000000A, 'loc_31D5'),
        (0x0000000B, 'loc_31DE'),
        (-1, 'loc_31E7'),
    )

    def _loc_317B(): pass

    label('loc_317B')

    NewScene('ED6_DT21/C5200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3184(): pass

    label('loc_3184')

    NewScene('ED6_DT21/C5201._SN', 100, 0, 0)
    IdleLoop()

    def _loc_318D(): pass

    label('loc_318D')

    NewScene('ED6_DT21/C5202._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3196(): pass

    label('loc_3196')

    NewScene('ED6_DT21/C5203._SN', 100, 0, 0)
    IdleLoop()

    def _loc_319F(): pass

    label('loc_319F')

    NewScene('ED6_DT21/C5204._SN', 100, 0, 0)
    IdleLoop()

    def _loc_31A8(): pass

    label('loc_31A8')

    NewScene('ED6_DT21/C5205._SN', 100, 0, 0)
    IdleLoop()

    def _loc_31B1(): pass

    label('loc_31B1')

    NewScene('ED6_DT21/C5206._SN', 100, 0, 0)
    IdleLoop()

    def _loc_31BA(): pass

    label('loc_31BA')

    NewScene('ED6_DT21/C5207._SN', 100, 0, 0)
    IdleLoop()

    def _loc_31C3(): pass

    label('loc_31C3')

    NewScene('ED6_DT21/C6000._SN', 100, 0, 0)
    IdleLoop()

    def _loc_31CC(): pass

    label('loc_31CC')

    NewScene('ED6_DT21/C6001._SN', 100, 0, 0)
    IdleLoop()

    def _loc_31D5(): pass

    label('loc_31D5')

    NewScene('ED6_DT21/C6002._SN', 100, 0, 0)
    IdleLoop()

    def _loc_31DE(): pass

    label('loc_31DE')

    NewScene('ED6_DT21/C6003._SN', 100, 0, 0)
    IdleLoop()

    def _loc_31E7(): pass

    label('loc_31E7')

    OP_5F(0x0004)

    Jump('loc_31ED')

    def _loc_31ED(): pass

    label('loc_31ED')

    OP_5F(0x0003)

    Jump('loc_35E2')

    def _loc_31F3(): pass

    label('loc_31F3')

    Talk(
        (
            TxtCtl.ShowAll,
            '中枢塔内部的哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        4,
        10,
        100,
        1,
        (
            TXT(0x00, 'C5300 中央中枢塔内部0\n'),
            TXT(0x01, 'C5301 中央中枢塔内部1\n'),
            TXT(0x02, 'C5302 中央中枢塔内部2\n'),
            TXT(0x03, 'C5303 中央中枢塔内部3\n'),
            TXT(0x04, 'C5304 中央中枢塔内部4\n'),
            TXT(0x05, 'C5305 中央中枢塔内部5\n'),
            TXT(0x06, 'C5306 中央中枢塔内部6\n'),
            TXT(0x07, 'C5307 中央中枢塔内部7\n'),
            TXT(0x08, 'C5308 中Boss地图1（布卢布兰）\n'),
            TXT(0x09, 'C5309 中Boss地图2（瓦鲁特）\n'),
            TXT(0x0A, 'C5310 中Boss地图3（露茜奥拉）\n'),
            TXT(0x0B, 'C5311 中Boss地图4（玲）\n'),
            TXT(0x0C, 'C5312 通路出来到Shaft内部\n'),
            TXT(0x0D, 'C5313 屋顶\n'),
            TXT(0x0E, 'C5314 最下部、Boss房间前通路、Boss房间\n'),
            TXT(0x0F, 'C5315 高速升降梯\n'),
            TXT(0x10, 'C5316 小升降梯\n'),
            TXT(0x11, 'C5317 Boss房间\n'),
            TXT(0x12, 'C5318 Boss战斗地图事件专用\n'),
            TXT(0x13, 'C5319 Boss房间前通路\n'),
            TXT(0x14, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_343E'),
        (0x00000001, 'loc_3447'),
        (0x00000002, 'loc_3450'),
        (0x00000003, 'loc_3459'),
        (0x00000004, 'loc_3462'),
        (0x00000005, 'loc_346B'),
        (0x00000006, 'loc_3474'),
        (0x00000007, 'loc_347D'),
        (0x00000008, 'loc_3486'),
        (0x00000009, 'loc_348F'),
        (0x0000000A, 'loc_3498'),
        (0x0000000B, 'loc_34A1'),
        (0x0000000C, 'loc_34AA'),
        (0x0000000D, 'loc_34B3'),
        (0x0000000E, 'loc_34BC'),
        (0x0000000F, 'loc_34C5'),
        (0x00000010, 'loc_34CE'),
        (0x00000011, 'loc_34D7'),
        (0x00000012, 'loc_34E0'),
        (0x00000013, 'loc_34E9'),
        (-1, 'loc_34F2'),
    )

    def _loc_343E(): pass

    label('loc_343E')

    NewScene('ED6_DT21/C5300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3447(): pass

    label('loc_3447')

    NewScene('ED6_DT21/C5301._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3450(): pass

    label('loc_3450')

    NewScene('ED6_DT21/C5302._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3459(): pass

    label('loc_3459')

    NewScene('ED6_DT21/C5303._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3462(): pass

    label('loc_3462')

    NewScene('ED6_DT21/C5304._SN', 100, 0, 0)
    IdleLoop()

    def _loc_346B(): pass

    label('loc_346B')

    NewScene('ED6_DT21/C5305._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3474(): pass

    label('loc_3474')

    NewScene('ED6_DT21/C5306._SN', 100, 0, 0)
    IdleLoop()

    def _loc_347D(): pass

    label('loc_347D')

    NewScene('ED6_DT21/C5307._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3486(): pass

    label('loc_3486')

    NewScene('ED6_DT21/C5308._SN', 100, 0, 0)
    IdleLoop()

    def _loc_348F(): pass

    label('loc_348F')

    NewScene('ED6_DT21/C5309._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3498(): pass

    label('loc_3498')

    NewScene('ED6_DT21/C5310._SN', 100, 0, 0)
    IdleLoop()

    def _loc_34A1(): pass

    label('loc_34A1')

    NewScene('ED6_DT21/C5311._SN', 100, 0, 0)
    IdleLoop()

    def _loc_34AA(): pass

    label('loc_34AA')

    NewScene('ED6_DT21/C5312._SN', 100, 0, 0)
    IdleLoop()

    def _loc_34B3(): pass

    label('loc_34B3')

    NewScene('ED6_DT21/C5313._SN', 100, 0, 0)
    IdleLoop()

    def _loc_34BC(): pass

    label('loc_34BC')

    NewScene('ED6_DT21/C5314._SN', 100, 0, 0)
    IdleLoop()

    def _loc_34C5(): pass

    label('loc_34C5')

    NewScene('ED6_DT21/C5315._SN', 100, 0, 0)
    IdleLoop()

    def _loc_34CE(): pass

    label('loc_34CE')

    NewScene('ED6_DT21/C5316._SN', 100, 0, 0)
    IdleLoop()

    def _loc_34D7(): pass

    label('loc_34D7')

    NewScene('ED6_DT21/C5317._SN', 100, 0, 0)
    IdleLoop()

    def _loc_34E0(): pass

    label('loc_34E0')

    NewScene('ED6_DT21/C5318._SN', 100, 0, 0)
    IdleLoop()

    def _loc_34E9(): pass

    label('loc_34E9')

    NewScene('ED6_DT21/C5319._SN', 100, 0, 0)
    IdleLoop()

    def _loc_34F2(): pass

    label('loc_34F2')

    OP_5F(0x0004)

    Jump('loc_34F8')

    def _loc_34F8(): pass

    label('loc_34F8')

    OP_5F(0x0003)

    Jump('loc_35E2')

    def _loc_34FE(): pass

    label('loc_34FE')

    Talk(
        (
            TxtCtl.ShowAll,
            '车站的哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        4,
        10,
        100,
        1,
        (
            TXT(0x00, 'C6000西卡尔玛丽车站\n'),
            TXT(0x01, 'C6001第35克雷德尔车站\n'),
            TXT(0x02, 'C6002第7法克特里亚车站\n'),
            TXT(0x03, 'C6003中枢塔前车站\n'),
            TXT(0x04, 'C6010单轨铁路移动中\n'),
            TXT(0x05, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_35A3'),
        (0x00000001, 'loc_35AC'),
        (0x00000002, 'loc_35B5'),
        (0x00000003, 'loc_35BE'),
        (0x00000004, 'loc_35C7'),
        (-1, 'loc_35D0'),
    )

    def _loc_35A3(): pass

    label('loc_35A3')

    NewScene('ED6_DT21/C6000._SN', 100, 0, 0)
    IdleLoop()

    def _loc_35AC(): pass

    label('loc_35AC')

    NewScene('ED6_DT21/C6001._SN', 100, 0, 0)
    IdleLoop()

    def _loc_35B5(): pass

    label('loc_35B5')

    NewScene('ED6_DT21/C6002._SN', 100, 0, 0)
    IdleLoop()

    def _loc_35BE(): pass

    label('loc_35BE')

    NewScene('ED6_DT21/C6003._SN', 100, 0, 0)
    IdleLoop()

    def _loc_35C7(): pass

    label('loc_35C7')

    NewScene('ED6_DT21/C6010._SN', 100, 0, 0)
    IdleLoop()

    def _loc_35D0(): pass

    label('loc_35D0')

    OP_5F(0x0004)

    Jump('loc_35D6')

    def _loc_35D6(): pass

    label('loc_35D6')

    OP_5F(0x0003)

    Jump('loc_35E2')

    def _loc_35DC(): pass

    label('loc_35DC')

    OP_5F(0x0003)

    Jump('loc_35E2')

    def _loc_35E2(): pass

    label('loc_35E2')

    Jump('loc_3976')

    def _loc_35E5(): pass

    label('loc_35E5')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, '哈梅尔\n'),
            TXT(0x01, '哈梅尔\n'),
            TXT(0x02, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_361F'),
        (0x00000001, 'loc_3628'),
        (-1, 'loc_3631'),
    )

    def _loc_361F(): pass

    label('loc_361F')

    NewScene('ED6_DT21/T5200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3628(): pass

    label('loc_3628')

    NewScene('ED6_DT21/T5201._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3631(): pass

    label('loc_3631')

    OP_5F(0x0003)

    Jump('loc_3637')

    def _loc_3637(): pass

    label('loc_3637')

    Jump('loc_3976')

    def _loc_363A(): pass

    label('loc_363A')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'C5400古罗力亚斯内部（艾丝蒂尔监禁房间）\n'),
            TXT(0x01, 'C5401古罗力亚斯内部（怀斯曼的房间）\n'),
            TXT(0x02, 'C5402古罗力亚斯内部（甲板方面通路）\n'),
            TXT(0x03, 'C5403古罗力亚斯内部（甲板～升降口方向通路）\n'),
            TXT(0x04, 'C5404古罗力亚斯内部（升降口～机库方面通路）\n'),
            TXT(0x05, 'C5405古罗力亚斯内部（机库错误）\n'),
            TXT(0x06, 'C5406古罗力亚斯内部（机库正确）\n'),
            TXT(0x07, 'C5407古罗力亚斯内部（升降梯箱）\n'),
            TXT(0x08, 'C5408古罗力亚斯外部（甲板）\n'),
            TXT(0x09, 'C5409古罗力亚斯外部（升降口）\n'),
            TXT(0x0A, 'C5410古罗力亚斯内部（升降口～机库方向通路入口追加）\n'),
            TXT(0x0B, 'C5411古罗力亚斯内部（机库入口）\n'),
            TXT(0x0C, 'C5412古罗力亚斯内部（机库错误）\n'),
            TXT(0x0D, 'C5413古罗力亚斯外部 升降口 夜晚\n'),
            TXT(0x0E, 'C5414古罗力亚斯外部 附窗外装\n'),
            TXT(0x0F, 'C5415古罗力亚斯内部 后部升降口\n'),
            TXT(0x10, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_38D0'),
        (0x00000001, 'loc_38D9'),
        (0x00000002, 'loc_38E2'),
        (0x00000003, 'loc_38EB'),
        (0x00000004, 'loc_38F4'),
        (0x00000005, 'loc_38FD'),
        (0x00000006, 'loc_3906'),
        (0x00000007, 'loc_390F'),
        (0x00000008, 'loc_3918'),
        (0x00000009, 'loc_3921'),
        (0x0000000A, 'loc_392A'),
        (0x0000000B, 'loc_3933'),
        (0x0000000C, 'loc_393C'),
        (0x0000000D, 'loc_3945'),
        (0x0000000E, 'loc_394E'),
        (0x0000000F, 'loc_3957'),
        (-1, 'loc_3960'),
    )

    def _loc_38D0(): pass

    label('loc_38D0')

    NewScene('ED6_DT21/C5400._SN', 100, 0, 0)
    IdleLoop()

    def _loc_38D9(): pass

    label('loc_38D9')

    NewScene('ED6_DT21/C5401._SN', 100, 0, 0)
    IdleLoop()

    def _loc_38E2(): pass

    label('loc_38E2')

    NewScene('ED6_DT21/C5402._SN', 100, 0, 0)
    IdleLoop()

    def _loc_38EB(): pass

    label('loc_38EB')

    NewScene('ED6_DT21/C5403._SN', 100, 0, 0)
    IdleLoop()

    def _loc_38F4(): pass

    label('loc_38F4')

    NewScene('ED6_DT21/C5404._SN', 100, 0, 0)
    IdleLoop()

    def _loc_38FD(): pass

    label('loc_38FD')

    NewScene('ED6_DT21/C5405._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3906(): pass

    label('loc_3906')

    NewScene('ED6_DT21/C5406._SN', 102, 0, 0)
    IdleLoop()

    def _loc_390F(): pass

    label('loc_390F')

    NewScene('ED6_DT21/C5407._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3918(): pass

    label('loc_3918')

    NewScene('ED6_DT21/C5408._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3921(): pass

    label('loc_3921')

    NewScene('ED6_DT21/C5409._SN', 100, 0, 0)
    IdleLoop()

    def _loc_392A(): pass

    label('loc_392A')

    NewScene('ED6_DT21/C5410._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3933(): pass

    label('loc_3933')

    NewScene('ED6_DT21/C5411._SN', 100, 0, 0)
    IdleLoop()

    def _loc_393C(): pass

    label('loc_393C')

    NewScene('ED6_DT21/C5412._SN', 102, 0, 0)
    IdleLoop()

    def _loc_3945(): pass

    label('loc_3945')

    NewScene('ED6_DT21/C5413._SN', 100, 0, 0)
    IdleLoop()

    def _loc_394E(): pass

    label('loc_394E')

    NewScene('ED6_DT21/C5414._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3957(): pass

    label('loc_3957')

    NewScene('ED6_DT21/C5415._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3960(): pass

    label('loc_3960')

    OP_5F(0x0003)

    Jump('loc_3966')

    def _loc_3966(): pass

    label('loc_3966')

    Jump('loc_3976')

    def _loc_3969(): pass

    label('loc_3969')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3976')

    def _loc_3976(): pass

    label('loc_3976')

    Jump('loc_2BE1')

    def _loc_3979(): pass

    label('loc_3979')

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

# id: 0x000D offset: 0x3989
@scena.Code('func_0D_3989')
def func_0D_3989():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    def _loc_3993(): pass

    label('loc_3993')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E57',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '许多船\n'),
            TXT(0x01, '埃尔赛尤\n'),
            TXT(0x02, '空中，水上事件用\n'),
            TXT(0x03, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_39E7'),
        (0x00000001, 'loc_3BB5'),
        (0x00000002, 'loc_3D2A'),
        (-1, 'loc_3E47'),
    )

    def _loc_39E7(): pass

    label('loc_39E7')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'E0000 定期船　林德号\n'),
            TXT(0x01, 'E0001 定期船　赛希莉亚号（绿色）\n'),
            TXT(0x02, 'E0002 工房船\n'),
            TXT(0x03, 'E0100 空贼用飞船\n'),
            TXT(0x04, 'E0101 空贼用飞船（夜用）\n'),
            TXT(0x05, 'E0111 空贼用飞船内装置\n'),
            TXT(0x06, 'E0200 军用扬陆舰\n'),
            TXT(0x07, 'E0400 特务艇\n'),
            TXT(0x08, 'E0600 红色高速飞艇外观（特务艇改变颜色+小改造）\n'),
            TXT(0x09, 'E0610 红色高速飞艇内部\n'),
            TXT(0x0A, 'E0700 国际定期船格雷特纳号（定期船蓝色）\n'),
            TXT(0x0B, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3B49'),
        (0x00000001, 'loc_3B52'),
        (0x00000002, 'loc_3B5B'),
        (0x00000003, 'loc_3B64'),
        (0x00000004, 'loc_3B6D'),
        (0x00000005, 'loc_3B76'),
        (0x00000006, 'loc_3B7F'),
        (0x00000007, 'loc_3B88'),
        (0x00000008, 'loc_3B91'),
        (0x00000009, 'loc_3B9A'),
        (0x0000000A, 'loc_3BA3'),
        (-1, 'loc_3BAC'),
    )

    def _loc_3B49(): pass

    label('loc_3B49')

    NewScene('ED6_DT21/E0000._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3B52(): pass

    label('loc_3B52')

    NewScene('ED6_DT21/E0001._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3B5B(): pass

    label('loc_3B5B')

    NewScene('ED6_DT21/E0002._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3B64(): pass

    label('loc_3B64')

    NewScene('ED6_DT21/E0100._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3B6D(): pass

    label('loc_3B6D')

    NewScene('ED6_DT21/E0101._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3B76(): pass

    label('loc_3B76')

    NewScene('ED6_DT21/E0111._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3B7F(): pass

    label('loc_3B7F')

    NewScene('ED6_DT21/E0200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3B88(): pass

    label('loc_3B88')

    NewScene('ED6_DT21/E0400._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3B91(): pass

    label('loc_3B91')

    NewScene('ED6_DT21/E0600._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3B9A(): pass

    label('loc_3B9A')

    NewScene('ED6_DT21/E0610._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3BA3(): pass

    label('loc_3BA3')

    NewScene('ED6_DT21/E0700._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3BAC(): pass

    label('loc_3BAC')

    OP_5F(0x0003)

    Jump('loc_3BB2')

    def _loc_3BB2(): pass

    label('loc_3BB2')

    Jump('loc_3E54')

    def _loc_3BB5(): pass

    label('loc_3BB5')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'E0300 埃尔赛尤外观测试\n'),
            TXT(0x01, 'E0301 埃尔赛尤外观 云上、全景、（以OPS切换）\n'),
            TXT(0x02, 'E0310 埃尔赛尤内部 甲板连络通路·驾驶室连络通路·驾驶室\n'),
            TXT(0x03, 'E0311 埃尔赛尤内部 连络通路１·作战会议室·休息室\n'),
            TXT(0x04, 'E0312 埃尔赛尤内部 连络通路２·工房·货舱通路·货舱\n'),
            TXT(0x05, 'E0313 埃尔赛尤内部 船仓\n'),
            TXT(0x06, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3CEB'),
        (0x00000001, 'loc_3CF4'),
        (0x00000002, 'loc_3CFD'),
        (0x00000003, 'loc_3D06'),
        (0x00000004, 'loc_3D0F'),
        (0x00000005, 'loc_3D18'),
        (-1, 'loc_3D21'),
    )

    def _loc_3CEB(): pass

    label('loc_3CEB')

    NewScene('ED6_DT21/E0300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3CF4(): pass

    label('loc_3CF4')

    NewScene('ED6_DT21/E0301._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3CFD(): pass

    label('loc_3CFD')

    NewScene('ED6_DT21/E0310._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3D06(): pass

    label('loc_3D06')

    NewScene('ED6_DT21/E0311._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3D0F(): pass

    label('loc_3D0F')

    NewScene('ED6_DT21/E0312._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3D18(): pass

    label('loc_3D18')

    NewScene('ED6_DT21/E0313._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3D21(): pass

    label('loc_3D21')

    OP_5F(0x0003)

    Jump('loc_3D27')

    def _loc_3D27(): pass

    label('loc_3D27')

    Jump('loc_3E54')

    def _loc_3D2A(): pass

    label('loc_3D2A')

    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        3,
        10,
        100,
        1,
        (
            TXT(0x00, 'Sky Books Test\n'),
            TXT(0x01, 'E0800 空中∶龙＋军用飞船\n'),
            TXT(0x02, 'E0810 空中∶龙＋军用飞船\n'),
            TXT(0x03, 'E0811 空中∶夜晚\n'),
            TXT(0x04, 'E0900 水上∶龙＋埃尔赛尤\n'),
            TXT(0x05, 'E0901 水上∶夜间船\n'),
            TXT(0x06, 'E1000 心象风景事件专用\n'),
            TXT(0x07, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3DFF'),
        (0x00000001, 'loc_3E08'),
        (0x00000002, 'loc_3E11'),
        (0x00000003, 'loc_3E1A'),
        (0x00000004, 'loc_3E23'),
        (0x00000005, 'loc_3E2C'),
        (0x00000006, 'loc_3E35'),
        (-1, 'loc_3E3E'),
    )

    def _loc_3DFF(): pass

    label('loc_3DFF')

    NewScene('ED6_DT21/E0500._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3E08(): pass

    label('loc_3E08')

    NewScene('ED6_DT21/E0800._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3E11(): pass

    label('loc_3E11')

    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3E1A(): pass

    label('loc_3E1A')

    NewScene('ED6_DT21/E0811._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3E23(): pass

    label('loc_3E23')

    NewScene('ED6_DT21/E0900._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3E2C(): pass

    label('loc_3E2C')

    NewScene('ED6_DT21/E0901._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3E35(): pass

    label('loc_3E35')

    NewScene('ED6_DT21/E1000._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3E3E(): pass

    label('loc_3E3E')

    OP_5F(0x0003)

    Jump('loc_3E44')

    def _loc_3E44(): pass

    label('loc_3E44')

    Jump('loc_3E54')

    def _loc_3E47(): pass

    label('loc_3E47')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3E54')

    def _loc_3E54(): pass

    label('loc_3E54')

    Jump('loc_3993')

    def _loc_3E57(): pass

    label('loc_3E57')

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

# id: 0x000E offset: 0x3E67
@scena.Code('func_0E_3E67')
def func_0E_3E67():
    EventBegin(0x00)
    OP_DA()
    OP_56(0x00)
    OP_5F(0x0000)
    OP_5F(0x0001)

    Talk(
        (
            TxtCtl.ShowAll,
            '哪个？',
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3E86(): pass

    label('loc_3E86')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40E4',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '片头\n'),
            TXT(0x01, '古罗力亚斯登场\n'),
            TXT(0x02, '辉之环出现\n'),
            TXT(0x03, '导力停止现象 [PSP]\n'),
            TXT(0x04, '古罗力亚斯袭击\n'),
            TXT(0x05, '辉之环上空\n'),
            TXT(0x06, '埃尔赛尤击落\n'),
            TXT(0x07, '辉之环崩溃\n'),
            TXT(0x08, '片尾\n'),
            TXT(0x09, 'Weissmann Transforms [PSP]\n'),
            TXT(0x0A, 'Weissmann\x27s Regrets [PSP]\n'),
            TXT(0x0B, '取消\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0002)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Gtr,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3F73',
    )

    Jump('loc_40E4')

    def _loc_3F73(): pass

    label('loc_3F73')

    FadeOut(2000, 0, -1)
    OP_20(0x000003E8)
    OP_0D()
    OP_21()
    OP_C4(0x00, 0x00000010)
    FadeIn(10, 0)
    OP_0D()

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3FBD'),
        (0x00000001, 'loc_3FD3'),
        (0x00000002, 'loc_3FE9'),
        (0x00000004, 'loc_403C'),
        (0x00000005, 'loc_4052'),
        (0x00000006, 'loc_4068'),
        (0x00000007, 'loc_407E'),
        (0x00000008, 'loc_4094'),
        (-1, 'loc_40AA'),
    )

    def _loc_3FBD(): pass

    label('loc_3FBD')

    PlayMovie(0x00, 'ed6_2_op.avi', 0x0007, 0x0000)

    Jump('loc_40AD')

    def _loc_3FD3(): pass

    label('loc_3FD3')

    PlayMovie(0x00, 'ED6_DT40.dat', 0x001C, 0x0001)

    Jump('loc_40AD')

    def _loc_3FE9(): pass

    label('loc_3FE9')

    PlayMovie(0x00, 'ED6_DT41.dat', 0x0082, 0x0001)
    Sleep(1000)

    OP_56(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0x2D),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4026',
    )

    FadeOut(2000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '', 0x0000, 0x0000)
    FadeIn(1, 0)
    OP_0D()

    def _loc_4026(): pass

    label('loc_4026')

    PlayMovie(0x00, 'ED6_DT42.dat', 0x0000, 0x0001)

    Jump('loc_40AD')

    def _loc_403C(): pass

    label('loc_403C')

    PlayMovie(0x00, 'ED6_DT43.dat', 0x0077, 0x0001)

    Jump('loc_40AD')

    def _loc_4052(): pass

    label('loc_4052')

    PlayMovie(0x00, 'ED6_DT44.dat', 0x0083, 0x0001)

    Jump('loc_40AD')

    def _loc_4068(): pass

    label('loc_4068')

    PlayMovie(0x00, 'ED6_DT45.dat', 0x0084, 0x0001)

    Jump('loc_40AD')

    def _loc_407E(): pass

    label('loc_407E')

    PlayMovie(0x00, 'ED6_DT46.dat', 0x0085, 0x0001)

    Jump('loc_40AD')

    def _loc_4094(): pass

    label('loc_4094')

    PlayMovie(0x00, 'ED6_DT47.dat', 0x0008, 0x0000)

    Jump('loc_40AD')

    def _loc_40AA(): pass

    label('loc_40AA')

    Jump('loc_40AD')

    def _loc_40AD(): pass

    label('loc_40AD')

    Sleep(1000)

    OP_56(0x02)
    FadeOut(2000, 0, -1)
    OP_20(0x000007D0)
    OP_21()
    OP_0D()
    PlayMovie(0x01, '', 0x0000, 0x0000)
    Sleep(500)

    OP_C4(0x01, 0x00000010)
    FadeIn(10, 0)
    OP_0D()

    Jump('loc_3E86')

    def _loc_40E4(): pass

    label('loc_40E4')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
