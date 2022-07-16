import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0132_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0132   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '伟诺'),
    TXT(0x02, '穿制服的少女'),
    TXT(0x03, '西加罗'),
    TXT(0x04, '艾德尔'),
    TXT(0x05, '目标用摄像机'),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0132.x'
    header.mapIndex       = 8
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1705
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00001770,
            dword_04        = 0x00000000,
            dword_08        = 0x0002CEC0,
            word_0C         = 0x0004,
            word_0E         = 0x010E,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 8,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00001F40,
            dword_04        = 0x00000000,
            dword_08        = 0x0002C308,
            word_0C         = 0x0004,
            word_0E         = 0x010E,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
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

# id: 0x10001 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH02330._CH', 'ED6_DT07/CH02330P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
    ]

# id: 0x10002 offset: 0x10E
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 4500,
            z                   = 0,
            y                   = 190662,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -88400,
            z                   = 0,
            y                   = 155930,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -48500,
            z                   = 0,
            y                   = 155890,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -44250,
            z                   = 0,
            y                   = 152480,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1AE
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1AE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1AE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 6598,
            triggerZ            = 0,
            triggerY            = 190158,
            triggerRange        = 1000,
            actorX              = 4500,
            actorZ              = 1500,
            actorY              = 190662,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3130,
            triggerZ            = 0,
            triggerY            = 192000,
            triggerRange        = 800,
            actorX              = 3130,
            actorZ              = 1000,
            actorY              = 192000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1F6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_20A',
    )

    ClearChrFlags(0x0009, 0x0080)

    Jump('loc_21B')

    def _loc_20A(): pass

    label('loc_20A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_21B',
    )

    ClearChrFlags(0x0009, 0x0080)

    def _loc_21B(): pass

    label('loc_21B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_225',
    )

    Jump('loc_24A')

    def _loc_225(): pass

    label('loc_225')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_239',
    )

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)

    Jump('loc_24A')

    def _loc_239(): pass

    label('loc_239')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_24A',
    )

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)

    def _loc_24A(): pass

    label('loc_24A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_256',
    )

    ClearChrFlags(0x0009, 0x0010)

    def _loc_256(): pass

    label('loc_256')

    Return()

# id: 0x0001 offset: 0x257
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26F',
    )

    OP_B1('t0132_y')

    Jump('loc_278')

    def _loc_26F(): pass

    label('loc_26F')

    OP_B1('t0132_n')

    def _loc_278(): pass

    label('loc_278')

    StopEffect(0x80, 0x00)
    StopEffect(0x81, 0x00)
    StopEffect(0x82, 0x00)

    Return()

# id: 0x0002 offset: 0x282
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_297',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_297(): pass

    label('loc_297')

    Return()

# id: 0x0003 offset: 0x298
@scena.Code('func_03_298')
def func_03_298():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2BB',
    )

    OP_8D(0x00FE, -86000, 151900, -82840, 154200, 3000)

    Jump('func_03_298')

    def _loc_2BB(): pass

    label('loc_2BB')

    Return()

# id: 0x0004 offset: 0x2BC
@scena.Code('func_04_2BC')
def func_04_2BC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2DF',
    )

    OP_8D(0x00FE, -46100, 153900, -42900, 151500, 3000)

    Jump('func_04_2BC')

    def _loc_2DF(): pass

    label('loc_2DF')

    Return()

# id: 0x0005 offset: 0x2E0
@scena.Code('func_05_2E0')
def func_05_2E0():
    SetMapFlags(0x00000080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_328',
    )

    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_32E')

    def _loc_328(): pass

    label('loc_328')

    StopEffect(0x80, 0x02)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_32E(): pass

    label('loc_32E')

    ClearMapFlags(0x00000080)

    Return()

# id: 0x0006 offset: 0x334
@scena.Code('func_06_334')
def func_06_334():
    SetMapFlags(0x00000080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37C',
    )

    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_382')

    def _loc_37C(): pass

    label('loc_37C')

    StopEffect(0x81, 0x02)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_382(): pass

    label('loc_382')

    ClearMapFlags(0x00000080)

    Return()

