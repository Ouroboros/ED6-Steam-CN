import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2310_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2310   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '迪恩'),
    TXT(0x02, '雷斯'),
    TXT(0x03, '洛克'),
    TXT(0x04, '青年'),
    TXT(0x05, '青年'),
    TXT(0x06, '青年'),
    TXT(0x07, '青年'),
    TXT(0x08, '青年'),
    TXT(0x09, '青年'),
    TXT(0x0A, '秘书基尔巴特'),
    TXT(0x0B, '卡露娜'),
    TXT(0x0C, '阿梅莉娅'),
    TXT(0x0D, '扎古'),
    TXT(0x0E, '索雷诺'),
    TXT(0x0F, '塞尔吉村长'),
    TXT(0x10, ''),
]

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

# id: 0xFFFF offset: 0x282F
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
        ('ED6_DT07/CH00374._CH', 'ED6_DT07/CH00374P._CP'),
        ('ED6_DT07/CH02420._CH', 'ED6_DT07/CH02420P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -31270,
            z                   = 0,
            y                   = 42780,
            direction           = 90,
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
            x                   = -30310,
            z                   = 0,
            y                   = 42270,
            direction           = 90,
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
            x                   = -28770,
            z                   = 0,
            y                   = 42770,
            direction           = 90,
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
            x                   = -31020,
            z                   = 0,
            y                   = 44700,
            direction           = 90,
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
            x                   = -30070,
            z                   = 0,
            y                   = 44130,
            direction           = 90,
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
            x                   = -29310,
            z                   = 0,
            y                   = 43790,
            direction           = 90,
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
            x                   = -31330,
            z                   = 0,
            y                   = 43790,
            direction           = 90,
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
            x                   = -30780,
            z                   = 0,
            y                   = 43810,
            direction           = 90,
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
            x                   = -30050,
            z                   = 0,
            y                   = 43240,
            direction           = 90,
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
            x                   = -26650,
            z                   = 0,
            y                   = 44050,
            direction           = 180,
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
            x                   = -30050,
            z                   = 0,
            y                   = 39240,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -200,
            z                   = 0,
            y                   = 8850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -3700,
            z                   = 0,
            y                   = 5500,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -25570,
            z                   = 0,
            y                   = 2300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -27510,
            z                   = 0,
            y                   = 8670,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
    )

# id: 0x10003 offset: 0x2C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x2C2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2C2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_2FF',
    )

    SetChrPos(0x0014, -26670, 0, 39530, 90)
    SetChrPos(0x0016, -30150, 0, 3860, 270)
    SetChrPos(0x0015, -29310, 0, 43880, 0)

    Jump('loc_3E4')

    def _loc_2FF(): pass

    label('loc_2FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_313',
    )

    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0014, 0x0008)

    Jump('loc_3E4')

    def _loc_313(): pass

    label('loc_313')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_31D',
    )

    Jump('loc_3E4')

    def _loc_31D(): pass

    label('loc_31D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_33B',
    )

    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0014, 0x0008)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0015, 0x0008)

    Jump('loc_3E4')

    def _loc_33B(): pass

    label('loc_33B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_359',
    )

    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0014, 0x0008)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0015, 0x0008)

    Jump('loc_3E4')

    def _loc_359(): pass

    label('loc_359')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_396',
    )

    SetChrPos(0x0014, -26670, 0, 39530, 90)
    SetChrPos(0x0016, -30150, 0, 3860, 270)
    SetChrPos(0x0015, -29310, 0, 43880, 0)

    Jump('loc_3E4')

    def _loc_396(): pass

    label('loc_396')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_3D3',
    )

    SetChrPos(0x0014, -26670, 0, 39530, 90)
    SetChrPos(0x0016, -30150, 0, 3860, 270)
    SetChrPos(0x0015, -29310, 0, 43880, 0)

    Jump('loc_3E4')

    def _loc_3D3(): pass

    label('loc_3D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_3DD',
    )

    Jump('loc_3E4')

    def _loc_3DD(): pass

    label('loc_3DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_3E4',
    )

    def _loc_3E4(): pass

    label('loc_3E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_411',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x04)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x001F, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_411',
    )

    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0013, 0x0008)

    def _loc_411(): pass

    label('loc_411')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_41F',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0008)

    def _loc_41F(): pass

    label('loc_41F')

    Return()

# id: 0x0001 offset: 0x420
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_438',
    )

    OP_B1('t2310_y')

    Jump('loc_441')

    def _loc_438(): pass

    label('loc_438')

    OP_B1('t2310_n')

    def _loc_441(): pass

    label('loc_441')

    Return()

