import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4300   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '雪拉扎德'),
    TXT(0x02, '奥利维尔'),
    TXT(0x03, '科洛丝'),
    TXT(0x04, '阿加特'),
    TXT(0x05, '提妲'),
    TXT(0x06, '金'),
    TXT(0x07, '拉赛尔博士'),
    TXT(0x08, '基库'),
    TXT(0x09, '特务兵'),
    TXT(0x0A, '特务兵'),
    TXT(0x0B, '特务兵'),
    TXT(0x0C, '特务兵'),
    TXT(0x0D, '特务兵'),
    TXT(0x0E, '特务兵'),
    TXT(0x0F, '特务兵'),
    TXT(0x10, '特务兵'),
    TXT(0x11, '特务兵'),
    TXT(0x12, '理查德上校'),
    TXT(0x13, '洛伦斯少尉'),
    TXT(0x14, '机器'),
    TXT(0x15, '机器'),
    TXT(0x16, '卡西乌斯'),
    TXT(0x17, '卡西乌斯'),
    TXT(0x18, '卡西乌斯'),
    TXT(0x19, '卡西乌斯'),
    TXT(0x1A, '卡西乌斯'),
    TXT(0x1B, '卡西乌斯'),
    TXT(0x1C, '卡西乌斯'),
    TXT(0x1D, '卡西乌斯'),
    TXT(0x1E, ''),
]

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

# id: 0xFFFF offset: 0x3446
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
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
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

# id: 0x10002 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x4DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x4DA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x4DA
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
@scena.Code('PreInit')
def PreInit():
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
    Event(0, 0x000C)

    def _loc_515(): pass

    label('loc_515')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_528',
    )

    SetMapFlags(0x40000000)
    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0010)

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
@scena.Code('Init')
def Init():
    LoadEffect(0x05, 'map\\\\mp027_00.eff')
    PlayEffect(0x05, 0x06, 0x00FF, 38290, 1200, -3310, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0002 offset: 0x594
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5A9',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

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

# id: 0x0004 offset: 0x61E
@scena.Code('func_04_61E')
def func_04_61E():
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

# id: 0x0005 offset: 0x6B0
@scena.Code('func_05_6B0')
def func_05_6B0():
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

# id: 0x0006 offset: 0x71C
@scena.Code('func_06_71C')
def func_06_71C():
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

# id: 0x0007 offset: 0x777
@scena.Code('func_07_777')
def func_07_777():
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

# id: 0x0008 offset: 0x7DF
@scena.Code('func_08_7DF')
def func_08_7DF():
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

# id: 0x0009 offset: 0x836
@scena.Code('func_09_836')
def func_09_836():
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
        'loc_8AB',
    )

    Call(0, 0x000A)
    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_8AB(): pass

    label('loc_8AB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8C2',
    )

    Call(0, 0x000B)
    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_8C2(): pass

    label('loc_8C2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_913',
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

    def _loc_913(): pass

    label('loc_913')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_924',
    )

    TalkEnd(0x000E)

    Return()

    def _loc_924(): pass

    label('loc_924')

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

# id: 0x000A offset: 0x99D
@scena.Code('func_0A_99D')
def func_0A_99D():
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

# id: 0x000B offset: 0x9DC
@scena.Code('func_0B_9DC')
def func_0B_9DC():
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

