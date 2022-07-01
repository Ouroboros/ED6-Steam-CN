import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T5110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T5110   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '亚妮拉丝'),
    TXT(0x02, '克鲁茨'),
    TXT(0x03, '维修师罗伯特'),
    TXT(0x04, '菲莉斯管理员'),
    TXT(0x05, '目标用照相机'),
    TXT(0x06, '器皿'),
    TXT(0x07, '器皿'),
    TXT(0x08, '器皿'),
    TXT(0x09, '咖啡'),
    TXT(0x0A, '咖啡'),
    TXT(0x0B, '艾丝蒂尔的背部'),
    TXT(0x0C, '新型导力器'),
    TXT(0x0D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'T5110.x'
    header.mapIndex       = 1
    header.bgm            = 25
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T5110._SN', 'ED6_DT21/T5110_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3664
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
        ('ED6_DT27/CH03090._CH', 'ED6_DT27/CH03090P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT27/CH03093._CH', 'ED6_DT27/CH03093P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT27/CH03900._CH', 'ED6_DT27/CH03900P._CP'),
        ('ED6_DT07/CH01623._CH', 'ED6_DT07/CH01623P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT26/CH20269._CH', 'ED6_DT26/CH20269P._CP'),
        ('ED6_DT26/CH20235._CH', 'ED6_DT26/CH20235P._CP'),
        ('ED6_DT27/CH03133._CH', 'ED6_DT27/CH03133P._CP'),
    ]

# id: 0x10002 offset: 0x102
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0003,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            x                   = 26690,
            z                   = 0,
            y                   = 5140,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 24500,
            z                   = 0,
            y                   = 12470,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0005,
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
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65543,
            chipIndex           = 7,
            npcIndex            = 0x01E6,
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
            dword_10            = 65543,
            chipIndex           = 7,
            npcIndex            = 0x01E6,
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
            dword_10            = 65543,
            chipIndex           = 7,
            npcIndex            = 0x01E6,
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
            dword_10            = 1572871,
            chipIndex           = 7,
            npcIndex            = 0x01E6,
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
            dword_10            = 1638407,
            chipIndex           = 7,
            npcIndex            = 0x01E6,
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
            dword_10            = 1245192,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
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
            dword_10            = 917512,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x282
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x282
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 120250,
            y           = 0,
            z           = 1000,
            range       = 123170,
            dword_10    = 0x000007D0,
            dword_14    = 0x000007D0,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000009,
        ),
    )

# id: 0x10005 offset: 0x2A2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 25470,
            triggerZ            = -300,
            triggerY            = 4940,
            triggerRange        = 800,
            actorX              = 26690,
            actorZ              = 1500,
            actorY              = 5140,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 22500,
            triggerZ            = 0,
            triggerY            = 12360,
            triggerRange        = 800,
            actorX              = 24500,
            actorZ              = 1500,
            actorY              = 12470,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 15050,
            triggerZ            = 0,
            triggerY            = 12130,
            triggerRange        = 800,
            actorX              = 15050,
            actorZ              = 1000,
            actorY              = 12130,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 85780,
            triggerZ            = 0,
            triggerY            = 41480,
            triggerRange        = 700,
            actorX              = 85180,
            actorZ              = 500,
            actorY              = 41480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 113640,
            triggerZ            = 0,
            triggerY            = 41480,
            triggerRange        = 700,
            actorX              = 113040,
            actorZ              = 500,
            actorY              = 41480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x356
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Return,
        ),
        'loc_360',
    )

    Jump('loc_445')

    def _loc_360(): pass

    label('loc_360')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 6, 0x1006)),
            Expr.Return,
        ),
        'loc_36A',
    )

    Jump('loc_445')

    def _loc_36A(): pass

    label('loc_36A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 5, 0x1005)),
            Expr.Return,
        ),
        'loc_374',
    )

    Jump('loc_445')

    def _loc_374(): pass

    label('loc_374')

    SetChrPos(0x0008, 115980, 0, 37820, 90)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0009, 84690, 0, -30350, 0)
    ClearChrFlags(0x0009, 0x0080)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    SetChrPos(0x000B, 25910, 0, 16520, 0)
    SetChrPos(0x000A, 27980, 0, 6920, 180)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            Expr.Return,
        ),
        'loc_3D7',
    )

    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    def _loc_3D7(): pass

    label('loc_3D7')

    SetChrPos(0x000D, 18160, 800, 11990, 0)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x0010, 17670, 800, 12040, 0)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x000E, 17600, 800, 11180, 0)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x0011, 18270, 800, 10980, 0)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x000F, 18190, 800, 11550, 0)
    ClearChrFlags(0x000F, 0x0080)

    def _loc_445(): pass

    label('loc_445')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 5, 0x1005)),
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 6, 0x1006)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4A9',
    )

    TerminateThread(0x0009, 0xFF)
    SetChrFlags(0x0009, 0x0010)
    SetChrFlags(0x0008, 0x0010)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x0008, 0x0004)
    SetChrPos(0x0009, 15080, 200, 14890, 180)
    SetChrPos(0x0008, 13670, 200, 12380, 0)
    SetChrSubChip(0x0009, 0)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0009, 10)
    SetChrChipByIndex(0x0008, 2)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)

    def _loc_4A9(): pass

    label('loc_4A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_4B7',
    )

    OP_A3(0x10F0)
    Event(0, 0x0005)

    def _loc_4B7(): pass

    label('loc_4B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_4C5',
    )

    OP_A3(0x10F1)
    Event(0, 0x0006)

    def _loc_4C5(): pass

    label('loc_4C5')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 5, 0x1005)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4E1',
    )

    Event(0, 0x0007)

    def _loc_4E1(): pass

    label('loc_4E1')

    Return()

