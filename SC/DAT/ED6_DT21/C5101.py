import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5101   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '暴动钢臂（黑）'),
    TXT(0x02, '目标探索者'),
    TXT(0x03, '目标探索者'),
    TXT(0x04, '中枢塔前道路'),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5101.x'
    header.mapIndex       = 1
    header.bgm            = 62
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x100E
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
        ('ED6_DT29/CH12520._CH', 'ED6_DT29/CH12520P._CP'),
        ('ED6_DT29/CH12521._CH', 'ED6_DT29/CH12521P._CP'),
        ('ED6_DT29/CH12522._CH', 'ED6_DT29/CH12522P._CP'),
        ('ED6_DT29/CH13080._CH', 'ED6_DT29/CH13080P._CP'),
        ('ED6_DT29/CH13081._CH', 'ED6_DT29/CH13081P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 4000,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 4000,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 4000,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 80,
            z                   = 4000,
            y                   = 65129,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x162
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x162
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -6540,
            y           = 4000,
            z           = 101490,
            range       = 6540,
            dword_10    = 0x00001770,
            dword_14    = 0x00019456,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = -6540,
            y           = 4000,
            z           = 101490,
            range       = 6540,
            dword_10    = 0x00001770,
            dword_14    = 0x00019456,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10005 offset: 0x1A2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1A2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045F, 4, 0x22FC)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x045F, 3, 0x22FB)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_20F',
    )

    SetChrPos(0x0008, 0, 8800, 112340, 180)
    SetChrPos(0x0009, -3880, 8000, 111800, 180)
    SetChrPos(0x000A, 3880, 8000, 111800, 180)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 0)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)

    def _loc_20F(): pass

    label('loc_20F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_220',
    )

    OP_A3(0x10F0)
    Event(0, 0x0004)

    Jump('loc_22E')

    def _loc_220(): pass

    label('loc_220')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_22E',
    )

    OP_A3(0x10F1)
    Event(0, 0x0005)

    def _loc_22E(): pass

    label('loc_22E')

    Return()

# id: 0x0001 offset: 0x22F
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE0C00, 0xFFFF8AD0, 0x00230072)
    Call(0, 0x0003)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 6, 0x223E)),
            Expr.Return,
        ),
        'loc_25D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x42),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x0085, 0x01, 0x5A)

    Jump('loc_262')

    def _loc_25D(): pass

    label('loc_25D')

    OP_22(0x01C7, 0x01, 0x5A)

    def _loc_262(): pass

    label('loc_262')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045F, 3, 0x22FB)),
            Expr.Return,
        ),
        'loc_271',
    )

    OP_B2(0x00, 0x00, 0x0080)

    Jump('loc_276')

    def _loc_271(): pass

    label('loc_271')

    OP_B2(0x00, 0x01, 0x0080)

    def _loc_276(): pass

    label('loc_276')

    Return()

# id: 0x0002 offset: 0x277
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_28C',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_28C(): pass

    label('loc_28C')

    Return()

