import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1111   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1111.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x0000BB80,
            dword_04        = 0xFFFFF448,
            dword_08        = 0x00006978,
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
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH02363._CH', 'ED6_DT07/CH02363P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '梅贝尔市长',
            x                   = -120760,
            z                   = 200,
            y                   = 68570,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '莉拉',
            x                   = -3220,
            z                   = -4000,
            y                   = 68110,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '管家门特斯',
            x                   = 4000,
            z                   = 500,
            y                   = -870,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '萨拉',
            x                   = -33400,
            z                   = -3000,
            y                   = 35100,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '米拉诺',
            x                   = -120820,
            z                   = 0,
            y                   = 66250,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
    )

# id: 0x10002 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x19A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1CB',
    )

    ChrSetPos(0x000B, -64150, -3000, 66390, 0)
    ChrSetPos(0x0009, -123500, 0, 66690, 275)
    ChrSetChipByIndex(0x0008, 9)

    Jump('loc_27E')

    def _loc_1CB(): pass

    label('loc_1CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1FA',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    ChrSetPos(0x000B, -64150, -3000, 66390, 0)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetChipByIndex(0x0008, 9)

    Jump('loc_27E')

    def _loc_1FA(): pass

    label('loc_1FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_213',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0008)
    ChrSetChipByIndex(0x0008, 9)

    Jump('loc_27E')

    def _loc_213(): pass

    label('loc_213')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_23D',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    ChrSetPos(0x000B, -64150, -3000, 66390, 0)
    ChrSetChipByIndex(0x0008, 9)

    Jump('loc_27E')

    def _loc_23D(): pass

    label('loc_23D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_256',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0008)
    ChrSetChipByIndex(0x0008, 9)

    Jump('loc_27E')

    def _loc_256(): pass

    label('loc_256')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_276',
    )

    ChrSetPos(0x000B, -65000, -3000, 64650, 270)
    ChrSetChipByIndex(0x0008, 9)

    Jump('loc_27E')

    def _loc_276(): pass

    label('loc_276')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 1, 0x309)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27E',
    )

    def _loc_27E(): pass

    label('loc_27E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AB',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)
    ChrSetPos(0x000B, -6030, 4500, 2470, 275)

    def _loc_2AB(): pass

    label('loc_2AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_2B9',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0C_38CD)

    def _loc_2B9(): pass

    label('loc_2B9')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_2C9'),
        (0x0000006E, 'loc_2DF'),
        (-1, 'loc_2F5'),
    )

    def _loc_2C9(): pass

    label('loc_2C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 1, 0x309)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 0, 0x308)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2DC',
    )

    SetScenaFlags(ScenaFlag(0x0061, 1, 0x309))
    Event(0, func_0A_23C3)

    def _loc_2DC(): pass

    label('loc_2DC')

    Jump('loc_2F5')

    def _loc_2DF(): pass

    label('loc_2DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 3, 0x313)),
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 7, 0x317)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F2',
    )

    SetScenaFlags(ScenaFlag(0x0062, 7, 0x317))
    Event(0, func_0B_2B53)

    def _loc_2F2(): pass

    label('loc_2F2')

    Jump('loc_2F5')

    def _loc_2F5(): pass

    label('loc_2F5')

    Return()

# id: 0x0001 offset: 0x2F6
@scena.Code('func_01_2F6')
def func_01_2F6():
    Return()

# id: 0x0002 offset: 0x2F7
@scena.Code('func_02_2F7')
def func_02_2F7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_30C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_2F7')

    def _loc_30C(): pass

    label('loc_30C')

    Return()

# id: 0x0003 offset: 0x30D
@scena.Code('func_03_30D')
def func_03_30D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_330',
    )

    OP_8D(0x00FE, -37400, -6200, -27800, -1300, 2000)

    Jump('func_03_30D')

    def _loc_330(): pass

    label('loc_330')

    Return()

# id: 0x0004 offset: 0x331
@scena.Code('func_04_331')
def func_04_331():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_350',
    )

    def _loc_338(): pass

    label('loc_338')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_34D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_338')

    def _loc_34D(): pass

    label('loc_34D')

    Jump('loc_392')

    def _loc_350(): pass

    label('loc_350')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_37D',
    )

    def _loc_357(): pass

    label('loc_357')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_37A',
    )

    OP_8D(0x00FE, -34800, 34500, -31600, 36300, 2000)

    Jump('loc_357')

    def _loc_37A(): pass

    label('loc_37A')

    Jump('loc_392')

    def _loc_37D(): pass

    label('loc_37D')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_392',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_37D')

    def _loc_392(): pass

    label('loc_392')

    Return()

