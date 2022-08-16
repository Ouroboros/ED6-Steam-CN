import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2310_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2310   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2310.x'
    header.mapIndex       = 1
    header.bgm            = 15
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
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '克拉姆',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '波利',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛丽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '达尼艾尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卢西亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '扎古',
            x                   = 4440,
            z                   = 0,
            y                   = 5030,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '阿梅莉娅',
            x                   = -130,
            z                   = 0,
            y                   = 8460,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '索雷诺',
            x                   = -32750,
            z                   = 0,
            y                   = 3570,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '塞尔吉村长',
            x                   = -28110,
            z                   = 0,
            y                   = 7510,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '目标用照相机',
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

# id: 0x10002 offset: 0x232
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x232
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x232
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x232
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_25E',
    )

    ChrSetDirection(0x000E, 0, 0)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetPos(0x0010, -30060, 0, 3800, 270)

    Jump('loc_299')

    def _loc_25E(): pass

    label('loc_25E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_268',
    )

    Jump('loc_299')

    def _loc_268(): pass

    label('loc_268')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_283',
    )

    ChrSetPos(0x0010, -27680, 0, 40800, 270)

    Jump('loc_299')

    def _loc_283(): pass

    label('loc_283')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_28D',
    )

    Jump('loc_299')

    def _loc_28D(): pass

    label('loc_28D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_299',
    )

    ChrSetFlags(0x0010, 0x0080)

    def _loc_299(): pass

    label('loc_299')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2AC',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_07_20E4)

    def _loc_2AC(): pass

    label('loc_2AC')

    Return()

# id: 0x0001 offset: 0x2AD
@scena.Code('func_01_2AD')
def func_01_2AD():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_2BC',
    )

    OP_71(0x0000, 0x0004)
    StopEffect(0x82, 0x00)

    def _loc_2BC(): pass

    label('loc_2BC')

    Return()