# id: 0x0003 offset: 0x28D
@scena.Code('func_03_28D')
def func_03_28D():
    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2BE'),
        (0x00000003, 'loc_2CB'),
        (0x00000004, 'loc_2D8'),
        (0x00000005, 'loc_2E5'),
        (0x00000006, 'loc_2F2'),
        (0x00000007, 'loc_2FF'),
        (0x00000008, 'loc_30C'),
        (0x0000000A, 'loc_319'),
        (0x0000000E, 'loc_326'),
        (0x0000000F, 'loc_333'),
        (-1, 'loc_340'),
    )

    def _loc_2BE(): pass

    label('loc_2BE')

    OP_D2(0x000701D0, 0x000701DC, 0x07)

    Jump('loc_340')

    def _loc_2CB(): pass

    label('loc_2CB')

    OP_D2(0x000701E8, 0x000701F4, 0x07)

    Jump('loc_340')

    def _loc_2D8(): pass

    label('loc_2D8')

    OP_D2(0x0027036E, 0x0027037B, 0x07)

    Jump('loc_340')

    def _loc_2E5(): pass

    label('loc_2E5')

    OP_D2(0x00070218, 0x00070224, 0x07)

    Jump('loc_340')

    def _loc_2F2(): pass

    label('loc_2F2')

    OP_D2(0x00070230, 0x0007023C, 0x07)

    Jump('loc_340')

    def _loc_2FF(): pass

    label('loc_2FF')

    OP_D2(0x00070248, 0x00070254, 0x07)

    Jump('loc_340')

    def _loc_30C(): pass

    label('loc_30C')

    OP_D2(0x00270176, 0x00270183, 0x07)

    Jump('loc_340')

    def _loc_319(): pass

    label('loc_319')

    OP_D2(0x000702B4, 0x000702BB, 0x07)

    Jump('loc_340')

    def _loc_326(): pass

    label('loc_326')

    OP_D2(0x002702D6, 0x002702E0, 0x07)

    Jump('loc_340')

    def _loc_333(): pass

    label('loc_333')

    OP_D2(0x002702C2, 0x002702CC, 0x07)

    Jump('loc_340')

    def _loc_340(): pass

    label('loc_340')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_371'),
        (0x00000003, 'loc_37E'),
        (0x00000004, 'loc_38B'),
        (0x00000005, 'loc_398'),
        (0x00000006, 'loc_3A5'),
        (0x00000007, 'loc_3B2'),
        (0x00000008, 'loc_3BF'),
        (0x0000000A, 'loc_3CC'),
        (0x0000000E, 'loc_3D9'),
        (0x0000000F, 'loc_3E6'),
        (-1, 'loc_3F3'),
    )

    def _loc_371(): pass

    label('loc_371')

    OP_D2(0x000701D0, 0x000701DC, 0x08)

    Jump('loc_3F3')

    def _loc_37E(): pass

    label('loc_37E')

    OP_D2(0x000701E8, 0x000701F4, 0x08)

    Jump('loc_3F3')

    def _loc_38B(): pass

    label('loc_38B')

    OP_D2(0x0027036E, 0x0027037B, 0x08)

    Jump('loc_3F3')

    def _loc_398(): pass

    label('loc_398')

    OP_D2(0x00070218, 0x00070224, 0x08)

    Jump('loc_3F3')

    def _loc_3A5(): pass

    label('loc_3A5')

    OP_D2(0x00070230, 0x0007023C, 0x08)

    Jump('loc_3F3')

    def _loc_3B2(): pass

    label('loc_3B2')

    OP_D2(0x00070248, 0x00070254, 0x08)

    Jump('loc_3F3')

    def _loc_3BF(): pass

    label('loc_3BF')

    OP_D2(0x00270176, 0x00270183, 0x08)

    Jump('loc_3F3')

    def _loc_3CC(): pass

    label('loc_3CC')

    OP_D2(0x000702B4, 0x000702BB, 0x08)

    Jump('loc_3F3')

    def _loc_3D9(): pass

    label('loc_3D9')

    OP_D2(0x002702D6, 0x002702E0, 0x08)

    Jump('loc_3F3')

    def _loc_3E6(): pass

    label('loc_3E6')

    OP_D2(0x002702C2, 0x002702CC, 0x08)

    Jump('loc_3F3')

    def _loc_3F3(): pass

    label('loc_3F3')

    Return()

