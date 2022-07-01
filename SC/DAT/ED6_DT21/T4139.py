import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4139_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4139   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '爱尔莎大使'),
    TXT(0x02, '约克姆派驻官'),
    TXT(0x03, '法拉'),
    TXT(0x04, '贝尼乔参事官'),
    TXT(0x05, '珊蒂'),
    TXT(0x06, '莉卡妲夫人'),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4139.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T4139_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x41DE
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
        ('ED6_DT27/CH03723._CH', 'ED6_DT27/CH03723P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 55000,
            z                   = 200,
            y                   = 65540,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -54910,
            z                   = 0,
            y                   = 61420,
            direction           = 101,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -51570,
            z                   = 0,
            y                   = -44740,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 55260,
            z                   = 0,
            y                   = 10640,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -6760,
            z                   = 0,
            y                   = 7960,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -52030,
            z                   = 0,
            y                   = 58230,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
    )

# id: 0x10003 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 1030,
            triggerZ            = 6000,
            triggerY            = 33170,
            triggerRange        = 800,
            actorX              = 1030,
            actorZ              = 6500,
            actorY              = 33170,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1030,
            triggerZ            = 6000,
            triggerY            = 33170,
            triggerRange        = 800,
            actorX              = 1030,
            actorZ              = 6500,
            actorY              = 33170,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -60560,
            triggerZ            = 0,
            triggerY            = -46570,
            triggerRange        = 600,
            actorX              = -60560,
            actorZ              = 1000,
            actorY              = -46470,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -60560,
            triggerZ            = 0,
            triggerY            = -44950,
            triggerRange        = 600,
            actorX              = -60560,
            actorZ              = 1000,
            actorY              = -44700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -60560,
            triggerZ            = 0,
            triggerY            = -43230,
            triggerRange        = 600,
            actorX              = -60560,
            actorZ              = 1000,
            actorY              = -42960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x24E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_269',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_266',
    )

    ClearChrFlags(0x000D, 0x0080)

    def _loc_266(): pass

    label('loc_266')

    Jump('loc_2A4')

    def _loc_269(): pass

    label('loc_269')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_289',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)

    Jump('loc_2A4')

    def _loc_289(): pass

    label('loc_289')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_293',
    )

    Jump('loc_2A4')

    def _loc_293(): pass

    label('loc_293')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            Expr.Return,
        ),
        'loc_29D',
    )

    Jump('loc_2A4')

    def _loc_29D(): pass

    label('loc_29D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2A4',
    )

    def _loc_2A4(): pass

    label('loc_2A4')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_2B0'),
        (-1, 'loc_2C4'),
    )

    def _loc_2B0(): pass

    label('loc_2B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 4, 0x161C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C1',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x000A)

    def _loc_2C1(): pass

    label('loc_2C1')

    Jump('loc_2C4')

    def _loc_2C4(): pass

    label('loc_2C4')

    Return()

# id: 0x0001 offset: 0x2C5
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E1',
    )

    OP_B1('t4139_y')

    Jump('loc_2EA')

    def _loc_2E1(): pass

    label('loc_2E1')

    OP_B1('t4139_n')

    def _loc_2EA(): pass

    label('loc_2EA')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_309',
    )

    OP_64(0x00, 0x0001)
    OP_72(0x0002, 0x0010)

    Jump('loc_32A')

    def _loc_309(): pass

    label('loc_309')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31D',
    )

    OP_64(0x01, 0x0001)
    OP_72(0x0002, 0x0010)

    Jump('loc_32A')

    def _loc_31D(): pass

    label('loc_31D')

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_71(0x0002, 0x0010)

    def _loc_32A(): pass

    label('loc_32A')

    Jump('loc_33A')

    def _loc_32D(): pass

    label('loc_32D')

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_71(0x0002, 0x0010)
    def _loc_33A(): pass

    label('loc_33A')

    Return()