# id: 0x0005 offset: 0x393
@scena.Code('func_05_393')
def func_05_393():
    TalkBegin(0x0008)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3B8',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_3D3')

    def _loc_3B8(): pass

    label('loc_3B8')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3CE',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_3D3')

    def _loc_3CE(): pass

    label('loc_3CE')

    ChrSetSubChip(0x00FE, 2)

    def _loc_3D3(): pass

    label('loc_3D3')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_759',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_722',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0360031982V#613F啊呀，是艾丝蒂尔……\n',
            '难道你们现在要出发了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031983V#000F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031984V#010F感谢最近一段时间\n',
            '您对我们的诸多照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360031985V#610F呵呵，\n',
            '受照顾的应该是我们才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360031986V如果像你们这样的游击士\n',
            '能一直呆在柏斯的话，\n',
            '大家一定会很高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031987V#008F市长姐姐这么说，\n',
            '我们会觉得非常不好意思的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360031988V#610F你们用不着谦虚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360031989V让我再次\n',
            '代表柏斯市民向你们致谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360031990V真的是\n',
            '太谢谢你们两位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031991V#501F市长姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360031992V#610F那么， \n',
            '我也不能留你们太久。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360031993V艾丝蒂尔、约修亚。\n',
            '路上小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031994V#001F嗯，市长姐姐也要保重身体。\n',
            '不要让工作累坏了身子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360031995V#617F呵呵，刚才已经被莉拉\n',
            '狠狠地说了一顿了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360031996V我会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031997V#010F那么我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_756')

    def _loc_722(): pass

    label('loc_722')

    ChrTalk(
        0x0008,
        (
            '#0360031998V#610F艾丝蒂尔、约修亚。\n',
            '后会有期。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_756(): pass

    label('loc_756')

    Jump('loc_FDF')

    def _loc_759(): pass

    label('loc_759')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_A02',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_99A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0360030571V#610F我刚从米拉诺那里\n',
            '知道了柏斯超市现在的经营状况。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030572V#612F定期船失踪事件还是\n',
            '造成了非常大的影响啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030573V#610F各位……\n',
            '如果掌握了什么线索，\n',
            '记得来我这里通知一声哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030574V#006F嘿嘿，知道吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030575V虽然还不太确定，\n',
            '不过也算是得到了一点点线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030576V#010F我们会在这段时间内，\n',
            '把收集到的情报呈上给您的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030577V#020F不过，也可能会是空欢喜一场。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030578V现在唯有请你们等上一段时间了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0360030579V#610F好的，\n',
            '那我就期待你们的好消息了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030580V务必要注意安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9FF')

    def _loc_99A(): pass

    label('loc_99A')

    ChrTalk(
        0x00FE,
        (
            '#0360030581V#612F真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030582V本来就是非常忙的时候，\n',
            '竟然还接连发生这么多的事件。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9FF(): pass

    label('loc_9FF')

    Jump('loc_FDF')

    def _loc_A02(): pass

    label('loc_A02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_BC5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B4B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0360030258V#615F在我的朋友里\n',
            '有一位叫米拉诺的女性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030259V她的父亲也在\n',
            '失踪的『林德号』乘客名册上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030260V#612F像她父亲那样还没有回到家，\n',
            '让家人十分担心的人也一定还有很多吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030261V这次强盗案与劫机案\n',
            '是同一伙人干的可能性非常高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030262V你们哪怕能查到一丝线索也好……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BC2')

    def _loc_B4B(): pass

    label('loc_B4B')

    ChrTalk(
        0x00FE,
        (
            '#0360030263V#612F这次，强盗案与劫机案\n',
            '是同一伙人干的可能性非常高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030264V你们哪怕能查到一丝线索也好……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BC2(): pass

    label('loc_BC2')

    Jump('loc_FDF')

    def _loc_BC5(): pass

    label('loc_BC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_E3E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DB4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0360021440V#610F啊，是你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021441V事件的调查有没有进展呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021442V#000F嗯～老实说，\n',
            '情报太少了，还是有点难办。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021443V不过也算是发现了一些线索。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021444V#010F虽说是线索，\n',
            '不过也不是什么可靠的情报……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021445V不管怎么说，\n',
            '我们打算先去拉文努村看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0360021446V#610F拉文努村……是吗？\n',
            '我记得军队那边已经调查过了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021447V不过现在没有别的线索，\n',
            '我们确实有再次调查的必要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021448V我明白了，\n',
            '那就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E3B')

    def _loc_DB4(): pass

    label('loc_DB4')

    ChrTalk(
        0x00FE,
        (
            '#0360021449V#610F拉文努村……是吗？\n',
            '我记得军队那边已经调查过了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021450V不过现在没有别的线索，\n',
            '我们确实有再次调查的必要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E3B(): pass

    label('loc_E3B')

    Jump('loc_FDF')

    def _loc_E3E(): pass

    label('loc_E3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 7, 0x317)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F1F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EEE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0360021258V#612F嗯～对劫机事件的处理\n',
            '要放在最优先的地位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021259V其他资料的整理就以后再做吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021260V#611F呵呵……\n',
            '要忙起来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1C')

    def _loc_EEE(): pass

    label('loc_EEE')

    ChrTalk(
        0x00FE,
        (
            '#0360021261V#611F呵呵……\n',
            '要忙起来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F1C(): pass

    label('loc_F1C')

    Jump('loc_FDF')

    def _loc_F1F(): pass

    label('loc_F1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_FDF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FA1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0360020649V#610F各位游击士，\n',
            '我期待你们的好消息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020650V如果能见到摩尔根将军，\n',
            '请代我向他问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FDF')

    def _loc_FA1(): pass

    label('loc_FA1')

    ChrTalk(
        0x00FE,
        (
            '#0360020651V#610F如果能见到摩尔根将军，\n',
            '请代我向他问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FDF(): pass

    label('loc_FDF')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x0008)

    Return()

# id: 0x0006 offset: 0xFE8
@scena.Code('func_06_FE8')
def func_06_FE8():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1058',
    )

    ChrTalk(
        0x00FE,
        (
            '#0370031999V#621F这下小姐终于可以高枕无忧了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370032000V真的多亏了大家……\n',
            '多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1625')

    def _loc_1058(): pass

    label('loc_1058')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_10ED',
    )

    ChrTalk(
        0x00FE,
        (
            '#0370030583V小姐连续好几天\n',
            '彻夜不眠地加班加点，\n',
            '来想办法如何处理强盗事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0370030584V如果我无法好好照顾\n',
            '小姐的身体状况的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1625')

    def _loc_10ED(): pass

    label('loc_10ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_12B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1257',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0370030265V#620F各位，这真是一场灾难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370030266V游击士协会那边\n',
            '已经与小姐联系过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030267V#002F嗯……\n',
            '虽说拿他们没办法，\n',
            '但我总觉得很没面子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030268V#010F算了，这次的事情是不可抗力造成的。\n',
            '不能全都怪在王国军头上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030269V#009F哼哼～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030270V空贼啊空贼～我们走着瞧吧。\n',
            '下次我一定会抓住你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12B5')

    def _loc_1257(): pass

    label('loc_1257')

    ChrTalk(
        0x00FE,
        (
            '#0370030271V#620F各位，这真是一场灾难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370030272V游击士协会那边\n',
            '已经与小姐联系过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12B5(): pass

    label('loc_12B5')

    Jump('loc_1625')

    def _loc_12B8(): pass

    label('loc_12B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1382',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1348',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0370021456V小姐就是那种自己越忙\n',
            '就越有干劲的类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0370021457V这可能是继承了前市长……\n',
            '她父亲血统的原因吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_137F')

    def _loc_1348(): pass

    label('loc_1348')

    ChrTalk(
        0x00FE,
        (
            '#0370021458V可是，\n',
            '我却非常担心小姐的身体状况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_137F(): pass

    label('loc_137F')

    Jump('loc_1625')

    def _loc_1382(): pass

    label('loc_1382')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_14CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_144A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0370021262V#620F摩尔根将军\n',
            '来过我们这里很多次了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370021263V不管怎么看，\n',
            '他都是一位非常出色的军人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370021264V#623F不管是好还是坏，\n',
            '我觉得他都是一位拥有军人气质的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14C8')

    def _loc_144A(): pass

    label('loc_144A')

    ChrTalk(
        0x00FE,
        (
            '#0370021265V#620F摩尔根将军\n',
            '是一位非常出色的军人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370021266V#623F不管是好还是坏，\n',
            '我觉得他都是一位拥有军人气质的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14C8(): pass

    label('loc_14C8')

    Jump('loc_1625')

    def _loc_14CB(): pass

    label('loc_14CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_1625',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15B6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0370020652V#620F这次的事情\n',
            '真的让小姐很头疼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020653V本来就有一大堆强盗案件\n',
            '等着小姐去应付……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020654V#621F各位游击士，\n',
            '请一定要帮小姐的忙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020655V作为她的随从，\n',
            '我也会很衷心地拜托你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1625')

    def _loc_15B6(): pass

    label('loc_15B6')

    ChrTalk(
        0x00FE,
        (
            '#0370020656V#621F各位游击士，\n',
            '请一定要帮小姐的忙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020657V作为她的随从，\n',
            '我也会很衷心地拜托你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1625(): pass

    label('loc_1625')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x1629
@scena.Code('func_07_1629')
def func_07_1629():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1759',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16E1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '真是要好好感谢一下各位才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐如果能\n',
            '趁此机会休息一下就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她只要一放松，\n',
            '一些杂事就会找上门来，\n',
            '这就是她的性格，我真替她担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1756')

    def _loc_16E1(): pass

    label('loc_16E1')

    ChrTalk(
        0x00FE,
        (
            '小姐如果能\n',
            '趁此机会休息一下就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她只要一放松，\n',
            '一些杂事就会找上门来，\n',
            '这就是她的性格，我真替她担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1756(): pass

    label('loc_1756')

    Jump('loc_1EF0')

    def _loc_1759(): pass

    label('loc_1759')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_191E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_189C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '在１０年前的战争中，\n',
            '帝国军破坏了柏斯的街道，\n',
            '并占据了整个柏斯地区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，小姐的父亲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也就是前一任市长，以他为先驱，\n',
            '尽全力复兴这座属于商人的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平时都是各自为政\n',
            '做自己买卖的大大小小的商人，\n',
            '就在那个紧要关头团结起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐决定继承父亲的\n',
            '这个伟大志向也是从那时开始的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_191B')

    def _loc_189C(): pass

    label('loc_189C')

    ChrTalk(
        0x00FE,
        (
            '战争结束以后，\n',
            '小姐的父亲作为先驱，\n',
            '尽全力复兴这座属于商人的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐决定继承父亲的\n',
            '这个伟大志向也是从那时开始的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_191B(): pass

    label('loc_191B')

    Jump('loc_1EF0')

    def _loc_191E(): pass

    label('loc_191E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1A51',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19F0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '虽然我劝过小姐，\n',
            '请她稍微休息一下的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过她说当务之急是要\n',
            '消除市民的不安，\n',
            '让街上恢复平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我对她能有\n',
            '如此大的长进感到十分欣慰，\n',
            '但是我也希望她能够为自己多着想一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A4E')

    def _loc_19F0(): pass

    label('loc_19F0')

    ChrTalk(
        0x00FE,
        (
            '小姐能有如此大的长进\n',
            '让我感到十分地欣慰……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '我也希望她能够为自己多着想一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A4E(): pass

    label('loc_1A4E')

    Jump('loc_1EF0')

    def _loc_1A51(): pass

    label('loc_1A51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1B8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B35',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '小姐当选柏斯市长的时候\n',
            '因为过于年轻，\n',
            '反对的声音一直不绝于耳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过当大家看到小姐制定的种种商业政策\n',
            '让城市迅速发展起来之后，\n',
            '支持者就陆续出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有势商人特里诺家的米拉诺小姐\n',
            '就是其中的代表。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B88')

    def _loc_1B35(): pass

    label('loc_1B35')

    ChrTalk(
        0x00FE,
        (
            '米拉诺小姐也很年轻，\n',
            '不过作为商人却十分有才华……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐对她的评价也很高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B88(): pass

    label('loc_1B88')

    Jump('loc_1EF0')

    def _loc_1B8B(): pass

    label('loc_1B8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 7, 0x317)),
            Expr.Return,
        ),
        'loc_1BED',
    )

    ChrTalk(
        0x00FE,
        (
            '各位辛苦了。\n',
            '看起来调查似乎有所进展呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐她也非常努力，\n',
            '现在正干劲十足呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EF0')

    def _loc_1BED(): pass

    label('loc_1BED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1C30',
    )

    ChrTalk(
        0x00FE,
        (
            '各位，欢迎回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐正在\n',
            '急切等待各位的报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EF0')

    def _loc_1C30(): pass

    label('loc_1C30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_1D43',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CE4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哦，各位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们是来找小姐……\n',
            '……市长的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论有什么事情，\n',
            '我们都欢迎你们随时过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐吩咐过，无论什么时候，\n',
            '我们都十分欢迎你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D40')

    def _loc_1CE4(): pass

    label('loc_1CE4')

    ChrTalk(
        0x00FE,
        (
            '有什么事情的话，\n',
            '欢迎随时过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐吩咐过，无论什么时候，\n',
            '我们都十分欢迎你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D40(): pass

    label('loc_1D40')

    Jump('loc_1EF0')

    def _loc_1D43(): pass

    label('loc_1D43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 2, 0x30A)),
            Expr.Return,
        ),
        'loc_1E3C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1DAC',
    )

    ChrTalk(
        0x00FE,
        (
            '你们可能已经知道了，\n',
            '超市就在北街区的中央。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从我们官邸正门出去，\n',
            '对面就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E39')

    def _loc_1DAC(): pass

    label('loc_1DAC')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哦，各位……\n',
            '你们已经找到莉拉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0134,
        (
            '#621F还在超市。\n',
            '我们正要去接她……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，不愧是小姐啊，\n',
            '对工作如此热心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E39(): pass

    label('loc_1E39')

    Jump('loc_1EF0')

    def _loc_1E3C(): pass

    label('loc_1E3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 1, 0x309)),
            Expr.Return,
        ),
        'loc_1E9C',
    )

    ChrTalk(
        0x00FE,
        (
            '市长刚刚去\n',
            '七耀教会做礼拜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有一个女佣与市长同行，\n',
            '你们就记住这个特征吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EF0')

    def _loc_1E9C(): pass

    label('loc_1E9C')

    ChrTalk(
        0x00FE,
        (
            '真是非常抱歉，\n',
            '市长现在不在官邸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果各位有什么事情的话，\n',
            '麻烦稍后再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EF0(): pass

    label('loc_1EF0')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x1EF4
@scena.Code('func_08_1EF4')
def func_08_1EF4():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F9A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '根据梅贝尔小姐所说的来看，\n',
            '定期船失踪很有可能是空贼团做的好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以赎金的数量来看，\n',
            '父亲多半还活着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样母亲也总算\n',
            '能够暂时安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FCD')

    def _loc_1F9A(): pass

    label('loc_1F9A')

    ChrTalk(
        0x00FE,
        (
            '你们是来调查\n',
            '这个事件的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜托你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FCD(): pass

    label('loc_1FCD')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0x1FD1
@scena.Code('func_09_1FD1')
def func_09_1FD1():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_2091',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2050',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '最近都是由\n',
            '莉拉来决定每天的食谱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '蔬菜不太够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '等会儿去超市买点回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_208E')

    def _loc_2050(): pass

    label('loc_2050')

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '蔬菜不太够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '等会儿去超市买点回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_208E(): pass

    label('loc_208E')

    Jump('loc_23BF')

    def _loc_2091(): pass

    label('loc_2091')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_210A',
    )

    ChrTalk(
        0x00FE,
        (
            '大小姐真的非常繁忙……\n',
            '如果能尽早将事件解决就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能够恢复平静，\n',
            '我就要约莉拉\n',
            '一起去外面购物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23BF')

    def _loc_210A(): pass

    label('loc_210A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_216A',
    )

    ChrTalk(
        0x00FE,
        (
            '快要到下午茶的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我虽然很笨，\n',
            '不过在泡茶技术这点上\n',
            '是不会输给莉拉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23BF')

    def _loc_216A(): pass

    label('loc_216A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_21C5',
    )

    ChrTalk(
        0x00FE,
        (
            '小姐不仅是个美人，\n',
            '还头脑聪明待人可亲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～简直就是我梦寐以求的类型㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23BF')

    def _loc_21C5(): pass

    label('loc_21C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 2, 0x30A)),
            Expr.Return,
        ),
        'loc_2364',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2227',
    )

    ChrTurnDirection(0x00FE, 0x0134, 0)

    ChrTalk(
        0x00FE,
        (
            '莉、莉拉……\n',
            '扫除马上就能做完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可没有\n',
            '偷懒去吃冰淇淋哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2361')

    def _loc_2227(): pass

    label('loc_2227')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    ChrTurnDirection(0x00FE, 0x0134, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，哎……莉拉！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(700)

    ChrTalk(
        0x00FE,
        (
            '这、这么早就回来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0134,
        (
            '#620F……事情还没有办完呢。\n',
            '我们正准备去超市接市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是、是这样啊。\n',
            '扫除马上就能做完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我可没有\n',
            '偷懒去吃冰淇淋哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F（莉拉小姐这么可怕吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（不知道……\n',
            '　不过应该是有着独特魄力的人吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2361(): pass

    label('loc_2361')

    Jump('loc_23BF')

    def _loc_2364(): pass

    label('loc_2364')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_23BF',
    )

    ChrTalk(
        0x00FE,
        (
            '如果不趁现在\n',
            '赶快打扫完毕的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(700)

    ChrTalk(
        0x00FE,
        (
            '又会被莉拉骂的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23BF(): pass

    label('loc_23BF')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x23C3
@scena.Code('func_0A_23C3')
def func_0A_23C3():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrSetPos(0x0101, 4000, 0, -5860, 0)
    ChrSetPos(0x0102, 3280, 0, -7224, 0)
    ChrSetPos(0x0103, 4570, 0, -6990, 0)
    ChrSetPos(0x000A, -1454, 500, 3536, 135)

    @scena.Lambda('lambda_2414')
    def lambda_2414():
        CameraMove(840, 500, 1500, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2414)

    Sleep(2500)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010020472V#004F哇啊啊～好豪华的房子啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020473V#001F快看快看，那个大吊灯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020020474V#017F不要兴奋过头了，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_24C8')
    def lambda_24C8():
        CameraMove(2860, 500, -380, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_24C8)

    @scena.Lambda('lambda_24E0')
    def lambda_24E0():
        ChrWalkTo(0x0101, 4790, 0, -3460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_24E0)

    Sleep(200)

    @scena.Lambda('lambda_2500')
    def lambda_2500():
        ChrWalkTo(0x0102, 3230, 0, -4000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_2500)

    Sleep(500)

    ChrWalkTo(0x0103, 4320, 0, -4350, 3000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0103,
        (
            '#0030020475V#020F看起来，\n',
            '这里就是柏斯市长的官邸了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020476V不知道市长在不在呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000A, 0x0008)
    OP_4A(0x000A, 0)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    OP_6F(0x0000, 30)
    Sleep(500)

    @scena.Lambda('lambda_25B9')
    def lambda_25B9():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_25B9')

    DispatchAsync2(0x0101, 0x0001, lambda_25B9)

    @scena.Lambda('lambda_25CA')
    def lambda_25CA():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_25CA')

    DispatchAsync2(0x0102, 0x0001, lambda_25CA)

    @scena.Lambda('lambda_25DB')
    def lambda_25DB():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_25DB')

    DispatchAsync2(0x0103, 0x0001, lambda_25DB)

    ChrWalkTo(0x000A, -610, 500, 1140, 2000, 0x00)
    ChrTurnDirection(0x000A, 0x0103, 400)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(500)

    OP_72(0x0000, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_70(0x0000, 0)
    Sleep(500)

    OP_71(0x0000, 0x0800)

    ChrTalk(
        0x000A,
        (
            '#1140020477V哎呀，是客人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_265B')
    def lambda_265B():
        CameraMove(3750, 250, -2570, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_265B)

    ChrWalkTo(0x000A, 3300, 500, -850, 3000, 0x00)
    ChrSetDirection(0x000A, 180, 400)

    ChrTalk(
        0x000A,
        (
            '#1140020478V欢迎光临。\n',
            '这里是柏斯市长官邸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1140020479V请问各位客人有何贵干呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020480V#020F我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020481V这次来访是想\n',
            '详细了解一下市长委托的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1140020482V原来如此，我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1140020483V可是，真的很不凑巧，\n',
            '市长刚好出去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1140020484V应该是在礼拜堂做礼拜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020485V#010F请问大概什么时候会回来呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1140020486V这个我也说不准……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1140020487V实际上，就算市长\n',
            '现在突然回来也完全不奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020488V#501F啊，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020489V那么我们到教会\n',
            '去找找市长怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1140020490V可、可是……\n',
            '要劳驾客人你们实在是不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020491V#000F别介意。\n',
            '这样对我们来说也省事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020492V说起来……\n',
            '市长是什么样子的呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020493V肯定是一幅有钱人的样子吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1140020494V说到外貌啊……唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1140020495V无论是言行还是气质，\n',
            '都越来越优秀、越来越优雅了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1140020496V要是能找到合适的另一半，\n',
            '我就可以放心地隐退了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020497V#004F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1140020498V啊！……失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1140020499V啊啊，对了，\n',
            '和市长同行的还有一位女佣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1140020500V这样找的话会比较方便些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020501V#010F带着女佣的人……\n',
            '这样就很容易分辨了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020502V#006F我们赶快去教会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0035, 0x01, 0x0008)
    OP_4B(0x000A, 0)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x2B53
@scena.Code('func_0B_2B53')
def func_0B_2B53():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-120000, 0, 67000, 0)
    ChrSetPos(0x0008, -120760, 200, 68570, 180)
    ChrSetPos(0x0101, -118370, 0, 64050, 0)
    ChrSetPos(0x0102, -117260, 0, 64450, 315)
    ChrSetPos(0x0103, -117990, 0, 62790, 0)
    OP_67(0, 6030, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(314000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0360021150V#612F市民的不满和意见的处理……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021151V由于柏斯上空飞行管制\n',
            '造成的市场商品进货推迟……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021152V#615F下水道设备的修理……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021153V给女王陛下的礼品的选定……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021154V安塞尔新街的魔兽作乱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0360021155V#616F不行了～什么时候\n',
            '才能把这些文书处理完啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021156V#008F请问……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetSubChip(0x0008, 1)
    CameraMove(-120700, 0, 68200, 1000)

    ChrTalk(
        0x0008,
        (
            '#0360021157V#613F哎、哎呀……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021158V#617F呵呵，各位。\n',
            '原来你们已经回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021159V#010F看来您正在忙于公务……\n',
            '不过我们可以占用一些时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360021160V#615F咳咳，当然可以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021161V#611F是从摩尔根将军那得到的消息吗？\n',
            '请赶快告诉我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-120570, 1000, 67100, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(314000, 0)
    OP_6E(280, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x0101, -120910, 0, 66260, 0)
    ChrSetPos(0x0102, -119750, 0, 66130, 0)
    ChrSetPos(0x0103, -120500, 0, 65129, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0360021162V#615F……真是辛苦你们了。\n',
            '大概的情况我已经了解了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021163V空贼团劫机，\n',
            '然后要求赎金对吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021164V#612F事态比我想象的要严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021165V#007F如果能隐瞒住游击士的身份，\n',
            '也许还能探听出其它的情报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360021166V#610F哪里，得到的并非坠机事故的消息，\n',
            '这就已经帮了我们很大的忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021167V接下来就是以柏斯市的立场\n',
            '来制定解决对策了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021168V要赶快向市民发表公告还有\n',
            '考虑应对乘客家属的措施才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021169V#010F真是繁忙啊……\n',
            '每天都要处理这么多的事务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360021170V#611F呵呵，那是市长的职责所在啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021171V#612F话说回来，\n',
            '既然知道了犯人的真实身份……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021172V能不能拜托你们\n',
            '继续调查并解决这个事件呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021173V#020F当然，我们也正有这个打算。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021174V况且我们和那个空贼团\n',
            '还有笔没算完的帐呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021175V我以游击士协会的荣誉担保，\n',
            '必定在王国军之前把这个事件解决！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021176V#006F嗯，说得对啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021177V还有老爸的事情，\n',
            '这次也一并解决掉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021178V#015F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010021179V#000F#1P嗯，怎么了？\n',
            '一脸严肃的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020021180V#013F#4P唔……\n',
            '尽管考虑了各种各样的情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021181V但不管怎么想，还是觉得不可思议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021182V#002F#1P不可思议？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021183V#012F#4P有父亲在，\n',
            '竟然也会被空贼得手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021184V以在洛连特出现的\n',
            '那伙人的实力来判断的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021185V#022F确实如你所说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021186V如果是对付那种程度的集团，\n',
            '以老师的实力还是游刃有余的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010021187V#007F#1P哎呀，真是的……\n',
            '约修亚和雪拉姐都把老爸想得太厉害了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021188V他的身手的确很棒，可是要和整个集团对抗，\n',
            '我觉得还是很够呛的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360021189V#613F………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021190V那个，稍稍打断一下可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_358F')
    def lambda_358F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_358F)

    @scena.Lambda('lambda_359D')
    def lambda_359D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_359D)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0360021191V#612F艾丝蒂尔你们的父亲\n',
            '也搭乘了那艘定期船吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021192V#008F啊，这个还没跟您说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021193V说起来真让人觉得不好意思。\n',
            '其实他也是一名游击士呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021194V他的名字叫卡西乌斯·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0360021195V#614F卡西乌斯·布莱特……\n',
            '刚才你说的就是他！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021196V#004F哎……嗯？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021197V难道您认识我老爸？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360021198V#612F虽然没有和他见过面，\n',
            '但是，他的大名我耳闻已久。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021199V原来……原来如此啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021200V这样的话，\n',
            '说不定可以借此和军队进行交涉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021201V#002F市长姐姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360021202V#615F……刚才真不好意思。\n',
            '各位的心情我可以理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021203V#610F只要能解决这个事件，\n',
            '无论要提供什么样的协助，我都在所不惜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360021204V有需要的时候，请各位不必\n',
            '多虑，尽管提出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x00400000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T1101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x38CD
@scena.Code('func_0C_38CD')
def func_0C_38CD():
    SetScenaFlags(ScenaFlag(0x0065, 3, 0x32B))
    OP_28(0x0037, 0x04, 0x02)
    OP_28(0x0037, 0x04, 0x04)
    OP_28(0x000F, 0x04, 0x40)
    OP_28(0x0010, 0x04, 0x40)
    OP_28(0x0012, 0x04, 0x40)
    OP_28(0x0017, 0x04, 0x40)
    EventBegin(0x00)
    CameraMove(-63360, 0, -3290, 0)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0103, 0x0004)
    ChrSetFlags(0x0104, 0x0004)
    ChrSetPos(0x0008, -64900, 200, -3990, 90)
    ChrSetPos(0x0101, -62760, 200, -5590, 0)
    ChrSetPos(0x0102, -60990, 200, -5640, 0)
    ChrSetPos(0x0103, -60990, 200, -2330, 180)
    ChrSetPos(0x0104, -62760, 200, -2330, 180)
    ChrSetChipByIndex(0x0008, 9)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetChipByIndex(0x0103, 7)
    ChrSetChipByIndex(0x0104, 8)
    ChrSetSubChip(0x0102, 1)
    ChrSetSubChip(0x0103, 2)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010030195V#007F没想到这家伙\n',
            '真的被释放出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030196V#027F好运来了挡也挡不住啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030197V#031F哈·哈·哈。\n',
            '你们就别这么夸奖人家嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0104, 2)
    Sleep(300)

    ChrTalk(
        0x0104,
        (
            '#0040030198V#030F可是，白白喝了那瓶酒，\n',
            '想起来还真的非常内疚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030199V按照之前的约定，\n',
            '我会为餐厅弹奏钢琴以作补偿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360030200V#610F呵呵，这就不用麻烦你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030201V因为那件事引起了不少的骚动，\n',
            '大家再见面也会很尴尬吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030202V#007F（唔，这家伙也真是的，\n',
            '　一点都不知道自己的过错……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030203V#019F（的确是脸皮超级厚啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360030204V#610F算了，其实这件事\n',
            '也不能完全算作不幸的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030205V#033F可是……\n',
            '我真的感到有点内疚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030206V嗯，对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030207V#030F你们不是正在\n',
            '调查一桩什么案件吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030208V作为那瓶酒的谢礼，\n',
            '我愿意协助你们的调查工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030209V#004F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360030210V#611F这样啊，听起来挺有趣的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030211V可是会不会麻烦你呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030212V#030F没问题，就包在我身上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0104, 0)
    Sleep(300)

    ChrTalk(
        0x0104,
        (
            '#0040030213V#031F就这样定了。\n',
            '你们以后要多多关照哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030214V#009F先等一下……\n',
            '谁叫你就这样定了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030215V#020F如果要一个门外汉跟着我们，\n',
            '老实说也很不方便……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030216V你有自信不会拖我们的后腿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0104, 1)
    Sleep(300)

    ChrTalk(
        0x0104,
        (
            '#0040030217V#035F#1P我对自己的枪法和魔法颇有自信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030218V要知道，天才可不单会演奏，\n',
            '就连其他技能也都不在话下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030219V#007F听了你这一段台词之后，\n',
            '我越来越感到强烈的不安了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030220V#010F多一个人帮忙也无妨啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030221V毕竟无法指望军队做些什么，\n',
            '而我们又处于人手不足的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030222V#026F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030223V#020F算了。\n',
            '就让你协助我们的工作吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030224V不过事先声明，你要是碍手碍脚的话，\n',
            '我可会毫不客气地请你离队哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030225V明白了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030226V#031F呵呵，没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030227V我绝对不会让大家失望的，\n',
            '敬请期待天才演奏家的精彩演出吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030228V#008F嗯，我们不会失望的，\n',
            '因为从一开始就没对你抱有期望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360030229V#615F呵呵……\n',
            '闲话就先到此为止吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030230V#612F因为我还有\n',
            '一件重要的事情要告诉大家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x0104, 0)
    Sleep(100)

    ChrSetSubChip(0x0104, 2)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010030231V#501F重要的事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030232V#020F说起来，在我们来之前，\n',
            '街上好像发生了什么骚动吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030233V究竟是什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360030234V#612F我要说的就是这件事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030235V其实昨天晚上，柏斯南街区发生了\n',
            '多起大规模的强盗事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030236V以武器店和导力器工房为首的\n',
            '多家商店都遭到了抢劫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030237V#004F啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030238V#012F难道说……\n',
            '这也是空贼做的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360030239V#612F目前还不清楚是何人所为，\n',
            '不过空贼的嫌疑最大。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030240V现在，王国军的部队正在对\n',
            '这些连环案件进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030241V#022F原来如此。\n',
            '看来我们也要马上展开调查才行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360030242V#610F嗯，拜托大家了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030243V至于之前的调查费用\n',
            '我已经预先向协会支付了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030244V作为日常的开支，希望\n',
            '你们能够好好利用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0035, 0x04, 0x10)
    OP_28(0x0036, 0x04, 0x10)
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    ChrSetPos(0x0101, 3450, 0, -5820, 0)
    ChrSetPos(0x0102, 4730, 0, -4890, 315)
    ChrSetPos(0x0103, 2900, 0, -4059, 135)
    ChrSetPos(0x0104, 4170, 0, -3340, 180)
    ChrSetPos(0x000A, -6290, 500, -8460, 296)
    ChrSetPos(0x0008, -120760, 0, 68570, 180)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0102, 0x0004)
    ChrClearFlags(0x0103, 0x0004)
    ChrClearFlags(0x0104, 0x0004)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x0103, 0)
    ChrSetSubChip(0x0104, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x0104, 65535)
    ChrTurnDirection(0x0101, 0x0104, 0)
    ChrTurnDirection(0x0102, 0x0103, 0)
    ChrTurnDirection(0x0103, 0x0102, 0)
    ChrTurnDirection(0x0104, 0x0101, 0)
    CameraMove(2900, 0, -3860, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010030245V#006F#3P虽然我觉得\n',
            '军队那些人还会来搅局……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030246V算了，到时候再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030247V#012F#4P先不说他们会不会来搅局……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030248V我觉得即使我们掌握了什么情报，\n',
            '也最好不要告诉军队。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030249V要是军队真的有间谍的话，\n',
            '那么肯定会泄漏给空贼知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030250V#020F#1P只有这样做了，虽然不是我们的本意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030251V总之，谨慎行动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030252V#035F#2P呵呵，那么诸位，\n',
            '马上前往南街区看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030253V#005F#3P我～知～道！\n',
            '为什么要听你发号施令啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