# id: 0x0002 offset: 0x2BD
@scena.Code('func_02_2BD')
def func_02_2BD():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E2',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_424')

    def _loc_2E2(): pass

    label('loc_2E2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FB',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_424')

    def _loc_2FB(): pass

    label('loc_2FB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_314',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_424')

    def _loc_314(): pass

    label('loc_314')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32D',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_424')

    def _loc_32D(): pass

    label('loc_32D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_346',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_424')

    def _loc_346(): pass

    label('loc_346')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35F',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_424')

    def _loc_35F(): pass

    label('loc_35F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_378',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_424')

    def _loc_378(): pass

    label('loc_378')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_391',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_424')

    def _loc_391(): pass

    label('loc_391')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AA',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_424')

    def _loc_3AA(): pass

    label('loc_3AA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C3',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_424')

    def _loc_3C3(): pass

    label('loc_3C3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DC',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_424')

    def _loc_3DC(): pass

    label('loc_3DC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F5',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_424')

    def _loc_3F5(): pass

    label('loc_3F5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40E',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_424')

    def _loc_40E(): pass

    label('loc_40E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_424',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_424(): pass

    label('loc_424')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_439',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_424')

    def _loc_439(): pass

    label('loc_439')

    Return()

# id: 0x0003 offset: 0x43A
@scena.Code('func_03_43A')
def func_03_43A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_73A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 5, 0x122D)),
            Expr.Return,
        ),
        'loc_51C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4A9',
    )

    ChrTalk(
        0x00FE,
        (
            '灯塔看守弗科特爷爷\n',
            '最近好像都没看见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爷爷也一把年纪了，\n',
            '偶尔去看看他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_519')

    def _loc_4A9(): pass

    label('loc_4A9')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '这么说来，灯塔看守\n',
            '弗科特爷爷还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近\n',
            '好像都没看见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他也一把年纪了，\n',
            '偶尔去看看他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_519(): pass

    label('loc_519')

    Jump('loc_737')

    def _loc_51C(): pass

    label('loc_51C')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    SetScenaFlags(ScenaFlag(0x0245, 5, 0x122D))
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哦，还以为是谁呢，\n',
            '是那时的游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去过孤儿院了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，看过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '变得和原来一模一样\n',
            '真是吃了一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帮过忙的我们\n',
            '也很得意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孩子们的笑容也回来了，\n',
            '感觉总算解决了一件大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过…\n',
            '发生什么事件了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_685',
    )

    ChrTalk(
        0x0106,
        (
            '#050F啊啊，是有点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '姑且算是解决了，\n',
            '可以放心啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6BD')

    def _loc_685(): pass

    label('loc_685')

    ChrTalk(
        0x0103,
        (
            '#020F嗯嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '姑且算是解决了，\n',
            '可以放心了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6BD(): pass

    label('loc_6BD')

    ChrTurnDirection(0x00FE, 0x00F7, 400)

    ChrTalk(
        0x00FE,
        (
            '呼，那就好。\n',
            '平安无事最重要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '那么再见，游击士们。\n',
            '今后也要继续加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_737(): pass

    label('loc_737')

    Jump('loc_142C')

    def _loc_73A(): pass

    label('loc_73A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_A7B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 5, 0x122D)),
            Expr.Return,
        ),
        'loc_847',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7C0',
    )

    ChrTalk(
        0x00FE,
        (
            '下任市长一定要\n',
            '选个心灵纯净的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过上次大家\n',
            '也一定都是这么想着投票的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，政治真复杂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_844')

    def _loc_7C0(): pass

    label('loc_7C0')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '那个恶德市长被捕之后\n',
            '已经过了相当长的时间',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以的话下任市长\n',
            '选个心灵纯净的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上次大家也都是这么想着\n',
            '投票的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_844(): pass

    label('loc_844')

    Jump('loc_A78')

    def _loc_847(): pass

    label('loc_847')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    SetScenaFlags(ScenaFlag(0x0245, 5, 0x122D))
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哦，还以为是谁呢，\n',
            '是那时的游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看过孤儿院了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，看过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '变得和原来一模一样\n',
            '真是吃了一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帮过忙的我们\n',
            '也很得意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孩子们的笑容也回来了，\n',
            '感觉总算解决了一件大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过…\n',
            '发生什么事件了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_9BA',
    )

    ChrTalk(
        0x0106,
        (
            '#050F不，只是有些事\n',
            '以防万一要调查一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不是事件，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9FE')

    def _loc_9BA(): pass

    label('loc_9BA')

    ChrTalk(
        0x0103,
        (
            '#020F是有些事要调查，\n',
            '不过事件性比较低。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不用担心，没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9FE(): pass

    label('loc_9FE')

    ChrTurnDirection(0x00FE, 0x00F7, 400)

    ChrTalk(
        0x00FE,
        (
            '呼，那就好。\n',
            '平安无事最重要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么再见，游击士们。\n',
            '今后也要继续加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_A78(): pass

    label('loc_A78')

    Jump('loc_142C')

    def _loc_A7B(): pass

    label('loc_A7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_D8C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 5, 0x122D)),
            Expr.Return,
        ),
        'loc_B58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AFC',
    )

    ChrTalk(
        0x00FE,
        (
            '我叔叔奥维德\n',
            '是处理食材的商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总是到处转悠，\n',
            '很少回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样的生活\n',
            '对于我来说太困难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B55')

    def _loc_AFC(): pass

    label('loc_AFC')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '平安无事虽好，\n',
            '但我也得早点找工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然想在本地工作，\n',
            '但很难找到好的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B55(): pass

    label('loc_B55')

    Jump('loc_D89')

    def _loc_B58(): pass

    label('loc_B58')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    SetScenaFlags(ScenaFlag(0x0245, 5, 0x122D))
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哦，还以为是谁呢，\n',
            '是那时的游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看过孤儿院了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F啊，看过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '变得和原来一模一样\n',
            '真是吃了一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帮过忙的我们\n',
            '也很得意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孩子们的笑容也回来了，\n',
            '感觉总算解决了一件大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过…\n',
            '发生什么事件了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_CCB',
    )

    ChrTalk(
        0x0106,
        (
            '#050F不，只是有些事\n',
            '以防万一要调查一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不是事件，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D0F')

    def _loc_CCB(): pass

    label('loc_CCB')

    ChrTalk(
        0x0103,
        (
            '#020F是有些事要调查，\n',
            '不过事件性比较低。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不用担心，没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D0F(): pass

    label('loc_D0F')

    ChrTurnDirection(0x00FE, 0x00F7, 400)

    ChrTalk(
        0x00FE,
        (
            '呼，那就好。\n',
            '平安无事最重要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '那么再见，游击士们。\n',
            '今后也要继续加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_D89(): pass

    label('loc_D89')

    Jump('loc_142C')

    def _loc_D8C(): pass

    label('loc_D8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 6, 0x1216)),
            Expr.Return,
        ),
        'loc_11B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 5, 0x122D)),
            Expr.Return,
        ),
        'loc_DE5',
    )

    ChrTalk(
        0x00FE,
        (
            '主日学校在村子南边的\n',
            '风车小屋上呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该快结束了\n',
            '去看看如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11B3')

    def _loc_DE5(): pass

    label('loc_DE5')

    SetScenaFlags(ScenaFlag(0x0245, 5, 0x122D))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_FD9',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哦，还以为是谁呢，\n',
            '是那时的游击士们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看过孤儿院了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F啊啊，刚刚\n',
            '从那边过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F变得和以前一样\n',
            '真是吃了一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帮过忙的我们\n',
            '也很得意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孩子们的笑容也回来了，\n',
            '这下总算解决一件大事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F啊，孩子们\n',
            '来上主日学校了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，在村子南边的\n',
            '风车小屋上呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该快结束了\n',
            '去看看如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F南边的风车小屋啊……\n',
            '好，去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F那么，回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，今后\n',
            '要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11B3')

    def _loc_FD9(): pass

    label('loc_FD9')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哦，还以为是谁呢，\n',
            '是那时的游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看过孤儿院了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，刚好\n',
            '从那边过来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '完全恢复了原样\n',
            '真是吃了一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帮过忙的我们\n',
            '也很得意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孩子们的笑容也回来了，\n',
            '这下总算解决一件大事了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F啊，孩子们\n',
            '来上主日学校了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，在村子南边的\n',
            '风车小屋上呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该快结束了\n',
            '去看看如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F南边的风车小屋啊。\n',
            '马上去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F那么，回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，今后\n',
            '要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11B3(): pass

    label('loc_11B3')

    Jump('loc_142C')

    def _loc_11B6(): pass

    label('loc_11B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_142C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 5, 0x122D)),
            Expr.Return,
        ),
        'loc_120D',
    )

    ChrTalk(
        0x00FE,
        (
            '承蒙你们游击士\n',
            '诸多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有空再来哦。\n',
            '我随时都热烈欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_142C')

    def _loc_120D(): pass

    label('loc_120D')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    SetScenaFlags(ScenaFlag(0x0245, 5, 0x122D))
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哦，还以为是谁呢，\n',
            '是那时的游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看过孤儿院了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F啊，正打算去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '正好有些事\n',
            '要调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道…\n',
            '是什么事件吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_130A',
    )

    ChrTalk(
        0x0106,
        (
            '#050F不，只是有些事\n',
            '以防万一要调查一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不是事件，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134A')

    def _loc_130A(): pass

    label('loc_130A')

    ChrTalk(
        0x0103,
        (
            '#020F是要去调查，\n',
            '不过事件性比较低。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不用担心，没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_134A(): pass

    label('loc_134A')

    ChrTurnDirection(0x00FE, 0x00F7, 400)

    ChrTalk(
        0x00FE,
        (
            '呼，是吗。\n',
            '不是事件就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '不着急的话\n',
            '稍微在村子里休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们的话\n',
            '我随时都热烈欢迎哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F嗯……不过现在\n',
            '还是要去孤儿院才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，再来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_142C(): pass

    label('loc_142C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x1430
@scena.Code('func_04_1430')
def func_04_1430():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1512',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14BF',
    )

    ChrTalk(
        0x00FE,
        (
            '用暖炉做料理\n',
            '真是好久没试过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在正和珂蕾妲婆婆\n',
            '学习简单的烹饪法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老人的智囊\n',
            '这时候真是靠得住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_150F')

    def _loc_14BF(): pass

    label('loc_14BF')

    ChrTalk(
        0x00FE,
        (
            '现在正和珂蕾妲婆婆\n',
            '学习简单的烹饪法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用暖炉做料理\n',
            '真是好久没试过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_150F(): pass

    label('loc_150F')

    Jump('loc_1912')

    def _loc_1512(): pass

    label('loc_1512')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_160F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15BE',
    )

    ChrTalk(
        0x00FE,
        (
            '警备艇被迫降落，\n',
            '导力器停止还真是不妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '慎重起见，弟弟扎古\n',
            '去看灯塔的情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里只有灯塔看守弗科特老人\n',
            '一个人在，实在是令人不放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_160C')

    def _loc_15BE(): pass

    label('loc_15BE')

    ChrTalk(
        0x00FE,
        (
            '慎重起见，弟弟扎古\n',
            '去看灯塔的情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候那孩子\n',
            '还真是可靠呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_160C(): pass

    label('loc_160C')

    Jump('loc_1912')

    def _loc_160F(): pass

    label('loc_160F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_16E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_167C',
    )

    ChrTalk(
        0x00FE,
        (
            '弟弟好像想做\n',
            '对本地有所贡献的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能找到那种工作，\n',
            '那孩子应该能耐心去做吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16E4')

    def _loc_167C(): pass

    label('loc_167C')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '弟弟好像想做\n',
            '对本地有所贡献的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孤儿院重建的时候\n',
            '也亲自去帮忙，\n',
            '这份心意我也很赞同呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16E4(): pass

    label('loc_16E4')

    Jump('loc_1912')

    def _loc_16E7(): pass

    label('loc_16E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_17E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1755',
    )

    ChrTalk(
        0x00FE,
        (
            '弟弟似乎对这次的市长选举\n',
            '很关心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想知道的\n',
            '不是卢安的未来\n',
            '而是扎古你的未来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17DE')

    def _loc_1755(): pass

    label('loc_1755')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '弟弟似乎对这次的市长选举\n',
            '很关心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想知道的\n',
            '不是卢安的未来\n',
            '而是扎古你的未来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '投票给谁都无所谓，\n',
            '早点去找工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17DE(): pass

    label('loc_17DE')

    Jump('loc_1912')

    def _loc_17E1(): pass

    label('loc_17E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_18AA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1834',
    )

    ChrTalk(
        0x00FE,
        (
            '叔叔怎么\n',
            '那么鲁莽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '弟弟扎古\n',
            '也有点像他，真令人担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18A7')

    def _loc_1834(): pass

    label('loc_1834')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '做食材商人的\n',
            '奥维德叔叔\n',
            '难得回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '却又说要去\n',
            '找新食材了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易留下他，\n',
            '怎么这样鲁莽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18A7(): pass

    label('loc_18A7')

    Jump('loc_1912')

    def _loc_18AA(): pass

    label('loc_18AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1912',
    )

    ChrTalk(
        0x00FE,
        (
            '孤儿院的孩子们\n',
            '似乎也完全恢复精神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在主日学校上课的日子，\n',
            '笑声乘着风\n',
            '在这里回响呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1912(): pass

    label('loc_1912')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x1916
@scena.Code('func_05_1916')
def func_05_1916():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_19EE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_197A',
    )

    ChrTalk(
        0x00FE,
        (
            '旅游业的推进，\n',
            '还是海运业……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '父亲说的对，\n',
            '这可不能用普通的方法解决。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19EB')

    def _loc_197A(): pass

    label('loc_197A')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '旅游业的推进，\n',
            '还是海运业的维持……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '实际的行政\n',
            '可没有黑白分明这么简单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯，这是父亲说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19EB(): pass

    label('loc_19EB')

    Jump('loc_1B67')

    def _loc_19EE(): pass

    label('loc_19EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1AC8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1A4D',
    )

    ChrTalk(
        0x00FE,
        (
            '选举也得在玛诺利亚\n',
            '准备投票所才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长选举之前\n',
            '需要做许多准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AC5')

    def _loc_1A4D(): pass

    label('loc_1A4D')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '父亲也为了选举的准备\n',
            '忙个不停的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '玛诺利亚也要\n',
            '准备投票所才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为村长\n',
            '也需要做许多准备哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AC5(): pass

    label('loc_1AC5')

    Jump('loc_1B67')

    def _loc_1AC8(): pass

    label('loc_1AC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_1B1C',
    )

    ChrTalk(
        0x00FE,
        (
            '看来主日学校\n',
            '好像结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才还那么热闹，\n',
            '现在就完全静下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B67')

    def _loc_1B1C(): pass

    label('loc_1B1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1B67',
    )

    ChrTalk(
        0x00FE,
        (
            '孤儿院的孩子们\n',
            '似乎很精神呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '重建工程那么努力\n',
            '也值得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B67(): pass

    label('loc_1B67')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x1B6B
@scena.Code('func_06_1B6B')
def func_06_1B6B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1C98',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C3F',
    )

    ChrTalk(
        0x00FE,
        (
            '玛诺利亚村自然资源丰富，\n',
            '收集柴火也很自由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不行的话野鸟、鱼、山菜\n',
            '都能拿来当食物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，像王都一样的都市\n',
            '就没办法这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果这状况长久持续，恐怕\n',
            '都市会陷入危机吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1C95')

    def _loc_1C3F(): pass

    label('loc_1C3F')

    ChrTalk(
        0x00FE,
        (
            '如果这状况长久持续，恐怕\n',
            '都市会陷入危机吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大城市可是相当\n',
            '依靠导力器的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C95(): pass

    label('loc_1C95')

    Jump('loc_20E0')

    def _loc_1C98(): pass

    label('loc_1C98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1DD0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D6F',
    )

    ChrTalk(
        0x00FE,
        (
            '风车小屋里食品和燃料\n',
            '都有少量的储备……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果只想有那些储备就可以的话，\n',
            '那很快就会开始匮乏的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了向卢安市请求支持，\n',
            '让儿子索雷诺去了城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能和新市长先生\n',
            '谈妥就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1DCD')

    def _loc_1D6F(): pass

    label('loc_1D6F')

    ChrTalk(
        0x00FE,
        (
            '风车小屋里那种程度的储备\n',
            '很快就会用完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此时间紧迫，\n',
            '就让儿子立即去请求支持了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DCD(): pass

    label('loc_1DCD')

    Jump('loc_20E0')

    def _loc_1DD0(): pass

    label('loc_1DD0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1EBB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1E45',
    )

    ChrTalk(
        0x00FE,
        (
            '贵族的前市长被逮捕，\n',
            '平民出身的候选人在竞争其继任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '此次的市长选举\n',
            '真像是时代变化的象征。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EB8')

    def _loc_1E45(): pass

    label('loc_1E45')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '诺曼氏和波尔多斯氏\n',
            '都是平民出身，\n',
            '两人都是出色的人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前要说选举\n',
            '都是从贵族中选，\n',
            '这时代真是变了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EB8(): pass

    label('loc_1EB8')

    Jump('loc_20E0')

    def _loc_1EBB(): pass

    label('loc_1EBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1F8A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1F16',
    )

    ChrTalk(
        0x00FE,
        (
            '上次选举时\n',
            '这里是投票所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '许多人相信戴尔蒙家\n',
            '的家名而投了票……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F87')

    def _loc_1F16(): pass

    label('loc_1F16')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '上次选举时\n',
            '这里曾经是投票所……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唔，怎么看都很狭窄啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大概还是只有拜托\n',
            '白之木莲亭合作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F87(): pass

    label('loc_1F87')

    Jump('loc_20E0')

    def _loc_1F8A(): pass

    label('loc_1F8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_1FF5',
    )

    ChrTalk(
        0x00FE,
        (
            '孤儿院开始重建工程时，\n',
            '村里的年轻人好像\n',
            '也都去帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望他们能一直\n',
            '保持这种心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20E0')

    def _loc_1FF5(): pass

    label('loc_1FF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_20E0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_205A',
    )

    ChrTalk(
        0x00FE,
        (
            '前市长引起的事件\n',
            '对玛诺利亚来说也是重伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生大事件之后\n',
            '游客也都不来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20E0')

    def _loc_205A(): pass

    label('loc_205A')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '哎呀，旅行的人吗？\n',
            '欢迎来到玛诺利亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '烧掉的孤儿院也被重建，\n',
            '恢复到平常的生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之后就只等\n',
            '后任的市长被选出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20E0(): pass

    label('loc_20E0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x20E4
@scena.Code('func_07_20E4')
def func_07_20E4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_20F5',
    )

    Call(0, 0x0008)

    def _loc_20F5(): pass

    label('loc_20F5')

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    FormationAddMember(ChrTable['凯文神父'], 0xF8, 0xFF)
    ChrSetStatus(ChrTable['凯文神父'], 0x00, 39)
    ChrSetStatus(ChrTable['凯文神父'], 0xFE, 0)
    EquipCmd(ChrTable['凯文神父'], ItemTable['战弩'], 0xFF)
    EquipCmd(ChrTable['凯文神父'], ItemTable['纤维护铠'], 0xFF)
    EquipCmd(ChrTable['凯文神父'], ItemTable['金属靴'], 0xFF)
    EquipCmd(ChrTable['凯文神父'], ItemTable['行动力１'], 0x00)
    EquipCmd(ChrTable['凯文神父'], ItemTable['ＥＰ１'], 0x01)
    EquipCmd(ChrTable['凯文神父'], ItemTable['ＨＰ１'], 0x02)
    EquipCmd(ChrTable['凯文神父'], ItemTable['精神２'], 0x03)
    EquipCmd(ChrTable['凯文神父'], ItemTable['防御２'], 0x04)
    AddCraft(ChrTable['凯文神父'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['凯文神父'], 0x0000)
    OP_BB(0x08, 0x06, 0x0000010E)
    ChrSetFlags(0x0101, 0x0008)
    ChrSetFlags(0x00F7, 0x0008)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x0101, -30000, 0, 34900, 0)
    ChrSetPos(0x00F7, -30000, 0, 34900, 0)
    ChrSetPos(0x0109, -30000, 0, 42500, 180)
    ChrSetPos(0x0008, -30000, 0, 40000, 0)
    ChrSetPos(0x0009, -28640, 0, 40440, 315)
    ChrSetPos(0x000A, -30970, 0, 40340, 0)
    ChrSetPos(0x000B, -31570, 0, 41240, 45)
    ChrSetPos(0x000C, -27690, 0, 41900, 315)

    ExecExpressionWithValue(
        0x0011,
        0x01,
        (
            (Expr.GetChrWork, 0x109, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x02,
        (
            (Expr.GetChrWork, 0x109, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x03,
        (
            (Expr.GetChrWork, 0x109, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0109, 0)
    OP_6C(45000, 0)
    CameraSetDistance(3010, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0109,
        (
            '#0180210194V#1065F『不必同情他啦。\n',
            '  真是的，蒂雅大人太善良了』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210195V#1067F老实说，加斯顿公爵\n',
            '会就这样默默地退出，\n',
            '佩德罗无论如何也没有想到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210196V#1063F还有那个诡异的蒙面人偶师，\n',
            '哈雷库因的动向也很令人在意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210197V虽然彼此似乎相识，\n',
            '但师父卡普利闪烁其词，\n',
            '完全没向自己说明些什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210198V#1065F不管怎么样，\n',
            '最近必定还会有一场动乱。\n',
            '佩德罗下定决心要改造苍骑士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210199V#1060F『真是的，佩德罗大人。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210200V稍显愠怒的语调\n',
            '让佩德罗回过神来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210201V#1061F『茶要凉了哦？』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210202V她那双照映着蓝天的清爽眼眸\n',
            '就好像在说『没问题』一样，\n',
            '闪耀着恶作剧般的光辉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210203V#1062F感到些许害羞的佩德罗，\n',
            '端起微温的红茶润了润喉咙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210204V#1071F……人偶骑士·完。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2524')
    def lambda_2524():
        ChrJumpToRelative(0x0008, 0, 0, 0, 600, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2524)

    @scena.Lambda('lambda_2542')
    def lambda_2542():
        ChrJumpToRelative(0x000A, 0, 0, 0, 600, 6000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2542)

    Sleep(50)

    @scena.Lambda('lambda_2565')
    def lambda_2565():
        ChrJumpToRelative(0x000B, 0, 0, 0, 600, 6000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2565)

    @scena.Lambda('lambda_2583')
    def lambda_2583():
        ChrJumpToRelative(0x000C, 0, 0, 0, 600, 6000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2583)

    Sleep(50)

    @scena.Lambda('lambda_25A6')
    def lambda_25A6():
        ChrJumpToRelative(0x0009, 0, 0, 0, 600, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_25A6)

    OP_62(0x0008, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000A, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000C, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(800)

    ChrTalk(
        0x0008,
        (
            '#0400210205V#774F咦咦～！\n',
            '这就完了吗～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400210206V跟哈雷库因的\n',
            '的决斗怎么办啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0008, 400)

    ChrTalk(
        0x000A,
        (
            '#0410210207V#1719F#6P白痴啊，克拉姆真是的。\n',
            '在这里结束不是正好吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410210208V#1718F#6P佩德罗和蒂雅公主\n',
            '总有一天会结婚，然后过着幸福的生活。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410210209V#1903F#6P啊～太浪漫了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000A, 400)

    ChrTalk(
        0x000C,
        (
            '#2830210210V嗯嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2830210211V的确要两人结婚的\n',
            '大团圆结局才行呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0420210212V#1720F我觉得\n',
            '好想喝老师的茶啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0430210213V#1730F#2P卡普利师父好帅哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210214V#1068F呼呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210215V把『人偶骑士』\n',
            '全２２卷一口气念完还真是辛苦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210216V#1062F好了，这样行了吧。\n',
            '今天的授课结束啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0400210217V#772F呵～呵～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0109, 400)

    ChrTalk(
        0x000A,
        (
            '#0410210218V#1710F#6P凯文老师，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210219V#1066F呼，真是被打败了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0109,
        (
            '#0180210220V#1062F啊～那边的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210221V授课结束了，\n',
            '可以进来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210222V#5P啊哈哈……\n',
            '注意到了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210223V嗯，打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    Sleep(300)

    @scena.Lambda('lambda_29C8')
    def lambda_29C8():
        CameraMove(-29990, 0, 40480, 1500)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_29C8)

    @scena.Lambda('lambda_29E0')
    def lambda_29E0():
        OP_67(0, 6620, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_29E0)

    @scena.Lambda('lambda_29F8')
    def lambda_29F8():
        ChrTurnDirection(0x0008, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_29F8)

    @scena.Lambda('lambda_2A06')
    def lambda_2A06():
        ChrTurnDirection(0x0009, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2A06)

    @scena.Lambda('lambda_2A14')
    def lambda_2A14():
        ChrTurnDirection(0x000A, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2A14)

    @scena.Lambda('lambda_2A22')
    def lambda_2A22():
        ChrTurnDirection(0x000B, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2A22)

    @scena.Lambda('lambda_2A30')
    def lambda_2A30():
        ChrTurnDirection(0x000C, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2A30)

    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x00F7, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0101, 0x0008)

    @scena.Lambda('lambda_2A59')
    def lambda_2A59():
        ChrMoveTo(0x0101, -30020, 0, 38000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A59)

    @scena.Lambda('lambda_2A74')
    def lambda_2A74():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2A74)

    Sleep(500)

    ChrClearFlags(0x00F7, 0x0008)

    @scena.Lambda('lambda_2A90')
    def lambda_2A90():
        ChrMoveTo(0x00F7, -30910, 0, 36720, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2A90)

    @scena.Lambda('lambda_2AAB')
    def lambda_2AAB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_2AAB)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0109, 0x0000)
    WaitForThreadExit(0x0109, 0x0001)
    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0109,
        (
            '#0180210224V#1064F#5P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0400210225V#774F#5P#3S啊啊啊啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0410210226V#1714F#5P#3S艾丝蒂尔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210227V#1018F#6P大家，好久不见呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210228V还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2C25')
    def lambda_2C25():
        OP_92(0x0008, 0x0101, 1000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2C25)

    Sleep(50)

    @scena.Lambda('lambda_2C3F')
    def lambda_2C3F():
        ChrWalkTo(0x0009, -29380, 0, 38050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2C3F)

    Sleep(50)

    @scena.Lambda('lambda_2C5F')
    def lambda_2C5F():
        ChrWalkTo(0x000A, -30980, 0, 38010, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2C5F)

    Sleep(50)

    @scena.Lambda('lambda_2C7F')
    def lambda_2C7F():
        ChrWalkTo(0x000B, -30960, 0, 38890, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2C7F)

    Sleep(50)

    @scena.Lambda('lambda_2C9F')
    def lambda_2C9F():
        ChrWalkTo(0x000C, -29200, 0, 39180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2C9F)

    Sleep(50)

    @scena.Lambda('lambda_2CBF')
    def lambda_2CBF():
        ChrWalkTo(0x0109, -30140, 0, 41270, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_2CBF)

    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)
    ChrTurnDirection(0x0009, 0x0101, 0)
    ChrTurnDirection(0x000A, 0x0101, 0)
    ChrTurnDirection(0x000B, 0x0101, 0)

    ChrTalk(
        0x0008,
        (
            '#0400210229V#771F#5P怎么啦！\n',
            '是来玩的吗～！？',
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x000C, 0x0001)
    ChrTurnDirection(0x000C, 0x0101, 0)
    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0410210230V#1718F#6P呜哇！\n',
            '真的是好久不见了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0420210231V#1721F#5P艾丝蒂尔姐姐。\n',
            '一起玩一起玩～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0430210232V#1732F#2P来得正好～\n',
            '欢迎欢迎～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210233V#1016F#6P啊哈哈……\n',
            '大家还是这么精神呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210234V#1017F啊。\n',
            '凯文先生也好久不见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210235V#1061F#5P哦哦、艾丝蒂尔。\n',
            '还记得我吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210236V#1006F#6P那当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210237V#1016F不过，你真的\n',
            '这副打扮来当神父啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210238V#1068F#5P这话是什么意思嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210239V#1062F不过，没想到\n',
            '能在这种地方重逢啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210240V#1061F难不成这是\n',
            '命运的重逢也说不定啊㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T2412._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x2F7F
@scena.Code('func_08_2F7F')
def func_08_2F7F():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2FF9'),
        (0x00000001, 'loc_2FFF'),
        (-1, 'loc_3005'),
    )

    def _loc_2FF9(): pass

    label('loc_2FF9')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_3005')

    def _loc_2FFF(): pass

    label('loc_2FFF')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_3005')

    def _loc_3005(): pass

    label('loc_3005')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3013',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_3017')

    def _loc_3013(): pass

    label('loc_3013')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_3017(): pass

    label('loc_3017')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