# id: 0x0004 offset: 0x3F4
@scena.Code('func_04_3F4')
def func_04_3F4():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(-200, 12000, 148580, 0)
    OP_67(0, -840, -10000, 0)
    OP_6B(5800, 0)
    OP_6C(359000, 0)
    OP_6E(1276, 0)
    FadeIn(500, 0)
    OP_0D()
    Sleep(2000)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('女孩的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0090350001V不、不可能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene('ED6_DT21/E0110._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x4AE
@scena.Code('func_05_4AE')
def func_05_4AE():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(-200, 12000, 148580, 0)
    OP_67(0, -840, -10000, 0)
    OP_6B(5800, 0)
    OP_6C(359000, 0)
    OP_6E(1276, 0)
    OP_C5(0x00, 0x0000, 0x0000, 0x0280, 0x0400, 0x0000, 0xFDE4, 0x0400, 0x0400, 0x0000, 0x0000, 0x0280, 0x0400, 0x00FFFFFF, 0x00, 'C_VIS189._CH')
    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x00, 0x03, -1, 2000, 0)
    OP_C6(0x00, 0x07, 0, 0, 7000)
    OP_C7(0x00, 0x00, 0x00)
    Sleep(1000)

    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    Sleep(2000)

    OP_A2(0x10F1)
    NewScene('ED6_DT21/C5100._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x58E
@scena.Code('func_06_58E')
def func_06_58E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045F, 4, 0x22FC)),
            Expr.Return,
        ),
        'loc_596',
    )

    Return()

    def _loc_596(): pass

    label('loc_596')

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5BB',
    )

    Call(0, 0x000C)
    Call(0, 0x000D)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_5BB(): pass

    label('loc_5BB')

    SetChrPos(0x0008, 0, 12800, 172800, 180)
    SetChrPos(0x0009, -3880, 18000, 111800, 180)
    SetChrPos(0x000A, 3880, 21000, 111800, 180)
    ClearChrFlags(0x0008, 0x0080)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
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
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(1140, 4170, 102820, 0)
    OP_67(0, 9410, -10000, 0)
    OP_6B(4240, 0)
    OP_6C(43000, 0)

    @scena.Lambda('lambda_0665')
    def lambda_0665():
        OP_6D(1140, 4170, 102820, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0665)

    @scena.Lambda('lambda_067D')
    def lambda_067D():
        OP_6C(43000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_067D)

    @scena.Lambda('lambda_068D')
    def lambda_068D():
        OP_67(0, 9410, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_068D)

    @scena.Lambda('lambda_06A5')
    def lambda_06A5():
        OP_6B(4240, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_06A5)

    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_06BA')
    def lambda_06BA():
        OP_6D(-1050, 12000, 161650, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_06BA)

    @scena.Lambda('lambda_06D2')
    def lambda_06D2():
        OP_6C(334000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_06D2)

    @scena.Lambda('lambda_06E2')
    def lambda_06E2():
        OP_67(0, 5260, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_06E2)

    @scena.Lambda('lambda_06FA')
    def lambda_06FA():
        OP_6B(6800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_06FA)

    WaitForThreadExit(0x0101, 0x0003)

    @scena.Lambda('lambda_070F')
    def lambda_070F():
        OP_6B(3930, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_070F)

    WaitForThreadExit(0x0101, 0x0000)
    SetChrPos(0x0101, -1830, 4000, 102580, 0)
    SetChrPos(0x0102, -490, 4000, 102010, 0)
    SetChrPos(0x00F8, -2820, 4000, 101160, 0)
    SetChrPos(0x00F9, -1540, 4000, 100700, 0)
    SetChrChipByIndex(0x0101, 5)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0102, 6)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x00F8, 7)
    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F9, 8)
    SetChrSubChip(0x00F9, 0)
    ClearMapFlags(0x00000010)
    OP_22(0x0193, 0x00, 0x64)
    Sleep(1200)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_07A8')
    def lambda_07A8():
        OP_6D(-930, 8000, 114170, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_07A8)

    @scena.Lambda('lambda_07C0')
    def lambda_07C0():
        OP_6C(330000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07C0)

    @scena.Lambda('lambda_07D0')
    def lambda_07D0():
        OP_6B(2650, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_07D0)

    CreateThread(0x0008, 0x00, 0x00, 0x0008)
    CreateThread(0x0008, 0x03, 0x00, 0x0009)
    WaitForThreadExit(0x0008, 0x0000)
    OP_7C(0x00000000, 0x000001F4, 0x00001388, 0x000001F4)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 0)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_0828')
    def lambda_0828():
        OP_8F(0x00FE, -3880, 8000, 111800, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0828)

    @scena.Lambda('lambda_0843')
    def lambda_0843():
        OP_8F(0x00FE, 3880, 8000, 111800, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0843)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)
    Sleep(1000)

    Fade(500)
    OP_6D(-330, 6800, 107210, 0)
    OP_67(0, 7780, -10000, 0)
    OP_6B(4550, 0)
    OP_6C(328000, 0)
    OP_6E(262, 0)
    OP_0D()
    TerminateThread(0x0008, 0x00)
    SetChrChipByIndex(0x0008, 2)
    SetChrSubChip(0x0008, 0)

    @scena.Lambda('lambda_08C3')
    def lambda_08C3():
        OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_08C3)

    WaitForThreadExit(0x0008, 0x0002)
    OP_22(0x0193, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_08E2')
    def lambda_08E2():
        OP_6D(-1890, 5200, 105220, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_08E2)

    @scena.Lambda('lambda_08FA')
    def lambda_08FA():
        OP_6B(3530, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_08FA)

    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_090F')
    def lambda_090F():
        OP_96(0x00FE, 0xFFFFFBF0, 0x000012C0, 0x00018DEE, 0x000005DC, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_090F)

    @scena.Lambda('lambda_092D')
    def lambda_092D():
        OP_99(0x00FE, 0x04, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_092D)

    ClearChrFlags(0x0009, 0x0004)
    ClearChrFlags(0x000A, 0x0004)

    @scena.Lambda('lambda_0947')
    def lambda_0947():
        OP_8F(0x00FE, -3040, 4800, 101870, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0947)

    @scena.Lambda('lambda_0962')
    def lambda_0962():
        OP_8F(0x00FE, 1040, 4800, 101870, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0962)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x00000525, 0x00000000, 0x00, 0x0000, 0xFF)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00000010)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_9C7'),
        (0x00000000, 'loc_9CC'),
        (0x00000002, 'loc_9D3'),
        (-1, 'loc_9DA'),
    )

    def _loc_9C7(): pass

    label('loc_9C7')

    OP_B4(0x00)

    Jump('loc_9DA')

    def _loc_9CC(): pass

    label('loc_9CC')

    Call(0, 0x000A)

    Jump('loc_9DA')

    def _loc_9D3(): pass

    label('loc_9D3')

    Call(0, 0x000B)

    Jump('loc_9DA')

    def _loc_9DA(): pass

    label('loc_9DA')

    Return()

