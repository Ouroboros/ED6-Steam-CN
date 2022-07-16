import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0001_3_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0001_3 ._SN')

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
    header.importTable    = ['ED6_DT01/T0001._SN', 'ED6_DT01/T0001_1._SN', 'ED6_DT01/T0001_2._SN', 'ED6_DT01/T0001_3._SN', 'ED6_DT01/T0001_4._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1D54
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
        'loc_275',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '30泛用ＮＰＬ\n'),
            TXT(0x01, '31我方队员和专用ＮＰＬ\n'),
            TXT(0x02, '32泛用ＮＰＬ和专用ＮＰＬ２＿ＡＰＬ\n'),
            TXT(0x03, '33PT战斗艾丝蒂尔、约修亚、金、阿加特、奥利维尔\n'),
            TXT(0x04, '34PT战斗约修亚、雪拉、提妲、科洛丝\n'),
            TXT(0x05, '35NPC战斗男女游击士、流氓、空贼\n'),
            TXT(0x06, '36NPC战斗流氓、男女游击士２\n'),
            TXT(0x07, '37NPC战斗王国士兵、军官、特务兵、洛伦斯、理查德、凯诺娜\n'),
            TXT(0x08, '39坐着的角色\n'),
            TXT(0x09, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_217'),
        (0x00000001, 'loc_220'),
        (0x00000002, 'loc_229'),
        (0x00000003, 'loc_232'),
        (0x00000004, 'loc_23B'),
        (0x00000005, 'loc_244'),
        (0x00000006, 'loc_24D'),
        (0x00000007, 'loc_256'),
        (0x00000008, 'loc_25F'),
        (-1, 'loc_268'),
    )

    def _loc_217(): pass

    label('loc_217')

    NewScene('ED6_DT01/T0030._SN', 0, 0, 0)
    IdleLoop()

    def _loc_220(): pass

    label('loc_220')

    NewScene('ED6_DT01/T0031._SN', 0, 0, 0)
    IdleLoop()

    def _loc_229(): pass

    label('loc_229')

    NewScene('ED6_DT01/T0032._SN', 0, 0, 0)
    IdleLoop()

    def _loc_232(): pass

    label('loc_232')

    NewScene('ED6_DT01/T0033._SN', 0, 0, 0)
    IdleLoop()

    def _loc_23B(): pass

    label('loc_23B')

    NewScene('ED6_DT01/T0034._SN', 0, 0, 0)
    IdleLoop()

    def _loc_244(): pass

    label('loc_244')

    NewScene('ED6_DT01/T0035._SN', 0, 0, 0)
    IdleLoop()

    def _loc_24D(): pass

    label('loc_24D')

    NewScene('ED6_DT01/T0036._SN', 0, 0, 0)
    IdleLoop()

    def _loc_256(): pass

    label('loc_256')

    NewScene('ED6_DT01/T0037._SN', 0, 0, 0)
    IdleLoop()

    def _loc_25F(): pass

    label('loc_25F')

    NewScene('ED6_DT01/T0039._SN', 0, 0, 0)
    IdleLoop()

    def _loc_268(): pass

    label('loc_268')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B2')

    def _loc_275(): pass

    label('loc_275')

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

