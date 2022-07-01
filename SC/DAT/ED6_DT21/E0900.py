import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0900_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0900   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '尤莉亚上尉'),
    TXT(0x02, '摩尔根将军'),
    TXT(0x03, '奈尔'),
    TXT(0x04, '朵洛希'),
    TXT(0x05, '士兵'),
    TXT(0x06, '士兵'),
    TXT(0x07, '士兵'),
    TXT(0x08, '士兵'),
    TXT(0x09, '埃尔赛尤'),
    TXT(0x0A, '警备艇'),
    TXT(0x0B, '古代龙'),
    TXT(0x0C, '船子'),
    TXT(0x0D, '龙'),
    TXT(0x0E, '拉赛尔博士'),
    TXT(0x0F, '亲卫队'),
    TXT(0x10, '维修员'),
    TXT(0x11, '维修员'),
    TXT(0x12, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0900.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x348F
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
        ('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT07/CH00324._CH', 'ED6_DT07/CH00324P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10002 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x32A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x32A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x32A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x32A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_340',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0002)

    Jump('loc_389')

    def _loc_340(): pass

    label('loc_340')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_35F',
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x000E)

    Jump('loc_389')

    def _loc_35F(): pass

    label('loc_35F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_379',
    )

    OP_A3(0x10F2)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x73),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x000F)

    Jump('loc_389')

    def _loc_379(): pass

    label('loc_379')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Return,
        ),
        'loc_389',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0005)

    def _loc_389(): pass

    label('loc_389')

    Return()

# id: 0x0001 offset: 0x38A
@scena.Code('Init')
def Init():
    OP_B1('E0900_1')
    OP_22(0x01C5, 0x00, 0x64)

    Return()