# id: 0x0007 offset: 0x9DB
@scena.Code('func_07_9DB')
def func_07_9DB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045F, 4, 0x22FC)),
            Expr.Return,
        ),
        'loc_9E3',
    )

    Return()

    def _loc_9E3(): pass

    label('loc_9E3')

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A08',
    )

    Call(0, 0x000C)
    Call(0, 0x000D)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_A08(): pass

    label('loc_A08')

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
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
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    OP_6D(-330, 6800, 107210, 0)
    OP_67(0, 7780, -10000, 0)
    OP_6B(4550, 0)
    OP_6C(328000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -1830, 4000, 102580, 0)
    SetChrPos(0x0102, -490, 4000, 102010, 0)
    SetChrPos(0x00F8, -2820, 4000, 101160, 0)
    SetChrPos(0x00F9, -1540, 4000, 100700, 0)
    SetChrChipByIndex(0x0101, 5)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0102, 6)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x00F8, 7)
    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F9, 8)
    SetChrSubChip(0x00F9, 0)
    OP_0D()
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000A, 0x00)
    SetChrChipByIndex(0x0008, 2)
    SetChrSubChip(0x0008, 0)

    @scena.Lambda('lambda_0B14')
    def lambda_0B14():
        OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0B14)

    WaitForThreadExit(0x0008, 0x0002)
    OP_22(0x0193, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0B33')
    def lambda_0B33():
        OP_6D(-1890, 5200, 105220, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0B33)

    @scena.Lambda('lambda_0B4B')
    def lambda_0B4B():
        OP_6B(3530, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B4B)

    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_0B60')
    def lambda_0B60():
        OP_96(0x00FE, 0xFFFFFBF0, 0x000012C0, 0x00018DEE, 0x000005DC, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B60)

    @scena.Lambda('lambda_0B7E')
    def lambda_0B7E():
        OP_99(0x00FE, 0x04, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0B7E)

    ClearChrFlags(0x0009, 0x0004)
    ClearChrFlags(0x000A, 0x0004)

    @scena.Lambda('lambda_0B98')
    def lambda_0B98():
        OP_8F(0x00FE, -3040, 4800, 101870, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B98)

    @scena.Lambda('lambda_0BB3')
    def lambda_0BB3():
        OP_8F(0x00FE, 1040, 4800, 101870, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BB3)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x00000525, 0x00000000, 0x00, 0x0000, 0xFF)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00000010)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_C18'),
        (0x00000000, 'loc_C1D'),
        (0x00000002, 'loc_C24'),
        (-1, 'loc_C2B'),
    )

    def _loc_C18(): pass

    label('loc_C18')

    OP_B4(0x00)

    Jump('loc_C2B')

    def _loc_C1D(): pass

    label('loc_C1D')

    Call(0, 0x000A)

    Jump('loc_C2B')

    def _loc_C24(): pass

    label('loc_C24')

    Call(0, 0x000B)

    Jump('loc_C2B')

    def _loc_C2B(): pass

    label('loc_C2B')

    Return()