# id: 0x0001 offset: 0x285
@scena.Code('Init')
def Init():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪个？',
            TxtCtl.Enter,
        ),
    )

    def _loc_28F(): pass

    label('loc_28F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_609',
    )

    Menu(
        1,
        10,
        32,
        1,
        (
            TXT(0x00, '40魔兽列表(10000-10290)\n'),
            TXT(0x01, '41魔兽列表(10300-10590)\n'),
            TXT(0x02, '42魔兽列表(10600-10890)\n'),
            TXT(0x03, '57魔兽列表(10900-11040)\n'),
            TXT(0x04, '60魔兽列表(11050-11190)\n'),
            TXT(0x05, '43魔兽动作(10000-10050)\n'),
            TXT(0x06, '44魔兽动作(10060-10140)\n'),
            TXT(0x07, '45魔兽动作(10150-10210)\n'),
            TXT(0x08, '46魔兽动作(10220-10290)\n'),
            TXT(0x09, '47魔兽动作(10300-10380)\n'),
            TXT(0x0A, '48魔兽动作(10390-10450)\n'),
            TXT(0x0B, '49魔兽动作(10460-10530)\n'),
            TXT(0x0C, '50魔兽动作(10540-10610)\n'),
            TXT(0x0D, '51魔兽动作(10620-10690)\n'),
            TXT(0x0E, '52魔兽动作(10700-10770)\n'),
            TXT(0x0F, '53魔兽动作(10780-10850)\n'),
            TXT(0x10, '54魔兽动作(10860-10900)\n'),
            TXT(0x11, '55魔兽动作(10910-10940)\n'),
            TXT(0x12, '56魔兽动作(10950-10990)\n'),
            TXT(0x13, '58魔兽动作(11000-11060)\n'),
            TXT(0x14, '59魔兽动作(11070-11110)\n'),
            TXT(0x15, '61魔兽动作(11120-11150)\n'),
            TXT(0x16, '62魔兽动作(11160-11190)\n'),
            TXT(0x17, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_536'),
        (0x00000001, 'loc_53F'),
        (0x00000002, 'loc_548'),
        (0x00000003, 'loc_551'),
        (0x00000004, 'loc_55A'),
        (0x00000005, 'loc_563'),
        (0x00000006, 'loc_56C'),
        (0x00000007, 'loc_575'),
        (0x00000008, 'loc_57E'),
        (0x00000009, 'loc_587'),
        (0x0000000A, 'loc_590'),
        (0x0000000B, 'loc_599'),
        (0x0000000C, 'loc_5A2'),
        (0x0000000D, 'loc_5AB'),
        (0x0000000E, 'loc_5B4'),
        (0x0000000F, 'loc_5BD'),
        (0x00000010, 'loc_5C6'),
        (0x00000011, 'loc_5CF'),
        (0x00000012, 'loc_5D8'),
        (0x00000013, 'loc_5E1'),
        (0x00000014, 'loc_5EA'),
        (0x00000015, 'loc_5F3'),
        (-1, 'loc_5FC'),
    )

    def _loc_536(): pass

    label('loc_536')

    NewScene('ED6_DT01/T0040._SN', 0, 0, 0)
    IdleLoop()

    def _loc_53F(): pass

    label('loc_53F')

    NewScene('ED6_DT01/T0041._SN', 0, 0, 0)
    IdleLoop()

    def _loc_548(): pass

    label('loc_548')

    NewScene('ED6_DT01/T0042._SN', 0, 0, 0)
    IdleLoop()

    def _loc_551(): pass

    label('loc_551')

    NewScene('ED6_DT01/T0057._SN', 0, 0, 0)
    IdleLoop()

    def _loc_55A(): pass

    label('loc_55A')

    NewScene('ED6_DT01/T0060._SN', 0, 0, 0)
    IdleLoop()

    def _loc_563(): pass

    label('loc_563')

    NewScene('ED6_DT01/T0043._SN', 0, 0, 0)
    IdleLoop()

    def _loc_56C(): pass

    label('loc_56C')

    NewScene('ED6_DT01/T0044._SN', 0, 0, 0)
    IdleLoop()

    def _loc_575(): pass

    label('loc_575')

    NewScene('ED6_DT01/T0045._SN', 0, 0, 0)
    IdleLoop()

    def _loc_57E(): pass

    label('loc_57E')

    NewScene('ED6_DT01/T0046._SN', 0, 0, 0)
    IdleLoop()

    def _loc_587(): pass

    label('loc_587')

    NewScene('ED6_DT01/T0047._SN', 0, 0, 0)
    IdleLoop()

    def _loc_590(): pass

    label('loc_590')

    NewScene('ED6_DT01/T0048._SN', 0, 0, 0)
    IdleLoop()

    def _loc_599(): pass

    label('loc_599')

    NewScene('ED6_DT01/T0049._SN', 0, 0, 0)
    IdleLoop()

    def _loc_5A2(): pass

    label('loc_5A2')

    NewScene('ED6_DT01/T0050._SN', 0, 0, 0)
    IdleLoop()

    def _loc_5AB(): pass

    label('loc_5AB')

    NewScene('ED6_DT01/T0051._SN', 0, 0, 0)
    IdleLoop()

    def _loc_5B4(): pass

    label('loc_5B4')

    NewScene('ED6_DT01/T0052._SN', 0, 0, 0)
    IdleLoop()

    def _loc_5BD(): pass

    label('loc_5BD')

    NewScene('ED6_DT01/T0053._SN', 0, 0, 0)
    IdleLoop()

    def _loc_5C6(): pass

    label('loc_5C6')

    NewScene('ED6_DT01/T0054._SN', 0, 0, 0)
    IdleLoop()

    def _loc_5CF(): pass

    label('loc_5CF')

    NewScene('ED6_DT01/T0055._SN', 0, 0, 0)
    IdleLoop()

    def _loc_5D8(): pass

    label('loc_5D8')

    NewScene('ED6_DT01/T0056._SN', 0, 0, 0)
    IdleLoop()

    def _loc_5E1(): pass

    label('loc_5E1')

    NewScene('ED6_DT01/T0058._SN', 0, 0, 0)
    IdleLoop()

    def _loc_5EA(): pass

    label('loc_5EA')

    NewScene('ED6_DT01/T0059._SN', 0, 0, 0)
    IdleLoop()

    def _loc_5F3(): pass

    label('loc_5F3')

    NewScene('ED6_DT01/T0061._SN', 0, 0, 0)
    IdleLoop()

    def _loc_5FC(): pass

    label('loc_5FC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_28F')

    def _loc_609(): pass

    label('loc_609')

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

# id: 0x0002 offset: 0x619
@scena.Code('ReInit')
def ReInit():
    Talk(
        (
            TxtCtl.ShowAll,
            '这些是地图。选一个吧。',
            TxtCtl.Enter,
        ),
    )

    def _loc_633(): pass

    label('loc_633')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6E1',
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
        (0x00000000, 'loc_6AA'),
        (0x00000001, 'loc_6B1'),
        (0x00000002, 'loc_6B8'),
        (0x00000003, 'loc_6BF'),
        (0x00000004, 'loc_6C6'),
        (0x00000005, 'loc_6CD'),
        (-1, 'loc_6D4'),
    )

    def _loc_6AA(): pass

    label('loc_6AA')

    Call(3, 0x0003)

    Jump('loc_6DE')

    def _loc_6B1(): pass

    label('loc_6B1')

    Call(3, 0x0004)

    Jump('loc_6DE')

    def _loc_6B8(): pass

    label('loc_6B8')

    Call(3, 0x0005)

    Jump('loc_6DE')

    def _loc_6BF(): pass

    label('loc_6BF')

    Call(3, 0x0006)

    Jump('loc_6DE')

    def _loc_6C6(): pass

    label('loc_6C6')

    Call(3, 0x0007)

    Jump('loc_6DE')

    def _loc_6CD(): pass

    label('loc_6CD')

    Call(3, 0x0008)

    Jump('loc_6DE')

    def _loc_6D4(): pass

    label('loc_6D4')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6DE(): pass

    label('loc_6DE')

    Jump('loc_633')

    def _loc_6E1(): pass

    label('loc_6E1')

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

# id: 0x0003 offset: 0x6F1
@scena.Code('func_03_6F1')
def func_03_6F1():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    def _loc_6FB(): pass

    label('loc_6FB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A42',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '城里\n'),
            TXT(0x01, '迷宫\n'),
            TXT(0x02, '街道\n'),
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
        (0x00000000, 'loc_744'),
        (0x00000001, 'loc_841'),
        (0x00000002, 'loc_970'),
        (0x00000003, 'loc_9EE'),
        (-1, 'loc_A35'),
    )

    def _loc_744(): pass

    label('loc_744')

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
            TXT(0x01, '市长官邸\n'),
            TXT(0x02, '布莱特家\n'),
            TXT(0x03, '帕赛尔农场\n'),
            TXT(0x04, '帕赛尔农场（夜晚）\n'),
            TXT(0x05, '威尔特关所\n'),
            TXT(0x06, '飞行场\n'),
            TXT(0x07, '布莱特家\n'),
            TXT(0x08, '格鲁纳门\n'),
            TXT(0x09, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_7E7'),
        (0x00000001, 'loc_7F0'),
        (0x00000002, 'loc_7F9'),
        (0x00000003, 'loc_802'),
        (0x00000004, 'loc_80B'),
        (0x00000005, 'loc_814'),
        (0x00000006, 'loc_81D'),
        (0x00000007, 'loc_826'),
        (0x00000008, 'loc_82F'),
        (-1, 'loc_838'),
    )

    def _loc_7E7(): pass

    label('loc_7E7')

    NewScene('ED6_DT01/T0100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_7F0(): pass

    label('loc_7F0')

    NewScene('ED6_DT01/T0200._SN', 0, 0, 0)
    IdleLoop()

    def _loc_7F9(): pass

    label('loc_7F9')

    NewScene('ED6_DT01/T0300._SN', 0, 0, 0)
    IdleLoop()

    def _loc_802(): pass

    label('loc_802')

    NewScene('ED6_DT01/T0400._SN', 0, 0, 0)
    IdleLoop()

    def _loc_80B(): pass

    label('loc_80B')

    NewScene('ED6_DT01/T0401._SN', 0, 0, 0)
    IdleLoop()

    def _loc_814(): pass

    label('loc_814')

    NewScene('ED6_DT01/T0500._SN', 0, 0, 0)
    IdleLoop()

    def _loc_81D(): pass

    label('loc_81D')

    NewScene('ED6_DT01/T0700._SN', 0, 0, 0)
    IdleLoop()

    def _loc_826(): pass

    label('loc_826')

    NewScene('ED6_DT01/T0300._SN', 0, 0, 0)
    IdleLoop()

    def _loc_82F(): pass

    label('loc_82F')

    NewScene('ED6_DT01/T0600._SN', 0, 0, 0)
    IdleLoop()

    def _loc_838(): pass

    label('loc_838')

    OP_5F(0x0003)

    Jump('loc_83E')

    def _loc_83E(): pass

    label('loc_83E')

    Jump('loc_A3F')

    def _loc_841(): pass

    label('loc_841')

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
            TXT(0x00, '玛鲁加矿山\n'),
            TXT(0x01, '神秘森林\n'),
            TXT(0x02, '翡翠之塔（后半）\n'),
            TXT(0x03, '地下水路\n'),
            TXT(0x04, '翡翠之塔1F（前半）\n'),
            TXT(0x05, '翡翠之塔2F（前半）\n'),
            TXT(0x06, '翡翠之塔3F（前半）\n'),
            TXT(0x07, '翡翠之塔4F（前半）\n'),
            TXT(0x08, '翡翠之塔5F（前半）\n'),
            TXT(0x09, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_916'),
        (0x00000001, 'loc_91F'),
        (0x00000002, 'loc_928'),
        (0x00000003, 'loc_931'),
        (0x00000004, 'loc_93A'),
        (0x00000005, 'loc_943'),
        (0x00000006, 'loc_94C'),
        (0x00000007, 'loc_955'),
        (0x00000008, 'loc_95E'),
        (-1, 'loc_967'),
    )

    def _loc_916(): pass

    label('loc_916')

    NewScene('ED6_DT01/C0100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_91F(): pass

    label('loc_91F')

    NewScene('ED6_DT01/C0300._SN', 0, 0, 0)
    IdleLoop()

    def _loc_928(): pass

    label('loc_928')

    NewScene('ED6_DT01/C0400._SN', 0, 0, 0)
    IdleLoop()

    def _loc_931(): pass

    label('loc_931')

    NewScene('ED6_DT01/C0500._SN', 0, 0, 0)
    IdleLoop()

    def _loc_93A(): pass

    label('loc_93A')

    NewScene('ED6_DT01/C0411._SN', 0, 0, 0)
    IdleLoop()

    def _loc_943(): pass

    label('loc_943')

    NewScene('ED6_DT01/C0412._SN', 0, 0, 0)
    IdleLoop()

    def _loc_94C(): pass

    label('loc_94C')

    NewScene('ED6_DT01/C0413._SN', 0, 0, 0)
    IdleLoop()

    def _loc_955(): pass

    label('loc_955')

    NewScene('ED6_DT01/C0414._SN', 0, 0, 0)
    IdleLoop()

    def _loc_95E(): pass

    label('loc_95E')

    NewScene('ED6_DT01/C0415._SN', 0, 0, 0)
    IdleLoop()

    def _loc_967(): pass

    label('loc_967')

    OP_5F(0x0003)

    Jump('loc_96D')

    def _loc_96D(): pass

    label('loc_96D')

    Jump('loc_A3F')

    def _loc_970(): pass

    label('loc_970')

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
            TXT(0x03, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_9C1'),
        (0x00000001, 'loc_9CD'),
        (0x00000002, 'loc_9D9'),
        (-1, 'loc_9E5'),
    )

    def _loc_9C1(): pass

    label('loc_9C1')

    NewScene('ED6_DT01/R0100._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_9EB')

    def _loc_9CD(): pass

    label('loc_9CD')

    NewScene('ED6_DT01/R0200._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_9EB')

    def _loc_9D9(): pass

    label('loc_9D9')

    NewScene('ED6_DT01/R0300._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_9EB')

    def _loc_9E5(): pass

    label('loc_9E5')

    OP_5F(0x0003)

    Jump('loc_9EB')

    def _loc_9EB(): pass

    label('loc_9EB')

    Jump('loc_A3F')

    def _loc_9EE(): pass

    label('loc_9EE')

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
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_A20'),
        (-1, 'loc_A2C'),
    )

    def _loc_A20(): pass

    label('loc_A20')

    NewScene('ED6_DT01/T0311._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_A32')

    def _loc_A2C(): pass

    label('loc_A2C')

    OP_5F(0x0003)

    Jump('loc_A32')

    def _loc_A32(): pass

    label('loc_A32')

    Jump('loc_A3F')

    def _loc_A35(): pass

    label('loc_A35')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_A3F(): pass

    label('loc_A3F')

    Jump('loc_6FB')

    def _loc_A42(): pass

    label('loc_A42')

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

# id: 0x0004 offset: 0xA52
@scena.Code('func_04_A52')
def func_04_A52():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    def _loc_A5C(): pass

    label('loc_A5C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E0C',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '城里\n'),
            TXT(0x01, '迷宫\n'),
            TXT(0x02, '街道\n'),
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
        (0x00000000, 'loc_AA5'),
        (0x00000001, 'loc_B98'),
        (0x00000002, 'loc_CC7'),
        (0x00000003, 'loc_DA0'),
        (-1, 'loc_DFC'),
    )

    def _loc_AA5(): pass

    label('loc_AA5')

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
            TXT(0x00, '柏斯市南口\n'),
            TXT(0x01, '柏斯市民家\n'),
            TXT(0x02, '古罗尼关所\n'),
            TXT(0x03, '古罗尼关所（夜晚）\n'),
            TXT(0x04, '柏斯国际空港\n'),
            TXT(0x05, '拉文努村\n'),
            TXT(0x06, '哈肯要塞\n'),
            TXT(0x07, '湖畔的旅店\n'),
            TXT(0x08, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_B47'),
        (0x00000001, 'loc_B50'),
        (0x00000002, 'loc_B59'),
        (0x00000003, 'loc_B62'),
        (0x00000004, 'loc_B6B'),
        (0x00000005, 'loc_B74'),
        (0x00000006, 'loc_B7D'),
        (0x00000007, 'loc_B86'),
        (-1, 'loc_B8F'),
    )

    def _loc_B47(): pass

    label('loc_B47')

    NewScene('ED6_DT01/T1100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B50(): pass

    label('loc_B50')

    NewScene('ED6_DT01/T1110._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B59(): pass

    label('loc_B59')

    NewScene('ED6_DT01/T1300._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B62(): pass

    label('loc_B62')

    NewScene('ED6_DT01/T1301._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B6B(): pass

    label('loc_B6B')

    NewScene('ED6_DT01/T1102._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B74(): pass

    label('loc_B74')

    NewScene('ED6_DT01/T1200._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B7D(): pass

    label('loc_B7D')

    NewScene('ED6_DT01/T1400._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B86(): pass

    label('loc_B86')

    NewScene('ED6_DT01/T1500._SN', 0, 0, 0)
    IdleLoop()

    def _loc_B8F(): pass

    label('loc_B8F')

    OP_5F(0x0003)

    Jump('loc_B95')

    def _loc_B95(): pass

    label('loc_B95')

    Jump('loc_E09')

    def _loc_B98(): pass

    label('loc_B98')

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
            TXT(0x00, '琥珀之塔（后半）\n'),
            TXT(0x01, '迷雾峡谷\n'),
            TXT(0x02, '拉文努废坑\n'),
            TXT(0x03, '空贼要塞\n'),
            TXT(0x04, '琥珀之塔1F（前半）\n'),
            TXT(0x05, '琥珀之塔2F（前半）\n'),
            TXT(0x06, '琥珀之塔3F（前半）\n'),
            TXT(0x07, '琥珀之塔4F（前半）\n'),
            TXT(0x08, '琥珀之塔5F（前半）\n'),
            TXT(0x09, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_C6D'),
        (0x00000001, 'loc_C76'),
        (0x00000002, 'loc_C7F'),
        (0x00000003, 'loc_C88'),
        (0x00000004, 'loc_C91'),
        (0x00000005, 'loc_C9A'),
        (0x00000006, 'loc_CA3'),
        (0x00000007, 'loc_CAC'),
        (0x00000008, 'loc_CB5'),
        (-1, 'loc_CBE'),
    )

    def _loc_C6D(): pass

    label('loc_C6D')

    NewScene('ED6_DT01/C1200._SN', 0, 0, 0)
    IdleLoop()

    def _loc_C76(): pass

    label('loc_C76')

    NewScene('ED6_DT01/C1400._SN', 0, 0, 0)
    IdleLoop()

    def _loc_C7F(): pass

    label('loc_C7F')

    NewScene('ED6_DT01/C1100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_C88(): pass

    label('loc_C88')

    NewScene('ED6_DT01/C1300._SN', 0, 0, 0)
    IdleLoop()

    def _loc_C91(): pass

    label('loc_C91')

    NewScene('ED6_DT01/C1211._SN', 0, 0, 0)
    IdleLoop()

    def _loc_C9A(): pass

    label('loc_C9A')

    NewScene('ED6_DT01/C1212._SN', 0, 0, 0)
    IdleLoop()

    def _loc_CA3(): pass

    label('loc_CA3')

    NewScene('ED6_DT01/C1213._SN', 0, 0, 0)
    IdleLoop()

    def _loc_CAC(): pass

    label('loc_CAC')

    NewScene('ED6_DT01/C1214._SN', 0, 0, 0)
    IdleLoop()

    def _loc_CB5(): pass

    label('loc_CB5')

    NewScene('ED6_DT01/C1215._SN', 0, 0, 0)
    IdleLoop()

    def _loc_CBE(): pass

    label('loc_CBE')

    OP_5F(0x0003)

    Jump('loc_CC4')

    def _loc_CC4(): pass

    label('loc_CC4')

    Jump('loc_E09')

    def _loc_CC7(): pass

    label('loc_CC7')

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
            TXT(0x05, '安塞尔新街(夜晚)\n'),
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
        (0x00000000, 'loc_D58'),
        (0x00000001, 'loc_D61'),
        (0x00000002, 'loc_D6A'),
        (0x00000003, 'loc_D73'),
        (0x00000004, 'loc_D7C'),
        (0x00000005, 'loc_D85'),
        (0x00000006, 'loc_D8E'),
        (-1, 'loc_D97'),
    )

    def _loc_D58(): pass

    label('loc_D58')

    NewScene('ED6_DT01/C1500._SN', 0, 0, 0)
    IdleLoop()

    def _loc_D61(): pass

    label('loc_D61')

    NewScene('ED6_DT01/R1300._SN', 0, 0, 0)
    IdleLoop()

    def _loc_D6A(): pass

    label('loc_D6A')

    NewScene('ED6_DT01/R1100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_D73(): pass

    label('loc_D73')

    NewScene('ED6_DT01/R1200._SN', 0, 0, 0)
    IdleLoop()

    def _loc_D7C(): pass

    label('loc_D7C')

    NewScene('ED6_DT01/R1400._SN', 0, 0, 0)
    IdleLoop()

    def _loc_D85(): pass

    label('loc_D85')

    NewScene('ED6_DT01/R1403._SN', 0, 0, 0)
    IdleLoop()

    def _loc_D8E(): pass

    label('loc_D8E')

    NewScene('ED6_DT01/R1500._SN', 0, 0, 0)
    IdleLoop()

    def _loc_D97(): pass

    label('loc_D97')

    OP_5F(0x0003)

    Jump('loc_D9D')

    def _loc_D9D(): pass

    label('loc_D9D')

    Jump('loc_E09')

    def _loc_DA0(): pass

    label('loc_DA0')

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
            TXT(0x00, '哈肯大门\n'),
            TXT(0x01, '古罗尼关所\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_DDB'),
        (0x00000001, 'loc_DE7'),
        (-1, 'loc_DF3'),
    )

    def _loc_DDB(): pass

    label('loc_DDB')

    NewScene('ED6_DT01/T1401._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_DF9')

    def _loc_DE7(): pass

    label('loc_DE7')

    NewScene('ED6_DT01/T1311._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_DF9')

    def _loc_DF3(): pass

    label('loc_DF3')

    OP_5F(0x0003)

    Jump('loc_DF9')

    def _loc_DF9(): pass

    label('loc_DF9')

    Jump('loc_E09')

    def _loc_DFC(): pass

    label('loc_DFC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_E09')

    def _loc_E09(): pass

    label('loc_E09')

    Jump('loc_A5C')

    def _loc_E0C(): pass

    label('loc_E0C')

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

# id: 0x0005 offset: 0xE1C
@scena.Code('func_05_E1C')
def func_05_E1C():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    def _loc_E26(): pass

    label('loc_E26')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1340',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '城里\n'),
            TXT(0x01, '迷宫\n'),
            TXT(0x02, '街道\n'),
            TXT(0x03, '夜\n'),
            TXT(0x04, '其它\n'),
            TXT(0x05, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_E78'),
        (0x00000001, 'loc_106C'),
        (0x00000002, 'loc_11AB'),
        (0x00000003, 'loc_124E'),
        (0x00000004, 'loc_12DE'),
        (-1, 'loc_1330'),
    )

    def _loc_E78(): pass

    label('loc_E78')

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
            TXT(0x00, '卢安市\n'),
            TXT(0x01, '飞行场\n'),
            TXT(0x02, '市长官邸\n'),
            TXT(0x03, '王立学院 旧校舍\n'),
            TXT(0x04, '王立学院 主楼\n'),
            TXT(0x05, '王立学院 主楼 学园祭\n'),
            TXT(0x06, '王立学院 主楼 学园祭准备\n'),
            TXT(0x07, '玛西亚孤儿院\n'),
            TXT(0x08, '玛西亚孤儿院（火灾后）\n'),
            TXT(0x09, '玛西亚孤儿院（再建后）\n'),
            TXT(0x0A, '民家\n'),
            TXT(0x0B, '店\n'),
            TXT(0x0C, '教会\n'),
            TXT(0x0D, '酒馆、赌场\n'),
            TXT(0x0E, '艾尔·雷登关所\n'),
            TXT(0x0F, '玛诺利亚村\n'),
            TXT(0x10, '玛西亚孤儿院内部（火灾中)\n'),
            TXT(0x11, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_FCA'),
        (0x00000001, 'loc_FD3'),
        (0x00000002, 'loc_FDC'),
        (0x00000003, 'loc_FE5'),
        (0x00000004, 'loc_FEE'),
        (0x00000005, 'loc_FF7'),
        (0x00000006, 'loc_1000'),
        (0x00000007, 'loc_1009'),
        (0x00000008, 'loc_1012'),
        (0x00000009, 'loc_101B'),
        (0x0000000A, 'loc_1024'),
        (0x0000000B, 'loc_102D'),
        (0x0000000C, 'loc_1036'),
        (0x0000000D, 'loc_103F'),
        (0x0000000E, 'loc_1048'),
        (0x0000000F, 'loc_1051'),
        (0x00000010, 'loc_105A'),
        (-1, 'loc_1063'),
    )

    def _loc_FCA(): pass

    label('loc_FCA')

    NewScene('ED6_DT01/T2100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_FD3(): pass

    label('loc_FD3')

    NewScene('ED6_DT01/T2102._SN', 0, 0, 0)
    IdleLoop()

    def _loc_FDC(): pass

    label('loc_FDC')

    NewScene('ED6_DT01/T2200._SN', 0, 0, 0)
    IdleLoop()

    def _loc_FE5(): pass

    label('loc_FE5')

    NewScene('ED6_DT01/T2600._SN', 0, 0, 0)
    IdleLoop()

    def _loc_FEE(): pass

    label('loc_FEE')

    NewScene('ED6_DT01/T2510._SN', 0, 0, 0)
    IdleLoop()

    def _loc_FF7(): pass

    label('loc_FF7')

    NewScene('ED6_DT01/T2520._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1000(): pass

    label('loc_1000')

    NewScene('ED6_DT01/T2530._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1009(): pass

    label('loc_1009')

    NewScene('ED6_DT01/T2400._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1012(): pass

    label('loc_1012')

    NewScene('ED6_DT01/T2401._SN', 0, 0, 0)
    IdleLoop()

    def _loc_101B(): pass

    label('loc_101B')

    NewScene('ED6_DT01/T2402._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1024(): pass

    label('loc_1024')

    NewScene('ED6_DT01/T2110._SN', 0, 0, 0)
    IdleLoop()

    def _loc_102D(): pass

    label('loc_102D')

    NewScene('ED6_DT01/T2120._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1036(): pass

    label('loc_1036')

    NewScene('ED6_DT01/T2130._SN', 0, 0, 0)
    IdleLoop()

    def _loc_103F(): pass

    label('loc_103F')

    NewScene('ED6_DT01/T2131._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1048(): pass

    label('loc_1048')

    NewScene('ED6_DT01/T2700._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1051(): pass

    label('loc_1051')

    NewScene('ED6_DT01/T2300._SN', 0, 0, 0)
    IdleLoop()

    def _loc_105A(): pass

    label('loc_105A')

    NewScene('ED6_DT01/T2411._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1063(): pass

    label('loc_1063')

    OP_5F(0x0003)

    Jump('loc_1069')

    def _loc_1069(): pass

    label('loc_1069')

    Jump('loc_133D')

    def _loc_106C(): pass

    label('loc_106C')

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
            TXT(0x00, '绀碧之塔（后半）\n'),
            TXT(0x01, '巴伦诺灯塔\n'),
            TXT(0x02, '巴伦诺灯塔（夜晚）\n'),
            TXT(0x03, '旧校舍地下遗迹\n'),
            TXT(0x04, '绀碧之塔1F（前半）\n'),
            TXT(0x05, '绀碧之塔2F（前半）\n'),
            TXT(0x06, '绀碧之塔3F（前半）\n'),
            TXT(0x07, '绀碧之塔4F（前半）\n'),
            TXT(0x08, '绀碧之塔5F（前半）\n'),
            TXT(0x09, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1151'),
        (0x00000001, 'loc_115A'),
        (0x00000002, 'loc_1163'),
        (0x00000003, 'loc_116C'),
        (0x00000004, 'loc_1175'),
        (0x00000005, 'loc_117E'),
        (0x00000006, 'loc_1187'),
        (0x00000007, 'loc_1190'),
        (0x00000008, 'loc_1199'),
        (-1, 'loc_11A2'),
    )

    def _loc_1151(): pass

    label('loc_1151')

    NewScene('ED6_DT01/C2100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_115A(): pass

    label('loc_115A')

    NewScene('ED6_DT01/C2209._SN', 1, 0, 0)
    IdleLoop()

    def _loc_1163(): pass

    label('loc_1163')

    NewScene('ED6_DT01/C2200._SN', 0, 0, 0)
    IdleLoop()

    def _loc_116C(): pass

    label('loc_116C')

    NewScene('ED6_DT01/C2400._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1175(): pass

    label('loc_1175')

    NewScene('ED6_DT01/C2111._SN', 0, 0, 0)
    IdleLoop()

    def _loc_117E(): pass

    label('loc_117E')

    NewScene('ED6_DT01/C2112._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1187(): pass

    label('loc_1187')

    NewScene('ED6_DT01/C2113._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1190(): pass

    label('loc_1190')

    NewScene('ED6_DT01/C2114._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1199(): pass

    label('loc_1199')

    NewScene('ED6_DT01/C2115._SN', 0, 0, 0)
    IdleLoop()

    def _loc_11A2(): pass

    label('loc_11A2')

    OP_5F(0x0003)

    Jump('loc_11A8')

    def _loc_11A8(): pass

    label('loc_11A8')

    Jump('loc_133D')

    def _loc_11AB(): pass

    label('loc_11AB')

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
            TXT(0x05, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1218'),
        (0x00000001, 'loc_1221'),
        (0x00000002, 'loc_122A'),
        (0x00000003, 'loc_1233'),
        (0x00000004, 'loc_123C'),
        (-1, 'loc_1245'),
    )

    def _loc_1218(): pass

    label('loc_1218')

    NewScene('ED6_DT01/C1501._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1221(): pass

    label('loc_1221')

    NewScene('ED6_DT01/R2100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_122A(): pass

    label('loc_122A')

    NewScene('ED6_DT01/R2400._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1233(): pass

    label('loc_1233')

    NewScene('ED6_DT01/R2200._SN', 0, 0, 0)
    IdleLoop()

    def _loc_123C(): pass

    label('loc_123C')

    NewScene('ED6_DT01/R2300._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1245(): pass

    label('loc_1245')

    OP_5F(0x0003)

    Jump('loc_124B')

    def _loc_124B(): pass

    label('loc_124B')

    Jump('loc_133D')

    def _loc_124E(): pass

    label('loc_124E')

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
            TXT(0x00, '玛诺利亚\n'),
            TXT(0x01, '玛诺利亚海岸\n'),
            TXT(0x02, '孤儿院\n'),
            TXT(0x03, '阿伊纳街道\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_12A5'),
        (0x00000001, 'loc_12B1'),
        (0x00000002, 'loc_12BD'),
        (0x00000003, 'loc_12C9'),
        (-1, 'loc_12D5'),
    )

    def _loc_12A5(): pass

    label('loc_12A5')

    NewScene('ED6_DT01/T2301._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_12DB')

    def _loc_12B1(): pass

    label('loc_12B1')

    NewScene('ED6_DT01/R2111._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_12DB')

    def _loc_12BD(): pass

    label('loc_12BD')

    NewScene('ED6_DT01/T2403._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_12DB')

    def _loc_12C9(): pass

    label('loc_12C9')

    NewScene('ED6_DT01/R2412._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_12DB')

    def _loc_12D5(): pass

    label('loc_12D5')

    OP_5F(0x0003)

    Jump('loc_12DB')

    def _loc_12DB(): pass

    label('loc_12DB')

    Jump('loc_133D')

    def _loc_12DE(): pass

    label('loc_12DE')

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
            TXT(0x00, '海卷轴\n'),
            TXT(0x01, '海\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_130F'),
        (0x00000001, 'loc_131B'),
        (-1, 'loc_1327'),
    )

    def _loc_130F(): pass

    label('loc_130F')

    NewScene('ED6_DT01/T2103._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_132D')

    def _loc_131B(): pass

    label('loc_131B')

    NewScene('ED6_DT01/T2104._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_132D')

    def _loc_1327(): pass

    label('loc_1327')

    OP_5F(0x0003)

    Jump('loc_132D')

    def _loc_132D(): pass

    label('loc_132D')

    Jump('loc_133D')

    def _loc_1330(): pass

    label('loc_1330')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_133D')

    def _loc_133D(): pass

    label('loc_133D')

    Jump('loc_E26')

    def _loc_1340(): pass

    label('loc_1340')

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

# id: 0x0006 offset: 0x1350
@scena.Code('func_06_1350')
def func_06_1350():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    def _loc_135A(): pass

    label('loc_135A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1794',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '城里\n'),
            TXT(0x01, '迷宫\n'),
            TXT(0x02, '街道\n'),
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
        (0x00000000, 'loc_13A3'),
        (0x00000001, 'loc_1504'),
        (0x00000002, 'loc_1696'),
        (0x00000003, 'loc_172E'),
        (-1, 'loc_1784'),
    )

    def _loc_13A3(): pass

    label('loc_13A3')

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
            TXT(0x00, '蔡斯市\n'),
            TXT(0x01, '蔡斯市民家１～３室内\n'),
            TXT(0x02, '中央工房　室内\n'),
            TXT(0x03, '沃尔费堡垒\n'),
            TXT(0x04, '蔡斯教会\n'),
            TXT(0x05, '武器店\n'),
            TXT(0x06, '拉赛尔工房\n'),
            TXT(0x07, '亚尔摩村外部\n'),
            TXT(0x08, '亚尔摩村外部（夜晚）\n'),
            TXT(0x09, '圣海姆门\n'),
            TXT(0x0A, '蔡斯市(夜晚)\n'),
            TXT(0x0B, '蔡斯市（停电）\n'),
            TXT(0x0C, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_148F'),
        (0x00000001, 'loc_1498'),
        (0x00000002, 'loc_14A1'),
        (0x00000003, 'loc_14AA'),
        (0x00000004, 'loc_14B3'),
        (0x00000005, 'loc_14BC'),
        (0x00000006, 'loc_14C5'),
        (0x00000007, 'loc_14CE'),
        (0x00000008, 'loc_14D7'),
        (0x00000009, 'loc_14E0'),
        (0x0000000A, 'loc_14E9'),
        (0x0000000B, 'loc_14F2'),
        (-1, 'loc_14FB'),
    )

    def _loc_148F(): pass

    label('loc_148F')

    NewScene('ED6_DT01/T3100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1498(): pass

    label('loc_1498')

    NewScene('ED6_DT01/T3110._SN', 0, 0, 0)
    IdleLoop()

    def _loc_14A1(): pass

    label('loc_14A1')

    NewScene('ED6_DT01/T3111._SN', 0, 0, 0)
    IdleLoop()

    def _loc_14AA(): pass

    label('loc_14AA')

    NewScene('ED6_DT01/T3300._SN', 100, 0, 0)
    IdleLoop()

    def _loc_14B3(): pass

    label('loc_14B3')

    NewScene('ED6_DT01/T3130._SN', 0, 0, 0)
    IdleLoop()

    def _loc_14BC(): pass

    label('loc_14BC')

    NewScene('ED6_DT01/T3120._SN', 0, 0, 0)
    IdleLoop()

    def _loc_14C5(): pass

    label('loc_14C5')

    NewScene('ED6_DT01/T3133._SN', 0, 0, 0)
    IdleLoop()

    def _loc_14CE(): pass

    label('loc_14CE')

    NewScene('ED6_DT01/T3200._SN', 0, 0, 0)
    IdleLoop()

    def _loc_14D7(): pass

    label('loc_14D7')

    NewScene('ED6_DT01/T3201._SN', 0, 0, 0)
    IdleLoop()

    def _loc_14E0(): pass

    label('loc_14E0')

    NewScene('ED6_DT01/T3400._SN', 0, 0, 0)
    IdleLoop()

    def _loc_14E9(): pass

    label('loc_14E9')

    NewScene('ED6_DT01/T3103._SN', 0, 0, 0)
    IdleLoop()

    def _loc_14F2(): pass

    label('loc_14F2')

    NewScene('ED6_DT01/T3106._SN', 0, 0, 0)
    IdleLoop()

    def _loc_14FB(): pass

    label('loc_14FB')

    OP_5F(0x0003)

    Jump('loc_1501')

    def _loc_1501(): pass

    label('loc_1501')

    Jump('loc_1791')

    def _loc_1504(): pass

    label('loc_1504')

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
            TXT(0x00, '红莲之塔（后半）\n'),
            TXT(0x01, '雷斯顿水上要塞外\n'),
            TXT(0x02, '雷斯顿水上要塞中\n'),
            TXT(0x03, '雷斯顿水上要塞外（夜晚)\n'),
            TXT(0x04, '卡鲁迪亚大钟乳洞\n'),
            TXT(0x05, '卡鲁迪亚大钟乳洞　BOSS房间\n'),
            TXT(0x06, '红莲之塔1F（前半）\n'),
            TXT(0x07, '红莲之塔2F（前半）\n'),
            TXT(0x08, '红莲之塔3F（前半）\n'),
            TXT(0x09, '红莲之塔4F（前半）\n'),
            TXT(0x0A, '红莲之塔5F（前半）\n'),
            TXT(0x0B, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_162A'),
        (0x00000001, 'loc_1633'),
        (0x00000002, 'loc_163C'),
        (0x00000003, 'loc_1645'),
        (0x00000004, 'loc_164E'),
        (0x00000005, 'loc_1657'),
        (0x00000006, 'loc_1660'),
        (0x00000007, 'loc_1669'),
        (0x00000008, 'loc_1672'),
        (0x00000009, 'loc_167B'),
        (0x0000000A, 'loc_1684'),
        (-1, 'loc_168D'),
    )

    def _loc_162A(): pass

    label('loc_162A')

    NewScene('ED6_DT01/C3500._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1633(): pass

    label('loc_1633')

    NewScene('ED6_DT01/C3100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_163C(): pass

    label('loc_163C')

    NewScene('ED6_DT01/C3110._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1645(): pass

    label('loc_1645')

    NewScene('ED6_DT01/C3104._SN', 0, 0, 0)
    IdleLoop()

    def _loc_164E(): pass

    label('loc_164E')

    NewScene('ED6_DT01/C3300._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1657(): pass

    label('loc_1657')

    NewScene('ED6_DT01/C3303._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1660(): pass

    label('loc_1660')

    NewScene('ED6_DT01/C3511._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1669(): pass

    label('loc_1669')

    NewScene('ED6_DT01/C3512._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1672(): pass

    label('loc_1672')

    NewScene('ED6_DT01/C3513._SN', 0, 0, 0)
    IdleLoop()

    def _loc_167B(): pass

    label('loc_167B')

    NewScene('ED6_DT01/C3514._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1684(): pass

    label('loc_1684')

    NewScene('ED6_DT01/C3515._SN', 0, 0, 0)
    IdleLoop()

    def _loc_168D(): pass

    label('loc_168D')

    OP_5F(0x0003)

    Jump('loc_1693')

    def _loc_1693(): pass

    label('loc_1693')

    Jump('loc_1791')

    def _loc_1696(): pass

    label('loc_1696')

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
            TXT(0x01, '卡鲁迪亚隧道（隧道)\n'),
            TXT(0x02, '托兰特平原道\n'),
            TXT(0x03, '利塔街道\n'),
            TXT(0x04, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1701'),
        (0x00000001, 'loc_170A'),
        (0x00000002, 'loc_1713'),
        (0x00000003, 'loc_171C'),
        (-1, 'loc_1725'),
    )

    def _loc_1701(): pass

    label('loc_1701')

    NewScene('ED6_DT01/R3300._SN', 0, 0, 0)
    IdleLoop()

    def _loc_170A(): pass

    label('loc_170A')

    NewScene('ED6_DT01/R3400._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1713(): pass

    label('loc_1713')

    NewScene('ED6_DT01/R3100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_171C(): pass

    label('loc_171C')

    NewScene('ED6_DT01/R3200._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1725(): pass

    label('loc_1725')

    OP_5F(0x0003)

    Jump('loc_172B')

    def _loc_172B(): pass

    label('loc_172B')

    Jump('loc_1791')

    def _loc_172E(): pass

    label('loc_172E')

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
            TXT(0x00, '蔡斯\n'),
            TXT(0x01, '中央工房\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1763'),
        (0x00000001, 'loc_176F'),
        (-1, 'loc_177B'),
    )

    def _loc_1763(): pass

    label('loc_1763')

    NewScene('ED6_DT01/T3103._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1781')

    def _loc_176F(): pass

    label('loc_176F')

    NewScene('ED6_DT01/T3104._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1781')

    def _loc_177B(): pass

    label('loc_177B')

    OP_5F(0x0003)

    Jump('loc_1781')

    def _loc_1781(): pass

    label('loc_1781')

    Jump('loc_1791')

    def _loc_1784(): pass

    label('loc_1784')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1791')

    def _loc_1791(): pass

    label('loc_1791')

    Jump('loc_135A')

    def _loc_1794(): pass

    label('loc_1794')

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

# id: 0x0007 offset: 0x17A4
@scena.Code('func_07_17A4')
def func_07_17A4():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    def _loc_17AE(): pass

    label('loc_17AE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BB7',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '城里\n'),
            TXT(0x01, '迷宫\n'),
            TXT(0x02, '街道\n'),
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
        (0x00000000, 'loc_17F7'),
        (0x00000001, 'loc_18CC'),
        (0x00000002, 'loc_1993'),
        (0x00000003, 'loc_19F0'),
        (-1, 'loc_1BA7'),
    )

    def _loc_17F7(): pass

    label('loc_17F7')

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
            TXT(0x00, '格兰赛尔\n'),
            TXT(0x01, '格兰赛尔城\n'),
            TXT(0x02, '艾尔贝离宫\n'),
            TXT(0x03, '旅馆（夜晚）\n'),
            TXT(0x04, '大圣堂（夜晚）\n'),
            TXT(0x05, '历史资料馆\n'),
            TXT(0x06, '竞技场\n'),
            TXT(0x07, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1884'),
        (0x00000001, 'loc_188D'),
        (0x00000002, 'loc_1896'),
        (0x00000003, 'loc_189F'),
        (0x00000004, 'loc_18A8'),
        (0x00000005, 'loc_18B1'),
        (0x00000006, 'loc_18BA'),
        (-1, 'loc_18C3'),
    )

    def _loc_1884(): pass

    label('loc_1884')

    NewScene('ED6_DT01/T4100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_188D(): pass

    label('loc_188D')

    NewScene('ED6_DT01/T4200._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1896(): pass

    label('loc_1896')

    NewScene('ED6_DT01/T4300._SN', 0, 0, 0)
    IdleLoop()

    def _loc_189F(): pass

    label('loc_189F')

    NewScene('ED6_DT01/T4133._SN', 0, 0, 0)
    IdleLoop()

    def _loc_18A8(): pass

    label('loc_18A8')

    NewScene('ED6_DT01/T4134._SN', 0, 0, 0)
    IdleLoop()

    def _loc_18B1(): pass

    label('loc_18B1')

    NewScene('ED6_DT01/T4135._SN', 0, 0, 0)
    IdleLoop()

    def _loc_18BA(): pass

    label('loc_18BA')

    NewScene('ED6_DT01/T4136._SN', 0, 0, 0)
    IdleLoop()

    def _loc_18C3(): pass

    label('loc_18C3')

    OP_5F(0x0003)

    Jump('loc_18C9')

    def _loc_18C9(): pass

    label('loc_18C9')

    Jump('loc_1BB4')

    def _loc_18CC(): pass

    label('loc_18CC')

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
            TXT(0x00, '地下水路Ａ\n'),
            TXT(0x01, '地下水路Ｂ\n'),
            TXT(0x02, '地下水路Ｃ\n'),
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
        (0x00000000, 'loc_1954'),
        (0x00000001, 'loc_195D'),
        (0x00000002, 'loc_1966'),
        (0x00000003, 'loc_196F'),
        (0x00000004, 'loc_1978'),
        (0x00000005, 'loc_1981'),
        (-1, 'loc_198A'),
    )

    def _loc_1954(): pass

    label('loc_1954')

    NewScene('ED6_DT01/C4200._SN', 100, 0, 0)
    IdleLoop()

    def _loc_195D(): pass

    label('loc_195D')

    NewScene('ED6_DT01/C4202._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1966(): pass

    label('loc_1966')

    NewScene('ED6_DT01/C4204._SN', 100, 0, 0)
    IdleLoop()

    def _loc_196F(): pass

    label('loc_196F')

    NewScene('ED6_DT01/C4300._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1978(): pass

    label('loc_1978')

    NewScene('ED6_DT01/C4301._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1981(): pass

    label('loc_1981')

    NewScene('ED6_DT01/C4302._SN', 0, 0, 0)
    IdleLoop()

    def _loc_198A(): pass

    label('loc_198A')

    OP_5F(0x0003)

    Jump('loc_1990')

    def _loc_1990(): pass

    label('loc_1990')

    Jump('loc_1BB4')

    def _loc_1993(): pass

    label('loc_1993')

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
            TXT(0x02, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_19D5'),
        (0x00000001, 'loc_19DE'),
        (-1, 'loc_19E7'),
    )

    def _loc_19D5(): pass

    label('loc_19D5')

    NewScene('ED6_DT01/C4100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_19DE(): pass

    label('loc_19DE')

    NewScene('ED6_DT01/R4100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_19E7(): pass

    label('loc_19E7')

    OP_5F(0x0003)

    Jump('loc_19ED')

    def _loc_19ED(): pass

    label('loc_19ED')

    Jump('loc_1BB4')

    def _loc_19F0(): pass

    label('loc_19F0')

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
            TXT(0x00, '艾尔贝周游道 C4111\n'),
            TXT(0x01, '艾尔贝周游道 C4113\n'),
            TXT(0x02, '艾尔贝离宫 入口庭园\n'),
            TXT(0x03, '艾尔贝离宫 中庭、回廊\n'),
            TXT(0x04, '艾尔贝离宫 大厅～\n'),
            TXT(0x05, '艾尔贝离宫 客室～\n'),
            TXT(0x06, '格兰赛尔 南街区\n'),
            TXT(0x07, '格兰赛尔 东街区\n'),
            TXT(0x08, '格兰赛尔 西街区\n'),
            TXT(0x09, '格兰赛尔 北街区\n'),
            TXT(0x0A, '格兰赛尔城\n'),
            TXT(0x0B, '格兰赛尔城 室内\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1B0E'),
        (0x00000001, 'loc_1B1A'),
        (0x00000002, 'loc_1B26'),
        (0x00000003, 'loc_1B32'),
        (0x00000004, 'loc_1B3E'),
        (0x00000005, 'loc_1B4A'),
        (0x00000006, 'loc_1B56'),
        (0x00000007, 'loc_1B62'),
        (0x00000008, 'loc_1B6E'),
        (0x00000009, 'loc_1B7A'),
        (0x0000000A, 'loc_1B86'),
        (0x0000000B, 'loc_1B92'),
        (-1, 'loc_1B9E'),
    )

    def _loc_1B0E(): pass

    label('loc_1B0E')

    NewScene('ED6_DT01/C4111._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1BA4')

    def _loc_1B1A(): pass

    label('loc_1B1A')

    NewScene('ED6_DT01/C4113._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1BA4')

    def _loc_1B26(): pass

    label('loc_1B26')

    NewScene('ED6_DT01/T4302._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1BA4')

    def _loc_1B32(): pass

    label('loc_1B32')

    NewScene('ED6_DT01/T4303._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1BA4')

    def _loc_1B3E(): pass

    label('loc_1B3E')

    NewScene('ED6_DT01/T4312._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1BA4')

    def _loc_1B4A(): pass

    label('loc_1B4A')

    NewScene('ED6_DT01/T4313._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1BA4')

    def _loc_1B56(): pass

    label('loc_1B56')

    NewScene('ED6_DT01/T4150._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1BA4')

    def _loc_1B62(): pass

    label('loc_1B62')

    NewScene('ED6_DT01/T4151._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1BA4')

    def _loc_1B6E(): pass

    label('loc_1B6E')

    NewScene('ED6_DT01/T4152._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1BA4')

    def _loc_1B7A(): pass

    label('loc_1B7A')

    NewScene('ED6_DT01/T4153._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1BA4')

    def _loc_1B86(): pass

    label('loc_1B86')

    NewScene('ED6_DT01/T4203._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1BA4')

    def _loc_1B92(): pass

    label('loc_1B92')

    NewScene('ED6_DT01/T4250._SN', 0, 0, 0)
    IdleLoop()

    Jump('loc_1BA4')

    def _loc_1B9E(): pass

    label('loc_1B9E')

    OP_5F(0x0003)

    Jump('loc_1BA4')

    def _loc_1BA4(): pass

    label('loc_1BA4')

    Jump('loc_1BB4')

    def _loc_1BA7(): pass

    label('loc_1BA7')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BB4')

    def _loc_1BB4(): pass

    label('loc_1BB4')

    Jump('loc_17AE')

    def _loc_1BB7(): pass

    label('loc_1BB7')

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

# id: 0x0008 offset: 0x1BC7
@scena.Code('func_08_1BC7')
def func_08_1BC7():
    Talk(
        (
            TxtCtl.ShowAll,
            '哪里？',
            TxtCtl.Enter,
        ),
    )

    def _loc_1BD1(): pass

    label('loc_1BD1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D32',
    )

    Menu(
        2,
        10,
        100,
        1,
        (
            TXT(0x00, '船\n'),
            TXT(0x01, '天空\n'),
            TXT(0x02, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1C08'),
        (0x00000001, 'loc_1CE3'),
        (-1, 'loc_1D22'),
    )

    def _loc_1C08(): pass

    label('loc_1C08')

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
            TXT(0x00, '定期船\n'),
            TXT(0x01, '定期船绿色\n'),
            TXT(0x02, '工房船\n'),
            TXT(0x03, '空贼艇\n'),
            TXT(0x04, '军用两栖舰\n'),
            TXT(0x05, '埃尔赛尤外\n'),
            TXT(0x06, '特务艇\n'),
            TXT(0x07, '空内装置\n'),
            TXT(0x08, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1C92'),
        (0x00000001, 'loc_1C9B'),
        (0x00000002, 'loc_1CA4'),
        (0x00000003, 'loc_1CAD'),
        (0x00000004, 'loc_1CB6'),
        (0x00000005, 'loc_1CBF'),
        (0x00000006, 'loc_1CC8'),
        (0x00000007, 'loc_1CD1'),
        (-1, 'loc_1CDA'),
    )

    def _loc_1C92(): pass

    label('loc_1C92')

    NewScene('ED6_DT01/E0000._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1C9B(): pass

    label('loc_1C9B')

    NewScene('ED6_DT01/E0001._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1CA4(): pass

    label('loc_1CA4')

    NewScene('ED6_DT01/E0002._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1CAD(): pass

    label('loc_1CAD')

    NewScene('ED6_DT01/E0100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1CB6(): pass

    label('loc_1CB6')

    NewScene('ED6_DT01/E0200._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1CBF(): pass

    label('loc_1CBF')

    NewScene('ED6_DT01/E0300._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1CC8(): pass

    label('loc_1CC8')

    NewScene('ED6_DT01/E0400._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1CD1(): pass

    label('loc_1CD1')

    NewScene('ED6_DT01/E0111._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1CDA(): pass

    label('loc_1CDA')

    OP_5F(0x0003)

    Jump('loc_1CE0')

    def _loc_1CE0(): pass

    label('loc_1CE0')

    Jump('loc_1D2F')

    def _loc_1CE3(): pass

    label('loc_1CE3')

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
            TXT(0x00, '天空\n'),
            TXT(0x01, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1D10'),
        (-1, 'loc_1D19'),
    )

    def _loc_1D10(): pass

    label('loc_1D10')

    NewScene('ED6_DT01/E0500._SN', 0, 0, 0)
    IdleLoop()

    def _loc_1D19(): pass

    label('loc_1D19')

    OP_5F(0x0003)

    Jump('loc_1D1F')

    def _loc_1D1F(): pass

    label('loc_1D1F')

    Jump('loc_1D2F')

    def _loc_1D22(): pass

    label('loc_1D22')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1D2F')

    def _loc_1D2F(): pass

    label('loc_1D2F')

    Jump('loc_1BD1')

    def _loc_1D32(): pass

    label('loc_1D32')

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
