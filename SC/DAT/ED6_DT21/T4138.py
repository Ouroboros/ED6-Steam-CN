import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4138_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4138   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '达维尔大使'),
    TXT(0x02, '穆拉'),
    TXT(0x03, '巴克雷书记官'),
    TXT(0x04, '杰拉尔德'),
    TXT(0x05, '阿尔夫参事官'),
    TXT(0x06, '卡米拉'),
    TXT(0x07, '尼赞'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4138.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x453A
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
        ('ED6_DT27/CH03713._CH', 'ED6_DT27/CH03713P._CP'),
        ('ED6_DT27/CH03570._CH', 'ED6_DT27/CH03570P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 1190,
            z                   = 300,
            y                   = 75010,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = -4180,
            z                   = 0,
            y                   = 66110,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 55300,
            z                   = 0,
            y                   = 59890,
            direction           = 93,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 53760,
            z                   = 0,
            y                   = 65280,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -49800,
            z                   = 0,
            y                   = 13300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -48940,
            z                   = 1000,
            y                   = 64599,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
    )

# id: 0x10003 offset: 0x1C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1C2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 1040,
            triggerZ            = 4000,
            triggerY            = 32049,
            triggerRange        = 800,
            actorX              = 1040,
            actorZ              = 4500,
            actorY              = 32049,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -42830,
            triggerZ            = 1000,
            triggerY            = 61060,
            triggerRange        = 600,
            actorX              = -42830,
            actorZ              = 2000,
            actorY              = 61060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -42800,
            triggerZ            = 1000,
            triggerY            = 59460,
            triggerRange        = 600,
            actorX              = -42800,
            actorZ              = 2000,
            actorY              = 59460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x22E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_255',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_252',
    )

    SetChrPos(0x000A, 5740, 0, 75240, 87)

    def _loc_252(): pass

    label('loc_252')

    Jump('loc_2AD')

    def _loc_255(): pass

    label('loc_255')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2AD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_27C',
    )

    SetChrPos(0x000A, 2430, 0, 76110, 180)

    Jump('loc_2AD')

    def _loc_27C(): pass

    label('loc_27C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 2, 0x1622)),
            Expr.Return,
        ),
        'loc_29C',
    )

    SetChrPos(0x0009, 54220, 0, 7400, 90)
    ClearChrFlags(0x0009, 0x0080)

    Jump('loc_2AD')

    def _loc_29C(): pass

    label('loc_29C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            Expr.Return,
        ),
        'loc_2A6',
    )

    Jump('loc_2AD')

    def _loc_2A6(): pass

    label('loc_2A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2AD',
    )

    def _loc_2AD(): pass

    label('loc_2AD')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_2B9'),
        (-1, 'loc_2CD'),
    )

    def _loc_2B9(): pass

    label('loc_2B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 0, 0x1620)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CA',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x000A)

    def _loc_2CA(): pass

    label('loc_2CA')

    Jump('loc_2CD')

    def _loc_2CD(): pass

    label('loc_2CD')

    Return()

# id: 0x0001 offset: 0x2CE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 2, 0x1622)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2EE',
    )

    OP_B1('t4138_y')

    Jump('loc_2F7')

    def _loc_2EE(): pass

    label('loc_2EE')

    OP_B1('t4138_n')

    def _loc_2F7(): pass

    label('loc_2F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 0, 0x1620)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_30F',
    )

    OP_64(0x00, 0x0001)
    OP_71(0x0002, 0x0010)

    Jump('loc_314')

    def _loc_30F(): pass

    label('loc_30F')

    OP_72(0x0002, 0x0010)

    def _loc_314(): pass

    label('loc_314')

    Return()