# id: 0x0001 offset: 0x4E2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F2',
    )

    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)

    def _loc_4F2(): pass

    label('loc_4F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 6, 0x1006)),
            Expr.Return,
        ),
        'loc_500',
    )

    OP_64(0x02, 0x0001)

    Jump('loc_522')

    def _loc_500(): pass

    label('loc_500')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 5, 0x1005)),
            Expr.Return,
        ),
        'loc_516',
    )

    OP_65(0x00, 0x0001)
    OP_65(0x01, 0x0001)
    OP_65(0x02, 0x0001)

    Jump('loc_522')

    def _loc_516(): pass

    label('loc_516')

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)

    def _loc_522(): pass

    label('loc_522')

    Return()

# id: 0x0002 offset: 0x523
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_554'),
        (0x00000001, 'loc_560'),
        (0x00000002, 'loc_56C'),
        (0x00000003, 'loc_578'),
        (0x00000004, 'loc_584'),
        (0x00000005, 'loc_590'),
        (0x00000006, 'loc_59C'),
        (-1, 'loc_5A8'),
    )

    def _loc_554(): pass

    label('loc_554')

    OP_99(0x00FE, 0x00, 0x07, 0x000005AA)

    Jump('loc_5B4')

    def _loc_560(): pass

    label('loc_560')

    OP_99(0x00FE, 0x00, 0x07, 0x0000060E)

    Jump('loc_5B4')

    def _loc_56C(): pass

    label('loc_56C')

    OP_99(0x00FE, 0x00, 0x07, 0x00000640)

    Jump('loc_5B4')

    def _loc_578(): pass

    label('loc_578')

    OP_99(0x00FE, 0x00, 0x07, 0x00000578)

    Jump('loc_5B4')

    def _loc_584(): pass

    label('loc_584')

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_5B4')

    def _loc_590(): pass

    label('loc_590')

    OP_99(0x00FE, 0x00, 0x07, 0x00000546)

    Jump('loc_5B4')

    def _loc_59C(): pass

    label('loc_59C')

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_5B4')

    def _loc_5A8(): pass

    label('loc_5A8')

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_5B4')

    def _loc_5B4(): pass

    label('loc_5B4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5C9',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_5B4')

    def _loc_5C9(): pass

    label('loc_5C9')

    Return()

# id: 0x0003 offset: 0x5CA
@scena.Code('func_03_5CA')
def func_03_5CA():
    Call(1, 0x0004)

    Return()

# id: 0x0004 offset: 0x5CF
@scena.Code('func_04_5CF')
def func_04_5CF():
    Call(1, 0x0005)

    Return()

# id: 0x0005 offset: 0x5D4
@scena.Code('func_05_5D4')
def func_05_5D4():
    EventBegin(0x00)
    OP_6D(27560, 0, 11600, 0)
    OP_67(0, 5860, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 18080, 200, 12890, 180)
    SetChrPos(0x0101, 18120, 200, 10470, 0)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0101, 1)
    SetChrChipByIndex(0x0008, 2)
    SetChrPos(0x000D, 18160, 800, 11990, 0)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x0010, 17670, 800, 12040, 0)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x000E, 17600, 800, 11180, 0)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x0011, 18270, 800, 10980, 0)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x000F, 18190, 800, 11550, 0)
    ClearChrFlags(0x000F, 0x0080)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_06D5')
    def lambda_06D5():
        OP_6D(18760, 200, 12150, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_06D5)

    @scena.Lambda('lambda_06ED')
    def lambda_06ED():
        OP_67(0, 7000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_06ED)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190461V#1016F呼……\n',
            '肚子吃得饱饱的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190462V演习前吃这么多\n',
            '好像不太好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190463V#811F#5P呵呵，管理员做的料理\n',
            '真的是很美味嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190464V#816F不过，这次演习和训练不同，\n',
            '中途是不能够休息的，\n',
            '吃饱点不是正好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190465V#1006F嗯，的确。\n',
            '毕竟体力是一切的基础嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190466V#1015F话说回来……\n',
            '来到这里已经３周了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190467V老实说，还真是一转眼的功夫呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190468V#810F#5P呵呵，艾丝蒂尔\n',
            '真是非常努力呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190469V我和你一起训练…\n',
            '真的，感觉太棒了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190470V#1008F嘿嘿……\n',
            '听你这么说我也很高兴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190471V#1006F不过，克鲁茨前辈\n',
            '会来到这里当训练教官\n',
            '已经够让人吃惊了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190472V亚妮拉丝竟然也会\n',
            '和我一起接受训练，\n',
            '实在是想都想不到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190473V#818F#5P嗯～我当上正游击士\n',
            '也才半年左右，还是个新手嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190474V#810F从雪拉前辈那里听说了\n',
            '艾丝蒂尔的事，\n',
            '就觉得这是个很好的机会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190475V以前听前辈们提过这个训练场之后，\n',
            '我就一直很有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190476V#1011F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190477V#1015F不过，竟然会有这种地方，\n',
            '看来协会也是相当大的组织呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190478V一开始听老爸他们说的时候\n',
            '还没有什么感觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_1F(0x46, 0x000003E8)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x0101, 65535)
    SetMapFlags(0x02000000)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T0310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0xB70