# id: 0x0008 offset: 0xC2C
@scena.Code('func_08_C2C')
def func_08_C2C():
    @scena.Lambda('lambda_0C32')
    def lambda_0C32():
        OP_8F(0x00FE, 0, 12800, 133020, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0C32)

    WaitForThreadExit(0x00FE, 0x0001)
    TerminateThread(0x00FE, 0x03)
    OP_23(0x013F)
    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_0C5E')
    def lambda_0C5E():
        OP_96(0x00FE, 0x00000000, 0x00002260, 0x0001B6D4, 0x00001F40, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0C5E)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_22(0x00C8, 0x00, 0x64)

    Return()

# id: 0x0009 offset: 0xC81
@scena.Code('func_09_C81')
def func_09_C81():
    Sleep(200)

    OP_22(0x013F, 0x00, 0x46)
    Sleep(500)

    OP_22(0x013F, 0x00, 0x50)
    Sleep(500)

    OP_22(0x013F, 0x00, 0x5A)
    Sleep(500)

    def _loc_CA4(): pass

    label('loc_CA4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CBA',
    )

    OP_22(0x013F, 0x00, 0x64)
    Sleep(500)

    Jump('loc_CA4')

    def _loc_CBA(): pass

    label('loc_CBA')

    Return()

# id: 0x000A offset: 0xCBB
@scena.Code('func_0A_CBB')
def func_0A_CBB():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000A, 0x00)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    OP_6D(-120, 4000, 100630, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -120, 4000, 100630, 0)
    SetChrPos(0x0001, -120, 4000, 100630, 0)
    SetChrPos(0x0002, -120, 4000, 100630, 0)
    SetChrPos(0x0003, -120, 4000, 100630, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x00F9, 0)
    OP_A2(0x22FC)
    OP_B2(0x00, 0x00, 0x0080)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0xDA4
@scena.Code('func_0B_DA4')
def func_0B_DA4():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetChrPos(0x0008, 0, 8800, 112340, 180)
    SetChrPos(0x0009, -3880, 8000, 111800, 180)
    SetChrPos(0x000A, 3880, 8000, 111800, 180)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 0)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    OP_6D(-120, 4000, 100630, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -120, 4000, 98630, 180)
    SetChrPos(0x0001, -120, 4000, 98630, 180)
    SetChrPos(0x0002, -120, 4000, 98630, 180)
    SetChrPos(0x0003, -120, 4000, 98630, 180)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x00F9, 0)
    OP_A2(0x22FB)
    OP_B2(0x00, 0x00, 0x0080)
    OP_B2(0x01, 0x01, 0x0080)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0xED8
@scena.Code('func_0C_ED8')
def func_0C_ED8():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
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
        (0x00000000, 'loc_F52'),
        (0x00000001, 'loc_F58'),
        (-1, 'loc_F5E'),
    )

    def _loc_F52(): pass

    label('loc_F52')

    OP_A2(0x1200)

    Jump('loc_F5E')

    def _loc_F58(): pass

    label('loc_F58')

    OP_A2(0x1201)

    Jump('loc_F5E')

    def _loc_F5E(): pass

    label('loc_F5E')

    Return()

# id: 0x000D offset: 0xF5F
@scena.Code('func_0D_F5F')
def func_0D_F5F():
    FadeOut(0, 0, -1)
    OP_6D(-27650, 0, -3680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