# id: 0x0002 offset: 0x399
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    OP_DB()
    SetChrFlags(0x0101, 0x0080)
    OP_6D(16050, -2990, 10740, 0)
    OP_67(0, 6840, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(109000, 0)
    OP_6E(592, 0)
    OP_A1(0x0013, 0x0003)
    SetChrPos(0x0013, 24950, -3000, 26730, 0)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x0000003C)
    OP_71(0x0000, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_71(0x0004, 0x0020)
    OP_B0(0x0004, 0x1E)
    OP_6F(0x0004, 330)
    OP_70(0x0004, 0x000001AE)
    OP_6F(0x0002, 15)
    Yield()
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrBattleFlags(0x000C, 0x0020)
    SetChrBattleFlags(0x000D, 0x0020)
    SetChrBattleFlags(0x000E, 0x0020)
    OP_89(0x000C, 24810, -2950, 27690, 0)
    OP_89(0x000D, 25230, -2930, 26770, 90)
    OP_89(0x000E, 24980, -2950, 25390, 180)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x000D, 0x0040)
    SetChrFlags(0x000E, 0x0040)
    SetChrChipByIndex(0x000C, 7)
    SetChrChipByIndex(0x000D, 7)
    SetChrChipByIndex(0x000E, 7)
    SetChrSubChip(0x000C, 3)
    SetChrSubChip(0x000D, 3)
    SetChrSubChip(0x000E, 3)
    SetChrFlags(0x000C, 0x0020)
    SetChrFlags(0x000D, 0x0020)
    SetChrFlags(0x000E, 0x0020)
    LoadEffect(0x00, 'map\\\\mpsibuk.eff')
    LoadEffect(0x01, 'map\\\\mp013_02.eff')
    LoadEffect(0x02, 'map\\\\mp013_00.eff')
    LoadEffect(0x03, 'map\\\\mp013_01.eff')
    OP_A1(0x0010, 0x0004)
    SetChrPos(0x0010, -69820, 15000, 28400, 90)
    ClearChrFlags(0x0010, 0x0100)
    OP_D1(16, 0, 90000, 0, 0)

    @scena.Lambda('lambda_0540')
    def lambda_0540():
        OP_6B(2960, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0540)

    OP_C8(0x0200, 0x0046, 'C_PLAC16._CH', 0x01, 0x03E8)
    FadeIn(1000, 0)
    Sleep(2000)

    @scena.Lambda('lambda_0573')
    def lambda_0573():
        OP_6D(18530, -2990, 19010, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0573)

    @scena.Lambda('lambda_058B')
    def lambda_058B():
        OP_67(0, 12280, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_058B)

    @scena.Lambda('lambda_05A3')
    def lambda_05A3():
        OP_6C(122000, 4000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_05A3)

    Sleep(500)

    CreateThread(0x0013, 0x00, 0x00, 0x0004)
    SetChrFlags(0x0010, 0x0001)
    ClearChrFlags(0x0010, 0x0080)

    ExecExpressionWithValue(
        0x0010,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x34,
        (
            (Expr.PushLong, 0x2BF20),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x0125, 0x01, 0x28)
    OP_24(0x0125, 0x28)
    Sleep(1000)

    OP_24(0x0125, 0x32)
    Sleep(1000)

    OP_24(0x0125, 0x3C)
    Sleep(1000)

    OP_24(0x0125, 0x46)
    Sleep(1000)

    OP_24(0x0125, 0x50)
    Sleep(1000)

    OP_24(0x0125, 0x55)
    Sleep(1000)

    OP_24(0x0125, 0x5A)
    Sleep(1000)

    OP_24(0x0125, 0x5F)

    @scena.Lambda('lambda_0638')
    def lambda_0638():
        OP_8F(0x00FE, 31820, 15000, 25400, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0638)

    Sleep(1000)

    OP_24(0x0125, 0x64)
    Fade(500)
    OP_6D(-1420, 17640, 19710, 0)
    OP_67(0, 8860, -10000, 0)
    OP_6B(5690, 0)
    OP_6C(146000, 0)
    OP_6E(592, 0)
    Sleep(1000)

    @scena.Lambda('lambda_06A3')
    def lambda_06A3():
        OP_6D(8660, 30000, 16320, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_06A3)

    @scena.Lambda('lambda_06BB')
    def lambda_06BB():
        OP_67(0, 12670, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_06BB)

    @scena.Lambda('lambda_06D3')
    def lambda_06D3():
        OP_6B(8100, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_06D3)

    Sleep(500)

    @scena.Lambda('lambda_06E8')
    def lambda_06E8():
        OP_D1(254, 0, 90000, -20000, 1500)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_06E8)

    WaitForThreadExit(0x0010, 0x0001)
    Fade(500)

    @scena.Lambda('lambda_070C')
    def lambda_070C():
        OP_97(0x0010, 0x000064DC, 0xFFFFE9EE, 0x00015F90, 0x00007530, 0x0001)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_070C)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_072D')
    def lambda_072D():
        OP_97(0x0010, 0x000064DC, 0xFFFFE9EE, 0x00015F90, 0x00005DC0, 0x0001)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_072D)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_074E')
    def lambda_074E():
        OP_97(0x0010, 0x000064DC, 0xFFFFE9EE, 0x000061A8, 0x00004E20, 0x0001)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_074E)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_076F')
    def lambda_076F():
        OP_97(0x0010, 0x000064DC, 0xFFFFE9EE, 0x00004E20, 0x00003E80, 0x0001)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_076F)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_0790')
    def lambda_0790():
        OP_97(0x0010, 0x000064DC, 0xFFFFE9EE, 0x00002710, 0x00002EE0, 0x0001)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0790)

    @scena.Lambda('lambda_07AC')
    def lambda_07AC():
        OP_D1(254, 0, 360000, 0, 1500)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_07AC)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_07CB')
    def lambda_07CB():
        OP_97(0x0010, 0x000064DC, 0xFFFFE9EE, 0x00001388, 0x00001F40, 0x0001)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_07CB)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_07EC')
    def lambda_07EC():
        OP_8F(0x0010, -4230, 15000, -7650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_07EC)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_080C')
    def lambda_080C():
        OP_6D(5290, -2990, 340, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_080C)

    @scena.Lambda('lambda_0824')
    def lambda_0824():
        OP_67(0, 8860, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0824)

    @scena.Lambda('lambda_083C')
    def lambda_083C():
        OP_6B(5980, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_083C)

    @scena.Lambda('lambda_084C')
    def lambda_084C():
        OP_6C(135000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_084C)

    @scena.Lambda('lambda_085C')
    def lambda_085C():
        OP_6E(592, 8000)

        ExitThread()

    DispatchAsync(0x0012, 0x0000, lambda_085C)

    SetChrPos(0x0010, -4230, 15000, -7650, 0)
    Sleep(1000)

    OP_72(0x0000, 0x0020)
    OP_73(0x0000)
    OP_6F(0x0004, 430)
    OP_70(0x0004, 0x00000320)
    CreateThread(0x0010, 0x03, 0x00, 0x0003)

    @scena.Lambda('lambda_089F')
    def lambda_089F():
        OP_8F(0x00FE, -4230, 50, -7650, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_089F)

    Sleep(2500)

    @scena.Lambda('lambda_08BF')
    def lambda_08BF():
        OP_8F(0x00FE, -4230, 50, -7650, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_08BF)

    Sleep(1500)

    @scena.Lambda('lambda_08DF')
    def lambda_08DF():
        OP_8F(0x00FE, -4230, 50, -7650, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_08DF)

    OP_22(0x00DC, 0x00, 0x64)
    OP_23(0x0079)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    OP_E8(0x88, 0x13, 0x00, 0x00)
    PlayEffect(0x00, 0xFF, 0x0010, 3600, 0, 22870, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, 5550, 0, 18820, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, 9480, 0, 16660, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, 8470, 0, 11180, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, 5930, 0, 13690, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, 5590, 0, 8880, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, 9170, 0, 6400, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, 11620, 0, 3140, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, 11760, 0, -2390, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, 11440, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, 9040, 0, -10280, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, 4730, 0, -11890, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, 5560, 0, -17380, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, -3600, 0, 22870, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, -5550, 0, 18820, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, -9480, 0, 16660, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, -8470, 0, 11180, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, -5930, 0, 13690, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, -5590, 0, 8880, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, -9170, 0, 6400, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, -11620, 0, 3140, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, -11760, 0, -2390, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, -11440, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, -9040, 0, -10280, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, -4730, 0, -11890, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0010, -5560, 0, -17380, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0010, 0x0001)
    OP_6F(0x0000, 1800)
    OP_70(0x0000, 0x0000073A)
    FadeOut(1000, 0, -1)
    OP_0D()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00000010)
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    OP_DC()
    SetMapFlags(0x02000000)
    OP_A2(0x10F5)
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0xEB5
@scena.Code('func_03_EB5')
def func_03_EB5():
    Sleep(2400)

    OP_22(0x00DD, 0x00, 0x64)
    Sleep(450)

    OP_22(0x00DD, 0x00, 0x64)
    Sleep(450)

    OP_22(0x00DD, 0x00, 0x64)
    Sleep(450)

    Return()