# id: 0x0002 offset: 0x33B
@scena.Code('ReInit')
def ReInit():
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
        'loc_360',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_4A2')

    def _loc_360(): pass

    label('loc_360')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_379',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_4A2')

    def _loc_379(): pass

    label('loc_379')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_392',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_4A2')

    def _loc_392(): pass

    label('loc_392')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AB',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_4A2')

    def _loc_3AB(): pass

    label('loc_3AB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C4',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_4A2')

    def _loc_3C4(): pass

    label('loc_3C4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DD',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_4A2')

    def _loc_3DD(): pass

    label('loc_3DD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F6',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_4A2')

    def _loc_3F6(): pass

    label('loc_3F6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40F',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_4A2')

    def _loc_40F(): pass

    label('loc_40F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_428',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_4A2')

    def _loc_428(): pass

    label('loc_428')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_441',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_4A2')

    def _loc_441(): pass

    label('loc_441')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45A',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_4A2')

    def _loc_45A(): pass

    label('loc_45A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_473',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_4A2')

    def _loc_473(): pass

    label('loc_473')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48C',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_4A2')

    def _loc_48C(): pass

    label('loc_48C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A2',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_4A2(): pass

    label('loc_4A2')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4B7',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_4A2')

    def _loc_4B7(): pass

    label('loc_4B7')

    Return()

# id: 0x0003 offset: 0x4B8
@scena.Code('func_03_4B8')
def func_03_4B8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4DB',
    )

    OP_8D(0x00FE, -59290, 60000, -52170, 63360, 2000)

    Jump('func_03_4B8')

    def _loc_4DB(): pass

    label('loc_4DB')

    Return()

# id: 0x0004 offset: 0x4DC
@scena.Code('func_04_4DC')
def func_04_4DC():
    TalkBegin(0x0008)
    ClearChrFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_501',
    )

    SetChrSubChip(0x0008, 1)

    Jump('loc_506')

    def _loc_501(): pass

    label('loc_501')

    SetChrSubChip(0x0008, 2)

    def _loc_506(): pass

    label('loc_506')

    OP_8C(0x0008, 180, 0)
    SetChrFlags(0x0008, 0x0010)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_998',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_995',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041B, 5, 0x20DD)),
            Expr.Return,
        ),
        'loc_5A7',
    )

    ChrTalk(
        0x0008,
        (
            '#0680370789V#1113F这样的话我们\n',
            '在黑暗中行动绝非上策。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680370790V#1110F虽然有不安，应该\n',
            '整理情绪做好万全的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_995')

    def _loc_5A7(): pass

    label('loc_5A7')

    ChrTalk(
        0x0101,
        (
            '#0010370791V#1000F爱尔莎大使，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680370792V#1110F艾丝蒂尔……来得正好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680370793V#1112F我就单刀直入地问了，\n',
            '有没有关于这个现象的情报？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680370794V看到王国军\n',
            '正式出动了，\n',
            '是不是预测到什么事态了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370795V#1013F（呜，好敏锐……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680370796V#1113F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680370797V呼，看来我\n',
            '也是相当着急了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680370798V#1110F看来利贝尔\n',
            '已经察觉有情况了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680370799V你即使知道什么\n',
            '应该也不会\n',
            '全盘告诉我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370800V#1016F嗯……对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680370801V#1111F别介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680370802V#1110F站在你的立场上想想，\n',
            '我也没什么理由抱怨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370803V#1000F爱尔莎大使……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680370804V#1112F我就问一件事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680370805V我们就这样\n',
            '等着没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370806V#1011F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370807V#1040F（就是说这事态就交给\n',
            '　游击士协会……交给我们\n',
            '　是吗。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370808V#1006F啊……是、是！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370809V现在，游击士协会和王国军\n',
            '正在尽全力搜查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370810V一定会解决这个现象，\n',
            '将一切都恢复原状的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680370811V#1111F呵呵，那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20DD)

    def _loc_995(): pass

    label('loc_995')

    Jump('loc_F84')

    def _loc_998(): pass

    label('loc_998')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_9AE',
    )

    Jump('loc_F84')

    def _loc_9AE(): pass

    label('loc_9AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_E2D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CA, 6, 0x1656)),
            Expr.Return,
        ),
        'loc_A21',
    )

    ChrTalk(
        0x0008,
        (
            '#0680250624V#1110F人一旦结缘\n',
            '就有可能获得强大的力量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250625V难得相识\n',
            '希望珍惜这缘分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E2A')

    def _loc_A21(): pass

    label('loc_A21')

    ChrTalk(
        0x0008,
        (
            '#0680250606V#1110F各位游击士……咦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250607V#1111F……今日带着\n',
            '好可爱的小姑娘啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250608V难道就是昨天说的\n',
            '克洛斯贝尔的小姑娘？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250609V#1011F啊，不是……\n',
            '不是这孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070250610V#064F嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250611V#060F初次见面。\n',
            '我是提妲·拉赛尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250612V#1112F……拉赛尔？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250613V难道是那个有名的\n',
            '拉赛尔博士的亲戚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070250614V#067F啊、是，拉赛尔博士\n',
            '是我的爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250615V#1113F是听说他有女儿夫妇，\n',
            '原来是孙女啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250616V#1111F呵呵，艾丝蒂尔也是，\n',
            '能遇上各种缘分真令人高兴啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250617V在卡尔瓦德，\n',
            '有『萍水相逢也是缘』\n',
            '这句俗话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250618V#070F与素不相识的人\n',
            '拂袖而过也是种缘分……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250619V记得是东方传来的话吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250620V#1110F嗯嗯，能和提妲\n',
            '相遇也是缘分啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250621V不仅如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250622V诸位能这样来到这里，\n',
            '或许也有重要的意义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250623V#1018F哦～真是浪漫的想法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250626V#1113F人一旦结缘\n',
            '就有可能获得强大的力量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250627V#1111F呵呵，当然不一定\n',
            '适合所有情况……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250628V难得相识\n',
            '希望珍惜这缘分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1656)

    def _loc_E2A(): pass

    label('loc_E2A')

    Jump('loc_F84')

    def _loc_E2D(): pass

    label('loc_E2D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            Expr.Return,
        ),
        'loc_F84',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EEC',
    )

    ChrTalk(
        0x0008,
        (
            '#0680250629V#1110F金先生几时预定\n',
            '等级提高到Ｓ级？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250630V据说大陆只有四个人\n',
            '的游击士专家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250631V第五个Ｓ级游击士，\n',
            '要是是出自于共和国的人就好了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F84')

    def _loc_EEC(): pass

    label('loc_EEC')

    ChrTalk(
        0x0008,
        (
            '#0680250632V#1110F艾丝蒂尔·布莱特吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250633V我们大使馆平时\n',
            '也总是承蒙协会的关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250603V今后，如果我们有委托\n',
            '你们能够接受就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F84(): pass

    label('loc_F84')

    SetChrSubChip(0x0008, 0)
    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xF8D
@scena.Code('func_05_F8D')
def func_05_F8D():
    TalkBegin(0x0009)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_109B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1098',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_FFF',
    )

    ChrTalk(
        0x00FE,
        (
            '过几天，共和国\n',
            '应该会派出调查团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们在那之前也有必要\n',
            '收集一些情报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1098')

    def _loc_FFF(): pass

    label('loc_FFF')

    ChrTalk(
        0x00FE,
        (
            '利贝尔的通讯\n',
            '要是全部断绝，这时候\n',
            '共和国也是一片骚乱吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '过几天，会找个代表\n',
            '应该会派出调查团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们在那之前也有必要\n',
            '收集一些情报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_1098(): pass

    label('loc_1098')

    Jump('loc_1373')

    def _loc_109B(): pass

    label('loc_109B')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1373',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_10B1',
    )

    Jump('loc_1373')

    def _loc_10B1(): pass

    label('loc_10B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_11C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1120',
    )

    ChrTalk(
        0x00FE,
        (
            '此次只是交换最终的文件\n',
            '确切的说还不是签字哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，为了方便理解，\n',
            '就这样称呼了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11C0')

    def _loc_1120(): pass

    label('loc_1120')

    ChrTalk(
        0x00FE,
        (
            '条约的缔结手续\n',
            '分为签字和批准两个阶段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '代表者确认条约的内容，\n',
            '作为证据签名就是签字……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '关于条约的内容国家最后确认，\n',
            '交换同意的文件就是批准。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_11C0(): pass

    label('loc_11C0')

    Jump('loc_1373')

    def _loc_11C3(): pass

    label('loc_11C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            Expr.Return,
        ),
        'loc_1250',
    )

    ChrTalk(
        0x00FE,
        (
            '爱尔莎大使的发言偶尔会过激\n',
            '我也捏着一把冷汗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，她对共和国的事\n',
            '是真的深思熟虑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对爱尔莎大使，\n',
            '我也不惜协力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1373')

    def _loc_1250(): pass

    label('loc_1250')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CA, 7, 0x1657)),
            Expr.Return,
        ),
        'loc_12B4',
    )

    ChrTalk(
        0x00FE,
        (
            '布置签字仪式真是\n',
            '忙得不可开交了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，想到是为了祖国，\n',
            '就一点儿也不觉得苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1373')

    def _loc_12B4(): pass

    label('loc_12B4')

    ChrTalk(
        0x00FE,
        (
            '怎么，金先生。\n',
            '又来利贝尔了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F约克姆爷爷，\n',
            '又得暂时麻烦你啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '话说回来，你好像\n',
            '忙得很啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然了，因为\n',
            '要布置条约的签字仪式啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，不好意思\n',
            '暂时没空管你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1657)

    def _loc_1373(): pass

    label('loc_1373')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x1377
@scena.Code('func_06_1377')
def func_06_1377():
    TalkBegin(0x000A)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_14AF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1404',
    )

    ChrTalk(
        0x00FE,
        (
            '我年轻的时候\n',
            '本就没有导力器之类的东西，\n',
            '所以并不像大家那样吃惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正是现在，才有机会\n',
            '帮上大使的忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14AF')

    def _loc_1404(): pass

    label('loc_1404')

    ChrTalk(
        0x00FE,
        (
            '我年轻的时候\n',
            '本就没有导力器之类的东西，\n',
            '所以并不像大家那样吃惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在导力器是司空见惯的了，\n',
            '我明白大家为何那么惊慌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正是现在，才有机会\n',
            '帮上大使的忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_14AF(): pass

    label('loc_14AF')

    Jump('loc_180F')

    def _loc_14B2(): pass

    label('loc_14B2')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_180F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1588',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1519',
    )

    ChrTalk(
        0x00FE,
        (
            '大使公开坦言\n',
            '讨厌埃雷波尼亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但其实其心里\n',
            '想的却是别的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1585')

    def _loc_1519(): pass

    label('loc_1519')

    ChrTalk(
        0x00FE,
        (
            '大使公开坦言\n',
            '讨厌埃雷波尼亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但其实其心里\n',
            '想的却是别的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼……\n',
            '我深深地明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1585(): pass

    label('loc_1585')

    Jump('loc_180F')

    def _loc_1588(): pass

    label('loc_1588')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_15F0',
    )

    ChrTalk(
        0x00FE,
        (
            '为何要做发出恐吓信\n',
            '这等悲哀的行为呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '国家之间亲密协作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底有哪里\n',
            '不利呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_180F')

    def _loc_15F0(): pass

    label('loc_15F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_180F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CB, 0, 0x1658)),
            Expr.Return,
        ),
        'loc_172D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            Expr.Return,
        ),
        'loc_16DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1650',
    )

    ChrTalk(
        0x00FE,
        (
            '我的推荐……\n',
            '还是『人偶骑士』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是暖人心怀的故事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16D8')

    def _loc_1650(): pass

    label('loc_1650')

    ChrTalk(
        0x00FE,
        (
            '如果有空，\n',
            '读读这里的书吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '书是心灵的营养，\n',
            '开卷有益哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的推荐……\n',
            '还是『人偶骑士』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是暖人心怀的故事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_16D8(): pass

    label('loc_16D8')

    Jump('loc_172A')

    def _loc_16DB(): pass

    label('loc_16DB')

    ChrTalk(
        0x00FE,
        (
            '金先生在利贝尔和共和国\n',
            '之间来来去去也真是辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可别勉强搞坏身体哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_172A(): pass

    label('loc_172A')

    Jump('loc_180F')

    def _loc_172D(): pass

    label('loc_172D')

    ChrTurnDirection(0x00FE, 0x0108, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，那大个子\n',
            '不是金先生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，无需看脸，\n',
            '就知道是谁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#073F喂喂，就靠体格\n',
            '来认我啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F……我们第一次\n',
            '遇到金先生的时候\n',
            '都误以为是熊来着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#044F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F……真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1658)

    def _loc_180F(): pass

    label('loc_180F')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x1813
@scena.Code('func_07_1813')
def func_07_1813():
    TalkBegin(0x000B)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1886',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1883',
    )

    ChrTalk(
        0x00FE,
        (
            '就连爱尔莎大使\n',
            '也是精疲力竭的样子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近连日，为了收集情报\n',
            '都不眠不休的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1883(): pass

    label('loc_1883')

    Jump('loc_1E65')

    def _loc_1886(): pass

    label('loc_1886')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_191C',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部什么的\n',
            '也引起了相当过激的事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，看这状况应该\n',
            '不会对签字仪式有什么影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能看出艾莉茜雅女王的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E65')

    def _loc_191C(): pass

    label('loc_191C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1A8A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1995',
    )

    ChrTalk(
        0x00FE,
        (
            '『克洛斯贝尔问题』\n',
            '对卡尔瓦德来说也是头痛问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '此次的互不侵犯条约会给议会\n',
            '带来怎样的影响……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A87')

    def _loc_1995(): pass

    label('loc_1995')

    ChrTalk(
        0x00FE,
        (
            '『克洛斯贝尔问题』\n',
            '对我们来说实在是头痛的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在，总统勉强\n',
            '封住了在野党的主张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但主张武力合并\n',
            '的意见绝对不算少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这就是每次，共和国议会\n',
            '都会暴乱的重大原因之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '此次的互不侵犯条约会给议会\n',
            '带来怎样的影响……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_1A87(): pass

    label('loc_1A87')

    Jump('loc_1E65')

    def _loc_1A8A(): pass

    label('loc_1A8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1E65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CB, 1, 0x1659)),
            Expr.Return,
        ),
        'loc_1C0B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            Expr.Return,
        ),
        'loc_1BB8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1B03',
    )

    ChrTalk(
        0x00FE,
        (
            '卢安是海上交通的要冲\n',
            '共和国的船也大量地出入着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长选举的结果\n',
            '必须经过检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BB5')

    def _loc_1B03(): pass

    label('loc_1B03')

    ChrTalk(
        0x00FE,
        (
            '卢安的市长选举\n',
            '不就是今天吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于戴尔蒙家的垮台\n',
            '将会有首个平民出身的卢安市长诞生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢安是海上交通的要冲\n',
            '共和国的船也大量地出入着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这可必须经过检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_1BB5(): pass

    label('loc_1BB5')

    Jump('loc_1C08')

    def _loc_1BB8(): pass

    label('loc_1BB8')

    ChrTalk(
        0x00FE,
        (
            '恐吓信只不过是恶作剧\n',
            '搞出来的勾当。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先听听爱尔莎大使\n',
            '的意见不好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1C08(): pass

    label('loc_1C08')

    Jump('loc_1E65')

    def _loc_1C0B(): pass

    label('loc_1C0B')

    ChrTalk(
        0x00FE,
        (
            '啊，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0108, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '呀呀，这不是金先生吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F参事官，又给你添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天还接二连三的……\n',
            '难道是客人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F嗯嗯，是协会的工作伙伴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……莫非是为了恐吓信的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F你真是明察。\n',
            '是来自王国军的委托。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#072F有什么线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个程度的恐吓信\n',
            '在共和国不算新奇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说实话，\n',
            '我并没在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#572F……的确国内是有\n',
            '不少过激的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，牵涉到移民问题\n',
            '每次必定引起事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯，有关这次的事\n',
            '我也没什么好说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E62',
    )

    ChrTalk(
        0x00FE,
        (
            '首先听听爱尔莎大使\n',
            '的意见不好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F嗯嗯，事不宜迟就这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E62(): pass

    label('loc_1E62')

    OP_A2(0x1659)

    def _loc_1E65(): pass

    label('loc_1E65')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x1E69
@scena.Code('func_08_1E69')
def func_08_1E69():
    TalkBegin(0x000C)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F78',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1F75',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1EE6',
    )

    ChrTalk(
        0x00FE,
        (
            '油灯不方便\n',
            '使用时需要注意\n',
            '不过总觉得有温暖的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的时候\n',
            '可能是有点不谨慎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F75')

    def _loc_1EE6(): pass

    label('loc_1EE6')

    ChrTalk(
        0x00FE,
        (
            '导力灯不能使用之后，\n',
            '就用火的油灯照明了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '油灯不方便\n',
            '使用时需要注意\n',
            '不过总觉得有温暖的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的时候\n',
            '可能是有点不谨慎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_1F75(): pass

    label('loc_1F75')

    Jump('loc_2207')

    def _loc_1F78(): pass

    label('loc_1F78')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2207',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1FE0',
    )

    ChrTalk(
        0x00FE,
        (
            '爱尔莎大使的话，\n',
            '去艾尔贝离宫视察了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么说\n',
            '都是签字仪式进行的会场嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2207')

    def _loc_1FE0(): pass

    label('loc_1FE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_20DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_204A',
    )

    ChrTalk(
        0x00FE,
        (
            '帝国的女佣\n',
            '毫无多余的举止，\n',
            '做事真是爽利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也试着学了学，\n',
            '还真是十分累人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D8')

    def _loc_204A(): pass

    label('loc_204A')

    ChrTalk(
        0x00FE,
        (
            '去百货商店采购\n',
            '偶然遇到了帝国\n',
            '大使馆的女佣哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帝国的女佣\n',
            '毫无多余的举止，\n',
            '真是精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也试着学了学，\n',
            '还真是十分累人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_20D8(): pass

    label('loc_20D8')

    Jump('loc_2207')

    def _loc_20DB(): pass

    label('loc_20DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2207',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CB, 2, 0x165A)),
            Expr.Return,
        ),
        'loc_2169',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            Expr.Return,
        ),
        'loc_211E',
    )

    ChrTalk(
        0x00FE,
        (
            '哼哼哼⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天难得全家\n',
            '去采购吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2166')

    def _loc_211E(): pass

    label('loc_211E')

    ChrTalk(
        0x00FE,
        (
            '金先生，随时\n',
            '都可以来住宿哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会打扫\n',
            '得干干净净地等你来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2166(): pass

    label('loc_2166')

    Jump('loc_2207')

    def _loc_2169(): pass

    label('loc_2169')

    ChrTurnDirection(0x00FE, 0x0108, 400)

    ChrTalk(
        0x00FE,
        (
            '……啊，金先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#071F哟，我又来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#070F可能要借用你的房间，\n',
            '到时候就靠你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，当然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会打扫\n',
            '得干干净净地等你来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x165A)

    def _loc_2207(): pass

    label('loc_2207')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0x220B
@scena.Code('func_09_220B')
def func_09_220B():
    TalkBegin(0x000D)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2320',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2320',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_227D',
    )

    ChrTalk(
        0x00FE,
        (
            '丈夫为了见女王，\n',
            '出发去格兰赛尔城了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明如果没有预约\n',
            '只能白白等着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2320')

    def _loc_227D(): pass

    label('loc_227D')

    ChrTalk(
        0x00FE,
        (
            '丈夫现在出门去\n',
            '格兰赛尔城了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了想办法和本国联络，\n',
            '说要找女王\n',
            '直接询问什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明如果没有预约\n',
            '只能白白等着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是那么不得要领的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_2320(): pass

    label('loc_2320')

    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0x2324
@scena.Code('func_0A_2324')
def func_0A_2324():
    EventBegin(0x00)
    OP_6D(-2640, 6000, 31460, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(315000, 0)
    OP_6E(467, 0)
    SetChrPos(0x0101, 1740, 0, 4440, 0)
    SetChrPos(0x0108, 470, 0, 4430, 0)
    SetChrPos(0x0104, 660, 0, 2980, 0)
    SetChrPos(0x0105, 2100, 0, 3060, 0)

    @scena.Lambda('lambda_23AD')
    def lambda_23AD():
        OP_6D(1080, 0, 6030, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_23AD)

    @scena.Lambda('lambda_23C5')
    def lambda_23C5():
        OP_67(0, 9000, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_23C5)

    OP_C8(0x0200, 0x0046, 'C_PLAC12._CH', 0x01, 0x07D0)
    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Fade(1000)
    OP_6D(1080, 0, 6030, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0104,
        (
            '#0040250501V#033F嗬，这可真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250502V#1011F#5P哦～这就是\n',
            '卡尔瓦德大使馆啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250503V到底是宏伟豪华啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250504V#048F还有这独特的\n',
            '异国情趣的内部装潢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250505V#070F#5P嗯，因为是接受了\n',
            '东方移民的国家嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0108, 90, 400)

    ChrTalk(
        0x0108,
        (
            '#0080250506V#070F#5P顺带一提爱尔莎大使的房间\n',
            '在2楼最里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250507V#1006F#4P嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x161C)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x25B7
@scena.Code('func_0B_25B7')
def func_0B_25B7():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 1240, 6000, 30810, 0)
    SetChrPos(0x0105, 1990, 6000, 29630, 0)
    SetChrPos(0x0104, 890, 6000, 29500, 0)
    SetChrPos(0x0108, 990, 6000, 32270, 180)
    OP_6D(880, 6000, 31940, 0)
    OP_67(0, 9360, -10000, 0)
    OP_6B(2360, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0108,
        (
            '#0080250508V#070F#5P这里就是大使的房间。\n',
            '马上去问吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
        0,
        (
            TXT(0x00, '【问问看】\n'),
            TXT(0x01, '【过一会再来】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_26DC'),
        (0x00000001, 'loc_2739'),
        (-1, 'loc_273C'),
    )

    def _loc_26DC(): pass

    label('loc_26DC')

    ChrTalk(
        0x0108,
        (
            '#0080250509V#070F#5P好，那么我们\n',
            '我来介绍你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0108, 0, 400)
    Sleep(500)

    OP_22(0x0071, 0x00, 0x64)
    Sleep(500)

    FadeOut(500, 0, -1)
    OP_0D()
    Call(0, 0x000C)

    Jump('loc_273C')

    def _loc_2739(): pass

    label('loc_2739')

    Jump('loc_273C')

    def _loc_273C(): pass

    label('loc_273C')

    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x273F
@scena.Code('func_0C_273F')
def func_0C_273F():
    EventBegin(0x00)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0105, 0x0080)
    SetChrFlags(0x0104, 0x0080)
    SetChrFlags(0x0108, 0x0080)
    SetChrPos(0x0101, 55250, 0, 53510, 0)
    SetChrPos(0x0105, 55250, 0, 53510, 0)
    SetChrPos(0x0104, 55250, 0, 53510, 0)
    SetChrPos(0x0108, 53600, 0, 57290, 0)
    OP_6D(54510, 0, 65790, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(500, 0)
    OP_0D()
    OP_62(0x0008, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0680250510V#1112F#2P……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250511V请，可以进来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250512V#2P……打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6D(54860, 0, 59130, 1500)
    SetChrPos(0x0108, 55250, 0, 53510, 0)
    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_2889')
    def lambda_2889():
        OP_6D(54870, 0, 64209, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2889)

    CreateThread(0x0108, 0x01, 0x00, 0x000D)
    Sleep(700)

    CreateThread(0x0101, 0x01, 0x00, 0x000E)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    CreateThread(0x0105, 0x01, 0x00, 0x000F)
    Sleep(500)

    CreateThread(0x0104, 0x01, 0x00, 0x0010)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0680250513V#1111F哎呀，这不是金先生吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250514V前阵子才刚回国\n',
            '又来利贝尔了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250515V#070F#6P呀，协会的工作\n',
            '还有些需要收尾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250516V所以大概还会\n',
            '暂时在利贝尔逗留吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250517V#1113F呵呵，不愧是Ａ级游击士。\n',
            '真是忙碌啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250518V#1110F对了，这些人是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250519V#1011F#6P嗯，幸会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250520V我是游击士协会所属的\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250521V这边的两位是协力的\n',
            '科洛丝和奥利维尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250522V#035F呼，请多指教大使殿下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250523V#048F初次见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250524V#1111F请多指教。\n',
            '我是卡尔瓦德共和国大使\n',
            '爱尔莎·柯库兰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250525V#1110F你们似乎是有麻烦\n',
            '才来拜访的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250526V#074F#6P嗯嗯，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等，询问了关于\n',
            '送到大使馆的恐吓信的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0680250527V#1113F那个恐吓信的事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250528V#1112F这么说你们\n',
            '是因王国军的委托而行动的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250529V#1002F#6P算是这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250530V不过，作为游击士协会\n',
            '也不能置之不理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250531V关于这个\n',
            '配合我们做一个调查吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250532V#1113F……嗯，也罢。\n',
            '和我们也有关系嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250533V#1110F那么，你们想问什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250534V#1015F#6P嗯，首先是关于威胁者\n',
            '您有没有线索？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250535V在共和国，是否有对条约缔结\n',
            '反对的势力存在等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250536V#1111F当然有了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250537V譬如我就是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010250538V#1020F#6P咦咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250539V#075F#6P我说大使……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250540V不要太戏弄\n',
            '年轻人行不行？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250541V#1110F哎呀，事实就是事实嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250542V我讨厌埃雷波尼亚\n',
            '这你也知道的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250543V#073F#6P这倒是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250544V#1111F呵呵，别误会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250545V总统已经决定\n',
            '议会也承认了这议案。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250546V我不会带个人感情\n',
            '去做事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250547V#1007F#6P是，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250548V#1015F那么其他\n',
            '反对的人们呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250549V#1113F有是有，不过是少数派。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250550V那些势力也应该\n',
            '不是当真要反对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250551V#1004F#6P不是当真反对？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250552V#1110F其实呢，互不侵犯条约本就\n',
            '不是具有实效性的条约。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250553V『国家间的对立不要经过战争\n',
            '用协商来和平解决吧』\n',
            '只是在提倡这种观点而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250554V从这个意义来说\n',
            '与其说是条约不如说是共同宣言。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250555V#030F只要情况需要，随时都可以\n',
            '破坏的口头约定而已吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250556V#1111F呵呵，正是如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250557V#1110F不过这十几年来，\n',
            '卡尔瓦德和埃雷波尼亚之间的关系\n',
            '变得越来越冷淡……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250558V通过这次机会\n',
            '来交流协商一下\n',
            '倒也是很有意义的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250559V#1015F#6P嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250560V确实不至于\n',
            '发出恐吓信来阻止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250561V#047F请问，爱尔莎大使。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250562V#042F如果卡尔瓦德相关人员\n',
            '不是恐吓犯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250563V那您认为谁比较可疑呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250564V#1110F呵呵，这个嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250565V以个人之见来说\n',
            '埃雷波尼亚的主战派\n',
            '非常可疑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250566V#1113F不过加上新型引擎的事\n',
            '这个可能性看来也不大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250567V#1004F#6P新型引擎……\n',
            '莫非是埃尔赛尤用的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250568V#1111F对，其样本会被\n',
            '呈送给卡尔瓦德和\n',
            '埃雷波尼亚双方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250569V在互不侵犯条约的签字仪式上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250570V#1004F#6P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250571V#031F呼，不愧是艾莉茜雅女王。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250572V完全将帝国和共和国\n',
            '掌控于股掌之间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250573V#1113F嗯嗯……\n',
            '虽然不甘心，但确实是个大人物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250574V#1112F新型引擎可说是新一代\n',
            '飞船的核心部件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250575V虽说只是样品，\n',
            '但到手的机会也是极为难得。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250576V就算是帝国的主战派\n',
            '应该也不想错失吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250577V#1016F#6P原、原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250578V#070F#6P唔，这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250579V帝国或共和国的人\n',
            '妨碍互不侵犯条约的可能性\n',
            '都是相当低的，没错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250580V#1110F是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250581V没帮上忙\n',
            '十分抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250582V#1006F#6P不，哪儿的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250583V嫌疑犯减少了\n',
            '就更容易判断状况了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250584V#1004F啊，此外还有\n',
            '别的事想问问……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '询问了爱尔莎大使关于玲的父母的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0680250585V#1112F克洛斯贝尔的贸易商\n',
            '哈罗德·海瓦斯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250586V#1113F唔，没有印象呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250587V至少应该没\n',
            '来过大使馆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250588V#1007F#6P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250589V#1110F说到克洛斯贝尔，\n',
            '那是帝国和共和国交界处的地区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250590V去帝国大使馆\n',
            '问问或许更好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250591V#1006F#6P好的，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250592V嗯，多谢您告诉我们\n',
            '这么多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250593V#1110F哎呀，客气什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250594V对了你……\n',
            '叫艾丝蒂尔·布莱特对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250595V难道是卡西乌斯准将的女儿？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250596V#1004F#6P啊，您认识我的父亲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250597V#1111F呵呵，当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250598V曾经战胜帝国军的英雄，\n',
            '王国军的新领导人嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250599V是听说他有个女儿\n',
            '没想到能以这种形式见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250600V#1015F#6P嗯，我还只是\n',
            '新手游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0680250601V#1110F嗯嗯，我明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250602V我们大使馆平时\n',
            '承蒙关照了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680250603V今后如果我们有委托的话，\n',
            '你们能接下就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250604V#1016F#6P啊哈哈……\n',
            '如果有机会的话，非常愿意效劳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250605V#1006F那么告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0000, 55140, 0, 59720, 180)
    SetChrPos(0x0001, 55140, 0, 59720, 180)
    SetChrPos(0x0002, 55140, 0, 59720, 180)
    SetChrPos(0x0003, 55140, 0, 59720, 180)
    OP_6D(55140, 0, 59720, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_71(0x0002, 0x0010)
    OP_64(0x00, 0x0001)
    OP_A2(0x161D)
    Sleep(500)

    FadeIn(1000, 0)
    OP_28(0x008B, 0x02, 0x0008)
    OP_28(0x008B, 0x01, 0x0010)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x3C24
@scena.Code('func_0D_3C24')
def func_0D_3C24():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_3C3A')
    def lambda_3C3A():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3C3A)

    OP_8E(0x00FE, 55930, 0, 62760, 2500, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x000E offset: 0x3C62
@scena.Code('func_0E_3C62')
def func_0E_3C62():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_3C78')
    def lambda_3C78():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3C78)

    OP_8E(0x00FE, 55020, 0, 62190, 2500, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x000F offset: 0x3CA0
@scena.Code('func_0F_3CA0')
def func_0F_3CA0():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_3CB6')
    def lambda_3CB6():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3CB6)

    OP_8E(0x00FE, 55890, 0, 60910, 2500, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x0010 offset: 0x3CDE
@scena.Code('func_10_3CDE')
def func_10_3CDE():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_3CF4')
    def lambda_3CF4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3CF4)

    OP_8E(0x00FE, 54630, 0, 60840, 2500, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x0011 offset: 0x3D1C
@scena.Code('func_11_3D1C')
def func_11_3D1C():
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0012 offset: 0x3D50
@scena.Code('func_12_3D50')
def func_12_3D50():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上有『人偶骑士』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
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

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '【读第１卷】\n'),
            TXT(0x01, '【读第２卷】\n'),
            TXT(0x02, '【读第３卷】\n'),
            TXT(0x03, '【读第４卷】\n'),
            TXT(0x04, '【读第５卷】\n'),
            TXT(0x05, '【读第６卷】\n'),
            TXT(0x06, '【读第７卷】\n'),
            TXT(0x07, '【读第８卷】\n'),
            TXT(0x08, '【放弃】\n'),
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
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E4D',
    )

    OP_B8(0x02EE, 0x0000)

    def _loc_3E4D(): pass

    label('loc_3E4D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E5F',
    )

    OP_B8(0x02EF, 0x0000)

    def _loc_3E5F(): pass

    label('loc_3E5F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E71',
    )

    OP_B8(0x02F0, 0x0000)

    def _loc_3E71(): pass

    label('loc_3E71')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E83',
    )

    OP_B8(0x02F1, 0x0000)

    def _loc_3E83(): pass

    label('loc_3E83')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E95',
    )

    OP_B8(0x02F2, 0x0000)

    def _loc_3E95(): pass

    label('loc_3E95')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EA7',
    )

    OP_B8(0x02F3, 0x0000)

    def _loc_3EA7(): pass

    label('loc_3EA7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EB9',
    )

    OP_B8(0x02F4, 0x0000)

    def _loc_3EB9(): pass

    label('loc_3EB9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3ECB',
    )

    OP_B8(0x02F5, 0x0000)

    def _loc_3ECB(): pass

    label('loc_3ECB')

    TalkEnd(0x00FF)

    Return()

# id: 0x0013 offset: 0x3ECF
@scena.Code('func_13_3ECF')
def func_13_3ECF():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上有『人偶骑士』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
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

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '【读第９卷】\n'),
            TXT(0x01, '【读第10卷】\n'),
            TXT(0x02, '【读第11卷】\n'),
            TXT(0x03, '【读第12卷】\n'),
            TXT(0x04, '【读第13卷】\n'),
            TXT(0x05, '【读第14卷】\n'),
            TXT(0x06, '【读第15卷】\n'),
            TXT(0x07, '【读第16卷】\n'),
            TXT(0x08, '【放弃】\n'),
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
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FCC',
    )

    OP_B8(0x02F6, 0x0000)

    def _loc_3FCC(): pass

    label('loc_3FCC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FDE',
    )

    OP_B8(0x02F7, 0x0000)

    def _loc_3FDE(): pass

    label('loc_3FDE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FF0',
    )

    OP_B8(0x02F8, 0x0000)

    def _loc_3FF0(): pass

    label('loc_3FF0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4002',
    )

    OP_B8(0x02F9, 0x0000)

    def _loc_4002(): pass

    label('loc_4002')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4014',
    )

    OP_B8(0x02FA, 0x0000)

    def _loc_4014(): pass

    label('loc_4014')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4026',
    )

    OP_B8(0x02FB, 0x0000)

    def _loc_4026(): pass

    label('loc_4026')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_405D',
    )

    OP_B8(0x02FC, 0x0000)

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x01, 0x0010)"),
            (Expr.Eval, "OP_29(0x00C4, 0x01, 0x0040)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_405D',
    )

    Sleep(500)

    Call(1, 0x0000)

    def _loc_405D(): pass

    label('loc_405D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_406F',
    )

    OP_B8(0x02FD, 0x0000)

    def _loc_406F(): pass

    label('loc_406F')

    TalkEnd(0x00FF)

    Return()

# id: 0x0014 offset: 0x4073
@scena.Code('func_14_4073')
def func_14_4073():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上有『人偶骑士』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
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

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '【读第17卷】\n'),
            TXT(0x01, '【读第18卷】\n'),
            TXT(0x02, '【读第19卷】\n'),
            TXT(0x03, '【读第20卷】\n'),
            TXT(0x04, '【读第21卷】\n'),
            TXT(0x05, '【读最终卷】\n'),
            TXT(0x06, '【放弃】\n'),
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
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4156',
    )

    OP_B8(0x02FE, 0x0000)

    def _loc_4156(): pass

    label('loc_4156')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4168',
    )

    OP_B8(0x02FF, 0x0000)

    def _loc_4168(): pass

    label('loc_4168')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_417A',
    )

    OP_B8(0x0300, 0x0000)

    def _loc_417A(): pass

    label('loc_417A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_418C',
    )

    OP_B8(0x0301, 0x0000)

    def _loc_418C(): pass

    label('loc_418C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_419E',
    )

    OP_B8(0x0302, 0x0000)

    def _loc_419E(): pass

    label('loc_419E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41B0',
    )

    OP_B8(0x0303, 0x0000)

    def _loc_41B0(): pass

    label('loc_41B0')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