# id: 0x000C offset: 0xA02
@scena.Code('func_0C_A02')
def func_0C_A02():
    EventBegin(0x00)
    LoadEffect(0x00, 'battle\\\\btbomb00.eff')
    FadeIn(2000, 0)
    CameraMove(38000, 17050, -14020, 0)
    OP_67(0, 4150, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(418, 0)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    SetChrPos(0x0019, 34660, 0, -13430, 270)
    SetChrPos(0x001A, 35900, 0, -15200, 270)
    SetChrPos(0x0010, 36160, 0, -11160, 270)
    SetChrPos(0x0011, 37460, 0, -14780, 270)
    SetChrPos(0x0012, 37460, 0, -13340, 270)
    SetChrPos(0x0013, 36220, 0, -17220, 270)
    SetChrPos(0x0014, 37460, 0, -12070, 270)
    SetChrPos(0x0015, 39500, 0, -13290, 270)
    SetChrPos(0x0016, 39500, 0, -14730, 270)
    SetChrPos(0x0017, 37460, 0, -16090, 270)
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

    @scena.Lambda('lambda_0BA8')
    def lambda_0BA8():
        CameraMove(19210, 0, -13380, 3500)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0BA8)

    @scena.Lambda('lambda_0BC0')
    def lambda_0BC0():
        OP_6C(135000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0BC0)

    Sleep(2000)

    @scena.Lambda('lambda_0BD5')
    def lambda_0BD5():
        OP_67(0, 10910, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0BD5)

    @scena.Lambda('lambda_0BED')
    def lambda_0BED():
        OP_6E(514, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0BED)

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

    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    SetChrFlags(0x001B, 0x0004)
    SetChrFlags(0x001C, 0x0004)
    SetChrPos(0x001B, 18010, 20220, 5070, 108)
    SetChrPos(0x001C, 16410, 20220, -120, 108)

    @scena.Lambda('lambda_0D14')
    def lambda_0D14():
        ChrTurnDirection(0x00FE, 0x001A, 0)
        Yield()

        Jump('lambda_0D14')

    DispatchAsync2(0x001B, 0x0003, lambda_0D14)

    @scena.Lambda('lambda_0D25')
    def lambda_0D25():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_0D25')

    DispatchAsync2(0x001C, 0x0003, lambda_0D25)

    ClearChrFlags(0x001B, 0x0001)
    ClearChrFlags(0x001C, 0x0001)

    @scena.Lambda('lambda_0D40')
    def lambda_0D40():
        ChrMoveTo(0x00FE, 31350, 0, -12230, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_0D40)

    Sleep(300)

    @scena.Lambda('lambda_0D60')
    def lambda_0D60():
        ChrMoveTo(0x00FE, 31230, 0, -15680, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_0D60)

    ChrTurnDirection(0x001A, 0x001B, 400)

    @scena.Lambda('lambda_0D82')
    def lambda_0D82():
        CameraMove(32409, 0, -13750, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0D82)

    @scena.Lambda('lambda_0D9A')
    def lambda_0D9A():
        OP_6C(90000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0D9A)

    @scena.Lambda('lambda_0DAA')
    def lambda_0DAA():
        OP_67(0, 7160, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0DAA)

    ChrWalkTo(0x001A, 34460, 0, -15230, 5000, 0x00)

    @scena.Lambda('lambda_0DD6')
    def lambda_0DD6():
        ChrTurnDirection(0x00FE, 0x001C, 0)
        Yield()

        Jump('lambda_0DD6')

    DispatchAsync2(0x001A, 0x0001, lambda_0DD6)

    @scena.Lambda('lambda_0DE7')
    def lambda_0DE7():
        ChrTurnDirection(0x00FE, 0x001B, 0)
        Yield()

        Jump('lambda_0DE7')

    DispatchAsync2(0x0019, 0x0001, lambda_0DE7)

    SetChrChipByIndex(0x001A, 13)
    SetChrChipByIndex(0x0019, 15)
    PlaySE(231, 0x00, 0x64)
    WaitForThreadExit(0x001B, 0x0001)
    SetChrChipByIndex(0x001B, 12)
    SetChrFlags(0x001B, 0x0001)
    SetChrFlags(0x001C, 0x0001)

    @scena.Lambda('lambda_0E1B')
    def lambda_0E1B():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0E1B')

    DispatchAsync2(0x001B, 0x0000, lambda_0E1B)

    ChrTurnDirection(0x001B, 0x0019, 0)
    WaitForThreadExit(0x001C, 0x0001)
    SetChrChipByIndex(0x001C, 12)

    @scena.Lambda('lambda_0E3F')
    def lambda_0E3F():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0E3F')

    DispatchAsync2(0x001C, 0x0000, lambda_0E3F)

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

    @scena.Lambda('lambda_0F21')
    def lambda_0F21():
        OP_94(0x01, 0x00FE, 0x00B4, 0x0000044C, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0F21)

    @scena.Lambda('lambda_0F37')
    def lambda_0F37():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000320, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_0F37)

    Sleep(50)

    @scena.Lambda('lambda_0F52')
    def lambda_0F52():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000002BC, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_0F52)

    @scena.Lambda('lambda_0F68')
    def lambda_0F68():
        OP_94(0x01, 0x00FE, 0x00B4, 0x0000044C, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_0F68)

    Sleep(100)

    @scena.Lambda('lambda_0F83')
    def lambda_0F83():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0F83)

    @scena.Lambda('lambda_0F99')
    def lambda_0F99():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000514, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_0F99)

    Sleep(50)

    @scena.Lambda('lambda_0FB4')
    def lambda_0FB4():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0FB4)

    Sleep(50)

    @scena.Lambda('lambda_0FCF')
    def lambda_0FCF():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_0FCF)

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

    @scena.Lambda('lambda_104C')
    def lambda_104C():
        OP_6C(70000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_104C)

    CameraSetDistance(2900, 1500)
    SetChrFlags(0x001A, 0x0040)
    SetChrFlags(0x0019, 0x0040)

    @scena.Lambda('lambda_106F')
    def lambda_106F():
        CameraMove(30310, 0, -13620, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_106F)

    @scena.Lambda('lambda_1087')
    def lambda_1087():
        CameraSetDistance(2500, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_1087)

    @scena.Lambda('lambda_1097')
    def lambda_1097():
        OP_67(0, 5500, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_1097)

    @scena.Lambda('lambda_10AF')
    def lambda_10AF():
        OP_6C(42000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_10AF)

    ChrSetRGBAMask(0x001D, 255, 200, 200, 200, 0)
    ChrSetRGBAMask(0x001E, 255, 150, 150, 150, 0)
    ChrSetRGBAMask(0x001F, 255, 100, 100, 100, 0)
    ChrSetRGBAMask(0x0020, 255, 50, 50, 50, 0)
    ChrSetRGBAMask(0x0021, 200, 255, 255, 200, 0)
    ChrSetRGBAMask(0x0022, 150, 255, 255, 150, 0)
    ChrSetRGBAMask(0x0023, 100, 255, 255, 100, 0)
    ChrSetRGBAMask(0x0024, 50, 255, 255, 50, 0)
    CreateThread(0x0011, 0x00, 0x00, 0x000D)
    Sleep(530)

    PlaySE(501, 0x00, 0x64)
    PlayEffect(0x08, 0xFF, 0x00FF, 31350, 1500, -12230, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    TerminateThread(0x001B, 0xFF)
    Sleep(150)

    PlaySE(504, 0x00, 0x64)
    PlayEffect(0x08, 0xFF, 0x00FF, 31230, 1500, -15680, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    TerminateThread(0x001C, 0xFF)
    Sleep(900)

    @scena.Lambda('lambda_11A9')
    def lambda_11A9():
        CameraSetDistance(2900, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_11A9)

    @scena.Lambda('lambda_11B9')
    def lambda_11B9():
        OP_6C(19000, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_11B9)

    @scena.Lambda('lambda_11C9')
    def lambda_11C9():
        OP_67(0, 7160, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_11C9)

    @scena.Lambda('lambda_11E1')
    def lambda_11E1():
        CameraMove(30310, 0, -13620, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_11E1)

    SetChrFlags(0x001B, 0x0004)
    PlayEffect(0x00, 0xFF, 0x001B, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1233')
    def lambda_1233():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x001B, 0x0000, lambda_1233)

    @scena.Lambda('lambda_1245')
    def lambda_1245():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_1245)

    Sleep(300)

    SetChrFlags(0x001C, 0x0004)
    PlayEffect(0x00, 0xFF, 0x001C, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_129F')
    def lambda_129F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x001C, 0x0000, lambda_129F)

    @scena.Lambda('lambda_12B1')
    def lambda_12B1():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_12B1)

    Sleep(1500)

    @scena.Lambda('lambda_12D1')
    def lambda_12D1():
        OP_99(0x00FE, 0x09, 0x0B, 1600)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_12D1)

    @scena.Lambda('lambda_12E1')
    def lambda_12E1():
        ChrJumpTo(0x00FE, 31460, 0, -15350, 700, 4000)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_12E1)

    SetChrFlags(0x0019, 0x0800)

    @scena.Lambda('lambda_1304')
    def lambda_1304():
        OP_99(0x00FE, 0x05, 0x0B, 2000)

        ExitThread()

    DispatchAsync(0x0019, 0x0003, lambda_1304)

    WaitForThreadExit(0x0019, 0x0003)
    SetChrChipByIndex(0x0019, 15)
    SetChrSubChip(0x0019, 0)
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

    SetChrFlags(0x0019, 0x0020)
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

    SetChrFlags(0x001A, 0x0020)
    ChrTurnDirection(0x001A, 0x0019, 400)

    @scena.Lambda('lambda_13F0')
    def lambda_13F0():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_13F0')

    DispatchAsync2(0x001A, 0x0003, lambda_13F0)

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
    SetChrSubChip(0x001A, 0)
    SetChrChipByIndex(0x001A, 9)
    ClearChrFlags(0x001A, 0x0020)
    ClearChrFlags(0x001A, 0x0800)

    @scena.Lambda('lambda_153F')
    def lambda_153F():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_153F)

    @scena.Lambda('lambda_154F')
    def lambda_154F():
        CameraMove(35740, 0, -13960, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_154F)

    ClearChrFlags(0x0019, 0x0020)
    ClearChrFlags(0x0019, 0x0800)
    SetChrChipByIndex(0x0019, 8)
    ChrWalkTo(0x0019, 31590, 0, -13350, 2000, 0x00)
    SetChrDirection(0x0019, 90, 400)
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
    SetChrName('特务兵们')

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
    SetChrName('特务兵们')

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

    SetMapFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x1736