@scena.Code('func_06_B70')
def func_06_B70():
    ClearMapFlags(0x02000000)
    OP_BB(0x00, 0x00, 0x00200032)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    EventBegin(0x00)
    OP_6D(18760, 200, 12150, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 18080, 200, 12890, 180)
    SetChrPos(0x0101, 18120, 200, 10470, 0)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0101, 1)
    SetChrChipByIndex(0x0008, 2)
    FadeIn(1000, 0)
    OP_1F(0x64, 0x000003E8)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0120190517V#810F#5P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190518V那套衣服，是雪拉前辈\n',
            '的祝贺礼物啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190519V#811F好羡慕～\n',
            '给你买这么可爱的衣服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190520V#1013F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190521V布料相当结实，\n',
            '活动起来也很方便……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190522V不过这种女性化的衣服\n',
            '大概不适合我吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190523V#816F#5P才没这回事！\n',
            '非常非常适合你哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190524V而且就算是游击士，\n',
            '女孩子也需要好好打扮哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190525V#815F不、正因为是游击士\n',
            '所以才必须要认真地打扮！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190526V#1004F亚、亚妮拉丝？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190527V#1310F#5P对了，艾丝蒂尔。\n',
            '想不想扎个丝带看看？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190528V#811F我想一定很好看的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190529V#1008F心、心领了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190530V#1016F话说回来……\n',
            '以前我就一直在想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190531V亚妮拉丝你\n',
            '是不是对可爱的东西毫无免疫力？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190532V#811F#5P当然了！\n',
            '可爱即是正义嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190533V#1310F虽然像雪拉前辈那样\n',
            '帅气的大姐姐也很令人向往……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190534V不过终究还是比不上\n',
            '打扮可爱的小女孩啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190535V#1311F如果再抱着布偶之类的东西…\n',
            '就让人更想紧紧地抱住了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190536V#1016F啊、啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190537V（她要是见到提妲的话，\n',
            '  说不定会激动得昏倒呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190538V#1314F#5P嘻嘻，话说回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190539V和第一次相遇时比起来，\n',
            '艾丝蒂尔，你变了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190540V#1004F咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190541V#817F#5P一开始就是个新人，\n',
            '给人一副涉世未深的印象……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190542V现在，虽然还是涉世未深，\n',
            '但给人的感觉却更加可靠了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190543V#816F你可真厉害哦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190544V#1008F讨、讨厌啦……\n',
            '亚妮拉丝，不要奉承我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190545V#811F#5P啊哈哈，别害羞别害羞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190546V#816F嗯，作为前辈\n',
            '我也不能输给你啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190547V#1013F真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190548V#1004F对了，亚妮拉丝。\n',
            '差不多到演习的时间了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190549V#814F#5P啊，是哦。\n',
            '先回房间吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190550V#811F那么，一会儿见～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 0)
    ClearChrFlags(0x0008, 0x0004)
    SetChrPos(0x0008, 19230, 0, 12970, 98)
    OP_0D()
    SetChrSubChip(0x0101, 2)
    OP_8E(0x0008, 20820, 0, 9330, 3000, 0x00)

    @scena.Lambda('lambda_133D')
    def lambda_133D():
        OP_8E(0x0008, 27820, 2000, 9030, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_133D)

    @scena.Lambda('lambda_1358')
    def lambda_1358():
        OP_6D(20870, 200, 10700, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1358)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_137A')
    def lambda_137A():
        OP_8E(0x0008, 27780, 2000, 10940, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_137A)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_139A')
    def lambda_139A():
        OP_8E(0x0008, 25560, 3500, 11290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_139A)

    @scena.Lambda('lambda_13B5')
    def lambda_13B5():
        OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_13B5)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_13CC')
    def lambda_13CC():
        OP_6D(18770, 200, 11170, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_13CC)

    WaitForThreadExit(0x0101, 0x0001)
    SetChrFlags(0x0008, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010190551V#5P#1017F呼～真是个充满朝气的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190552V和亚妮拉丝在一起，\n',
            '我也轻松多了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190553V#5P#1006F好了，我也回房间\n',
            '准备一下必要的装备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(ItemTable['卢·洛克尔地图'], 1)
    AddItem(ItemTable['正游击士的徽章'], 1)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(19120, 0, 10210, 0)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    ClearChrFlags(0x0101, 0x0004)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 19120, 0, 10210, 103)
    OP_A2(0x1004)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1520