# id: 0x0002 offset: 0x315
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
        'loc_33A',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_47C')

    def _loc_33A(): pass

    label('loc_33A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_353',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_47C')

    def _loc_353(): pass

    label('loc_353')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36C',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_47C')

    def _loc_36C(): pass

    label('loc_36C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_385',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_47C')

    def _loc_385(): pass

    label('loc_385')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39E',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_47C')

    def _loc_39E(): pass

    label('loc_39E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B7',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_47C')

    def _loc_3B7(): pass

    label('loc_3B7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D0',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_47C')

    def _loc_3D0(): pass

    label('loc_3D0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E9',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_47C')

    def _loc_3E9(): pass

    label('loc_3E9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_402',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_47C')

    def _loc_402(): pass

    label('loc_402')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41B',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_47C')

    def _loc_41B(): pass

    label('loc_41B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_434',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_47C')

    def _loc_434(): pass

    label('loc_434')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44D',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_47C')

    def _loc_44D(): pass

    label('loc_44D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_466',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_47C')

    def _loc_466(): pass

    label('loc_466')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47C',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_47C(): pass

    label('loc_47C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_491',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_47C')

    def _loc_491(): pass

    label('loc_491')

    Return()

# id: 0x0003 offset: 0x492
@scena.Code('func_03_492')
def func_03_492():
    TalkBegin(0x0008)
    ClearChrFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0002, 0)

    If(
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4B7',
    )

    SetChrSubChip(0x0008, 1)

    Jump('loc_4BC')

    def _loc_4B7(): pass

    label('loc_4B7')

    SetChrSubChip(0x0008, 2)

    def _loc_4BC(): pass

    label('loc_4BC')

    OP_8C(0x0008, 180, 0)
    SetChrFlags(0x0008, 0x0010)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_92A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_927',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041B, 6, 0x20DE)),
            Expr.Return,
        ),
        'loc_518',
    )

    ChrTalk(
        0x0008,
        (
            '#0670370827V#1100F至、至少，\n',
            '想让通信恢复……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_927')

    def _loc_518(): pass

    label('loc_518')

    ChrTalk(
        0x0008,
        (
            '#0670370828V#1102F呜唔唔唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670370829V那最后的通信到底是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370830V#1000F您好，大使先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670370831V#1101F哦哦、诸位是……\n',
            '来得正好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670370832V#1100F关于现在的状况\n',
            '了解到什么了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670370833V无论怎样细微的事都行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370834V#1011F真，真突然啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670370835V#1101F导力器竟然全部\n',
            '停止真是前所未闻的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670370836V#1100F这样下去别说\n',
            '和本国取得联络，\n',
            '即使平常的业务也做不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370837V#1015F嗯～话虽这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370838V#1042F恕我直言大使阁下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370839V这样的话去格兰赛尔城\n',
            '询问看看怎样呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370840V#1040F那位艾莉茜雅女王\n',
            '说不定已经采取了\n',
            '适当的策略了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670370841V#1101F这，这当然已经试过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670370842V#1100F但是，格兰赛尔城内\n',
            '仍然是相当混乱的情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670370843V催促了几次\n',
            '至今还未收到\n',
            '艾莉茜雅女王的回答。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370844V#1004F哎呀呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670370827V#1100F至、至少，\n',
            '想让通信恢复……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370846V#1011F（……『零力场发生器』\n',
            '　不能交给他吧？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370847V#1042F（当然了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370848V（装置的数量有限……\n',
            '　现在只有忍耐了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20DE)

    def _loc_927(): pass

    label('loc_927')

    Jump('loc_F3C')

    def _loc_92A(): pass

    label('loc_92A')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F3C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_D79',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CB, 3, 0x165B)),
            Expr.Return,
        ),
        'loc_9FC',
    )

    ChrTalk(
        0x0008,
        (
            '#0670271482V#1100F……你们特地\n',
            '前来这里，\n',
            '请让我表示谢意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670271483V多亏你们，对我国的\n',
            '不当怀疑确实消释了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670271484V虽说是小事，\n',
            '但因这种事有损\n',
            '帝国的威信绝非我本意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D76')

    def _loc_9FC(): pass

    label('loc_9FC')

    ChrTalk(
        0x0008,
        (
            '#0670271485V#1100F唔……奥利维尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670271486V还有前几天的那几位游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040271487V#031F贵安，大使殿下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670271488V#1100F哼……今天又在\n',
            '游手好闲啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670271489V穆拉不在\n',
            '你就放羊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040271490V#030F呼，你还是那么严厉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670271491V#1100F……今天到底有什么事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670271492V要是恐吓信的事\n',
            '我已经收到报告了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271493V#1011F咦，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670271494V#1102F啊啊，犯人似乎是\n',
            '王国军特务兵的逃兵。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670271495V#1100F就像我说的，不是\n',
            '帝国关系者所为吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271496V#1015F（嗯～虽说正确\n',
            '　说来也不是特务兵……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C74',
    )

    ChrTalk(
        0x0106,
        (
            '#0050271497V#053F（嗯，没必要在这里\n',
            '　说出实话引人不安吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CBE')

    def _loc_C74(): pass

    label('loc_C74')

    ChrTalk(
        0x0103,
        (
            '#0030271498V#020F（嗯，在这里就算说实话\n',
            '　也只会让事情变得更复杂。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CBE(): pass

    label('loc_CBE')

    ChrTalk(
        0x0008,
        (
            '#0670271482V#1100F……你们特地\n',
            '前来这里，\n',
            '请让我表示谢意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670271483V多亏你们，对我国的\n',
            '不当怀疑确实消释了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670271484V虽说是小事，\n',
            '但因这种事有损\n',
            '帝国的威信绝非我本意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x165B)

    def _loc_D76(): pass

    label('loc_D76')

    Jump('loc_F3C')

    def _loc_D79(): pass

    label('loc_D79')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            Expr.Return,
        ),
        'loc_F3C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_E31',
    )

    ChrTalk(
        0x0008,
        (
            '#0670250829V#1100F帝国内的协会支部\n',
            '似乎接连受到什么人的袭击\n',
            '情报已经传来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250830V考虑到组织的性格，\n',
            '必定有什么目的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250831V要努力不输给他们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F3C')

    def _loc_E31(): pass

    label('loc_E31')

    ChrTalk(
        0x0008,
        (
            '#0670250832V#1100F唔，游击士\n',
            '看来也是很辛苦的工作啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250833V这么说来，几个月前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250834V帝国内的协会支部\n',
            '似乎接连受到什么人的袭击\n',
            '情报已经传来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250835V#1102F考虑到组织的性格，\n',
            '必定有什么目的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250836V#1100F要努力不输给他们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_F3C(): pass

    label('loc_F3C')

    SetChrSubChip(0x0008, 0)
    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0xF45
@scena.Code('func_04_F45')
def func_04_F45():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 2, 0x1622)),
            Expr.Return,
        ),
        'loc_F7A',
    )

    ChrTalk(
        0x0009,
        (
            '#0110250837V#270F怎么了，忘了东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F7A(): pass

    label('loc_F7A')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0xF7E
@scena.Code('func_05_F7E')
def func_05_F7E():
    TalkBegin(0x000A)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FF3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_FF0',
    )

    ChrTalk(
        0x00FE,
        (
            '导力停止发生之前\n',
            '好象收到过本国奇怪的指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大使问起这个的时候，\n',
            '通讯似乎就断了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FF0(): pass

    label('loc_FF0')

    Jump('loc_111F')

    def _loc_FF3(): pass

    label('loc_FF3')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_111F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1042',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，奇怪啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯的穆拉\n',
            '没有发来定时联络……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_111F')

    def _loc_1042(): pass

    label('loc_1042')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            Expr.Return,
        ),
        'loc_111F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_109E',
    )

    ChrTalk(
        0x00FE,
        (
            '不过寻找恐吓信的犯人\n',
            '是相当辛苦的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能帮上忙就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_111F')

    def _loc_109E(): pass

    label('loc_109E')

    ChrTalk(
        0x00FE,
        (
            '不过寻找恐吓信的犯人\n',
            '是相当辛苦的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论怎么说，那个内容\n',
            '就等于完全没有线索一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能帮上忙就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_111F(): pass

    label('loc_111F')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x1123
@scena.Code('func_06_1123')
def func_06_1123():
    TalkBegin(0x000B)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_119D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_119A',
    )

    ChrTalk(
        0x00FE,
        (
            '大使殿下从本国\n',
            '收到的最后的联络\n',
            '是怎样的内容？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『别动是怎么回事！』\n',
            '像是这样的怒吼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_119A(): pass

    label('loc_119A')

    Jump('loc_14C4')

    def _loc_119D(): pass

    label('loc_119D')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1303',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1216',
    )

    ChrTalk(
        0x00FE,
        (
            '合并自治州的时候，\n',
            '宰相阁下的指挥相当漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，导力铁路的整备\n',
            '就是因为这个啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1300')

    def _loc_1216(): pass

    label('loc_1216')

    ChrTalk(
        0x00FE,
        (
            '在跟自治州的纠纷中，\n',
            '宰相阁下的指挥相当漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '配置在广大领土上的战力\n',
            '由导力铁路暂时向国境集中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '闪电战取得胜利后\n',
            '又将各部队很快返回守备地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力铁路的整备\n',
            '就是因为这个啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是是，我们祖国\n',
            '已经毫无空隙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_1300(): pass

    label('loc_1300')

    Jump('loc_14C4')

    def _loc_1303(): pass

    label('loc_1303')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            Expr.Return,
        ),
        'loc_1386',
    )

    ChrTalk(
        0x00FE,
        (
            '奥斯本宰相阁下\n',
            '原本是军部出身的政治家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '成为宰相\n',
            '大概是１０年前吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以惊人的速度\n',
            '出人头地令人印象深刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14C4')

    def _loc_1386(): pass

    label('loc_1386')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_14C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_140B',
    )

    ChrTalk(
        0x00FE,
        (
            '离利贝尔的国境最近的\n',
            '帝国城市被称为帕鲁姆市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我就是那个帕鲁姆出身的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '离柏斯很近，\n',
            '返回故乡很方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14C4')

    def _loc_140B(): pass

    label('loc_140B')

    ChrTalk(
        0x00FE,
        (
            '离利贝尔的国境最近的\n',
            '帝国城市被称为帕鲁姆市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我就是那个帕鲁姆出身的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '离柏斯很近，\n',
            '返回故乡很方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '相反去帝都\n',
            '更费时间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帝国没有定期船，\n',
            '只能换乘铁路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_14C4(): pass

    label('loc_14C4')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0x14C8
@scena.Code('func_07_14C8')
def func_07_14C8():
    TalkBegin(0x000C)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_154A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1547',
    )

    ChrTalk(
        0x00FE,
        (
            '那个湖上浮现的\n',
            '物体是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个现象帝国也\n',
            '发生了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么都不清楚的\n',
            '状态很令人不安啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1547(): pass

    label('loc_1547')

    Jump('loc_1827')

    def _loc_154A(): pass

    label('loc_154A')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1827',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_167C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_15BF',
    )

    ChrTalk(
        0x00FE,
        (
            '犯人若是共和国的人，\n',
            '我帝国无法沉默下去了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反之亦然。\n',
            '条约缔结也有影响啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1679')

    def _loc_15BF(): pass

    label('loc_15BF')

    ChrTalk(
        0x00FE,
        (
            '虽然这么说\n',
            '可能不太好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但知道骚动的犯人\n',
            '是原王国军，松了口气的\n',
            '该是艾莉茜雅女王吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这若是共和国的人，\n',
            '我帝国无法沉默下去了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反之亦然。\n',
            '条约缔结也有影响啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_1679(): pass

    label('loc_1679')

    Jump('loc_1827')

    def _loc_167C(): pass

    label('loc_167C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            Expr.Return,
        ),
        'loc_17AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_16EB',
    )

    ChrTalk(
        0x00FE,
        (
            '艾莉茜雅女王活用\n',
            '导力技术的政策就是绝妙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果她有难题……\n',
            '那还是继任者的问题吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17AB')

    def _loc_16EB(): pass

    label('loc_16EB')

    ChrTalk(
        0x00FE,
        (
            '利贝尔王国\n',
            '成为所谓的缓冲国。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '缓冲国就是在大国之间，\n',
            '抵御互相矛盾的国家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '缓冲国为了保持独立，\n',
            '要与周围的势力相称\n',
            '必须不懈努力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约或许也有\n',
            '均衡势力的目的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_17AB(): pass

    label('loc_17AB')

    Jump('loc_1827')

    def _loc_17AE(): pass

    label('loc_17AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1827',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，这不是奥利维尔吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然去了温泉\n',
            '真令人羡慕啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我为了准备签字仪式\n',
            '可是连日工作到筋疲力尽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1827(): pass

    label('loc_1827')

    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x182B
@scena.Code('func_08_182B')
def func_08_182B():
    TalkBegin(0x000D)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18CF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_18CC',
    )

    ChrTalk(
        0x00FE,
        (
            '在帝国的爸爸\n',
            '和妈妈是否平安呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前几天，回国的奥利维尔先生\n',
            '是否还好好地活着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的状况下和国家\n',
            '联络不上真是令人不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18CC(): pass

    label('loc_18CC')

    Jump('loc_1B85')

    def _loc_18CF(): pass

    label('loc_18CF')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B85',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1935',
    )

    ChrTalk(
        0x00FE,
        (
            '喂喂，奥利维尔先生，\n',
            '请别打扰我工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别看大使那样\n',
            '其实很爱干净的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B85')

    def _loc_1935(): pass

    label('loc_1935')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            Expr.Return,
        ),
        'loc_1995',
    )

    ChrTalk(
        0x00FE,
        (
            '……奥利维尔先生，\n',
            '可别太戏弄大使哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他被宰相虐待，最近\n',
            '头发都变得稀薄了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B85')

    def _loc_1995(): pass

    label('loc_1995')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1B85',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CB, 4, 0x165C)),
            Expr.Return,
        ),
        'loc_1A27',
    )

    ChrTalk(
        0x00FE,
        (
            '客人和穆拉先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，奥利维尔先生\n',
            '真正喜欢的是谁呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#030F想知道吗？\n',
            '说来话长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1019F真是的，算了啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B85')

    def _loc_1A27(): pass

    label('loc_1A27')

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0104, 400)
    Sleep(600)

    ChrTalk(
        0x00FE,
        (
            '哎呀，奥利维尔先生……\n',
            '真是好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这些是您的客人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#035F唔，的确是客人\n',
            '也因为一起旅行……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#030F是共同渡过连玫瑰也自愧不如\n',
            '的甘美浓厚时光的亲密关系啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#037F对吧、艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，穆拉先生\n',
            '就被抛弃了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1019F头、头痛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '穆拉先生的辛苦\n',
            '我似乎能够明白一点了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x165C)

    def _loc_1B85(): pass

    label('loc_1B85')

    TalkEnd(0x000D)

    Return()

# id: 0x0009 offset: 0x1B89
@scena.Code('func_09_1B89')
def func_09_1B89():
    TalkBegin(0x000E)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C0F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1C0C',
    )

    ChrTalk(
        0x00FE,
        (
            '金光闪耀的浮游物体吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那种东西，到现在为止\n',
            '见所未见闻所未闻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之只能说是让人毛骨悚然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C0C(): pass

    label('loc_1C0C')

    Jump('loc_1FE3')

    def _loc_1C0F(): pass

    label('loc_1C0F')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FE3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1D7D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1CBD',
    )

    ChrTalk(
        0x00FE,
        (
            '埃雷波尼亚帝国有限制\n',
            '出版物什么的要经过严格检查哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是适合国风的内容，\n',
            '有没有大不敬的内容……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我在帝国\n',
            '也担任这样的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D7A')

    def _loc_1CBD(): pass

    label('loc_1CBD')

    ChrTalk(
        0x00FE,
        (
            '听说利贝尔王国承认\n',
            '国民的言论自由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '埃雷波尼亚帝国有限制\n',
            '出版物什么的要经过严格检查哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是适合国风的内容，\n',
            '有没有大不敬的内容……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我在帝国\n',
            '也担任这样的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_1D7A(): pass

    label('loc_1D7A')

    Jump('loc_1FE3')

    def _loc_1D7D(): pass

    label('loc_1D7D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            Expr.Return,
        ),
        'loc_1F53',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0217, 0, 0x10B8)),
            Expr.Return,
        ),
        'loc_1E21',
    )

    ChrTalk(
        0x00FE,
        (
            '因此我推荐的书\n',
            '该是『红耀石』小说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作者是哪里人不太清楚，\n',
            '不过应该是帝国出身吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不是在帝都住过一阵子\n',
            '应该描写不出那种风格吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F50')

    def _loc_1E21(): pass

    label('loc_1E21')

    ChrTalk(
        0x00FE,
        (
            '这，这本书……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不是在埃雷波尼亚\n',
            '禁止发行的吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谁，谁把这种东西\n',
            '放进书架的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x2F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EB2',
    )

    ChrTalk(
        0x0130,
        (
            '#274F（…………………………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EB2(): pass

    label('loc_1EB2')

    ChrTalk(
        0x00FE,
        (
            '如果被达维尔大使知道\n',
            '可就够受的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对，对了，就是你。\n',
            '快把这本书拿走！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['牌技师杰克 ４卷']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    AddItem(ItemTable['牌技师杰克 ４卷'], 1)
    OP_A2(0x10B8)

    def _loc_1F50(): pass

    label('loc_1F50')

    Jump('loc_1FE3')

    def _loc_1F53(): pass

    label('loc_1F53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1FE3',
    )

    ChrTalk(
        0x00FE,
        (
            '这个房间的书全部\n',
            '都是利贝尔出版的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要了解别的国家，\n',
            '首先要从文化开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们可以随便读，\n',
            '不过一定要放回到原来的地方哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FE3(): pass

    label('loc_1FE3')

    TalkEnd(0x000E)

    Return()

# id: 0x000A offset: 0x1FE7
@scena.Code('func_0A_1FE7')
def func_0A_1FE7():
    EventBegin(0x00)
    OP_6D(910, 4000, 27010, 0)
    OP_67(0, 10110, -10000, 0)
    OP_6B(2140, 0)
    OP_6C(45000, 0)
    OP_6E(453, 0)
    SetChrPos(0x0104, 1590, 0, 4140, 0)
    SetChrPos(0x0101, 430, 0, 4150, 0)
    SetChrPos(0x0105, 210, 0, 2710, 0)
    SetChrPos(0x0108, 1520, 0, 2840, 0)

    @scena.Lambda('lambda_2070')
    def lambda_2070():
        OP_6D(970, 0, 5940, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2070)

    @scena.Lambda('lambda_2088')
    def lambda_2088():
        OP_67(0, 10110, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2088)

    OP_C8(0x0200, 0x0046, 'C_PLAC12._CH', 0x00, 0x07D0)
    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Fade(1000)
    OP_6D(1490, 0, 4150, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0108,
        (
            '#0080250698V#073F喔……\n',
            '这真是华丽的建筑物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250699V#1011F#6P呜哇～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250700V毫不逊色于卡尔瓦德大使馆\n',
            '豪华气氛的内部装潢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250701V#047F壮丽而强有力的氛围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250702V#048F用帝国风情的装饰品\n',
            '装饰起来的内部装潢看起来很协调呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250703V#030F呼，因为这里是\n',
            '显耀帝国威光的舞台嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250704V#035F遗憾的是工作人员\n',
            '似乎稍稍相形见绌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    OP_72(0x0003, 0x0010)
    OP_6F(0x0003, 60)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 12690, 0, 5860, 270)
    OP_4A(0x0009, 255)

    NpcTalk(
        0x0009,
        '男人的声音',
        (
            '#0110250705V#3P干嘛说这\n',
            '危险的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0108, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0104, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_234F')
    def lambda_234F():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_234F')

    DispatchAsync2(0x0104, 0x0002, lambda_234F)

    @scena.Lambda('lambda_2360')
    def lambda_2360():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2360')

    DispatchAsync2(0x0101, 0x0002, lambda_2360)

    Sleep(200)

    @scena.Lambda('lambda_2376')
    def lambda_2376():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2376')

    DispatchAsync2(0x0108, 0x0002, lambda_2376)

    @scena.Lambda('lambda_2387')
    def lambda_2387():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2387')

    DispatchAsync2(0x0105, 0x0002, lambda_2387)

    OP_6D(10750, 0, 5950, 2000)

    @scena.Lambda('lambda_23A9')
    def lambda_23A9():
        OP_8E(0x00FE, 860, 0, 5480, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_23A9)

    @scena.Lambda('lambda_23C4')
    def lambda_23C4():
        OP_6D(990, 0, 4480, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_23C4)

    OP_72(0x0003, 0x0800)
    OP_71(0x0003, 0x0010)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0x00000000)
    OP_23(0x0006)
    OP_22(0x0007, 0x00, 0x64)
    WaitForThreadExit(0x0009, 0x0000)
    OP_8C(0x0009, 180, 400)
    OP_71(0x0003, 0x0800)
    TerminateThread(0x0104, 0x02)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0108, 0x02)
    TerminateThread(0x0105, 0x02)
    OP_8C(0x0104, 0, 0)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0104,
        (
            '#0040250706V#031F#6P哦哦，亲爱的朋友啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250707V好久不见呢。\n',
            '还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110250708V#274F#5P你这家伙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250709V我那样嘱咐你\n',
            '要告诉我你到了哪里的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250710V#037F#6P呼，这也算是爱的私奔吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250711V正因为分开了\n',
            '才会有积累的感情嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110250712V#276F#5P……艾丝蒂尔，谢谢你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250713V看来这个轻佻的大赖皮蛋\n',
            '给你添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250714V#1016F#6P啊哈哈……\n',
            '嗯，也没什么啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250715V#1006F还算比较安分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110250716V#272F#5P嗯，那个怪人\n',
            '暂且不管……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250717V#277F你们来帝国大使馆\n',
            '好像有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250718V#1002F#6P啊，嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250719V其实，是有些事情\n',
            '想问问这里的大使……',
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
            '说明为了询问恐吓信\n',
            '前来会见帝国大使的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#0110250720V#273F#5P那个恐吓信啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250721V#270F我也很在意\n',
            '但没想到协会也行动了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250722V是王国军的委托吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250723V#1006F#6P姑且算是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250724V不过我们打算尽可能\n',
            '以中立的立场来调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110250725V#277F#5P呵呵，想得真周到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250726V那么，由我来\n',
            '向达维尔大使介绍吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250727V那个轻佻的大赖皮蛋\n',
            '应该能够相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250728V#1004F#6P咦，可以吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250729V#071F呀，帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250730V#041F#6P非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0104, 225, 400)

    ChrTalk(
        0x0104,
        (
            '#0040250731V#036F#5P嗯……\n',
            '我就那么不可信？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250732V#1004F#6P哎……\n',
            '你以为可信！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250733V#070F嗯，要是你来介绍\n',
            '看来会导致多余的误解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0105, 45, 400)

    ChrTalk(
        0x0105,
        (
            '#0060250734V#045F#6P嗯……\n',
            '抱歉了，奥利维尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250735V#034F#5P啜泣啜泣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110250736V#272F#5P贤明的判断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 0, 400)
    OP_8C(0x0105, 0, 400)
    OP_8C(0x0104, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#0110250737V#277F#5P达维尔大使\n',
            '在2楼的办公室。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250738V我去确认一下\n',
            '你们稍等片刻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250739V#1006F#6P嗯，ＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 90, 400)

    @scena.Lambda('lambda_2AAF')
    def lambda_2AAF():
        OP_6D(6830, 0, 8520, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2AAF)

    @scena.Lambda('lambda_2AC7')
    def lambda_2AC7():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2AC7')

    DispatchAsync2(0x0104, 0x0002, lambda_2AC7)

    @scena.Lambda('lambda_2AD8')
    def lambda_2AD8():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2AD8')

    DispatchAsync2(0x0101, 0x0002, lambda_2AD8)

    @scena.Lambda('lambda_2AE9')
    def lambda_2AE9():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2AE9')

    DispatchAsync2(0x0108, 0x0002, lambda_2AE9)

    @scena.Lambda('lambda_2AFA')
    def lambda_2AFA():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2AFA')

    DispatchAsync2(0x0105, 0x0002, lambda_2AFA)

    OP_8E(0x0009, 8770, 0, 7910, 3000, 0x00)
    OP_8E(0x0009, 9300, 2000, 15090, 3000, 0x00)
    SetChrFlags(0x0009, 0x0080)
    OP_6D(1020, 0, 3870, 2000)
    TerminateThread(0x0104, 0x02)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0108, 0x02)
    TerminateThread(0x0105, 0x02)
    OP_72(0x0002, 0x0010)
    OP_65(0x00, 0x0001)
    OP_A2(0x1620)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x2B62
@scena.Code('func_0B_2B62')
def func_0B_2B62():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0104, 1500, 4000, 29410, 0)
    SetChrPos(0x0101, 320, 4000, 29600, 0)
    SetChrPos(0x0108, 1380, 4000, 28080, 0)
    SetChrPos(0x0105, -110, 4000, 28000, 0)
    OP_6D(920, 4000, 30680, 0)
    OP_67(0, 7300, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x0009, 255)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010250740V#1015F#6P嗯……\n',
            '这里是办公室吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250741V#031F#2P呼，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250742V那么就华丽地闯入\n',
            '吓大使殿下一跳吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250743V#1019F#6P会被穆拉先生\n',
            '暴扁的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_22(0x0006, 0x00, 0x64)
    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x0000003C)
    Sleep(1000)

    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x0009, 1020, 4000, 32900, 180)
    ClearChrFlags(0x0009, 0x0080)
    OP_8C(0x0101, 0, 400)

    @scena.Lambda('lambda_2CFF')
    def lambda_2CFF():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2CFF)

    OP_8E(0x0009, 900, 4000, 31210, 2000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0110250744V#277F#5P久等了。\n',
            '大使说可以见你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250745V#1006F#6P啊，嗯。\n',
            '那么就有劳了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2D8C')
    def lambda_2D8C():
        OP_8E(0x00FE, 2410, 4000, 31240, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2D8C)

    WaitForThreadExit(0x0009, 0x0000)
    OP_8C(0x0009, 270, 400)
    CreateThread(0x0101, 0x00, 0x00, 0x0011)
    Sleep(500)

    CreateThread(0x0104, 0x00, 0x00, 0x0011)
    Sleep(300)

    CreateThread(0x0105, 0x00, 0x00, 0x0011)
    Sleep(600)

    CreateThread(0x0108, 0x00, 0x00, 0x0011)
    Sleep(500)

    FadeOut(1000, 0, -1)
    OP_0D()
    FormationAddMember(ChrTable['穆拉2'], 0xFF, 0xFF)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0105, 0x0080)
    SetChrFlags(0x0104, 0x0080)
    SetChrFlags(0x0108, 0x0080)
    SetChrFlags(0x0130, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    OP_6D(450, 0, 67280, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_2E56')
    def lambda_2E56():
        OP_6D(1760, 0, 73830, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2E56)

    CreateThread(0x0101, 0x01, 0x00, 0x000C)
    Sleep(600)

    CreateThread(0x0104, 0x01, 0x00, 0x000D)
    Sleep(600)

    CreateThread(0x0105, 0x01, 0x00, 0x000E)
    Sleep(600)

    CreateThread(0x0108, 0x01, 0x00, 0x000F)
    Sleep(600)

    CreateThread(0x0130, 0x01, 0x00, 0x0010)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0002)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0670250746V#1100F#5P欢迎光临\n',
            '埃雷波尼亚大使馆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250747V我是驻利贝尔大使\n',
            '达维尔·克莱纳赫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250748V#1011F#6P嗯，我是游击士协会的\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250749V#070F#4P金·瓦赛克。\n',
            '同是游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250750V#040F杰尼丝王立学院２年级生，\n',
            '我叫科洛丝·琳希。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250751V#031F还有爱与和平的使者，\n',
            '奥利维尔·朗海姆！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670250752V#1102F#5P哼……是你啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250753V#1100F听说你去了亚尔摩村\n',
            '就行踪不明了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250754V太让穆拉\n',
            '担心可不行哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250755V当然还有我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250756V#035F呼，您真是严厉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670250757V#1100F#5P别提这个了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250758V你们似乎是来问\n',
            '那个恐吓信的事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250759V想知道些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250760V#1002F#6P嗯，那么\n',
            '我们就单刀直入地问了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250761V大使对威胁者\n',
            '有线索吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250762V譬如帝国内\n',
            '反对条约缔结的势力什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670250763V#1102F#5P哈哈，你说话真直啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250764V#1100F不过很不巧\n',
            '我完全没有线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250765V皇帝陛下对条约缔结\n',
            '也相当积极。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250766V而且异端不规矩之人等\n',
            '怎么可能出现在我帝国？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250767V#1007F#6P这、这样断言\n',
            '真是直截了当啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250768V#1015F那么大使先生认为\n',
            '是帝国以外的人做的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670250769V#1100F#5P当然，必然是这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250770V很可能是卡尔瓦德附近的\n',
            '在野党势力在作祟吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250771V愚民政治的弊病就在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250772V#073F#4P这我觉得难说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250773V#070F的确共和国的执政党\n',
            '和在野党总是对立的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250774V但哪怕条约缔结被阻止了\n',
            '我也不认为会变成总统的责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670250775V#1102F#5P哼，详情我可不知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250776V#1100F能肯定的，只有威胁者\n',
            '不可能是帝国的人这件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250777V知道这个不就够了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250778V#1015F#6P嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250779V#047F#4P……那个，达维尔大使。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250780V#042F奥斯本宰相阁下\n',
            '对于互不侵犯条约，\n',
            '是持什么样的态度呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0670250781V#1101F#5P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0130, 225, 400)
    Sleep(200)

    ChrTalk(
        0x0130,
        (
            '#0110250782V#273F#5P哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250783V#035F呼呼……\n',
            '相当尖锐的问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250784V#1016F#6P嗯……\n',
            '那个奥斯本大人是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250785V#030F帝国政府的代表，\n',
            '铁血宰相奥斯本。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250786V『国家的稳定要靠铁血』\n',
            '毫不忌讳公开如此宣称的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250787V#035F在帝国全土铺设导力铁道\n',
            '武力合并几个自治州\n',
            '嗯，总之是精力充沛的政治家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250788V#1004F#5P有，有这种人啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(800)

    ChrTalk(
        0x0008,
        (
            '#0670250789V#1103F#5P喂、我说奥利维尔！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250790V对于本国的宰相，\n',
            '不许使用带批判性的言词！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 0, 400)

    ChrTalk(
        0x0104,
        (
            '#0040250791V#035F呼～\n',
            '其实没有批判的意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250792V#030F只是，如果再合作点儿\n',
            '也不会不合适吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250793V之前，共和国的爱尔莎大使\n',
            '也说了很多情况……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250794V他们可是合作多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670250795V#1101F#5P什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250796V#034F这样下去埃雷波尼亚帝国\n',
            '的度量就会被人怀疑了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250797V这我可不能忍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670250798V#1101F#5P唔唔唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0130, 270, 400)

    ChrTalk(
        0x0130,
        (
            '#0110250799V#276F#2P达维尔大使。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250800V关于这件事\n',
            '没有什么情报好隐瞒的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250801V直率说明情况\n',
            '也没有什么问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670250802V#1102F#5P……哼，好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250803V#1100F关于之前的问题……\n',
            '和陛下一样奥斯本宰相\n',
            '对条约缔结也非常积极。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250804V听说反而是宰相\n',
            '向陛下进言的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250805V#044F#4P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250806V#030F哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250807V#1015F#6P嗯，这么说果然\n',
            '还是以新型引擎为目标吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670250808V#1102F#5P不，他向陛下进言似乎\n',
            '是在新型引擎的事情出来之前。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250809V#1100F嗯，事情就是如此\n',
            '我也少了奇怪的压力\n',
            '说实话倒是松了口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250810V#074F#4P唔，原来如此啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250811V#070F这样看来帝国关系者\n',
            '无辜的可能性似乎很高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250812V#1007F#6P嗯，似乎是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250813V#1006F大使先生，非常感谢您能\n',
            '告诉我们这些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0670250814V#1101F#5P哼、哼……怎么样。\n',
            '我一开始就说了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250815V要找犯人\n',
            '就赶快去别处吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250816V#1004F#6P啊，稍等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250817V#1015F嗯，其实还有\n',
            '一件事想问……',
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
            '关于玲的父母，试着询问了达维尔大使。',
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
            '#0670250818V#1102F#5P是吗……\n',
            '那真是可怜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250819V#1100F唔～帝国商人的话时常\n',
            '会来这个大使馆……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250820V不过说到克洛斯贝尔的\n',
            '贸易商倒是真的没印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 1)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0670250821V#1100F#5P穆拉怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0130,
        (
            '#0110250822V#272F#2P不……\n',
            '我也没有记忆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250823V#1015F#6P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250824V#1007F嗯～这边\n',
            '看来也是前途多难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 0)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0670250825V#1100F#5P不过竟然要同时寻找\n',
            '恐吓犯和迷路孩子的亲人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670250826V虽然是老调重弹\n',
            '还请你们加油不要放弃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250827V#1006F#6P啊……是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0130, 225, 400)
    Sleep(400)

    ChrTalk(
        0x0130,
        (
            '#0110250828V#277F#5P那么，我送你们到门口吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(700, 0, 70010, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 700, 0, 70010, 180)
    SetChrPos(0x0001, 700, 0, 70010, 180)
    SetChrPos(0x0002, 700, 0, 70010, 180)
    SetChrPos(0x0003, 700, 0, 70010, 180)
    SetChrPos(0x0130, 700, 0, 70010, 180)
    OP_71(0x0002, 0x0010)
    OP_64(0x00, 0x0001)
    OP_A2(0x1621)
    OP_28(0x008B, 0x02, 0x0020)
    OP_28(0x008B, 0x01, 0x0040)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x406C
@scena.Code('func_0C_406C')
def func_0C_406C():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -220, 0, 63670, 0)

    @scena.Lambda('lambda_4093')
    def lambda_4093():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4093)

    OP_8E(0x00FE, 1030, 0, 72080, 2000, 0x00)

    Return()

# id: 0x000D offset: 0x40B4
@scena.Code('func_0D_40B4')
def func_0D_40B4():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -220, 0, 63670, 0)

    @scena.Lambda('lambda_40DB')
    def lambda_40DB():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_40DB)

    OP_8E(0x00FE, -210, 0, 71510, 2000, 0x00)

    Return()

# id: 0x000E offset: 0x40FC
@scena.Code('func_0E_40FC')
def func_0E_40FC():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -220, 0, 63670, 0)

    @scena.Lambda('lambda_4123')
    def lambda_4123():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4123)

    OP_8E(0x00FE, 1850, 0, 71350, 2000, 0x00)

    Return()

# id: 0x000F offset: 0x4144
@scena.Code('func_0F_4144')
def func_0F_4144():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -220, 0, 63670, 0)

    @scena.Lambda('lambda_416B')
    def lambda_416B():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_416B)

    OP_8E(0x00FE, 590, 0, 70770, 2000, 0x00)

    Return()

# id: 0x0010 offset: 0x418C
@scena.Code('func_10_418C')
def func_10_418C():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, -220, 0, 63670, 0)

    @scena.Lambda('lambda_41B3')
    def lambda_41B3():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_41B3)

    OP_8E(0x00FE, -70, 0, 65349, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)
    OP_22(0x0007, 0x00, 0x64)
    Sleep(500)

    OP_8E(0x00FE, 3250, 0, 69520, 2500, 0x00)
    OP_8E(0x00FE, 3250, 0, 73470, 2500, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0011 offset: 0x4214
@scena.Code('func_11_4214')
def func_11_4214():
    OP_8E(0x00FE, 970, 4000, 33490, 2000, 0x00)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0012 offset: 0x4239
@scena.Code('func_12_4239')
def func_12_4239():
    OP_8E(0x00FE, 770, 4000, 31320, 3000, 0x00)
    OP_8E(0x00FE, 970, 4000, 33490, 3000, 0x00)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0013 offset: 0x4272
@scena.Code('func_13_4272')
def func_13_4272():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
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

# id: 0x0014 offset: 0x42AF
@scena.Code('func_14_42AF')
def func_14_42AF():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上有『红耀石』。',
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
        'loc_4390',
    )

    OP_B8(0x0212, 0x0000)

    def _loc_4390(): pass

    label('loc_4390')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43A2',
    )

    OP_B8(0x0213, 0x0000)

    def _loc_43A2(): pass

    label('loc_43A2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43B4',
    )

    OP_B8(0x0214, 0x0000)

    def _loc_43B4(): pass

    label('loc_43B4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43C6',
    )

    OP_B8(0x0215, 0x0000)

    def _loc_43C6(): pass

    label('loc_43C6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43D8',
    )

    OP_B8(0x0216, 0x0000)

    def _loc_43D8(): pass

    label('loc_43D8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43EA',
    )

    OP_B8(0x0217, 0x0000)

    def _loc_43EA(): pass

    label('loc_43EA')

    TalkEnd(0x00FF)

    Return()

# id: 0x0015 offset: 0x43EE
@scena.Code('func_15_43EE')
def func_15_43EE():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上有『红耀石』。',
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
            TXT(0x00, '【读第７卷】\n'),
            TXT(0x01, '【读第８卷】\n'),
            TXT(0x02, '【读第９卷】\n'),
            TXT(0x03, '【读第10卷】\n'),
            TXT(0x04, '【读最终卷】\n'),
            TXT(0x05, '【放弃】\n'),
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
        'loc_44C2',
    )

    OP_B8(0x0218, 0x0000)

    def _loc_44C2(): pass

    label('loc_44C2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44D4',
    )

    OP_B8(0x0219, 0x0000)

    def _loc_44D4(): pass

    label('loc_44D4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44E6',
    )

    OP_B8(0x021A, 0x0000)

    def _loc_44E6(): pass

    label('loc_44E6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44F8',
    )

    OP_B8(0x021B, 0x0000)

    def _loc_44F8(): pass

    label('loc_44F8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_450A',
    )

    OP_B8(0x021C, 0x0000)

    def _loc_450A(): pass

    label('loc_450A')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