@scena.Code('func_0D_1736')
def func_0D_1736():
    CreateThread(0x001A, 0x01, 0x00, 0x000E)
    Sleep(70)

    CreateThread(0x001D, 0x01, 0x00, 0x000E)
    CreateThread(0x0019, 0x01, 0x00, 0x000F)
    Sleep(70)

    CreateThread(0x001E, 0x01, 0x00, 0x000E)
    CreateThread(0x0021, 0x01, 0x00, 0x000F)
    Sleep(70)

    CreateThread(0x001F, 0x01, 0x00, 0x000E)
    CreateThread(0x0022, 0x01, 0x00, 0x000F)
    Sleep(70)

    CreateThread(0x0020, 0x01, 0x00, 0x000E)
    CreateThread(0x0023, 0x01, 0x00, 0x000F)
    Sleep(70)

    CreateThread(0x0024, 0x01, 0x00, 0x000F)
    WaitForThreadExit(0x0020, 0x0001)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001E, 0x0080)
    SetChrFlags(0x001F, 0x0080)
    SetChrFlags(0x0020, 0x0080)
    WaitForThreadExit(0x0024, 0x0001)
    SetChrFlags(0x0021, 0x0080)
    SetChrFlags(0x0022, 0x0080)
    SetChrFlags(0x0023, 0x0080)
    SetChrFlags(0x0024, 0x0080)

    Return()