# id: 0x0002 offset: 0x442
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_457',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_457(): pass

    label('loc_457')

    Return()

# id: 0x0003 offset: 0x458
@scena.Code('func_03_458')
def func_03_458():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_4A9',
    )

    ChrTalk(
        0x00FE,
        (
            '扎古这次\n',
            '又跑到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还想要他\n',
            '去卢安买东西呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF4')

    def _loc_4A9(): pass

    label('loc_4A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_542',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_510',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '听说犯人都藏在\n',
            '巴伦诺灯塔里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道守护灯塔的\n',
            '弗科特爷爷有没有出事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_53F')

    def _loc_510(): pass

    label('loc_510')

    ChrTalk(
        0x00FE,
        (
            '不知道守护灯塔的\n',
            '弗科特爷爷有没有出事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53F(): pass

    label('loc_53F')

    Jump('loc_EF4')

    def _loc_542(): pass

    label('loc_542')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_5CD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '孩子们都一边哭，\n',
            '一边回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是让人担心啊……\n',
            '是不是碰到什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5CA')

    def _loc_5A9(): pass

    label('loc_5A9')

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '扎古去了哪里呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5CA(): pass

    label('loc_5CA')

    Jump('loc_EF4')

    def _loc_5CD(): pass

    label('loc_5CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_A01',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_946',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001F, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8FD',
    )

    OP_28(0x001F, 0x01, 0x8000)

    If(
        (
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_70B',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，是各位游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '叔父还是没有回家来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，已经没事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '现在，您叔父\n',
            '应该已经精神抖擞地向卢安进发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F您叔父在古罗尼山道\n',
            '被魔兽袭击的时候，\n',
            '我们正巧路过把他救了出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他没有受伤，请您放心。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_865')

    def _loc_70B(): pass

    label('loc_70B')

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '叔父真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道真的\n',
            '自己一个人\n',
            '去了古罗尼山道吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，\n',
            '你说的那个叔父，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '难不成是去采野菜了吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '他确实这么说过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那就没事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他现在正在去卢安的路上呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F您叔父在古罗尼山道\n',
            '被魔兽袭击的时候，\n',
            '我们正巧路过把他救了出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他没有受伤，请您放心。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_865(): pass

    label('loc_865')

    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对不起啊。\n',
            '给你们添麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '发生那种事情，\n',
            '叔父好歹也该跟家里说一声吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '他也太性急了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_943')

    def _loc_8FD(): pass

    label('loc_8FD')

    ChrTalk(
        0x00FE,
        (
            '对不起啊。\n',
            '给你们添麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '叔父他也太性急了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_943(): pass

    label('loc_943')

    Jump('loc_9FE')

    def _loc_946(): pass

    label('loc_946')

    ChrTalk(
        0x00FE,
        (
            '以前我是和扎古还有叔父\n',
            '三个人一起生活的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从奥维德叔父走了之后\n',
            '已经过了好几年了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他偶尔也会回来，\n',
            '但是马上又不见踪影了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '我可不希望扎古也变成那样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_9FE(): pass

    label('loc_9FE')

    Jump('loc_EF4')

    def _loc_A01(): pass

    label('loc_A01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_AD3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A91',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '听说孤儿院的火灾\n',
            '是有人故意纵火造成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好过分啊……\n',
            '那些人为什么要这么做……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我等会儿也要去\n',
            '卡拉那里帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AD0')

    def _loc_A91(): pass

    label('loc_A91')

    ChrTalk(
        0x00FE,
        (
            '听说孤儿院的火灾\n',
            '是有人故意纵火造成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好过分啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AD0(): pass

    label('loc_AD0')

    Jump('loc_EF4')

    def _loc_AD3(): pass

    label('loc_AD3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_BB4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B5F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '昨天晚上，一听说孤儿院着火，\n',
            '扎古就飞奔出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在好像又在\n',
            '处理火灾的后事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候\n',
            '他还真靠得住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BB1')

    def _loc_B5F(): pass

    label('loc_B5F')

    ChrTalk(
        0x00FE,
        (
            '昨天晚上，一听说孤儿院着火，\n',
            '扎古就飞奔出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候\n',
            '他还真靠得住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BB1(): pass

    label('loc_BB1')

    Jump('loc_EF4')

    def _loc_BB4(): pass

    label('loc_BB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_CAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C4B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '啊啊～\n',
            '老是担心弟弟的话，\n',
            '我就要成老寡妇了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在扎古成家之前，\n',
            '还是得不断操心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '实在没办法\n',
            '先考虑自己的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CAC')

    def _loc_C4B(): pass

    label('loc_C4B')

    ChrTalk(
        0x00FE,
        (
            '啊啊～\n',
            '老是担心弟弟的话，\n',
            '我就要成老寡妇了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在扎古成家之前，\n',
            '还是得不断操心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CAC(): pass

    label('loc_CAC')

    Jump('loc_EF4')

    def _loc_CAF(): pass

    label('loc_CAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_D8C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D3F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '扎古今后\n',
            '到底想做什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不认真工作的话，\n',
            '可不会有女孩子喜欢上他哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个孩子，\n',
            '一直都很让人替他操心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D89')

    def _loc_D3F(): pass

    label('loc_D3F')

    ChrTalk(
        0x00FE,
        (
            '扎古今后\n',
            '到底想做什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个孩子，\n',
            '一直都很让人替他操心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D89(): pass

    label('loc_D89')

    Jump('loc_EF4')

    def _loc_D8C(): pass

    label('loc_D8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_DF6',
    )

    ChrTalk(
        0x00FE,
        (
            '问我有没有看到一个男孩？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要说这村里的孩子，\n',
            '只有卢希娅一个，\n',
            '看来他不是这个村里的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF4')

    def _loc_DF6(): pass

    label('loc_DF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_EF4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E94',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '扎古在卢安工作的时候被开除了，\n',
            '然后就回村里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '一点也不为自己的将来着想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我作为他的姐姐，\n',
            '为他担心得不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF4')

    def _loc_E94(): pass

    label('loc_E94')

    ChrTalk(
        0x00FE,
        (
            '扎古在卢安工作的时候被开除了，\n',
            '然后就回村里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '一点也不为自己的将来着想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EF4(): pass

    label('loc_EF4')

    TalkEnd(0x0013)

    Return()

# id: 0x0004 offset: 0xEF8
@scena.Code('func_04_EF8')
def func_04_EF8():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1012',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FAB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '真没想到竟然是市长他们犯的罪，\n',
            '太让人吃惊了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，事件被查证清楚后\n',
            '老师他们应该也能获得赔偿金吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是修建孤儿院的话，\n',
            '我是很乐意帮忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_100F')

    def _loc_FAB(): pass

    label('loc_FAB')

    ChrTalk(
        0x00FE,
        (
            '事件被查证清楚后，\n',
            '老师他们应该也能获得赔偿金吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是修建孤儿院的话，\n',
            '我是很乐意帮忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_100F(): pass

    label('loc_100F')

    Jump('loc_15A8')

    def _loc_1012(): pass

    label('loc_1012')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_10DC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_108D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '纵火犯被关起来了，\n',
            '是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是你们逮捕他们的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '干得好啊！\n',
            '不愧是守护正义的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D9')

    def _loc_108D(): pass

    label('loc_108D')

    ChrTalk(
        0x00FE,
        (
            '就是你们\n',
            '把纵火犯给逮捕了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '干得好啊！\n',
            '不愧是守护正义的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10D9(): pass

    label('loc_10D9')

    Jump('loc_15A8')

    def _loc_10DC(): pass

    label('loc_10DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_126D',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001F, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_1193',
    )

    ChrTalk(
        0x00FE,
        (
            '就是你们\n',
            '救了叔父吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是非常感谢。\n',
            '这么忙还劳烦你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，孤儿院事件的\n',
            '调查工作也要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '做出那种事情的家伙，\n',
            '我是绝对不会原谅他的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_126A')

    def _loc_1193(): pass

    label('loc_1193')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_121A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '失火现场的整理\n',
            '终于告一段落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '到底是谁做出这种事情的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可恶，\n',
            '我绝对不饶恕那些放火的犯人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_126A')

    def _loc_121A(): pass

    label('loc_121A')

    ChrTalk(
        0x00FE,
        (
            '失火现场的整理\n',
            '终于告一段落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可恶，\n',
            '我绝对不饶恕那些放火的犯人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_126A(): pass

    label('loc_126A')

    Jump('loc_15A8')

    def _loc_126D(): pass

    label('loc_126D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1342',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_131A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '那个城市……\n',
            '卢安变了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前卢安是以贸易\n',
            '和渔业为中心的城镇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在渐渐被游客看作是\n',
            '观光和休闲胜地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近听说那里\n',
            '治安有点不太好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_133F')

    def _loc_131A(): pass

    label('loc_131A')

    ChrTalk(
        0x00FE,
        (
            '最近听说卢安的\n',
            '治安有点不太好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_133F(): pass

    label('loc_133F')

    Jump('loc_15A8')

    def _loc_1342(): pass

    label('loc_1342')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_144B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13E9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我也去过\n',
            '玛西亚孤儿院。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时候会和索雷诺那家伙\n',
            '一起去帮忙干些体力活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为那里只有\n',
            '特蕾莎老师一个人在打理，\n',
            '一个男的劳动力都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1448')

    def _loc_13E9(): pass

    label('loc_13E9')

    ChrTalk(
        0x00FE,
        (
            '我也去过\n',
            '玛西亚孤儿院。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为那里只有\n',
            '特蕾莎老师一个人在打理，\n',
            '一个男的劳动力都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1448(): pass

    label('loc_1448')

    Jump('loc_15A8')

    def _loc_144B(): pass

    label('loc_144B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_1492',
    )

    ChrTalk(
        0x00FE,
        (
            '……男孩吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一直在家，\n',
            '没有看到你说的那个男孩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A8')

    def _loc_1492(): pass

    label('loc_1492')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_15A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_153B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我曾经在卢安的港口工作过，\n',
            '不过现在我\n',
            '回到了自己的故乡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然还是在自己生长的\n',
            '土地上生活比较安稳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '除了姐姐一直\n',
            '在旁边啰里啰嗦的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A8')

    def _loc_153B(): pass

    label('loc_153B')

    ChrTalk(
        0x00FE,
        (
            '我曾经在卢安的港口工作过，\n',
            '不过现在我\n',
            '回到了自己的故乡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然还是在自己生长的\n',
            '土地上生活比较安稳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15A8(): pass

    label('loc_15A8')

    TalkEnd(0x0014)

    Return()

# id: 0x0005 offset: 0x15AC
@scena.Code('func_05_15AC')
def func_05_15AC():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_15F2',
    )

    ChrTalk(
        0x00FE,
        (
            '在这里也能听到\n',
            '孩子们玩耍的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B4E')

    def _loc_15F2(): pass

    label('loc_15F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_1648',
    )

    ChrTalk(
        0x00FE,
        (
            '犯人被逮捕了，\n',
            '我也松了一口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真不愧是游击士。\n',
            '果然很靠得住啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B4E')

    def _loc_1648(): pass

    label('loc_1648')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
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
        'loc_16F4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '玛西亚孤儿院的老师和孩子们\n',
            '到底被什么人袭击了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是同一伙犯人所为，\n',
            '为什么他们还要加害那些孩子们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些孩子们\n',
            '什么坏事也没有做啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1756')

    def _loc_16F4(): pass

    label('loc_16F4')

    ChrTalk(
        0x00FE,
        (
            '如果是同一伙犯人所为，\n',
            '为什么他们还要加害那些孩子们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些孩子们\n',
            '什么坏事也没有做啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1756(): pass

    label('loc_1756')

    Jump('loc_1B4E')

    def _loc_1759(): pass

    label('loc_1759')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1848',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17E9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '孤儿院里只剩下\n',
            '瓦砾和灰烬了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那天的火势\n',
            '还真是强啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里本来是一个能勾起老师和\n',
            '孩子们许多回忆的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1845')

    def _loc_17E9(): pass

    label('loc_17E9')

    ChrTalk(
        0x00FE,
        (
            '孤儿院里只剩下\n',
            '瓦砾和灰烬了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里本来是一个能勾起老师和\n',
            '孩子们许多回忆的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1845(): pass

    label('loc_1845')

    Jump('loc_1B4E')

    def _loc_1848(): pass

    label('loc_1848')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1917',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18CF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '明天要和扎古一起\n',
            '运送食物到孤儿院。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我考虑到孩子的数量，\n',
            '所以准备了很多哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在必须要开始准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1914')

    def _loc_18CF(): pass

    label('loc_18CF')

    ChrTalk(
        0x00FE,
        (
            '明天要和扎古一起\n',
            '运送食物到孤儿院。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在必须要开始准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1914(): pass

    label('loc_1914')

    Jump('loc_1B4E')

    def _loc_1917(): pass

    label('loc_1917')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_1A01',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19B2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '这个村的村民\n',
            '也在帮助玛西亚孤儿院。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特蕾莎院长\n',
            '真的是非常辛苦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '扎古辞掉了工作\n',
            '回到这里之后，\n',
            '好像经常去那里帮忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19FE')

    def _loc_19B2(): pass

    label('loc_19B2')

    ChrTalk(
        0x00FE,
        (
            '这个村的村民\n',
            '也在帮助玛西亚孤儿院。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特蕾莎院长\n',
            '真的是非常辛苦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19FE(): pass

    label('loc_19FE')

    Jump('loc_1B4E')

    def _loc_1A01(): pass

    label('loc_1A01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_1A3B',
    )

    ChrTalk(
        0x00FE,
        (
            '戴着帽子的男孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真抱歉，我没看到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B4E')

    def _loc_1A3B(): pass

    label('loc_1A3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1B4E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AEA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '啊呀，是旅行者吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果你们要找吃饭的地方，\n',
            '我推荐你们去『白之木莲亭』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里的饭菜味道很好，\n',
            '价格也非常适中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有许多额外的赠品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B4E')

    def _loc_1AEA(): pass

    label('loc_1AEA')

    ChrTalk(
        0x00FE,
        (
            '如果你们要找吃饭的地方，\n',
            '我推荐你们去『白之木莲亭』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『白之木莲亭』\n',
            '就在这座房屋的旁边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B4E(): pass

    label('loc_1B4E')

    TalkEnd(0x0015)

    Return()

# id: 0x0006 offset: 0x1B52
@scena.Code('func_06_1B52')
def func_06_1B52():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1BB5',
    )

    ChrTalk(
        0x00FE,
        (
            '真没想到戴尔蒙市长\n',
            '竟然做出这么过分的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直不敢相信，\n',
            '实在难以理解呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_235D')

    def _loc_1BB5(): pass

    label('loc_1BB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_1C64',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C26',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '哦哦，是几位游击士啊。\n',
            '听说你们抓到了犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要我们能帮得上忙，\n',
            '请你们尽管开口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C61')

    def _loc_1C26(): pass

    label('loc_1C26')

    ChrTalk(
        0x00FE,
        (
            '竟然做出这么过分的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们到底\n',
            '打算干什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C61(): pass

    label('loc_1C61')

    Jump('loc_235D')

    def _loc_1C64(): pass

    label('loc_1C64')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_1D3F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CEA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '事情的经过\n',
            '我已经听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一次还不够，\n',
            '竟然又做出如此令人发指的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这真是令人\n',
            '痛心不已啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D3C')

    def _loc_1CEA(): pass

    label('loc_1CEA')

    ChrTalk(
        0x00FE,
        (
            '一次还不够，\n',
            '竟然又做出如此令人发指的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这真是令人\n',
            '痛心不已啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D3C(): pass

    label('loc_1D3C')

    Jump('loc_235D')

    def _loc_1D3F(): pass

    label('loc_1D3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1DE6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DBA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '孤儿院的孩子们\n',
            '好像渐渐恢复精神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且也习惯了这里的生活，\n',
            '最近都能够听得到他们的笑声了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DE3')

    def _loc_1DBA(): pass

    label('loc_1DBA')

    ChrTalk(
        0x00FE,
        (
            '孤儿院的孩子们\n',
            '好像渐渐恢复精神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DE3(): pass

    label('loc_1DE3')

    Jump('loc_235D')

    def _loc_1DE6(): pass

    label('loc_1DE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1EE6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E9A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '哎呀～『白之木莲亭』的雷克斯\n',
            '主动向孤儿院提供房间，\n',
            '真是帮了院长和孩子们大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这就是患难见真情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也会不惜一切\n',
            '来帮助孤儿院的孩子们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EE3')

    def _loc_1E9A(): pass

    label('loc_1E9A')

    ChrTalk(
        0x00FE,
        (
            '这就是患难见真情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也会不惜一切\n',
            '来帮助孤儿院的孩子们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EE3(): pass

    label('loc_1EE3')

    Jump('loc_235D')

    def _loc_1EE6(): pass

    label('loc_1EE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_2060',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FCF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '昨天晚上，\n',
            '可以在这里看到东边的天空\n',
            '有红色的火光和冲天的黑烟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我马上叫\n',
            '村里的年轻人都赶去了，\n',
            '但还是没有免除全部烧毁的命运……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '孤儿院的老师和孩子们都没有受伤，\n',
            '这已经是不幸中的万幸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_205D')

    def _loc_1FCF(): pass

    label('loc_1FCF')

    ChrTalk(
        0x00FE,
        (
            '昨天晚上，\n',
            '可以在这里看到东边的天空\n',
            '有红色的火光和冲天的黑烟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我马上叫\n',
            '村里的年轻人都赶去了，\n',
            '但还是没有免除全部烧毁的命运……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_205D(): pass

    label('loc_205D')

    Jump('loc_235D')

    def _loc_2060(): pass

    label('loc_2060')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_2171',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2107',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '通往卢安的\n',
            '梅威海道被称为\n',
            '『风与海的道路』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那条街道的景色非常美丽，\n',
            '经常有舒服的海风吹过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我把去那里散步\n',
            '作为我的每日必行之事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_216E')

    def _loc_2107(): pass

    label('loc_2107')

    ChrTalk(
        0x00FE,
        (
            '通往卢安的\n',
            '梅威海道被称为\n',
            '『风与海的道路』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那条街道的景色非常美丽，\n',
            '经常有舒服的海风吹过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_216E(): pass

    label('loc_216E')

    Jump('loc_235D')

    def _loc_2171(): pass

    label('loc_2171')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_21E6',
    )

    ChrTalk(
        0x00FE,
        (
            '特蕾莎老师有时候\n',
            '会带着孤儿院的孩子们\n',
            '来玛诺利亚村玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都相处得非常好，\n',
            '就像亲兄弟姐妹一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_235D')

    def _loc_21E6(): pass

    label('loc_21E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_221A',
    )

    ChrTalk(
        0x00FE,
        (
            '男孩子吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他没有到这里来过哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_235D')

    def _loc_221A(): pass

    label('loc_221A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_235D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22F9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '哦，是旅行者啊。\n',
            '欢迎来到玛诺利亚村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前，这个村子是\n',
            '作为『驿站之村』而繁荣起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，自从定期船开航以来，\n',
            '这里过往的行人就明显减少了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在只能勉勉强强\n',
            '以『花之村』闻名了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_235D')

    def _loc_22F9(): pass

    label('loc_22F9')

    ChrTalk(
        0x00FE,
        (
            '自从定期船开航以来，\n',
            '这里过往的行人就明显减少了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在只能勉勉强强\n',
            '以『花之村』闻名了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_235D(): pass

    label('loc_235D')

    TalkEnd(0x0016)

    Return()

# id: 0x0007 offset: 0x2361
@scena.Code('func_07_2361')
def func_07_2361():
    TalkBegin(0x0012)

    ChrTalk(
        0x0012,
        (
            '那帮家伙由我看着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320061360V你们就赶去卢安，\n',
            '向嘉恩报告昨天的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0012)

    Return()

# id: 0x0008 offset: 0x23B2
@scena.Code('func_08_23B2')
def func_08_23B2():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-29840, 0, 41310, 0)
    FormationDelMember(0x05, 0xFF)
    SetChrPos(0x0101, -29970, 0, 37680, 0)
    SetChrPos(0x0102, -30850, 0, 37060, 0)
    SetChrPos(0x0105, -29450, 0, 36780, 0)
    SetChrDirection(0x0012, 180, 0)

    ChrTalk(
        0x0012,
        (
            '好了……\n',
            '那帮家伙由我看着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0320061336V你们就赶去卢安，\n',
            '向嘉恩报告昨天的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我们倒是没关系，不过……\n',
            '卡露娜姐姐您已经没事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '当然啦。只是被人抓住破绽，\n',
            '熏了点催眠药而已嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '还真是丢脸啊。\n',
            '竟然被那些家伙钻了空子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061341V#010F这也不能怪您。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们也是四人联手\n',
            '才勉强击退那些犯人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061343V#040F那些孩子们平安无事，\n',
            '也都多亏了卡露娜小姐啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061344V真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '哈哈……\n',
            '是啊，总算是不幸中的大幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '我听说阿加特\n',
            '自己一个人去追那帮家伙了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '虽然他的身手不容置疑，\n',
            '但说到底还是有点担心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯、嗯……\n',
            '要是没捉到他们反而受伤的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F现在也唯有相信阿加特先生了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '从昨天他所说的话判断，\n',
            '他好像一直在追那些犯人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对于他们的做事手法似乎也很了解，\n',
            '我想应该不会那么轻易失手的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……也对呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061353V所以，我们现在也应该\n',
            '尽力做好自己能做的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '没错，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '在事情了结之前，\n',
            '这些属于特蕾莎院长的捐款\n',
            '就先由我来暂代保管吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0320061356V这次我一定会保护好的，\n',
            '所以你们就安心出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F好的，拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#000F那么，Let’s go！',
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
