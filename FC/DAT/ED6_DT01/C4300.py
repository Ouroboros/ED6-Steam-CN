import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4300   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4300.x'
    header.mapIndex       = 216
    header.bgm            = 35
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
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT09/CH10941._CH', 'ED6_DT09/CH10941P._CP'),
        ('ED6_DT09/CH10940._CH', 'ED6_DT09/CH10940P._CP'),
        ('ED6_DT07/CH00260._CH', 'ED6_DT07/CH00260P._CP'),
        ('ED6_DT07/CH00262._CH', 'ED6_DT07/CH00262P._CP'),
        ('ED6_DT07/CH00270._CH', 'ED6_DT07/CH00270P._CP'),
        ('ED6_DT07/CH00272._CH', 'ED6_DT07/CH00272P._CP'),
        ('ED6_DT06/CH20051._CH', 'ED6_DT06/CH20051P._CP'),
    ]

# id: 0x10001 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '科洛丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '金',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '拉赛尔博士',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '基库',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '理查德上校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛伦斯少尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '机器',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '机器',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卡西乌斯',
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
            name                = '卡西乌斯',
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
            name                = '卡西乌斯',
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
            name                = '卡西乌斯',
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
            name                = '卡西乌斯',
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
            name                = '卡西乌斯',
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
            name                = '卡西乌斯',
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
            name                = '卡西乌斯',
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
    )