# id: 0x000E offset: 0x17C8
@scena.Code('func_0E_17C8')
def func_0E_17C8():
    SetChrChipByIndex(0x00FE, 13)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)
    SetChrPos(0x00FE, 34460, 0, -15230, 270)

    @scena.Lambda('lambda_17EE')
    def lambda_17EE():
        ChrTurnDirection(0x00FE, 0x001C, 0)
        Yield()

        Jump('lambda_17EE')

    DispatchAsync2(0x00FE, 0x0003, lambda_17EE)

    ChrJumpTo(0x00FE, 33350, 0, -15590, 1000, 9000)
    TerminateThread(0x00FE, 0x03)
    SetChrChipByIndex(0x00FE, 14)
    SetChrFlags(0x00FE, 0x0800)

    @scena.Lambda('lambda_1824')
    def lambda_1824():
        OP_99(0x00FE, 0x00, 0x05, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1824)

    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0004)
    ChrJumpTo(0x00FE, 32619, 1200, -15520, 1250, 5000)
    ChrMoveTo(0x00FE, 29300, 150, -15330, 13000, 0x00)

    Return()

# id: 0x000F offset: 0x1864
@scena.Code('func_0F_1864')
def func_0F_1864():
    ClearChrFlags(0x001A, 0x0800)
    SetChrChipByIndex(0x00FE, 15)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)
    SetChrPos(0x00FE, 34660, 0, -13430, 270)

    @scena.Lambda('lambda_188F')
    def lambda_188F():
        ChrTurnDirection(0x00FE, 0x001B, 0)
        Yield()

        Jump('lambda_188F')

    DispatchAsync2(0x00FE, 0x0003, lambda_188F)

    ChrMoveTo(0x00FE, 33410, 0, -12320, 5000, 0x00)
    TerminateThread(0x00FE, 0x03)
    SetChrChipByIndex(0x00FE, 16)
    SetChrFlags(0x00FE, 0x0800)

    @scena.Lambda('lambda_18C2')
    def lambda_18C2():
        OP_99(0x00FE, 0x00, 0x05, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_18C2)

    ChrWalkTo(0x00FE, 28880, 150, -12230, 11000, 0x00)

    Return()