# id: 0x0004 offset: 0xED9
@scena.Code('func_04_ED9')
def func_04_ED9():
    PlayEffect(0x02, 0x05, 0x0013, 0, 0, 2200, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x06, 0x0013, 0, -150, -1800, 180, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0F49')
    def lambda_0F49():
        OP_8F(0x00FE, 22370, -2990, 22580, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0F49)

    Sleep(100)

    @scena.Lambda('lambda_0F69')
    def lambda_0F69():
        OP_8C(0x00FE, 90, 20)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0F69)

    Sleep(300)

    @scena.Lambda('lambda_0F7C')
    def lambda_0F7C():
        OP_8C(0x00FE, 90, 0)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_0F7C)

    @scena.Lambda('lambda_0F8A')
    def lambda_0F8A():
        OP_8C(0x00FE, 180, 0)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0F8A)

    @scena.Lambda('lambda_0F98')
    def lambda_0F98():
        OP_8C(0x00FE, 270, 0)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_0F98)

    WaitForThreadExit(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0002)

    @scena.Lambda('lambda_0FB0')
    def lambda_0FB0():
        OP_8F(0x00FE, 13400, -2990, 22790, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0FB0)

    Sleep(100)

    @scena.Lambda('lambda_0FD0')
    def lambda_0FD0():
        OP_8F(0x00FE, 13400, -2990, 22790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0FD0)

    Sleep(3000)

    @scena.Lambda('lambda_0FF0')
    def lambda_0FF0():
        OP_8F(0x00FE, 13400, -2990, 22790, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0FF0)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_82(0x05, 0x00)
    OP_82(0x06, 0x00)
    PlayEffect(0x01, 0xFF, 0x0013, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    SetChrSubChip(0x000C, 0)
    Sleep(100)

    SetChrSubChip(0x000D, 0)
    Sleep(100)

    SetChrSubChip(0x000E, 0)
    Sleep(100)

    @scena.Lambda('lambda_106E')
    def lambda_106E():
        OP_8C(0x00FE, 180, 0)
        Yield()

        Jump('lambda_106E')

    DispatchAsync2(0x000C, 0x0002, lambda_106E)

    @scena.Lambda('lambda_107F')
    def lambda_107F():
        OP_8C(0x00FE, 180, 0)
        Yield()

        Jump('lambda_107F')

    DispatchAsync2(0x000D, 0x0002, lambda_107F)

    @scena.Lambda('lambda_1090')
    def lambda_1090():
        OP_8C(0x00FE, 180, 0)
        Yield()

        Jump('lambda_1090')

    DispatchAsync2(0x000E, 0x0002, lambda_1090)

    Return()

# id: 0x0005 offset: 0x109C
@scena.Code('func_05_109C')
def func_05_109C():
    EventBegin(0x00)
    OP_DB()
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0105, 0x0080)
    SetChrFlags(0x0103, 0x0080)
    SetChrFlags(0x0104, 0x0080)
    SetChrFlags(0x0108, 0x0080)
    OP_6D(470, 3050, 11510, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(107000, 0)
    OP_6E(348, 0)
    SetChrPos(0x0009, -2450, 2550, 7820, 45)
    SetChrPos(0x0008, -4050, 2550, 8210, 45)
    SetChrPos(0x000A, -4620, 3050, 9670, 45)
    SetChrPos(0x000B, -3020, 3050, 9520, 45)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x0008, 0x0004)

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A1(0x0013, 0x0003)
    SetChrPos(0x0013, 9510, -3000, 21510, 67)
    Yield()
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrBattleFlags(0x000C, 0x0020)
    SetChrBattleFlags(0x000D, 0x0020)
    SetChrBattleFlags(0x000E, 0x0020)
    OP_89(0x000C, 10370, -2960, 21920, 72)
    OP_89(0x000D, 9200, -2950, 21540, 162)
    OP_89(0x000E, 8220, -2960, 21060, 162)
    SetChrChipByIndex(0x000C, 7)
    SetChrSubChip(0x000C, 3)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x000D, 0x0040)
    SetChrFlags(0x000E, 0x0040)
    OP_E5(0x0C, 0x00, 0x00)
    OP_E5(0x0D, 0x00, 0x00)
    OP_E5(0x0E, 0x00, 0x00)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 301)
    OP_70(0x0003, 0x00000168)
    SetChrSubChip(0x000B, 0)
    SetChrChipByIndex(0x000B, 6)
    OP_8C(0x0014, 45, 0)
    OP_CF(0x0014, 0x01, 'Frame127_FireEmitter')
    OP_A1(0x0012, 0x0001)
    SetChrPos(0x0012, 24820, -2550, 8060, 285)
    SetChrFlags(0x0012, 0x0001)
    ClearChrFlags(0x0012, 0x0080)

    ExecExpressionWithValue(
        0x0012,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x34,
        (
            (Expr.PushLong, 0x249F0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    LoadEffect(0x00, 'map\\mp032_00.eff')
    LoadEffect(0x01, 'map\\mp007_00.eff')
    LoadEffect(0x02, 'monster\\ms30703.eff')
    LoadEffect(0x03, 'map\\mp013_02.eff')
    LoadEffect(0x04, 'map\\mp013_00.eff')
    LoadEffect(0x05, 'map\\mp013_01.eff')
    LoadEffect(0x06, 'map\\mpsibuk.eff')
    PlayEffect(0x03, 0x05, 0x0013, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0075, 0x01, 0x50)
    FadeIn(1000, 0)
    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000B, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000B, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000B, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000B, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000B, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000B, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000B, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    SetChrSubChip(0x000B, 0)
    SetChrChipByIndex(0x000B, 5)
    Sleep(1000)

    OP_DC()

    ChrTalk(
        0x000B,
        (
            '#0280310566V#151F哇～好大啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280310567V#150F不过这条龙这么英俊，\n',
            '睡着的话实在是太可惜了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280310568V不知道会不会早点醒过来呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0270310569V#145F不是说过了吗～一旦它醒过来\n',
            '会有大麻烦的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310570V#140F不过……\n',
            '真是让人吃惊的生物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x006D, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_16E1')
    def lambda_16E1():
        OP_6D(430, 2550, 8189, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_16E1)

    @scena.Lambda('lambda_16F9')
    def lambda_16F9():
        OP_67(0, 6790, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_16F9)

    @scena.Lambda('lambda_1711')
    def lambda_1711():
        OP_6B(2830, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_1711)

    @scena.Lambda('lambda_1721')
    def lambda_1721():
        OP_6C(108000, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_1721)

    @scena.Lambda('lambda_1731')
    def lambda_1731():
        OP_6E(364, 3000)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_1731)

    @scena.Lambda('lambda_1741')
    def lambda_1741():
        OP_8C(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1741)

    Sleep(100)

    @scena.Lambda('lambda_1754')
    def lambda_1754():
        OP_8C(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1754)

    Sleep(100)

    @scena.Lambda('lambda_1767')
    def lambda_1767():
        OP_8C(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1767)

    Sleep(100)

    @scena.Lambda('lambda_177A')
    def lambda_177A():
        OP_8C(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_177A)

    CreateThread(0x0101, 0x01, 0x00, 0x0008)
    Sleep(300)

    CreateThread(0x0105, 0x01, 0x00, 0x0009)
    Sleep(300)

    CreateThread(0x0103, 0x01, 0x00, 0x000A)
    Sleep(300)

    CreateThread(0x0104, 0x01, 0x00, 0x000B)
    Sleep(300)

    CreateThread(0x0108, 0x01, 0x00, 0x000C)
    WaitForThreadExit(0x0108, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010310571V#1018F#4P哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0103, 0x0001)

    ChrTalk(
        0x0103,
        (
            '#0030310572V#023F这……实在很壮观呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0280310573V#151F啊，小艾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0270310574V#141F呵呵，你们也来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600310575V#161F#6P殿下……\n',
            '这儿太危险了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310576V请您快返回舰内吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0105, 315, 400)
    Sleep(300)

    ChrTalk(
        0x0105,
        (
            '#0060310577V#045F#2P呵呵，没事的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310578V#040F话说回来，近看真的是\n',
            '非常巨大的生物呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 315, 400)

    ChrTalk(
        0x0101,
        (
            '#0010310579V#1015F#2P它真的睡着了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100310580V#176F#6P已确认过还有心跳，\n',
            '应该没有死。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310581V#170F也难怪，打了那么大剂量的麻醉剂\n',
            '足够使一千只普通魔兽\n',
            '睡着的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310582V所以没那么容易醒的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310583V#1006F#2P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010310584V#1004F#2P咦，对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310585V那个叫莱维的男人\n',
            '到哪儿去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1A9A')
    def lambda_1A9A():
        OP_8C(0x00FE, 315, 300)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1A9A)

    Sleep(50)

    @scena.Lambda('lambda_1AAD')
    def lambda_1AAD():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1AAD)

    Sleep(50)

    OP_8C(0x0104, 315, 400)
    Sleep(200)

    ChrTalk(
        0x0108,
        (
            '#0080310586V#072F#4P嗯，似乎感觉不到\n',
            '他潜伏在附近的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040310587V#032F#4P『试验』中最为重要的『福音』\n',
            '应该在那个莱维的手上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310588V既然他本人不在这里的话……\n',
            '就是说已经放弃『试验』了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100310589V#170F#6P根据正在追击龙的巡逻艇发来的报告，\n',
            '并没有发现人影。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310590V有可能他一开始\n',
            '就没骑在上面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600310591V#163F#6P呵呵，也难怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310592V#160F大概是得知了我们的作战计划，\n',
            '所以心生恐惧而逃跑了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310593V#1015F#2P唔～我倒不觉得\n',
            '他会是个那么识趣的男人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030310594V#026F#2P是啊……\n',
            '还是不要疏忽大意为好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310595V#020F对了，那龙接下来\n',
            '会被运送到哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600310596V#160F#6P总之先以这个状态\n',
            '拖航到雷斯顿要塞去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310597V接下来的事就等我和陛下与\n',
            '卡西乌斯商议之后再做决定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030310598V#027F#2P原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x000B, 45, 400)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0280310599V#153F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0103, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0104, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(100)

    OP_62(0x0108, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(700)

    @scena.Lambda('lambda_1ECF')
    def lambda_1ECF():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1ECF)

    Sleep(50)

    @scena.Lambda('lambda_1EE2')
    def lambda_1EE2():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1EE2)

    Sleep(50)

    @scena.Lambda('lambda_1EF5')
    def lambda_1EF5():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1EF5)

    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0270310600V#143F#6P怎么了？朵洛希？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310601V#1004F#2P又发现什么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0280310602V#154F#6P唔……\n',
            '有可能是错觉～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280310603V你们不觉得它额头的凸起部分\n',
            '很奇怪吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310604V#1020F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1FE0')
    def lambda_1FE0():
        OP_6D(10820, -2990, 12220, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1FE0)

    @scena.Lambda('lambda_1FF8')
    def lambda_1FF8():
        OP_67(0, 5770, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1FF8)

    @scena.Lambda('lambda_2010')
    def lambda_2010():
        OP_6B(3240, 5000)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_2010)

    @scena.Lambda('lambda_2020')
    def lambda_2020():
        OP_6C(116000, 5000)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_2020)

    @scena.Lambda('lambda_2030')
    def lambda_2030():
        OP_6E(258, 5000)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_2030)

    @scena.Lambda('lambda_2040')
    def lambda_2040():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2040)

    @scena.Lambda('lambda_204E')
    def lambda_204E():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_204E)

    Sleep(80)

    @scena.Lambda('lambda_2061')
    def lambda_2061():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2061)

    @scena.Lambda('lambda_206F')
    def lambda_206F():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_206F)

    Sleep(80)

    @scena.Lambda('lambda_2082')
    def lambda_2082():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2082)

    @scena.Lambda('lambda_2090')
    def lambda_2090():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2090)

    Sleep(80)

    @scena.Lambda('lambda_20A3')
    def lambda_20A3():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_20A3)

    Sleep(80)

    @scena.Lambda('lambda_20B6')
    def lambda_20B6():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_20B6)

    WaitForThreadExit(0x0105, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010310605V#1004F#5P真的呢……\n',
            '整块圆圆地凸起来了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310606V#1016F上面好像有个裂口，\n',
            '莫非是眼睛──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_72(0x0001, 0x0020)
    OP_6F(0x0001, 370)
    OP_70(0x0001, 0x00000190)
    OP_22(0x0211, 0x00, 0x64)
    OP_73(0x0001)
    Fade(500)
    OP_6D(-530, 2550, 7580, 0)
    OP_67(0, 7130, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(96000, 0)
    OP_6E(316, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010310607V#1020F#4P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060310608V#042F#6P难道……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080310609V#077F#4P原来这才是元凶！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    OP_22(0x0090, 0x00, 0x64)
    PlayEffect(0x01, 0x01, 0x0014, -700, 1000, -300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010310610V#1002F#4P可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600310611V#162F#4P唔……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    OP_DB()
    OP_1D(0x2D)
    Sleep(200)

    Fade(500)
    OP_6D(-20890, 24910, 27240, 0)
    OP_67(0, 6480, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(117000, 0)
    OP_6E(393, 0)
    OP_82(0x01, 0x02)
    OP_0D()
    OP_6F(0x0001, 410)
    OP_70(0x0001, 0x000001AE)
    Sleep(800)

    OP_22(0x0195, 0x00, 0x64)
    OP_7C(0x0000012C, 0x0000012C, 0x00001388, 0x000001F4)
    OP_73(0x0001)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 430)
    OP_70(0x0001, 0x000001C2)
    CreateThread(0x0013, 0x03, 0x00, 0x000D)
    OP_22(0x0128, 0x00, 0x64)
    CreateThread(0x0012, 0x00, 0x00, 0x0006)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    OP_E8(0x88, 0x13, 0x00, 0x00)
    PlayEffect(0x06, 0xFF, 0x00FF, 15370, -2990, 13060, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 13970, -2990, 15960, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 18150, -2990, 13900, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 18080, -2990, 15980, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 17330, -2990, 17950, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 17340, -2990, 19770, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 17580, -2990, 21340, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 19480, -2990, 22570, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 21630, -2990, 24490, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 23880, -2990, 26250, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 26120, -2990, 28050, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 28120, -2990, 27060, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 27960, -2990, 23990, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 24680, -2990, 11900, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 39640, -2990, 1370, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 39400, -2990, 4550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 36700, -2990, 5030, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 21270, -2990, -2410, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 20050, -2990, -5190, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 18770, -2990, -8060, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 15030, -2990, -9420, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 12190, -2990, -9520, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 10510, -2990, -7130, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 9840, -2990, -4250, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 10850, -2990, -940, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 12660, -2990, 1300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 13230, -2990, 4340, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 15410, -2990, 5750, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 17030, -2990, 6320, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 15860, -2990, 7910, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 14220, -2990, 8830, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 11220, -2990, 7340, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 11280, -2990, 10620, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x06, 0xFF, 0x00FF, 11240, -2990, 13590, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(3000)

    OP_72(0x0001, 0x0020)
    OP_73(0x0001)
    OP_6F(0x0001, 450)
    OP_70(0x0001, 0x000001F4)
    OP_56(0x00)

    @scena.Lambda('lambda_2A7B')
    def lambda_2A7B():
        OP_91(0x00FE, 0, 3000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2A7B)

    @scena.Lambda('lambda_2A96')
    def lambda_2A96():
        OP_6D(-4430, 27000, 22590, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A96)

    @scena.Lambda('lambda_2AAE')
    def lambda_2AAE():
        OP_67(0, 5870, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2AAE)

    @scena.Lambda('lambda_2AC6')
    def lambda_2AC6():
        OP_6E(470, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2AC6)

    Sleep(2200)

    Fade(500)
    LoadEffect(0x06, 'map\\mp007_00.eff')
    OP_73(0x0001)
    OP_71(0x0001, 0x0020)
    OP_D8(0x01, 0x01F4)
    OP_B0(0x0001, 0x0A)
    OP_6F(0x0001, 650)
    OP_70(0x0001, 0x0000029E)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    OP_22(0x0195, 0x00, 0x64)
    OP_7C(0x000001F4, 0x000001F4, 0x00001388, 0x000001F4)
    OP_7C(0x0000012C, 0x0000012C, 0x00001388, 0x000001F4)
    PlayEffect(0x02, 0xFF, 0x0014, 1000, 1000, 0, 90, -90, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0121, 0x00, 0x64)

    @scena.Lambda('lambda_2B85')
    def lambda_2B85():
        OP_6D(-90, 22490, 20940, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2B85)

    @scena.Lambda('lambda_2B9D')
    def lambda_2B9D():
        OP_67(0, 4820, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2B9D)

    @scena.Lambda('lambda_2BB5')
    def lambda_2BB5():
        OP_6C(128000, 1500)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2BB5)

    @scena.Lambda('lambda_2BC5')
    def lambda_2BC5():
        OP_6B(1820, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2BC5)

    Sleep(1000)

    FadeOut(1000, 0, -1)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00000010)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_DC()
    OP_A2(0x10F6)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x2C00
@scena.Code('func_06_2C00')
def func_06_2C00():
    Sleep(700)

    OP_22(0x0120, 0x00, 0x64)
    Sleep(1300)

    OP_22(0x0120, 0x00, 0x64)
    Sleep(1300)

    OP_22(0x0120, 0x00, 0x64)
    Sleep(2100)

    OP_22(0x0120, 0x00, 0x64)
    Sleep(1300)

    OP_22(0x0120, 0x00, 0x64)
    Sleep(1300)

    OP_22(0x0120, 0x00, 0x64)

    Return()

# id: 0x0007 offset: 0x2C3D
@scena.Code('func_07_2C3D')
def func_07_2C3D():
    OP_22(0x01F6, 0x00, 0x64)
    Sleep(100)

    OP_22(0x01F6, 0x00, 0x64)
    Sleep(100)

    OP_22(0x01F6, 0x00, 0x64)

    Return()

# id: 0x0008 offset: 0x2C57
@scena.Code('func_08_2C57')
def func_08_2C57():
    SetChrPos(0x00FE, -4170, 2550, 1210, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, -4410, 2550, 2910, 3000, 0x00)
    OP_8E(0x00FE, -2160, 2550, 6020, 3000, 0x00)
    OP_8C(0x00FE, 45, 400)

    Return()

# id: 0x0009 offset: 0x2C9D
@scena.Code('func_09_2C9D')
def func_09_2C9D():
    SetChrPos(0x00FE, -4170, 2550, 1210, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, -4410, 2550, 2910, 3000, 0x00)
    OP_8E(0x00FE, -3750, 2550, 6210, 3000, 0x00)
    OP_8E(0x00FE, -2480, 2550, 6810, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0014, 400)
    OP_8C(0x00FE, 45, 400)

    Return()

# id: 0x000A offset: 0x2CFE
@scena.Code('func_0A_2CFE')
def func_0A_2CFE():
    SetChrPos(0x00FE, -4170, 2550, 1210, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, -4410, 2550, 2910, 3000, 0x00)
    OP_8E(0x00FE, -2320, 2550, 5030, 3000, 0x00)
    OP_8C(0x00FE, 45, 400)

    Return()

# id: 0x000B offset: 0x2D44
@scena.Code('func_0B_2D44')
def func_0B_2D44():
    SetChrPos(0x00FE, -4170, 2550, 1210, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, -4410, 2550, 2910, 3000, 0x00)
    OP_8E(0x00FE, -3920, 2550, 6280, 3000, 0x00)
    OP_8C(0x00FE, 45, 400)

    Return()

# id: 0x000C offset: 0x2D8A
@scena.Code('func_0C_2D8A')
def func_0C_2D8A():
    SetChrPos(0x00FE, -4170, 2550, 1210, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, -4410, 2550, 2910, 3000, 0x00)
    OP_8E(0x00FE, -3830, 2550, 5100, 3000, 0x00)
    OP_8C(0x00FE, 45, 400)

    Return()

# id: 0x000D offset: 0x2DD0
@scena.Code('func_0D_2DD0')
def func_0D_2DD0():
    OP_82(0x05, 0x02)
    PlayEffect(0x04, 0x06, 0x0013, 0, -100, 2200, 0, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x05, 0x07, 0x0013, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_2E43')
    def lambda_2E43():
        OP_8F(0x00FE, 4680, -2990, 27620, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_2E43)

    @scena.Lambda('lambda_2E5E')
    def lambda_2E5E():
        OP_8C(0x00FE, 0, 100)

        ExitThread()

    DispatchAsync(0x0013, 0x0000, lambda_2E5E)

    Sleep(200)

    SetChrChipByIndex(0x000D, 11)
    SetChrSubChip(0x000D, 0)
    Sleep(100)

    SetChrChipByIndex(0x000E, 11)
    SetChrSubChip(0x000E, 0)
    WaitForThreadExit(0x0013, 0x0002)
    OP_8C(0x000D, 180, 400)
    OP_8C(0x000E, 180, 400)
    OP_82(0x06, 0x00)
    OP_82(0x07, 0x00)
    PlayEffect(0x03, 0x05, 0x0013, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x000E offset: 0x2ED3
@scena.Code('func_0E_2ED3')
def func_0E_2ED3():
    EventBegin(0x00)
    OP_6D(-2009, 4490, 8140, 0)
    OP_67(0, 6010, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(227000, 0)
    OP_6E(268, 0)
    SetChrPos(0x0101, -2160, 2550, 6020, 45)
    SetChrPos(0x0103, -2320, 2550, 5030, 45)
    SetChrPos(0x0105, -2480, 2550, 6810, 45)
    SetChrPos(0x0104, -3920, 2550, 6280, 45)
    SetChrPos(0x0108, -3830, 2550, 5100, 45)
    SetChrPos(0x0009, -2450, 2550, 7820, 45)
    SetChrPos(0x0008, -3730, 2550, 7850, 45)
    SetChrPos(0x000A, -4620, 3050, 9670, 45)
    SetChrPos(0x000B, -3020, 3050, 9520, 45)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0004)

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_22(0x0075, 0x01, 0x50)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010310612V#1020F#5P啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600310613V#162F#5P混帐……不能让它逃走！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310614V『埃尔赛尤』紧急起飞！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0100310615V#177F#2P是！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x1A24)
    SetMapFlags(0x02000000)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/E0800._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x317E
@scena.Code('func_0F_317E')
def func_0F_317E():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    SetChrBattleFlags(0x0017, 0x0020)
    SetChrBattleFlags(0x0018, 0x0020)
    SetChrBattleFlags(0x0016, 0x0020)
    OP_89(0x0017, -5390, 1550, -16510, 135)
    OP_89(0x0018, -2410, 1550, -15670, 135)
    OP_89(0x0016, -5090, 1550, -12910, 315)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0008, -5260, 2550, 6560, 68)
    SetChrPos(0x0015, -3970, 2550, 6620, 273)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    OP_6D(-5540, 2140, -8240, 0)
    OP_67(0, 7350, -10000, 0)
    OP_6B(5670, 0)
    OP_6C(37000, 0)
    OP_6E(395, 0)
    CreateThread(0x0018, 0x01, 0x00, 0x0010)
    CreateThread(0x0016, 0x01, 0x00, 0x0011)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x0015, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x00)
    OP_C8(0x0200, 0x0046, 'C_PLAC16._CH', 0x01, 0x03E8)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_32C3')
    def lambda_32C3():
        OP_6D(-4280, 2550, 6090, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_32C3)

    @scena.Lambda('lambda_32DB')
    def lambda_32DB():
        OP_67(0, 6070, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_32DB)

    @scena.Lambda('lambda_32F3')
    def lambda_32F3():
        OP_6B(5290, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_32F3)

    @scena.Lambda('lambda_3303')
    def lambda_3303():
        OP_6C(126000, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3303)

    @scena.Lambda('lambda_3313')
    def lambda_3313():
        OP_6E(331, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_3313)

    Sleep(1000)

    Sleep(1000)

    Sleep(1000)

    Sleep(1000)

    Sleep(1000)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F5)
    NewScene('ED6_DT21/T1121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x3354
@scena.Code('func_10_3354')
def func_10_3354():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_33D2',
    )

    OP_8E(0x00FE, -2090, 1550, -13310, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)
    Sleep(700)

    OP_8E(0x00FE, -2370, 1550, -11060, 2000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_8C(0x00FE, 45, 400)
    Sleep(700)

    OP_8E(0x00FE, -2410, 1550, -15670, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)
    Sleep(700)

    Jump('func_10_3354')

    def _loc_33D2(): pass

    label('loc_33D2')

    Return()

# id: 0x0011 offset: 0x33D3
@scena.Code('func_11_33D3')
def func_11_33D3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_346A',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_8E(0x00FE, -7140, 1550, -11210, 2000, 0x00)
    OP_8C(0x00FE, 315, 400)
    Sleep(600)

    OP_8E(0x00FE, -5090, 1550, -12910, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)
    Sleep(800)

    OP_8E(0x00FE, -3410, 1550, -11200, 2000, 0x00)
    Sleep(800)

    OP_8E(0x00FE, -5090, 1550, -12910, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)
    Sleep(800)

    Jump('func_11_33D3')

    def _loc_346A(): pass

    label('loc_346A')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