@scena.Code('func_07_1520')
def func_07_1520():
    EventBegin(0x00)
    OP_6D(87090, 0, 40680, 0)
    OP_67(0, 6050, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 86470, 0, 35830, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrPos(0x0012, 84860, 100, 41540, 0)
    SetChrChipByIndex(0x0012, 8)
    SetChrSubChip(0x0012, 0)
    ClearChrFlags(0x0012, 0x0080)
    FadeIn(1000, 0)
    OP_9F(0x0101, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_15B4')
    def lambda_15B4():
        OP_9F(0x0101, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_15B4)

    OP_8E(0x0101, 86510, 0, 37420, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190554V#1015F#5P那么，既然是演习，\n',
            '一般的装备还是必要的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190555V毕竟和实战一样，\n',
            '也不知道会发生什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_165F')
    def lambda_165F():
        OP_6D(87290, 0, 42930, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_165F)

    @scena.Lambda('lambda_1677')
    def lambda_1677():
        OP_67(0, 6050, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1677)

    @scena.Lambda('lambda_168F')
    def lambda_168F():
        OP_6B(2800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_168F)

    OP_8E(0x0101, 86200, 0, 41710, 2000, 0x00)
    OP_8C(0x0101, 261, 500)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0101)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔从背包里取出了口琴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Fade(500)
    SetChrFlags(0x0101, 0x0002)
    SetChrChipByIndex(0x0101, 9)
    SetChrSubChip(0x0101, 7)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010190556V#5P#1025F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190557V#1012F嗯，今天也要加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    ClearChrFlags(0x0101, 0x0002)
    OP_0D()
    OP_9F(0x0012, 0xFF, 0xFF, 0xFF, 0x00, 0x000001F4)
    SetChrFlags(0x0012, 0x0080)
    OP_D6(0x01)
    AddItem(ItemTable['利贝尔王国地图'], 1)
    AddItem(ItemTable['卢·洛克尔地图'], 1)
    AddItem(ItemTable['正游击士的徽章'], 1)
    AddItem(ItemTable['约修亚的口琴'], 1)
    AddMira(1000)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['战斗用棍'], 0xFF)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['强化皮铠'], 0xFF)
    EquipCmd(ChrTable['艾丝蒂尔'], ItemTable['强化皮靴'], 0xFF)
    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['约修亚的口琴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['战斗用棍']),
            (TxtCtl.SetColor, 0x0),
            '装备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['强化皮铠']),
            (TxtCtl.SetColor, 0x0),
            '装备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['强化皮靴']),
            (TxtCtl.SetColor, 0x0),
            '装备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0456, 3, 0x22B3)),
            Expr.Return,
        ),
        'loc_1866',
    )

    AddItem(ItemTable['塞姆里亚石'], 1)
    OP_A3(0x22B3)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['塞姆里亚石']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1866(): pass

    label('loc_1866')

    OP_22(0x0014, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x4),
            '１０００',
            (TxtCtl.SetColor, 0x0),
            '米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010190558V#5P#1006F这样就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190559V……那么\n',
            '去大门吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1005)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x18E3