# id: 0x0010 offset: 0x18E1
@scena.Code('func_10_18E1')
def func_10_18E1():
    EventBegin(0x00)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationAddMember(0x01, 0xFF)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    OP_4A(0x000E, 255)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    SetChrPos(0x0101, 37080, 0, -15050, 270)
    SetChrPos(0x0102, 37170, 0, -12980, 270)
    SetChrPos(0x000E, 38760, 0, -14790, 258)
    SetChrPos(0x000B, 37850, 0, -16410, 222)
    SetChrPos(0x000C, 39400, 0, -15590, 222)
    SetChrPos(0x0009, 39020, 0, -12220, 293)
    SetChrPos(0x0008, 39710, 0, -13330, 262)
    SetChrPos(0x000D, 40420, 0, -14130, 260)
    SetChrPos(0x000A, 38260, 0, -13640, 265)
    SetChrPos(0x000F, 40960, 500, -20390, 314)
    CameraMove(80, 0, 35850, 0)
    OP_67(0, 9440, -34740, 0)
    CameraSetDistance(1000, 0)
    OP_6C(0, 0)
    OP_6E(663, 0)
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_1A49')
    def lambda_1A49():
        CameraMove(50, 0, -20330, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A49)

    Sleep(3000)

    @scena.Lambda('lambda_1A66')
    def lambda_1A66():
        OP_6C(77000, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1A66)

    Sleep(7000)

    @scena.Lambda('lambda_1A7B')
    def lambda_1A7B():
        CameraMove(39590, 0, -14310, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A7B)

    @scena.Lambda('lambda_1A93')
    def lambda_1A93():
        OP_67(0, 22340, -34740, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1A93)

    @scena.Lambda('lambda_1AAB')
    def lambda_1AAB():
        OP_6E(343, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1AAB)

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

    @scena.Lambda('lambda_1D8F')
    def lambda_1D8F():
        OP_6E(300, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1D8F)

    @scena.Lambda('lambda_1D9F')
    def lambda_1D9F():
        OP_6C(90000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1D9F)

    @scena.Lambda('lambda_1DAF')
    def lambda_1DAF():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1DAF)

    @scena.Lambda('lambda_1DBD')
    def lambda_1DBD():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1DBD)

    Sleep(100)

    @scena.Lambda('lambda_1DD0')
    def lambda_1DD0():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1DD0)

    Sleep(100)

    @scena.Lambda('lambda_1DE3')
    def lambda_1DE3():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1DE3)

    @scena.Lambda('lambda_1DF1')
    def lambda_1DF1():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1DF1)

    Sleep(100)

    @scena.Lambda('lambda_1E04')
    def lambda_1E04():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1E04)

    @scena.Lambda('lambda_1E12')
    def lambda_1E12():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1E12)

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

    @scena.Lambda('lambda_201E')
    def lambda_201E():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_201E)

    @scena.Lambda('lambda_202C')
    def lambda_202C():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_202C)

    @scena.Lambda('lambda_203A')
    def lambda_203A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_203A)

    @scena.Lambda('lambda_2048')
    def lambda_2048():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2048)

    @scena.Lambda('lambda_2056')
    def lambda_2056():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2056)

    @scena.Lambda('lambda_2064')
    def lambda_2064():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2064)

    @scena.Lambda('lambda_2072')
    def lambda_2072():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2072)

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
        'loc_231C',
    )

    WaitEffect(0x17, 0x00)

    def _loc_231C(): pass

    label('loc_231C')

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
        'loc_2338',
    )

    WaitEffect(0x17, 0x00)

    def _loc_2338(): pass

    label('loc_2338')

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
        'loc_2354',
    )

    WaitEffect(0x17, 0x00)

    def _loc_2354(): pass

    label('loc_2354')

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
        'loc_2370',
    )

    WaitEffect(0x18, 0x00)

    def _loc_2370(): pass

    label('loc_2370')

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
        'loc_238C',
    )

    WaitEffect(0x18, 0x00)

    def _loc_238C(): pass

    label('loc_238C')

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
        'loc_23A8',
    )

    WaitEffect(0x18, 0x00)

    def _loc_23A8(): pass

    label('loc_23A8')

    SetChrFlags(0x000F, 0x0080)

    @scena.Lambda('lambda_23B3')
    def lambda_23B3():
        ChrTurnDirection(0x00FE, 0x000A, 0)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_23B3)

    @scena.Lambda('lambda_23C1')
    def lambda_23C1():
        ChrTurnDirection(0x00FE, 0x000A, 0)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_23C1)

    @scena.Lambda('lambda_23CF')
    def lambda_23CF():
        ChrTurnDirection(0x00FE, 0x000A, 0)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_23CF)

    @scena.Lambda('lambda_23DD')
    def lambda_23DD():
        ChrTurnDirection(0x00FE, 0x000A, 0)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_23DD)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24FA',
    )

    SetChrPos(0x000A, 36030, 0, -8640, 225)
    SetChrPos(0x000F, 36210, 0, -9110, 225)
    SetChrChipByIndex(0x000A, 17)
    SetChrSubChip(0x000A, 1)
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

    Jump('loc_2611')

    def _loc_24FA(): pass

    label('loc_24FA')

    @scena.Lambda('lambda_2500')
    def lambda_2500():
        SetChrDirection(0x00FE, 225, 0)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2500)

    SetChrPos(0x0105, 36030, 0, -8640, 225)
    SetChrPos(0x000F, 36210, 0, -9110, 225)
    SetChrChipByIndex(0x0105, 17)
    SetChrSubChip(0x0105, 1)
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

    def _loc_2611(): pass

    label('loc_2611')

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
    ClearChrFlags(0x000F, 0x0080)

    @scena.Lambda('lambda_269B')
    def lambda_269B():
        ChrTurnDirection(0x00FE, 0x000F, 800)
        Yield()

        Jump('lambda_269B')

    DispatchAsync2(0x0000, 0x0001, lambda_269B)

    @scena.Lambda('lambda_26AC')
    def lambda_26AC():
        ChrTurnDirection(0x00FE, 0x000F, 800)
        Yield()

        Jump('lambda_26AC')

    DispatchAsync2(0x0001, 0x0001, lambda_26AC)

    @scena.Lambda('lambda_26BD')
    def lambda_26BD():
        ChrTurnDirection(0x00FE, 0x000F, 800)
        Yield()

        Jump('lambda_26BD')

    DispatchAsync2(0x0002, 0x0001, lambda_26BD)

    @scena.Lambda('lambda_26CE')
    def lambda_26CE():
        ChrTurnDirection(0x00FE, 0x000F, 800)
        Yield()

        Jump('lambda_26CE')

    DispatchAsync2(0x0003, 0x0001, lambda_26CE)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26F4',
    )

    SetChrFlags(0x000A, 0x0020)
    SetChrSubChip(0x000A, 3)

    Jump('loc_2702')

    def _loc_26F4(): pass

    label('loc_26F4')

    TerminateThread(0x0105, 0xFF)
    SetChrFlags(0x0105, 0x0020)
    SetChrSubChip(0x0105, 3)

    def _loc_2702(): pass

    label('loc_2702')

    PlaySE(140, 0x00, 0x64)
    SetChrFlags(0x000F, 0x0040)
    SetChrFlags(0x000F, 0x0004)

    @scena.Lambda('lambda_2717')
    def lambda_2717():
        ChrWalkTo(0x00FE, 35070, 2000, -10300, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2717)

    Sleep(100)

    @scena.Lambda('lambda_2737')
    def lambda_2737():
        ChrWalkTo(0x00FE, 35070, 2000, -10300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2737)

    Sleep(100)

    @scena.Lambda('lambda_2757')
    def lambda_2757():
        ChrWalkTo(0x00FE, 35070, 2000, -10300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2757)

    Sleep(100)

    @scena.Lambda('lambda_2777')
    def lambda_2777():
        ChrWalkTo(0x00FE, 31500, 0, -12890, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2777)

    @scena.Lambda('lambda_2792')
    def lambda_2792():
        CameraMove(25620, 0, -12350, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2792)

    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27C9',
    )

    SetChrChipByIndex(0x000A, 2)
    ClearChrFlags(0x000A, 0x0020)
    SetChrSubChip(0x000A, 0)

    Jump('loc_27D8')

    def _loc_27C9(): pass

    label('loc_27C9')

    SetChrChipByIndex(0x0105, 65535)
    ClearChrFlags(0x0105, 0x0020)
    SetChrSubChip(0x0105, 0)

    def _loc_27D8(): pass

    label('loc_27D8')

    @scena.Lambda('lambda_27DE')
    def lambda_27DE():
        ChrWalkTo(0x00FE, 12310, 5000, -14560, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_27DE)

    Sleep(2500)

    @scena.Lambda('lambda_27FE')
    def lambda_27FE():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_27FE)

    @scena.Lambda('lambda_280C')
    def lambda_280C():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_280C)

    @scena.Lambda('lambda_281A')
    def lambda_281A():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_281A)

    @scena.Lambda('lambda_2828')
    def lambda_2828():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2828)

    @scena.Lambda('lambda_2836')
    def lambda_2836():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2836)

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
    SetChrFlags(0x000F, 0x0080)
    OP_4B(0x000E, 255)
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    OP_4B(0x000A, 255)
    OP_4B(0x000B, 255)
    OP_4B(0x000C, 255)
    OP_4B(0x000D, 255)
    CreateThread(0x000E, 0x00, 0x00, 0x0002)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x297C