# id: 0x0007 offset: 0x388
@scena.Code('func_07_388')
def func_07_388():
    SetMapFlags(0x00000080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D0',
    )

    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_3D6')

    def _loc_3D0(): pass

    label('loc_3D0')

    StopEffect(0x82, 0x02)
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_3D6(): pass

    label('loc_3D6')

    ClearMapFlags(0x00000080)

    Return()

# id: 0x0008 offset: 0x3DC
@scena.Code('func_08_3DC')
def func_08_3DC():
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0x3E1
@scena.Code('func_09_3E1')
def func_09_3E1():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 1, 0x229)),
            Expr.Return,
        ),
        'loc_455',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '休息\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_444',
    )

    OP_0D()
    OP_A9(0x03)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_444(): pass

    label('loc_444')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_455',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_455(): pass

    label('loc_455')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_5DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_578',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '咦……\n',
            '这副装束……难道你们要去旅行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可是，\n',
            '定期船已经停止航运了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，\n',
            '其实我们打算走路到柏斯去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我们有一些事情要到那里去调查。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哦哦，难道说\n',
            '你们有什么紧要的工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊，不好意思多问了。\n',
            '不管怎样，请你们路上多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DA')

    def _loc_578(): pass

    label('loc_578')

    ChrTalk(
        0x0008,
        (
            '今天早上就已经有几位乘客\n',
            '步行向着柏斯方向走去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '定期船停航之后，\n',
            '的确引来诸多的不便啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5DA(): pass

    label('loc_5DA')

    Jump('loc_1100')

    def _loc_5DD(): pass

    label('loc_5DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_802',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 2, 0x262)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7A1',
    )

    EventBegin(0x00)
    OP_69(0x0008, 1000)

    ChrTalk(
        0x0008,
        (
            '#1000011137V艾丝蒂尔、约修亚。\n',
            '啊，连雪拉扎德也来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1000011138V发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011139V#002F伟诺叔叔，你认识乔丝特吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011140V#002F就是住在你们这里的\n',
            '那个王立学院女学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1000011141V当然认识啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1000011142V不过她……\n',
            '刚才已经结账离开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011143V#022F啊，来迟一步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011144V#012F去飞艇坪看看吧，\n',
            '说不定还来得及。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011145V#007F唔～\n',
            '我怎么看不出来她是个坏孩子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1000011146V？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x004C, 2, 0x262))
    OP_28(0x001B, 0x01, 0x0004)
    OP_28(0x001B, 0x01, 0x0008)
    EventEnd(0x01)

    Jump('loc_7FF')

    def _loc_7A1(): pass

    label('loc_7A1')

    ChrTalk(
        0x0008,
        (
            '乔丝特小姐在刚才\n',
            '已经办理退房手续了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '也许是我心里作用，\n',
            '看她样子好像要急着回去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7FF(): pass

    label('loc_7FF')

    Jump('loc_1100')

    def _loc_802(): pass

    label('loc_802')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_8ED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_895',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔、约修亚。\n',
            '我听说了你们在农场和矿山有活跃的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '连客人中也有人\n',
            '想打听你们俩的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今后也要努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8EA')

    def _loc_895(): pass

    label('loc_895')

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔、约修亚。\n',
            '我听说了你们在农场和矿山有活跃的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今后也要努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8EA(): pass

    label('loc_8EA')

    Jump('loc_1100')

    def _loc_8ED(): pass

    label('loc_8ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Return,
        ),
        'loc_960',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Return,
        ),
        'loc_937',
    )

    ChrTalk(
        0x0008,
        (
            '看来你们\n',
            '顺利找到那些记者了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要努力工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_95D')

    def _loc_937(): pass

    label('loc_937')

    ChrTalk(
        0x0008,
        (
            '怎么了？\n',
            '你们找到\n',
            '那些记者了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_95D(): pass

    label('loc_95D')

    Jump('loc_1100')

    def _loc_960(): pass

    label('loc_960')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 0, 0x250)),
            Expr.Return,
        ),
        'loc_BBE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 1, 0x251)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B7A',
    )

    EventBegin(0x00)
    OP_69(0x0008, 1000)
    SetScenaFlags(ScenaFlag(0x004A, 1, 0x251))
    OP_28(0x0019, 0x01, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010010424V#000F伟诺叔叔。\n',
            '我想问一件事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010425V#000F杂志社的那两个记者\n',
            '是住在这里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1000010426V哦，你竟然知道这个啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1000010427V有什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010428V#010F其实是协会委派的工作，\n',
            '我们是为协助他们取材而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1000010429V哦，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1000010430V不过现在……\n',
            '那两个人都出去了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010431V#004F这样啊。\n',
            '那你知道他们去了哪里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1000010432V那位记者的话，\n',
            '好像说过要去酒馆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1000010433V你们就去那里看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010434V#001F酒馆是吗，谢谢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010435V#010F那我们先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_BBB')

    def _loc_B7A(): pass

    label('loc_B7A')

    ChrTalk(
        0x0008,
        (
            '那位记者的话，\n',
            '好像说过要去酒馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你们就去那里看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BBB(): pass

    label('loc_BBB')

    Jump('loc_1100')

    def _loc_BBE(): pass

    label('loc_BBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_C1E',
    )

    ChrTalk(
        0x0008,
        (
            '今天有两位王都的记者\n',
            '在本旅馆预定了房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看看时间，\n',
            '他们差不多该到了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1100')

    def _loc_C1E(): pass

    label('loc_C1E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_C94',
    )

    ChrTalk(
        0x0008,
        (
            '本旅馆时常\n',
            '会有各地的游击士\n',
            '来这里下榻住宿的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '常常会有所属于\n',
            '其它支部的游击士\n',
            '被派遣到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1100')

    def _loc_C94(): pass

    label('loc_C94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_D35',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CFD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '前台工作\n',
            '总算告一段落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '定期船起飞和到达前后\n',
            '出入的客人果然是最多的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D32')

    def _loc_CFD(): pass

    label('loc_CFD')

    ChrTalk(
        0x0008,
        (
            '定期船起飞和到达前后\n',
            '出入的客人果然是最多的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D32(): pass

    label('loc_D32')

    Jump('loc_1100')

    def _loc_D35(): pass

    label('loc_D35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_E2F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DDB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔，我听说了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你们终于成为游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我从心底祝福你们，\n',
            '希望你们将来能够大展身手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F……嗯，非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E2C')

    def _loc_DDB(): pass

    label('loc_DDB')

    ChrTalk(
        0x0008,
        (
            '你们终于成为游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我从心底祝福你们，\n',
            '希望你们将来能够大展身手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E2C(): pass

    label('loc_E2C')

    Jump('loc_1100')

    def _loc_E2F(): pass

    label('loc_E2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_F17',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EC8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '刚才有一位\n',
            '稀罕的客人来住宿哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '怎么看都是\n',
            '杰尼丝王立学院的学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好像是为了学习，\n',
            '专门来洛连特\n',
            '做什么调查研究的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F14')

    def _loc_EC8(): pass

    label('loc_EC8')

    ChrTalk(
        0x0008,
        (
            '刚才有一位\n',
            '稀罕的客人来住宿哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '怎么看都是\n',
            '杰尼丝王立学院的学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F14(): pass

    label('loc_F14')

    Jump('loc_1100')

    def _loc_F17(): pass

    label('loc_F17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 1, 0x229)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1085',
    )

    ChrTalk(
        0x0008,
        (
            '欢迎光临。\n',
            '这里是洛连特旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '两位是来住宿的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F啊？那个……！？\n',
            '伟诺叔叔，是我们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0008,
        (
            '哈哈，我知道。\n',
            '开玩笑的，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '刚才那个只是练习问好而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(700)

    ChrTalk(
        0x0101,
        (
            '#008F是、是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#007F（伟诺叔叔还真是喜欢\n',
            '　一本正经地开玩笑啊。）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（……喜欢开玩笑也\n',
            '　不算什么坏习惯嘛。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1100')

    def _loc_1085(): pass

    label('loc_1085')

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔游击士测试合格之后，\n',
            '就会成为继雪拉扎德小姐之后\n',
            '洛连特的第二位女性游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '约修亚，\n',
            '你也要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1100(): pass

    label('loc_1100')

    SetScenaFlags(ScenaFlag(0x0045, 1, 0x229))
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

# id: 0x000A offset: 0x1109
@scena.Code('func_0A_1109')
def func_0A_1109():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_11F6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_119F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    NpcTalk(
        0x0009,
        '乔丝特',
        (
            '#0090010438V#217F啊，艾丝蒂尔，\n',
            '还有约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010439V你们是来\n',
            '找我玩的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010440V不介意的话，\n',
            '我给你们泡杯红茶吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11F3')

    def _loc_119F(): pass

    label('loc_119F')

    NpcTalk(
        0x0009,
        '乔丝特',
        (
            '#0090010441V#217F啊，艾丝蒂尔，\n',
            '还有约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010442V你们是来\n',
            '找我玩的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11F3(): pass

    label('loc_11F3')

    Jump('loc_1389')

    def _loc_11F6(): pass

    label('loc_11F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1233',
    )

    ChrTalk(
        0x0009,
        (
            '#217F我应该在教会。\n',
            '看到这句台词就表示有BUG。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1389')

    def _loc_1233(): pass

    label('loc_1233')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_1269',
    )

    ChrTalk(
        0x0009,
        (
            '#0090010447V好了，\n',
            '得去跟市长做个预约了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1389')

    def _loc_1269(): pass

    label('loc_1269')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_12D9',
    )

    ChrTalk(
        0x0009,
        (
            '#0090010445V市长官邸在城镇东面……\n',
            '游击士协会在钟楼的南面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010446V城镇的地理位置\n',
            '我基本上弄清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1389')

    def _loc_12D9(): pass

    label('loc_12D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1331',
    )

    ChrTalk(
        0x0009,
        (
            '#0090010443V呼……\n',
            '终于抵达洛连特了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010444V那么，\n',
            '首先要到处逛逛才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1389')

    def _loc_1331(): pass

    label('loc_1331')

    ChrTalk(
        0x0009,
        (
            '#217F我在这个时候\n',
            '应该还没有到达洛连特这里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#217F所以……\n',
            '请装作没看见我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1389(): pass

    label('loc_1389')

    TalkEnd(0x0009)

    Return()

# id: 0x000B offset: 0x138D
@scena.Code('func_0B_138D')
def func_0B_138D():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_13F7',
    )

    ChrTalk(
        0x00FE,
        (
            '我们准备乘坐\n',
            '下一班的定期船去柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近柏斯好像\n',
            '发生了不少事件，\n',
            '有些不放心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1456')

    def _loc_13F7(): pass

    label('loc_13F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1456',
    )

    ChrTalk(
        0x00FE,
        (
            '本来只是为了巡礼才来的，\n',
            '没想到洛连特还真是个\n',
            '地灵人杰的好地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我很喜欢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1456(): pass

    label('loc_1456')

    TalkEnd(0x000A)

    Return()

# id: 0x000C offset: 0x145A
@scena.Code('func_0C_145A')
def func_0C_145A():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1593',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1553',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '接下来终于要去柏斯地区了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起柏斯的话，\n',
            '果然还是柏斯超市最吸引我啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说店里摆满了各种\n',
            '来自帝国的稀奇物品呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了这一天我一直在筹私房钱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '准备充足，干劲充足，\n',
            '钱包充～足！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '向柏斯超市出击！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1590')

    def _loc_1553(): pass

    label('loc_1553')

    ChrTalk(
        0x00FE,
        (
            '准备充足，干劲充足，\n',
            '钱包充～足！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '向柏斯超市出击！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1590(): pass

    label('loc_1590')

    Jump('loc_1677')

    def _loc_1593(): pass

    label('loc_1593')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1677',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1625',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，\n',
            '这旅馆比想象中的要好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '主管的服务很周到，\n',
            '而且又安静又整洁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和王都的高级酒店相比\n',
            '一点都不逊色呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1677')

    def _loc_1625(): pass

    label('loc_1625')

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，\n',
            '这旅馆比想象中的要好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和王都的高级酒店相比\n',
            '一点都不逊色呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1677(): pass

    label('loc_1677')

    TalkEnd(0x000B)

    Return()

# id: 0x000D offset: 0x167B
@scena.Code('func_0D_167B')
def func_0D_167B():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　　　　洗衣房　　　　　　　\n',
            '※工作人员以外禁止进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