@scena.Code('func_08_18E3')
def func_08_18E3():
    EventBegin(0x00)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x0008, 0x00)
    Fade(1000)
    SetChrFlags(0x0101, 0x0004)
    SetChrPos(0x0101, 15080, 200, 12380, 0)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 1)
    OP_6D(15150, 0, 14940, 0)
    OP_67(0, 6200, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19FB',
    )

    ChrTalk(
        0x0009,
        (
            '#0330190560V#843F来了吗，艾丝蒂尔。\n',
            '那么现在马上开始演习吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190561V#842F今天的演习是遗迹探索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190562V你们要进入宿舍西边的\n',
            '『巴斯塔尔水道』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A5D')

    def _loc_19FB(): pass

    label('loc_19FB')

    ChrTalk(
        0x0009,
        (
            '#0330190561V#842F今天的演习是遗迹探索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190562V你们要进入宿舍西边的\n',
            '『巴斯塔尔水道』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A5D(): pass

    label('loc_1A5D')

    ChrTalk(
        0x0101,
        (
            '#0010190565V#1002F『巴斯塔尔水道』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190566V好古老的名字，\n',
            '是训练用的设施吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330190567V#840F啊啊。\n',
            '是在中世纪遗迹上重建而成的设施。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190568V里面遗留着从前的机关，\n',
            '同时也游荡着大量危险的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190569V#816F#6P原——来如此。\n',
            '看起来相当接近实战呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190570V那么我们就\n',
            '马上出发前往那个水道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330190571V#843F不，在那之前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190572V#842F你们两人先看看这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '克鲁茨取出了陌生形状的导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0x0013, 0x0004)
    OP_22(0x0082, 0x00, 0x64)
    SetChrPos(0x0013, 14500, 150, 13630, 180)
    OP_9F(0x0013, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrChipByIndex(0x0013, 8)
    SetChrSubChip(0x0013, 1)
    ClearChrFlags(0x0013, 0x0080)
    OP_9F(0x0013, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)
    Sleep(500)

    FadeOut(300, 0, 100)
    OP_AD(0x0024008F, 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010190573V#1004F咦，这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName('亚妮拉丝')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0120190574V#814F#6P难不成……\n',
            '是战术导力器吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(180, 0, -1, -1)
    SetChrName('克鲁茨')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0330190575V#840F嗯嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190576V可以使用导力魔法的\n',
            '战术导力器，据说是\n',
            '『爱普斯坦财团』制造的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190577V这是在上个月\n',
            '刚从财团送来的最新型。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190578V结晶孔的数量增加为７个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190579V在现有的魔法基础上\n',
            '还能组合出新型的魔法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010190580V#1006F哟～很棒嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName('亚妮拉丝')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0120190581V#811F#6P嗯嗯！\n',
            '看来相当值得期待呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190582V#810F那，克鲁茨前辈。\n',
            '我们也能够拿到吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(180, 0, -1, -1)
    SetChrName('克鲁茨')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0330190583V#840F嗯嗯，只要提出申请，\n',
            '协会就会免费提供。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190584V#843F只是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(500)

    FadeIn(300, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0330190585V#842F目前有一个难题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190586V新型导力器大幅改动了\n',
            '以往基本构造。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190587V但是，由于兼容性的问题\n',
            '无法安装以前的结晶回路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190588V而是需要新规格的结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190589V#1004F咦咦～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190590V那、那就是说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190591V#814F#6P以前合成的结晶回路\n',
            '都白费了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330190592V#840F很遗憾，没有错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190593V虽然相当麻烦，不过\n',
            '只能从头一个个去收集了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190594V#1007F不，不是吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190595V#1316F#6P嗯……\n',
            '真是让人犹豫呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190596V#810F就这样继续使用\n',
            '现在的导力器不行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330190597V#843F虽然不是不行，但并不推荐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190598V#842F新型导力器各方面的性能\n',
            '都比以前的型号更高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190599V不但最大ＥＰ大幅度地提高了，\n',
            '而且适用于最新型的结晶回路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190600V就前景来说，可以期待它\n',
            '更进一步地提高身体能力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190601V#843F而且不管怎么说，\n',
            '最大优点就是在于可以组合出\n',
            '以前的导力器所没有的新魔法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190602V#842F……艾丝蒂尔。\n',
            '你还记得洛伦斯少尉吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190603V#1020F哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD(0x002400BF, 0x0000, 0x0000, 0x000000C8)
    Sleep(2000)

    OP_AE(0x000000C8)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190604V#1026F嗯，嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190605V这个对手让人\n',
            '想忘都忘不掉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330190606V#842F雪拉告诉过我，\n',
            '他似乎使用了未知的魔法吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190607V除了大范围攻击对手之外，\n',
            '还能带来混乱效果的高级魔法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190608V其实，新型导力器\n',
            '也可以组合出这种魔法哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190609V名为『银色荆棘』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190610V#1002F『银色荆棘』……',
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
            '#0120190611V#812F#6P这、这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190612V那个蒙面队长\n',
            '早就在使用新型的导力器吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330190613V#843F很有可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190614V#842F好了，你们怎么决定？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190615V#813F#6P呜、嗯……\n',
            '果然还是很犹豫呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190616V就前景方面虽然是新型胜出，\n',
            '但目前的战力下降实在让人心痛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190617V#1010F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190618V#1011F我……\n',
            '想试着运用新型导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 2)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0120190619V#814F#6P咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190620V#1003F那个时候，我完全\n',
            '无法对抗那名银发男子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190621V更换导力器的话，\n',
            '虽然并不代表可以让自己变强……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190622V#1002F但是我还是希望能\n',
            '试着将更强大的力量运用自如。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190623V所以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190624V#814F#6P艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190625V#816F……嗯，说得是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0120190626V#1310F#6P克鲁茨前辈。\n',
            '请让我也使用新型的吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330190627V#841F好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190628V那么收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9F(0x0013, 0xFF, 0xFF, 0xFF, 0x00, 0x000001F4)
    ClearChrFlags(0x0013, 0x0080)
    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '得到新型战术导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    AddItem(ItemTable['正游击士手册'], 1)
    FadeIn(300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0330190629V#840F还有，给你们这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '得到了各属性的耀晶片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    AddSepith(0x00, 0x0014)
    AddSepith(0x01, 0x0014)
    AddSepith(0x02, 0x0032)
    AddSepith(0x03, 0x0014)
    AddSepith(0x04, 0x0064)
    AddSepith(0x06, 0x0014)
    FadeIn(300, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0330190630V#840F只要有这些\n',
            '基本的结晶回路就齐了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190631V去演习之前，到那边的工房\n',
            '请罗伯特合成就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190632V新的结晶回路和导力魔法列表\n',
            '已经追加在游击士手册里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190633V去工房的时候\n',
            '自己去确认吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190634V#1006F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330190635V#840F还有……\n',
            '今天的演习应该过程较长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190636V为预防万一，\n',
            '最好连食材也准备好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190637V#818F#6P嗯～食材啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190638V#816F这个去找菲莉斯小姐\n',
            '就ＯＫ了对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330190639V#843F啊啊，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190640V罗伯特先生和菲莉斯管理员……\n',
            '罗伯特先生和菲莉斯管理员……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x35),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B46',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x34),
            (Expr.PushLong, 0x170),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2B39',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2B43')

    def _loc_2B39(): pass

    label('loc_2B39')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2B43(): pass

    label('loc_2B43')

    Jump('loc_2B75')

    def _loc_2B46(): pass

    label('loc_2B46')

    If(
        (
            (Expr.PushValueByIndex, 0x35),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B5F',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2B75')

    def _loc_2B5F(): pass

    label('loc_2B5F')

    If(
        (
            (Expr.PushValueByIndex, 0x35),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B75',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2B75(): pass

    label('loc_2B75')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31B5',
    )

    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0330190641V#840F好了，艾丝蒂尔\n',
            '顺便也收下这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000001, 'loc_2BDF'),
        (0x00000002, 'loc_2DAA'),
        (0x00000003, 'loc_2F1D'),
        (0x00000004, 'loc_306D'),
        (-1, 'loc_31AC'),
    )

    def _loc_2BDF(): pass

    label('loc_2BDF')

    AddItem(ItemTable['机械手套'], 1)
    AddItem(ItemTable['圣灵药'], 1)
    AddItem(ItemTable['土人偶'], 1)
    AddItem(ItemTable['幸运'], 1)
    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['机械手套']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['土人偶']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['幸运']),
            (TxtCtl.SetColor, 0x0),
            '结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010190642V#1004F咦，这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190643V#1310F#6P啊，好羡慕～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190644V#811F而且是相当\n',
            '好的东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330190645V#841F啊啊，都是特别定制的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190646V当然结晶回路\n',
            '是新型导力器用的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190647V就当作是协会对于你之前\n',
            '准游击士的功绩所给予的报酬吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190648V#1008F嘿嘿，谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31AC')

    def _loc_2DAA(): pass

    label('loc_2DAA')

    FadeOut(300, 0, 100)
    AddItem(ItemTable['机械手套'], 1)
    AddItem(ItemTable['圣灵药'], 1)
    AddItem(ItemTable['土人偶'], 1)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['机械手套']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['土人偶']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010190642V#1004F咦，这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190643V#1310F#6P啊，好羡慕～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190644V#811F而且是相当\n',
            '好的东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330190652V#841F啊啊，每个都是特别定制的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190647V就当是由于准游击士的功绩\n',
            '行会给予的报酬吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190648V#1008F嘿嘿，谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31AC')

    def _loc_2F1D(): pass

    label('loc_2F1D')

    FadeOut(300, 0, 100)
    AddItem(ItemTable['机械手套'], 1)
    AddItem(ItemTable['圣灵药'], 1)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['机械手套']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010190642V#1004F咦，这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190643V#1310F#6P啊，好羡慕～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190644V#811F而且是相当\n',
            '好的东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330190658V#841F啊啊，是特别定制的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190647V就当是由于准游击士的功绩\n',
            '行会给予的报酬吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190648V#1008F嘿嘿，谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31AC')

    def _loc_306D(): pass

    label('loc_306D')

    FadeOut(300, 0, 100)
    AddItem(ItemTable['机械手套'], 1)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['机械手套']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010190642V#1004F咦，这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190643V#1310F#6P啊，好羡慕～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190644V#811F而且看来是\n',
            '相当好的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330190658V#841F嗯嗯，是特别定制的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190647V就当作是协会对你之前\n',
            '准游击士的功绩所给予的报酬吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190648V#1008F嘿嘿，谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31AC')

    def _loc_31AC(): pass

    label('loc_31AC')

    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_31B5(): pass

    label('loc_31B5')

    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0330190667V#840F那么我就在\n',
            '宿舍的出口等你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190668V准备完毕的话就过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    SetChrPos(0x0009, 16210, 0, 14960, 93)
    ClearChrFlags(0x0009, 0x0004)
    SetChrSubChip(0x0009, 0)
    SetChrChipByIndex(0x0009, 3)
    OP_0D()

    @scena.Lambda('lambda_3243')
    def lambda_3243():
        OP_6D(18450, 0, 12380, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3243)

    SetChrSubChip(0x0008, 2)

    @scena.Lambda('lambda_3260')
    def lambda_3260():
        OP_8E(0x0009, 18650, 0, 14500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3260)

    Sleep(500)

    SetChrSubChip(0x0101, 2)
    WaitForThreadExit(0x0009, 0x0000)

    @scena.Lambda('lambda_328A')
    def lambda_328A():
        OP_8E(0x0009, 21140, 0, 11910, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_328A)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_32AA')
    def lambda_32AA():
        OP_8E(0x0009, 21480, -300, 7000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_32AA)

    WaitForThreadExit(0x0009, 0x0002)
    SetChrFlags(0x0009, 0x0080)
    Sleep(1000)

    @scena.Lambda('lambda_32D4')
    def lambda_32D4():
        OP_6D(14220, 600, 12150, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_32D4)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0120190669V#816F#6P那么，艾丝蒂尔。\n',
            '我们马上开始演习的准备吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 0)
    Sleep(75)

    SetChrSubChip(0x0101, 1)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010190670V#1006F#2P嗯，要去菲莉斯小姐\n',
            '和罗伯特先生那里\n',
            '询问他们一下才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x0101, 0)
    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0008, 0x0080)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    SetChrPos(0x0101, 16020, 0, 11870, 160)
    SetChrPos(0x010A, 16020, 0, 11870, 160)
    OP_6D(16020, 0, 11870, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['直刃剑'], 0xFF)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['强化皮铠'], 0xFF)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['强化皮靴'], 0xFF)
    OP_BB(0x09, 0x06, 0x00000110)
    SetChrStatus(ChrTable['亚妮拉丝'], 0x00, 40)
    SetChrStatus(ChrTable['亚妮拉丝'], 0xFE, 0)
    AddCraft(ChrTable['亚妮拉丝'], 0x0000)
    Sleep(500)

    OP_64(0x02, 0x0001)
    OP_A2(0x1006)
    OP_28(0x00C5, 0x04, 0x02)
    OP_28(0x00C5, 0x04, 0x08)
    OP_28(0x00C5, 0x01, 0x0001)
    OP_28(0x00C5, 0x01, 0x0002)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※『正游击士手册』（游击士手册）能够使用了。\n',
            '　工作上的事情和导力器的详细说明\n',
            '　都可以参考这本手册。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '※游击士手册的打开方法：在整备画面内［Item］栏\n',
            '  的［书籍］分类标签当中使用『正游击士手册』，\n',
            '  或是点选画面右下角的图示（蓝）。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x3557
@scena.Code('func_09_3557')
def func_09_3557():
    EventBegin(0x01)
    OP_8C(0x0000, 174, 500)
    OP_22(0x0071, 0x00, 0x64)
    Sleep(1000)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门牢牢地锁着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_90(0x0000, 0, 0, 1000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000A offset: 0x35AF
@scena.Code('func_0A_35AF')
def func_0A_35AF():
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
            TXT(0x00, '休息\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3633',
    )

    OP_20(0x00000BB8)
    FadeOut(1000, 0, -1)
    Sleep(700)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    SetChrStatus(ChrTable['亚妮拉丝'], 0xFE, 0)
    OP_8C(0x0000, 270, 0)
    OP_30(0x00)
    Sleep(3500)

    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_3633(): pass

    label('loc_3633')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_364D',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_364D(): pass

    label('loc_364D')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