# id: 0x10002 offset: 0x4DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x4DA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x4DA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 38290,
            triggerZ            = 0,
            triggerY            = -3310,
            triggerRange        = 1000,
            actorX              = 38290,
            actorZ              = 1200,
            actorY              = -3310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x4FE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_515',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x5C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0C_A52)

    def _loc_515(): pass

    label('loc_515')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_528',
    )

    MapSetFlags(0x40000000)
    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_10_19AE)

    def _loc_528(): pass

    label('loc_528')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 7, 0x667)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 0, 0x668)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_538',
    )

    Call(0, 0x0012)

    def _loc_538(): pass

    label('loc_538')

    ExecExpressionWithValue(
        0x000F,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x54A
@scena.Code('func_01_54A')
def func_01_54A():
    LoadEffect(0x05, 'map\\\\mp027_00.eff')
    PlayEffect(0x05, 0x06, 0x00FF, 38290, 1200, -3310, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0002 offset: 0x594
@scena.Code('func_02_594')
def func_02_594():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5A9',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_594')

    def _loc_5A9(): pass

    label('loc_5A9')

    Return()

# id: 0x0003 offset: 0x5AA
@scena.Code('func_03_5AA')
def func_03_5AA():
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0030140068V#022F上校如此不择手段\n',
            '想要得到的『辉之环』究竟是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030140069V不管怎样，\n',
            '应该不是个受欢迎的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x628
@scena.Code('func_04_628')
def func_04_628():
    TalkBegin(0x0009)

    ChrTalk(
        0x0009,
        (
            '#0040140066V#035F在地下企图做的\n',
            '肯定不是什么好事，\n',
            '前人的经验这么告诉我们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140067V#030F早点把上校逼入绝境，\n',
            '然后华丽地演奏最终乐章吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0x6C4
@scena.Code('func_05_6C4')
def func_05_6C4():
    TalkBegin(0x000A)

    ChrTalk(
        0x000A,
        (
            '#0060140064V#042F祖母大人有尤莉亚中尉跟随，\n',
            '肯定不会有事的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140065V我相信她们，\n',
            '所以现在要前进……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x73A
@scena.Code('func_06_73A')
def func_06_73A():
    TalkBegin(0x000B)

    ChrTalk(
        0x000B,
        (
            '#0050140062V#050F如何，路线清楚了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050140063V尽快找到上校，\n',
            '然后狠狠教训他一顿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0x79F
@scena.Code('func_07_79F')
def func_07_79F():
    TalkBegin(0x000C)

    ChrTalk(
        0x000C,
        (
            '#0070140060V#063F艾丝蒂尔姐姐，\n',
            '约修亚哥哥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070140061V如果遇到什么危险，\n',
            '可要立刻回到这里来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x811
@scena.Code('func_08_811')
def func_08_811():
    TalkBegin(0x000D)

    ChrTalk(
        0x000D,
        (
            '#0080140058V#070F这里就由我『不动金』来守护。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140059V你们就放心\n',
            '去前方探路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000D)

    Return()

# id: 0x0009 offset: 0x872
@scena.Code('func_09_872')
def func_09_872():
    TalkBegin(0x000E)
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
            TXT(0x01, '改造·换钱\n'),
            TXT(0x02, '购买道具\n'),
            TXT(0x03, '更换队员\n'),
            TXT(0x04, '取消\n'),
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
        'loc_8E7',
    )

    Call(0, 0x000A)
    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_8E7(): pass

    label('loc_8E7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8FE',
    )

    Call(0, 0x000B)
    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_8FE(): pass

    label('loc_8FE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_94F',
    )

    EventBegin(0x00)
    OP_4A(0x000E, 255)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    Call(0, 0x0011)
    OP_4B(0x000E, 255)
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    OP_4B(0x000A, 255)
    OP_4B(0x000B, 255)
    OP_4B(0x000C, 255)
    OP_4B(0x000D, 255)
    EventEnd(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_94F(): pass

    label('loc_94F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_960',
    )

    TalkEnd(0x000E)

    Return()

    def _loc_960(): pass

    label('loc_960')

    ChrTalk(
        0x000E,
        (
            '#0540140056V#100F如果需要改造导力器的话，\n',
            '说一声就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140057V我从王都的店铺里拿来了一些道具，\n',
            '可以代其进行销售。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000E)

    Return()

# id: 0x000A offset: 0x9E3
@scena.Code('func_0A_9E3')
def func_0A_9E3():
    ChrTalk(
        0x000E,
        (
            '#0540140055V#100F来吧，我会给你们\n',
            '比这边的工房更好的服务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_0D()
    OP_A9(0x6A)

    Return()

# id: 0x000B offset: 0xA27
@scena.Code('func_0B_A27')
def func_0B_A27():
    ChrTalk(
        0x000E,
        (
            '#0540140054V#100F有什么需要的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_0D()
    OP_A9(0x6B)

    Return()

# id: 0x000C offset: 0xA52
@scena.Code('func_0C_A52')
def func_0C_A52():
    EventBegin(0x00)
    LoadEffect(0x00, 'battle\\\\btbomb00.eff')
    FadeIn(2000, 0)
    CameraMove(38000, 17050, -14020, 0)
    OP_67(0, 4150, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(418, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x0019, 34660, 0, -13430, 270)
    ChrSetPos(0x001A, 35900, 0, -15200, 270)
    ChrSetPos(0x0010, 36160, 0, -11160, 270)
    ChrSetPos(0x0011, 37460, 0, -14780, 270)
    ChrSetPos(0x0012, 37460, 0, -13340, 270)
    ChrSetPos(0x0013, 36220, 0, -17220, 270)
    ChrSetPos(0x0014, 37460, 0, -12070, 270)
    ChrSetPos(0x0015, 39500, 0, -13290, 270)
    ChrSetPos(0x0016, 39500, 0, -14730, 270)
    ChrSetPos(0x0017, 37460, 0, -16090, 270)
    FadeIn(2000, 0)
    CameraMove(38000, 2550, -14020, 5000)

    ChrTalk(
        0x0010,
        (
            '#2620121640V#5P这、这里是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2630121641V#5P这、这种地方\n',
            '竟然真的存在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0C02')
    def lambda_0C02():
        CameraMove(19210, 0, -13380, 3500)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0C02)

    @scena.Lambda('lambda_0C1A')
    def lambda_0C1A():
        OP_6C(135000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0C1A)

    Sleep(2000)

    @scena.Lambda('lambda_0C2F')
    def lambda_0C2F():
        OP_67(0, 10910, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0C2F)

    @scena.Lambda('lambda_0C47')
    def lambda_0C47():
        OP_6E(514, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0C47)

    Sleep(4000)

    Fade(1000)
    CameraMove(36830, 0, -13980, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(135000, 0)
    OP_6E(332, 0)
    OP_0D()

    ChrTalk(
        0x0019,
        (
            '#0130121642V#115F#6P呵呵，规模比预想的还要大啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130121643V#110F洛伦斯少尉，\n',
            '带我到最深处去好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0140121644V#281F#5P明白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x001A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrSetFlags(0x001B, 0x0004)
    ChrSetFlags(0x001C, 0x0004)
    ChrSetPos(0x001B, 18010, 20220, 5070, 108)
    ChrSetPos(0x001C, 16410, 20220, -120, 108)

    @scena.Lambda('lambda_0D7D')
    def lambda_0D7D():
        ChrTurnDirection(0x00FE, 0x001A, 0)
        Yield()

        Jump('lambda_0D7D')

    DispatchAsync2(0x001B, 0x0003, lambda_0D7D)

    @scena.Lambda('lambda_0D8E')
    def lambda_0D8E():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_0D8E')

    DispatchAsync2(0x001C, 0x0003, lambda_0D8E)

    ChrClearFlags(0x001B, 0x0001)
    ChrClearFlags(0x001C, 0x0001)

    @scena.Lambda('lambda_0DA9')
    def lambda_0DA9():
        ChrMoveTo(0x00FE, 31350, 0, -12230, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_0DA9)

    Sleep(300)

    @scena.Lambda('lambda_0DC9')
    def lambda_0DC9():
        ChrMoveTo(0x00FE, 31230, 0, -15680, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_0DC9)

    ChrTurnDirection(0x001A, 0x001B, 400)

    @scena.Lambda('lambda_0DEB')
    def lambda_0DEB():
        CameraMove(32409, 0, -13750, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0DEB)

    @scena.Lambda('lambda_0E03')
    def lambda_0E03():
        OP_6C(90000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0E03)

    @scena.Lambda('lambda_0E13')
    def lambda_0E13():
        OP_67(0, 7160, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0E13)

    ChrWalkTo(0x001A, 34460, 0, -15230, 5000, 0x00)

    @scena.Lambda('lambda_0E3F')
    def lambda_0E3F():
        ChrTurnDirection(0x00FE, 0x001C, 0)
        Yield()

        Jump('lambda_0E3F')

    DispatchAsync2(0x001A, 0x0001, lambda_0E3F)

    @scena.Lambda('lambda_0E50')
    def lambda_0E50():
        ChrTurnDirection(0x00FE, 0x001B, 0)
        Yield()

        Jump('lambda_0E50')

    DispatchAsync2(0x0019, 0x0001, lambda_0E50)

    ChrSetChipByIndex(0x001A, 13)
    ChrSetChipByIndex(0x0019, 15)
    PlaySE(231, 0x00, 0x64)
    WaitForThreadExit(0x001B, 0x0001)
    ChrSetChipByIndex(0x001B, 12)
    ChrSetFlags(0x001B, 0x0001)
    ChrSetFlags(0x001C, 0x0001)

    @scena.Lambda('lambda_0E84')
    def lambda_0E84():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0E84')

    DispatchAsync2(0x001B, 0x0000, lambda_0E84)

    ChrTurnDirection(0x001B, 0x0019, 0)
    WaitForThreadExit(0x001C, 0x0001)
    ChrSetChipByIndex(0x001C, 12)

    @scena.Lambda('lambda_0EA8')
    def lambda_0EA8():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0EA8')

    DispatchAsync2(0x001C, 0x0000, lambda_0EA8)

    ChrTurnDirection(0x001C, 0x001A, 0)
    ChrTurnDirection(0x0010, 0x001B, 0)
    ChrTurnDirection(0x0011, 0x001B, 0)
    ChrTurnDirection(0x0012, 0x001B, 0)
    ChrTurnDirection(0x0013, 0x001B, 0)
    ChrTurnDirection(0x0014, 0x001B, 0)
    ChrTurnDirection(0x0015, 0x001B, 0)
    ChrTurnDirection(0x0016, 0x001B, 0)
    ChrTurnDirection(0x0017, 0x001B, 0)
    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0011, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0012, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0013, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0014, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0015, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0016, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0017, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_0F8A')
    def lambda_0F8A():
        OP_94(0x01, 0x00FE, 0x00B4, 0x0000044C, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0F8A)

    @scena.Lambda('lambda_0FA0')
    def lambda_0FA0():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000320, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_0FA0)

    Sleep(50)

    @scena.Lambda('lambda_0FBB')
    def lambda_0FBB():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000002BC, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_0FBB)

    @scena.Lambda('lambda_0FD1')
    def lambda_0FD1():
        OP_94(0x01, 0x00FE, 0x00B4, 0x0000044C, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_0FD1)

    Sleep(100)

    @scena.Lambda('lambda_0FEC')
    def lambda_0FEC():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0FEC)

    @scena.Lambda('lambda_1002')
    def lambda_1002():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000514, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_1002)

    Sleep(50)

    @scena.Lambda('lambda_101D')
    def lambda_101D():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_101D)

    Sleep(50)

    @scena.Lambda('lambda_1038')
    def lambda_1038():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_1038)

    WaitForThreadExit(0x0000, 0x0002)

    ChrTalk(
        0x0010,
        (
            '#2620121645V哦啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2630121646V机、机械怪物！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#0130121647V#110F#5P呵呵……\n',
            '是古代的人形兵器啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_10C4')
    def lambda_10C4():
        OP_6C(70000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_10C4)

    CameraSetDistance(2900, 1500)
    ChrSetFlags(0x001A, 0x0040)
    ChrSetFlags(0x0019, 0x0040)

    @scena.Lambda('lambda_10E7')
    def lambda_10E7():
        CameraMove(30310, 0, -13620, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_10E7)

    @scena.Lambda('lambda_10FF')
    def lambda_10FF():
        CameraSetDistance(2500, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_10FF)

    @scena.Lambda('lambda_110F')
    def lambda_110F():
        OP_67(0, 5500, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_110F)

    @scena.Lambda('lambda_1127')
    def lambda_1127():
        OP_6C(42000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_1127)

    ChrSetRGBAMask(0x001D, 255, 200, 200, 200, 0)
    ChrSetRGBAMask(0x001E, 255, 150, 150, 150, 0)
    ChrSetRGBAMask(0x001F, 255, 100, 100, 100, 0)
    ChrSetRGBAMask(0x0020, 255, 50, 50, 50, 0)
    ChrSetRGBAMask(0x0021, 200, 255, 255, 200, 0)
    ChrSetRGBAMask(0x0022, 150, 255, 255, 150, 0)
    ChrSetRGBAMask(0x0023, 100, 255, 255, 100, 0)
    ChrSetRGBAMask(0x0024, 50, 255, 255, 50, 0)
    CreateThread(0x0011, 0x00, 0x00, func_0D_1803)
    Sleep(530)

    PlaySE(501, 0x00, 0x64)
    PlayEffect(0x08, 0xFF, 0x00FF, 31350, 1500, -12230, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    TerminateThread(0x001B, 0xFF)
    Sleep(150)

    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x08, 0xFF, 0x00FF, 31230, 1500, -15680, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    TerminateThread(0x001C, 0xFF)
    Sleep(900)

    @scena.Lambda('lambda_1221')
    def lambda_1221():
        CameraSetDistance(2900, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_1221)

    @scena.Lambda('lambda_1231')
    def lambda_1231():
        OP_6C(19000, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_1231)

    @scena.Lambda('lambda_1241')
    def lambda_1241():
        OP_67(0, 7160, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_1241)

    @scena.Lambda('lambda_1259')
    def lambda_1259():
        CameraMove(30310, 0, -13620, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1259)

    ChrSetFlags(0x001B, 0x0004)
    PlayEffect(0x00, 0xFF, 0x001B, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_12AB')
    def lambda_12AB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x001B, 0x0000, lambda_12AB)

    @scena.Lambda('lambda_12BD')
    def lambda_12BD():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_12BD)

    Sleep(300)

    ChrSetFlags(0x001C, 0x0004)
    PlayEffect(0x00, 0xFF, 0x001C, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1317')
    def lambda_1317():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x001C, 0x0000, lambda_1317)

    @scena.Lambda('lambda_1329')
    def lambda_1329():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_1329)

    Sleep(1500)

    @scena.Lambda('lambda_1349')
    def lambda_1349():
        OP_99(0x00FE, 0x09, 0x0B, 1600)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_1349)

    @scena.Lambda('lambda_1359')
    def lambda_1359():
        ChrJumpTo(0x00FE, 31460, 0, -15350, 700, 4000)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_1359)

    ChrSetFlags(0x0019, 0x0800)

    @scena.Lambda('lambda_137C')
    def lambda_137C():
        OP_99(0x00FE, 0x05, 0x0B, 2000)

        ExitThread()

    DispatchAsync(0x0019, 0x0003, lambda_137C)

    WaitForThreadExit(0x0019, 0x0003)
    ChrSetChipByIndex(0x0019, 15)
    ChrSetSubChip(0x0019, 0)
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#2620121648V好、好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#4300121649V那样的怪物一刀就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrSetFlags(0x0019, 0x0020)
    ChrTurnDirection(0x0019, 0x001A, 400)

    ChrTalk(
        0x0019,
        (
            '#0130121650V#111F#5P呵呵，\n',
            '还是你的反应要快一些啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130121651V如果你真的出尽全力，\n',
            '我也许真的没有什么胜算。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrSetFlags(0x001A, 0x0020)
    ChrTurnDirection(0x001A, 0x0019, 400)

    @scena.Lambda('lambda_147C')
    def lambda_147C():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_147C')

    DispatchAsync2(0x001A, 0x0003, lambda_147C)

    ChrTalk(
        0x001A,
        (
            '#0140121652V#280F#6P您过谦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140121653V不愧是继承了『剑圣』\n',
            '之技的神速拔剑法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140121654V终于可以一睹其风采了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#0130121655V#115F#5P呼，还不成熟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130121656V#116F不过，时代正在迅速地远去，\n',
            '不能继续等待不成熟的人停滞不前啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130121657V不管怎样，也只有靠这笨拙的双手\n',
            '来为王国的明天开拓出一个新天地了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x001A, 0)
    ChrSetChipByIndex(0x001A, 9)
    ChrClearFlags(0x001A, 0x0020)
    ChrClearFlags(0x001A, 0x0800)

    @scena.Lambda('lambda_15E9')
    def lambda_15E9():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_15E9)

    @scena.Lambda('lambda_15F9')
    def lambda_15F9():
        CameraMove(35740, 0, -13960, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_15F9)

    ChrClearFlags(0x0019, 0x0020)
    ChrClearFlags(0x0019, 0x0800)
    ChrSetChipByIndex(0x0019, 8)
    ChrWalkTo(0x0019, 31590, 0, -13350, 2000, 0x00)
    ChrSetDirection(0x0019, 90, 400)
    WaitForThreadExit(0x0000, 0x0001)

    ChrTalk(
        0x0019,
        (
            '#0130121658V#114F#5P各位勇士！\n',
            '通向巨硕之力的道路已经开启！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130121659V我们所热爱的利贝尔\n',
            '即将迎来光辉的黎明！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130121660V我期待各位的表现！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2630121661V#5P明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2660121662V#5P我们特务兵会团结一致，\n',
            '竭尽全力效忠上校！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    SetMessageWindowPos(40, 60, -1, -1)
    TalkSetChrName('特务兵们')

    Talk(
        (
            '#2620121663V',
            (TxtCtl.SetColor, 0x0),
            '#3S为利贝尔的荣誉而战！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)
    Sleep(400)

    SetMessageWindowPos(150, 100, -1, -1)
    TalkSetChrName('特务兵们')

    Talk(
        (
            '#2630121664V',
            (TxtCtl.SetColor, 0x0),
            '#5S为利贝尔的荣誉而战！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(2000)

    PlaySE(13, 0x00, 0x64)
    Sleep(3000)

    MapSetFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x1803
@scena.Code('func_0D_1803')
def func_0D_1803():
    CreateThread(0x001A, 0x01, 0x00, func_0E_1895)
    Sleep(70)

    CreateThread(0x001D, 0x01, 0x00, func_0E_1895)
    CreateThread(0x0019, 0x01, 0x00, func_0F_1931)
    Sleep(70)

    CreateThread(0x001E, 0x01, 0x00, func_0E_1895)
    CreateThread(0x0021, 0x01, 0x00, func_0F_1931)
    Sleep(70)

    CreateThread(0x001F, 0x01, 0x00, func_0E_1895)
    CreateThread(0x0022, 0x01, 0x00, func_0F_1931)
    Sleep(70)

    CreateThread(0x0020, 0x01, 0x00, func_0E_1895)
    CreateThread(0x0023, 0x01, 0x00, func_0F_1931)
    Sleep(70)

    CreateThread(0x0024, 0x01, 0x00, func_0F_1931)
    WaitForThreadExit(0x0020, 0x0001)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    WaitForThreadExit(0x0024, 0x0001)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    ChrSetFlags(0x0024, 0x0080)

    Return()

# id: 0x000E offset: 0x1895
@scena.Code('func_0E_1895')
def func_0E_1895():
    ChrSetChipByIndex(0x00FE, 13)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetPos(0x00FE, 34460, 0, -15230, 270)

    @scena.Lambda('lambda_18BB')
    def lambda_18BB():
        ChrTurnDirection(0x00FE, 0x001C, 0)
        Yield()

        Jump('lambda_18BB')

    DispatchAsync2(0x00FE, 0x0003, lambda_18BB)

    ChrJumpTo(0x00FE, 33350, 0, -15590, 1000, 9000)
    TerminateThread(0x00FE, 0x03)
    ChrSetChipByIndex(0x00FE, 14)
    ChrSetFlags(0x00FE, 0x0800)

    @scena.Lambda('lambda_18F1')
    def lambda_18F1():
        OP_99(0x00FE, 0x00, 0x05, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_18F1)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetFlags(0x00FE, 0x0004)
    ChrJumpTo(0x00FE, 32619, 1200, -15520, 1250, 5000)
    ChrMoveTo(0x00FE, 29300, 150, -15330, 13000, 0x00)

    Return()

# id: 0x000F offset: 0x1931
@scena.Code('func_0F_1931')
def func_0F_1931():
    ChrClearFlags(0x001A, 0x0800)
    ChrSetChipByIndex(0x00FE, 15)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetPos(0x00FE, 34660, 0, -13430, 270)

    @scena.Lambda('lambda_195C')
    def lambda_195C():
        ChrTurnDirection(0x00FE, 0x001B, 0)
        Yield()

        Jump('lambda_195C')

    DispatchAsync2(0x00FE, 0x0003, lambda_195C)

    ChrMoveTo(0x00FE, 33410, 0, -12320, 5000, 0x00)
    TerminateThread(0x00FE, 0x03)
    ChrSetChipByIndex(0x00FE, 16)
    ChrSetFlags(0x00FE, 0x0800)

    @scena.Lambda('lambda_198F')
    def lambda_198F():
        OP_99(0x00FE, 0x00, 0x05, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_198F)

    ChrWalkTo(0x00FE, 28880, 150, -12230, 11000, 0x00)

    Return()

# id: 0x0010 offset: 0x19AE
@scena.Code('func_10_19AE')
def func_10_19AE():
    EventBegin(0x00)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationAddMember(0x01, 0xFF)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    OP_4A(0x000E, 255)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    ChrSetPos(0x0101, 37080, 0, -15050, 270)
    ChrSetPos(0x0102, 37170, 0, -12980, 270)
    ChrSetPos(0x000E, 38760, 0, -14790, 258)
    ChrSetPos(0x000B, 37850, 0, -16410, 222)
    ChrSetPos(0x000C, 39400, 0, -15590, 222)
    ChrSetPos(0x0009, 39020, 0, -12220, 293)
    ChrSetPos(0x0008, 39710, 0, -13330, 262)
    ChrSetPos(0x000D, 40420, 0, -14130, 260)
    ChrSetPos(0x000A, 38260, 0, -13640, 265)
    ChrSetPos(0x000F, 40960, 500, -20390, 314)
    CameraMove(80, 0, 35850, 0)
    OP_67(0, 9440, -34740, 0)
    CameraSetDistance(1000, 0)
    OP_6C(0, 0)
    OP_6E(663, 0)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_1B16')
    def lambda_1B16():
        CameraMove(50, 0, -20330, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B16)

    Sleep(3000)

    @scena.Lambda('lambda_1B33')
    def lambda_1B33():
        OP_6C(77000, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1B33)

    Sleep(7000)

    @scena.Lambda('lambda_1B48')
    def lambda_1B48():
        CameraMove(39590, 0, -14310, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B48)

    @scena.Lambda('lambda_1B60')
    def lambda_1B60():
        OP_67(0, 22340, -34740, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1B60)

    @scena.Lambda('lambda_1B78')
    def lambda_1B78():
        OP_6E(343, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1B78)

    Sleep(6000)

    ChrTalk(
        0x0101,
        (
            '#0010140001V#580F这、这里是什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140002V#012F古代塞姆里亚文明的遗迹……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0540140003V#102F#5P看来这里是相当古老的遗迹啊，\n',
            '而且竟然还没有湮灭掉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140004V和『四轮之塔』不同，\n',
            '这里的装置还在继续运转着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050140005V#057F而且还不只是装置在运转吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050140006V我注意到这个地方\n',
            '还有许多怪物在成群地蠕动着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070140007V#065F#2P啊，呀啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030140008V#022F那边的建筑材料是最近才拿进来的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030140009V是根据上校的指示去修建的吗……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040140010V#030F应该没错吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140011V#035F在这样深的地下施工，\n',
            '那些黑衣男子一定很辛苦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060140012V#043F不过这个巨大的遗迹\n',
            '远远超出了我的想象……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140013V如果不用心去探索，\n',
            '肯定很快就会被困在里面的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080140014V#074F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140015V#072F我们最好在这里将人员分为\n',
            '探索组和待机组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1EA7')
    def lambda_1EA7():
        OP_6E(300, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1EA7)

    @scena.Lambda('lambda_1EB7')
    def lambda_1EB7():
        OP_6C(90000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1EB7)

    @scena.Lambda('lambda_1EC7')
    def lambda_1EC7():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1EC7)

    @scena.Lambda('lambda_1ED5')
    def lambda_1ED5():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1ED5)

    Sleep(100)

    @scena.Lambda('lambda_1EE8')
    def lambda_1EE8():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1EE8)

    Sleep(100)

    @scena.Lambda('lambda_1EFB')
    def lambda_1EFB():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1EFB)

    @scena.Lambda('lambda_1F09')
    def lambda_1F09():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1F09)

    Sleep(100)

    @scena.Lambda('lambda_1F1C')
    def lambda_1F1C():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1F1C)

    @scena.Lambda('lambda_1F2A')
    def lambda_1F2A():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1F2A)

    ChrTurnDirection(0x0102, 0x000D, 400)
    ChrTurnDirection(0x0101, 0x000D, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010140016V#505F啊，这是什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140017V#010F也就是说，以安全的地方作为据点，\n',
            '然后从那里展开搜索对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080140018V#070F对，就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140019V探索组在寻找路线的同时，\n',
            '待机组守卫据点，然后准备随时交换成员。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140020V一旦找到了正确的路线，\n',
            '我们就全部移动过去并将那作为新的据点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050140021V#051F原来如此……很合理嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0540140022V#104F#2P就这样决定好了。\n',
            '就把目前我们所在的地方作为据点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '#0540140023V#100F艾丝蒂尔、约修亚，\n',
            '立刻决定探索组的成员吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_215E')
    def lambda_215E():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_215E)

    @scena.Lambda('lambda_216C')
    def lambda_216C():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_216C)

    @scena.Lambda('lambda_217A')
    def lambda_217A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_217A)

    @scena.Lambda('lambda_2188')
    def lambda_2188():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2188)

    @scena.Lambda('lambda_2196')
    def lambda_2196():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2196)

    @scena.Lambda('lambda_21A4')
    def lambda_21A4():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_21A4)

    @scena.Lambda('lambda_21B2')
    def lambda_21B2():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_21B2)

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010140024V#004F啊，我们决定！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140025V#014F可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0540140026V#100F#2P与这次事件关联最深的就是你们俩了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140027V大家都没有异议吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030140028V#021F嗯，我很赞成哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060140029V#040F我当然也赞成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070140030V#560F我、我也赞成让姐姐他们来决定呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050140031V#053F哼，没办法了。\n',
            '也只有听从你们两个的指挥了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040140032V#035F#5P呵呵……我相信你们哦。\n',
            '我看中的小猫咪准能成大事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080140033V#070F嗯，就是这样，\n',
            '好好的选择组员吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010140034V#505F约修亚……怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020140035V#010F已经来不及仔细考虑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140036V如果想改变主意，\n',
            '回据点这里替换成员就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140037V#006F对啊，这样就行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Call(0, 0x0011)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24A2',
    )

    WaitEffect(0x17, 0x00)

    def _loc_24A2(): pass

    label('loc_24A2')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24BE',
    )

    WaitEffect(0x17, 0x00)

    def _loc_24BE(): pass

    label('loc_24BE')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24DA',
    )

    WaitEffect(0x17, 0x00)

    def _loc_24DA(): pass

    label('loc_24DA')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24F6',
    )

    WaitEffect(0x18, 0x00)

    def _loc_24F6(): pass

    label('loc_24F6')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2512',
    )

    WaitEffect(0x18, 0x00)

    def _loc_2512(): pass

    label('loc_2512')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_252E',
    )

    WaitEffect(0x18, 0x00)

    def _loc_252E(): pass

    label('loc_252E')

    ChrSetFlags(0x000F, 0x0080)

    @scena.Lambda('lambda_2539')
    def lambda_2539():
        ChrTurnDirection(0x00FE, 0x000A, 0)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2539)

    @scena.Lambda('lambda_2547')
    def lambda_2547():
        ChrTurnDirection(0x00FE, 0x000A, 0)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2547)

    @scena.Lambda('lambda_2555')
    def lambda_2555():
        ChrTurnDirection(0x00FE, 0x000A, 0)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2555)

    @scena.Lambda('lambda_2563')
    def lambda_2563():
        ChrTurnDirection(0x00FE, 0x000A, 0)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2563)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2694',
    )

    ChrSetPos(0x000A, 36030, 0, -8640, 225)
    ChrSetPos(0x000F, 36210, 0, -9110, 225)
    ChrSetChipByIndex(0x000A, 17)
    ChrSetSubChip(0x000A, 1)
    TerminateThread(0x000A, 0xFF)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0060140038V#040F#5P基库这孩子也会跟着艾丝蒂尔你们\n',
            '一起行动的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140039V如果发现了可以作为新据点的地方，\n',
            '它会回来向我们报告的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140040V然后我们就会跟着它\n',
            '到艾丝蒂尔你们所在的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0440140041V#310F#2P啾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27BF')

    def _loc_2694(): pass

    label('loc_2694')

    @scena.Lambda('lambda_269A')
    def lambda_269A():
        ChrSetDirection(0x00FE, 225, 0)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_269A)

    ChrSetPos(0x0105, 36030, 0, -8640, 225)
    ChrSetPos(0x000F, 36210, 0, -9110, 225)
    ChrSetChipByIndex(0x0105, 17)
    ChrSetSubChip(0x0105, 1)
    Sleep(1000)

    ChrTalk(
        0x0105,
        (
            '#0060140042V#040F#5P如果发现了可以作为新的据点的地方，\n',
            '基库会回来报告的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140043V跟着它就可以来到我们所在的地方了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140044V还有，就算我离开探索组，\n',
            '基库还是会跟着艾丝蒂尔你们行动哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0440140041V#310F#2P啾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27BF(): pass

    label('loc_27BF')

    ChrTalk(
        0x0102,
        (
            '#0020140046V#010F原来如此，\n',
            '这样我们就不用专程赶回这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140047V#006F靠你了哦，基库！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0440140048V#311F#2P啾啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrClearFlags(0x000F, 0x0080)

    @scena.Lambda('lambda_2858')
    def lambda_2858():
        ChrTurnDirection(0x00FE, 0x000F, 800)
        Yield()

        Jump('lambda_2858')

    DispatchAsync2(0x0000, 0x0001, lambda_2858)

    @scena.Lambda('lambda_2869')
    def lambda_2869():
        ChrTurnDirection(0x00FE, 0x000F, 800)
        Yield()

        Jump('lambda_2869')

    DispatchAsync2(0x0001, 0x0001, lambda_2869)

    @scena.Lambda('lambda_287A')
    def lambda_287A():
        ChrTurnDirection(0x00FE, 0x000F, 800)
        Yield()

        Jump('lambda_287A')

    DispatchAsync2(0x0002, 0x0001, lambda_287A)

    @scena.Lambda('lambda_288B')
    def lambda_288B():
        ChrTurnDirection(0x00FE, 0x000F, 800)
        Yield()

        Jump('lambda_288B')

    DispatchAsync2(0x0003, 0x0001, lambda_288B)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28B1',
    )

    ChrSetFlags(0x000A, 0x0020)
    ChrSetSubChip(0x000A, 3)

    Jump('loc_28BF')

    def _loc_28B1(): pass

    label('loc_28B1')

    TerminateThread(0x0105, 0xFF)
    ChrSetFlags(0x0105, 0x0020)
    ChrSetSubChip(0x0105, 3)

    def _loc_28BF(): pass

    label('loc_28BF')

    PlaySE(140, 0x00, 0x64)
    ChrSetFlags(0x000F, 0x0040)
    ChrSetFlags(0x000F, 0x0004)

    @scena.Lambda('lambda_28D4')
    def lambda_28D4():
        ChrWalkTo(0x00FE, 35070, 2000, -10300, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_28D4)

    Sleep(100)

    @scena.Lambda('lambda_28F4')
    def lambda_28F4():
        ChrWalkTo(0x00FE, 35070, 2000, -10300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_28F4)

    Sleep(100)

    @scena.Lambda('lambda_2914')
    def lambda_2914():
        ChrWalkTo(0x00FE, 35070, 2000, -10300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2914)

    Sleep(100)

    @scena.Lambda('lambda_2934')
    def lambda_2934():
        ChrWalkTo(0x00FE, 31500, 0, -12890, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2934)

    @scena.Lambda('lambda_294F')
    def lambda_294F():
        CameraMove(25620, 0, -12350, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_294F)

    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2986',
    )

    ChrSetChipByIndex(0x000A, 2)
    ChrClearFlags(0x000A, 0x0020)
    ChrSetSubChip(0x000A, 0)

    Jump('loc_2995')

    def _loc_2986(): pass

    label('loc_2986')

    ChrSetChipByIndex(0x0105, 65535)
    ChrClearFlags(0x0105, 0x0020)
    ChrSetSubChip(0x0105, 0)

    def _loc_2995(): pass

    label('loc_2995')

    @scena.Lambda('lambda_299B')
    def lambda_299B():
        ChrWalkTo(0x00FE, 12310, 5000, -14560, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_299B)

    Sleep(2500)

    @scena.Lambda('lambda_29BB')
    def lambda_29BB():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_29BB)

    @scena.Lambda('lambda_29C9')
    def lambda_29C9():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_29C9)

    @scena.Lambda('lambda_29D7')
    def lambda_29D7():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_29D7)

    @scena.Lambda('lambda_29E5')
    def lambda_29E5():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_29E5)

    @scena.Lambda('lambda_29F3')
    def lambda_29F3():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_29F3)

    CameraMove(35010, 0, -7430, 2000)

    ChrTalk(
        0x000E,
        (
            '#0540140049V#102F#5P探索的任务就拜托你们了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140050V为了慎重起见，我为你们准备了\n',
            '一整套工具和简单的物品箱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140051V如果要改造导力器，\n',
            '你们就尽管告诉我就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140052V#006F嗯，明白啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140053V#012F那么我们就出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00CC, 7, 0x667))
    OP_28(0x004F, 0x01, 0x0001)
    OP_28(0x004F, 0x01, 0x0002)
    OP_28(0x004F, 0x01, 0x0004)
    ChrSetFlags(0x000F, 0x0080)
    OP_4B(0x000E, 255)
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    OP_4B(0x000A, 255)
    OP_4B(0x000B, 255)
    OP_4B(0x000C, 255)
    OP_4B(0x000D, 255)
    CreateThread(0x000E, 0x00, 0x00, func_02_594)
    CreateThread(0x000A, 0x00, 0x00, func_02_594)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x2B52
@scena.Code('func_11_2B52')
def func_11_2B52():
    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B63',
    )

    FormationDelMember(0x02, 0xFF)

    def _loc_2B63(): pass

    label('loc_2B63')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B74',
    )

    FormationDelMember(0x03, 0xFF)

    def _loc_2B74(): pass

    label('loc_2B74')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B85',
    )

    FormationDelMember(0x05, 0xFF)

    def _loc_2B85(): pass

    label('loc_2B85')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B96',
    )

    FormationDelMember(0x04, 0xFF)

    def _loc_2B96(): pass

    label('loc_2B96')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BA7',
    )

    FormationDelMember(0x06, 0xFF)

    def _loc_2BA7(): pass

    label('loc_2BA7')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BB8',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_2BB8(): pass

    label('loc_2BB8')

    Fade(1000)
    ChrSetPos(0x0101, 34210, 0, -9750, 350)
    ChrSetPos(0x0102, 33060, 0, -8430, 45)
    ChrSetPos(0x000E, 34700, 0, -7770, 222)
    Call(0, 0x0012)
    CameraMove(35570, 0, -7090, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择除约修亚和艾丝蒂尔以外的两名成员。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    def _loc_2C7F(): pass

    label('loc_2C7F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3252',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D18',
    )

    Menu(
        0,
        10,
        106,
        1,
        (
            TXT(0x00, '★【　雪拉扎德　】\n'),
            TXT(0x01, '　【　奥利维尔　】\n'),
            TXT(0x02, '　【　 阿加特 　】\n'),
            TXT(0x03, '　【　　提妲　　】\n'),
            TXT(0x04, '　【　　 金 　　】\n'),
            TXT(0x05, '　【　 科洛丝 　】\n'),
        ),
    )

    Jump('loc_304F')

    def _loc_2D18(): pass

    label('loc_2D18')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DA4',
    )

    Menu(
        0,
        10,
        106,
        1,
        (
            TXT(0x00, '　【　雪拉扎德　】\n'),
            TXT(0x01, '★【　奥利维尔　】\n'),
            TXT(0x02, '　【　 阿加特 　】\n'),
            TXT(0x03, '　【　　提妲　　】\n'),
            TXT(0x04, '　【　　 金 　　】\n'),
            TXT(0x05, '　【　 科洛丝 　】\n'),
        ),
    )

    Jump('loc_304F')

    def _loc_2DA4(): pass

    label('loc_2DA4')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E30',
    )

    Menu(
        0,
        10,
        106,
        1,
        (
            TXT(0x00, '　【　雪拉扎德　】\n'),
            TXT(0x01, '　【　奥利维尔　】\n'),
            TXT(0x02, '★【　 阿加特 　】\n'),
            TXT(0x03, '　【　　提妲　　】\n'),
            TXT(0x04, '　【　　 金 　　】\n'),
            TXT(0x05, '　【　 科洛丝 　】\n'),
        ),
    )

    Jump('loc_304F')

    def _loc_2E30(): pass

    label('loc_2E30')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2EBC',
    )

    Menu(
        0,
        10,
        106,
        1,
        (
            TXT(0x00, '　【　雪拉扎德　】\n'),
            TXT(0x01, '　【　奥利维尔　】\n'),
            TXT(0x02, '　【　 阿加特 　】\n'),
            TXT(0x03, '★【　　提妲　　】\n'),
            TXT(0x04, '　【　　 金 　　】\n'),
            TXT(0x05, '　【　 科洛丝 　】\n'),
        ),
    )

    Jump('loc_304F')

    def _loc_2EBC(): pass

    label('loc_2EBC')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F48',
    )

    Menu(
        0,
        10,
        106,
        1,
        (
            TXT(0x00, '　【　雪拉扎德　】\n'),
            TXT(0x01, '　【　奥利维尔　】\n'),
            TXT(0x02, '　【　 阿加特 　】\n'),
            TXT(0x03, '　【　　提妲　　】\n'),
            TXT(0x04, '★【　　 金 　　】\n'),
            TXT(0x05, '　【　 科洛丝 　】\n'),
        ),
    )

    Jump('loc_304F')

    def _loc_2F48(): pass

    label('loc_2F48')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2FD4',
    )

    Menu(
        0,
        10,
        106,
        1,
        (
            TXT(0x00, '　【　雪拉扎德　】\n'),
            TXT(0x01, '　【　奥利维尔　】\n'),
            TXT(0x02, '　【　 阿加特 　】\n'),
            TXT(0x03, '　【　　提妲　　】\n'),
            TXT(0x04, '　【　　 金 　　】\n'),
            TXT(0x05, '★【　 科洛丝 　】\n'),
        ),
    )

    Jump('loc_304F')

    def _loc_2FD4(): pass

    label('loc_2FD4')

    Menu(
        0,
        10,
        106,
        0,
        (
            TXT(0x00, '　【　雪拉扎德　】\n'),
            TXT(0x01, '　【　奥利维尔　】\n'),
            TXT(0x02, '　【　 阿加特 　】\n'),
            TXT(0x03, '　【　　提妲　　】\n'),
            TXT(0x04, '　【　　 金 　　】\n'),
            TXT(0x05, '　【　 科洛丝 　】\n'),
        ),
    )

    def _loc_304F(): pass

    label('loc_304F')

    MenuEnd(0x0000)
    OP_5F(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3076'),
        (0x00000001, 'loc_3090'),
        (0x00000002, 'loc_30AA'),
        (0x00000003, 'loc_30C4'),
        (0x00000004, 'loc_30DE'),
        (0x00000005, 'loc_30F8'),
        (-1, 'loc_3112'),
    )

    def _loc_3076(): pass

    label('loc_3076')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_308A',
    )

    FormationAddMember(0x02, 0xFF)

    Jump('loc_308D')

    def _loc_308A(): pass

    label('loc_308A')

    FormationDelMember(0x02, 0xFF)

    def _loc_308D(): pass

    label('loc_308D')

    Jump('loc_318A')

    def _loc_3090(): pass

    label('loc_3090')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30A4',
    )

    FormationAddMember(0x03, 0xFF)

    Jump('loc_30A7')

    def _loc_30A4(): pass

    label('loc_30A4')

    FormationDelMember(0x03, 0xFF)

    def _loc_30A7(): pass

    label('loc_30A7')

    Jump('loc_318A')

    def _loc_30AA(): pass

    label('loc_30AA')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30BE',
    )

    FormationAddMember(0x05, 0xFF)

    Jump('loc_30C1')

    def _loc_30BE(): pass

    label('loc_30BE')

    FormationDelMember(0x05, 0xFF)

    def _loc_30C1(): pass

    label('loc_30C1')

    Jump('loc_318A')

    def _loc_30C4(): pass

    label('loc_30C4')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30D8',
    )

    FormationAddMember(0x06, 0xFF)

    Jump('loc_30DB')

    def _loc_30D8(): pass

    label('loc_30D8')

    FormationDelMember(0x06, 0xFF)

    def _loc_30DB(): pass

    label('loc_30DB')

    Jump('loc_318A')

    def _loc_30DE(): pass

    label('loc_30DE')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30F2',
    )

    FormationAddMember(0x07, 0xFF)

    Jump('loc_30F5')

    def _loc_30F2(): pass

    label('loc_30F2')

    FormationDelMember(0x07, 0xFF)

    def _loc_30F5(): pass

    label('loc_30F5')

    Jump('loc_318A')

    def _loc_30F8(): pass

    label('loc_30F8')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_310C',
    )

    FormationAddMember(0x04, 0xFF)

    Jump('loc_310F')

    def _loc_310C(): pass

    label('loc_310C')

    FormationDelMember(0x04, 0xFF)

    def _loc_310F(): pass

    label('loc_310F')

    Jump('loc_318A')

    def _loc_3112(): pass

    label('loc_3112')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3126',
    )

    FormationDelMember(0x02, 0xFF)

    Jump('loc_3187')

    def _loc_3126(): pass

    label('loc_3126')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_313A',
    )

    FormationDelMember(0x03, 0xFF)

    Jump('loc_3187')

    def _loc_313A(): pass

    label('loc_313A')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_314E',
    )

    FormationDelMember(0x05, 0xFF)

    Jump('loc_3187')

    def _loc_314E(): pass

    label('loc_314E')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3162',
    )

    FormationDelMember(0x04, 0xFF)

    Jump('loc_3187')

    def _loc_3162(): pass

    label('loc_3162')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3176',
    )

    FormationDelMember(0x06, 0xFF)

    Jump('loc_3187')

    def _loc_3176(): pass

    label('loc_3176')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3187',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_3187(): pass

    label('loc_3187')

    Jump('loc_318A')

    def _loc_318A(): pass

    label('loc_318A')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31AD',
    )

    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0002, 0x0080)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_322D')

    def _loc_31AD(): pass

    label('loc_31AD')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31EC',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择除约修亚和艾丝蒂尔以外的两名成员。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_322D')

    def _loc_31EC(): pass

    label('loc_31EC')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_322D',
    )

    ChrSetFlags(0x0002, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择除约修亚和艾丝蒂尔以外的两名成员。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    def _loc_322D(): pass

    label('loc_322D')

    ChrSetPos(0x0101, 34210, 0, -9750, 350)
    ChrSetPos(0x0102, 33060, 0, -8430, 45)

    Jump('loc_2C7F')

    def _loc_3252(): pass

    label('loc_3252')

    OP_5F(0x0000)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(300, 0)
    Fade(1000)
    ChrSetPos(0x0101, 34210, 0, -9750, 350)
    ChrSetPos(0x0102, 33060, 0, -8430, 45)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    ChrSetPos(0x0002, 32130, 0, -9730, 45)
    ChrSetPos(0x0003, 33020, 0, -10520, 45)
    Call(0, 0x0012)
    CameraMove(35570, 0, -7090, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    Return()

# id: 0x0012 offset: 0x32FE
@scena.Code('func_12_32FE')
def func_12_32FE():
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 34700, 0, -7770, 225)

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_333B',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 35690, 0, -4120, 180)

    Jump('loc_3340')

    def _loc_333B(): pass

    label('loc_333B')

    ChrSetFlags(0x000B, 0x0080)

    def _loc_3340(): pass

    label('loc_3340')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3367',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 34740, 0, -6560, 180)

    Jump('loc_336C')

    def _loc_3367(): pass

    label('loc_3367')

    ChrSetFlags(0x000C, 0x0080)

    def _loc_336C(): pass

    label('loc_336C')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3393',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 37870, 0, -7040, 225)

    Jump('loc_3398')

    def _loc_3393(): pass

    label('loc_3393')

    ChrSetFlags(0x0009, 0x0080)

    def _loc_3398(): pass

    label('loc_3398')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33BF',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 37210, 0, -5860, 225)

    Jump('loc_33C4')

    def _loc_33BF(): pass

    label('loc_33BF')

    ChrSetFlags(0x0008, 0x0080)

    def _loc_33C4(): pass

    label('loc_33C4')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33EB',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 39350, 0, -8220, 270)

    Jump('loc_33F0')

    def _loc_33EB(): pass

    label('loc_33EB')

    ChrSetFlags(0x000D, 0x0080)

    def _loc_33F0(): pass

    label('loc_33F0')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3417',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 36420, 0, -7530, 225)

    Jump('loc_341C')

    def _loc_3417(): pass

    label('loc_3417')

    ChrSetFlags(0x000A, 0x0080)

    def _loc_341C(): pass

    label('loc_341C')

    Return()

# id: 0x0013 offset: 0x341D
@scena.Code('func_13_341D')
def func_13_341D():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
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

    Menu(
        0,
        10,
        32,
        1,
        (
            TXT(0x00, '在此休息\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35D9',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_72(0x0010, 0x0020)
    OP_6F(0x0010, 300)
    OP_70(0x0010, 500)
    OP_73(0x0010)
    OP_6F(0x0010, 500)
    OP_70(0x0010, 700)
    OP_71(0x0010, 0x0020)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x06, 0x02)
    LoadEffect(0x05, 'map\\\\mp027_01.eff')
    PlayEffect(0x05, 0x06, 0x00FF, 38290, 1200, -3310, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1500, 0, -1)
    Sleep(1500)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x00)
    Sleep(3500)

    StopEffect(0x06, 0x00)
    LoadEffect(0x05, 'map\\\\mp027_00.eff')
    PlayEffect(0x05, 0x00, 0x00FF, 38290, 1200, -3310, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0010, 0)
    OP_70(0x0010, 250)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_35D9(): pass

    label('loc_35D9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35F3',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_35F3(): pass

    label('loc_35F3')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