@scena.Code('func_11_297C')
def func_11_297C():
    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_298D',
    )

    FormationDelMember(0x02, 0xFF)

    def _loc_298D(): pass

    label('loc_298D')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_299E',
    )

    FormationDelMember(0x03, 0xFF)

    def _loc_299E(): pass

    label('loc_299E')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29AF',
    )

    FormationDelMember(0x05, 0xFF)

    def _loc_29AF(): pass

    label('loc_29AF')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29C0',
    )

    FormationDelMember(0x04, 0xFF)

    def _loc_29C0(): pass

    label('loc_29C0')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29D1',
    )

    FormationDelMember(0x06, 0xFF)

    def _loc_29D1(): pass

    label('loc_29D1')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29E2',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_29E2(): pass

    label('loc_29E2')

    Fade(1000)
    SetChrPos(0x0101, 34210, 0, -9750, 350)
    SetChrPos(0x0102, 33060, 0, -8430, 45)
    SetChrPos(0x000E, 34700, 0, -7770, 222)
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

    def _loc_2AA9(): pass

    label('loc_2AA9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_307C',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B42',
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

    Jump('loc_2E79')

    def _loc_2B42(): pass

    label('loc_2B42')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BCE',
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

    Jump('loc_2E79')

    def _loc_2BCE(): pass

    label('loc_2BCE')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C5A',
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

    Jump('loc_2E79')

    def _loc_2C5A(): pass

    label('loc_2C5A')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CE6',
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

    Jump('loc_2E79')

    def _loc_2CE6(): pass

    label('loc_2CE6')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D72',
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

    Jump('loc_2E79')

    def _loc_2D72(): pass

    label('loc_2D72')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DFE',
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

    Jump('loc_2E79')

    def _loc_2DFE(): pass

    label('loc_2DFE')

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

    def _loc_2E79(): pass

    label('loc_2E79')

    MenuEnd(0x0000)
    OP_5F(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2EA0'),
        (0x00000001, 'loc_2EBA'),
        (0x00000002, 'loc_2ED4'),
        (0x00000003, 'loc_2EEE'),
        (0x00000004, 'loc_2F08'),
        (0x00000005, 'loc_2F22'),
        (-1, 'loc_2F3C'),
    )

    def _loc_2EA0(): pass

    label('loc_2EA0')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EB4',
    )

    FormationAddMember(0x02, 0xFF)

    Jump('loc_2EB7')

    def _loc_2EB4(): pass

    label('loc_2EB4')

    FormationDelMember(0x02, 0xFF)

    def _loc_2EB7(): pass

    label('loc_2EB7')

    Jump('loc_2FB4')

    def _loc_2EBA(): pass

    label('loc_2EBA')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2ECE',
    )

    FormationAddMember(0x03, 0xFF)

    Jump('loc_2ED1')

    def _loc_2ECE(): pass

    label('loc_2ECE')

    FormationDelMember(0x03, 0xFF)

    def _loc_2ED1(): pass

    label('loc_2ED1')

    Jump('loc_2FB4')

    def _loc_2ED4(): pass

    label('loc_2ED4')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EE8',
    )

    FormationAddMember(0x05, 0xFF)

    Jump('loc_2EEB')

    def _loc_2EE8(): pass

    label('loc_2EE8')

    FormationDelMember(0x05, 0xFF)

    def _loc_2EEB(): pass

    label('loc_2EEB')

    Jump('loc_2FB4')

    def _loc_2EEE(): pass

    label('loc_2EEE')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F02',
    )

    FormationAddMember(0x06, 0xFF)

    Jump('loc_2F05')

    def _loc_2F02(): pass

    label('loc_2F02')

    FormationDelMember(0x06, 0xFF)

    def _loc_2F05(): pass

    label('loc_2F05')

    Jump('loc_2FB4')

    def _loc_2F08(): pass

    label('loc_2F08')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F1C',
    )

    FormationAddMember(0x07, 0xFF)

    Jump('loc_2F1F')

    def _loc_2F1C(): pass

    label('loc_2F1C')

    FormationDelMember(0x07, 0xFF)

    def _loc_2F1F(): pass

    label('loc_2F1F')

    Jump('loc_2FB4')

    def _loc_2F22(): pass

    label('loc_2F22')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F36',
    )

    FormationAddMember(0x04, 0xFF)

    Jump('loc_2F39')

    def _loc_2F36(): pass

    label('loc_2F36')

    FormationDelMember(0x04, 0xFF)

    def _loc_2F39(): pass

    label('loc_2F39')

    Jump('loc_2FB4')

    def _loc_2F3C(): pass

    label('loc_2F3C')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F50',
    )

    FormationDelMember(0x02, 0xFF)

    Jump('loc_2FB1')

    def _loc_2F50(): pass

    label('loc_2F50')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F64',
    )

    FormationDelMember(0x03, 0xFF)

    Jump('loc_2FB1')

    def _loc_2F64(): pass

    label('loc_2F64')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F78',
    )

    FormationDelMember(0x05, 0xFF)

    Jump('loc_2FB1')

    def _loc_2F78(): pass

    label('loc_2F78')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F8C',
    )

    FormationDelMember(0x04, 0xFF)

    Jump('loc_2FB1')

    def _loc_2F8C(): pass

    label('loc_2F8C')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2FA0',
    )

    FormationDelMember(0x06, 0xFF)

    Jump('loc_2FB1')

    def _loc_2FA0(): pass

    label('loc_2FA0')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2FB1',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_2FB1(): pass

    label('loc_2FB1')

    Jump('loc_2FB4')

    def _loc_2FB4(): pass

    label('loc_2FB4')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FD7',
    )

    SetChrFlags(0x0003, 0x0080)
    SetChrFlags(0x0002, 0x0080)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3057')

    def _loc_2FD7(): pass

    label('loc_2FD7')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3016',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择除约修亚和艾丝蒂尔以外的两名成员。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_3057')

    def _loc_3016(): pass

    label('loc_3016')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3057',
    )

    SetChrFlags(0x0002, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择除约修亚和艾丝蒂尔以外的两名成员。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    def _loc_3057(): pass

    label('loc_3057')

    SetChrPos(0x0101, 34210, 0, -9750, 350)
    SetChrPos(0x0102, 33060, 0, -8430, 45)

    Jump('loc_2AA9')

    def _loc_307C(): pass

    label('loc_307C')

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
    SetChrPos(0x0101, 34210, 0, -9750, 350)
    SetChrPos(0x0102, 33060, 0, -8430, 45)
    ClearChrFlags(0x0002, 0x0080)
    ClearChrFlags(0x0003, 0x0080)
    SetChrPos(0x0002, 32130, 0, -9730, 45)
    SetChrPos(0x0003, 33020, 0, -10520, 45)
    Call(0, 0x0012)
    CameraMove(35570, 0, -7090, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    Return()

# id: 0x0012 offset: 0x3128
@scena.Code('func_12_3128')
def func_12_3128():
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 34700, 0, -7770, 225)

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3165',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 35690, 0, -4120, 180)

    Jump('loc_316A')

    def _loc_3165(): pass

    label('loc_3165')

    SetChrFlags(0x000B, 0x0080)

    def _loc_316A(): pass

    label('loc_316A')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3191',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 34740, 0, -6560, 180)

    Jump('loc_3196')

    def _loc_3191(): pass

    label('loc_3191')

    SetChrFlags(0x000C, 0x0080)

    def _loc_3196(): pass

    label('loc_3196')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31BD',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 37870, 0, -7040, 225)

    Jump('loc_31C2')

    def _loc_31BD(): pass

    label('loc_31BD')

    SetChrFlags(0x0009, 0x0080)

    def _loc_31C2(): pass

    label('loc_31C2')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31E9',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 37210, 0, -5860, 225)

    Jump('loc_31EE')

    def _loc_31E9(): pass

    label('loc_31E9')

    SetChrFlags(0x0008, 0x0080)

    def _loc_31EE(): pass

    label('loc_31EE')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3215',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 39350, 0, -8220, 270)

    Jump('loc_321A')

    def _loc_3215(): pass

    label('loc_3215')

    SetChrFlags(0x000D, 0x0080)

    def _loc_321A(): pass

    label('loc_321A')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3241',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 36420, 0, -7530, 225)

    Jump('loc_3246')

    def _loc_3241(): pass

    label('loc_3241')

    SetChrFlags(0x000A, 0x0080)

    def _loc_3246(): pass

    label('loc_3246')

    Return()

# id: 0x0013 offset: 0x3247
@scena.Code('func_13_3247')
def func_13_3247():
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
        'loc_3403',
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
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
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

    def _loc_3403(): pass

    label('loc_3403')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_341D',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_341D(): pass

    label('loc_341D')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
