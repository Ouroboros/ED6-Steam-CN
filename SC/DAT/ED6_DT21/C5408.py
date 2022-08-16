import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5408_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5408   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5408.x'
    header.mapIndex       = 1
    header.bgm            = 28
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '结社艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '结社艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '结社艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '结社艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '结社艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '基尔巴特',
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
            name                = '约修亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '约修亚残像',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '剑帝莱维',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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

# id: 0x10002 offset: 0x268
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x268
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -8100,
            y           = 0,
            z           = -65500,
            range       = 9750,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFEF854,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000010,
        ),
    )

# id: 0x10004 offset: 0x288
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x288
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_299',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_02_52B)

    Jump('loc_2FF')

    def _loc_299(): pass

    label('loc_299')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_2B3',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x72),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_04_75F)

    Jump('loc_2FF')

    def _loc_2B3(): pass

    label('loc_2B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_2CD',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    Event(0, func_2D_58BA)

    Jump('loc_2FF')

    def _loc_2CD(): pass

    label('loc_2CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_2E7',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    Event(0, func_2F_5B7F)

    Jump('loc_2FF')

    def _loc_2E7(): pass

    label('loc_2E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 6, 0x1C26)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FF',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FF',
    )

    Event(0, func_0F_11F9)

    def _loc_2FF(): pass

    label('loc_2FF')

    Return()

# id: 0x0001 offset: 0x300
@scena.Code('func_01_300')
def func_01_300():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31E',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_31E(): pass

    label('loc_31E')

    PlaySE(305, 0x01, 0x46)
    PlaySE(451, 0x01, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 7, 0x1C27)),
            Expr.Return,
        ),
        'loc_33C',
    )

    LoadChip('ED6_DT26/CH20501._CH', 'ED6_DT26/CH20501P._CP', 0)

    Jump('loc_4E2')

    def _loc_33C(): pass

    label('loc_33C')

    LoadChip('ED6_DT27/CH04610._CH', 'ED6_DT27/CH04610P._CP', 0)
    LoadChip('ED6_DT27/CH03750._CH', 'ED6_DT27/CH03750P._CP', 1)
    LoadChip('ED6_DT27/CH04750._CH', 'ED6_DT27/CH04750P._CP', 2)
    LoadChip('ED6_DT27/CH03610._CH', 'ED6_DT27/CH03610P._CP', 3)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 4)
    LoadChip('ED6_DT27/CH04002._CH', 'ED6_DT27/CH04002P._CP', 5)
    LoadChip('ED6_DT27/CH04002._CH', 'ED6_DT27/CH04002P._CP', 6)
    LoadChip('ED6_DT27/CH04610._CH', 'ED6_DT27/CH04610P._CP', 7)
    LoadChip('ED6_DT27/CH04611._CH', 'ED6_DT27/CH04611P._CP', 8)
    LoadChip('ED6_DT27/CH04751._CH', 'ED6_DT27/CH04751P._CP', 9)

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x42A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E2',
    )

    LoadChip('ED6_DT27/CH04610._CH', 'ED6_DT27/CH04610P._CP', 0)
    LoadChip('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP', 1)
    LoadChip('ED6_DT27/CH04750._CH', 'ED6_DT27/CH04750P._CP', 2)
    LoadChip('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP', 3)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 4)
    LoadChip('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP', 5)
    LoadChip('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04004P._CP', 6)
    LoadChip('ED6_DT27/CH04610._CH', 'ED6_DT27/CH04610P._CP', 7)
    LoadChip('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP', 8)
    LoadChip('ED6_DT27/CH04614._CH', 'ED6_DT27/CH04614P._CP', 9)
    LoadChip('ED6_DT26/CH20501._CH', 'ED6_DT26/CH20501P._CP', 10)
    LoadChip('ED6_DT27/CH04754._CH', 'ED6_DT27/CH04754P._CP', 11)
    LoadChip('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP', 12)
    LoadChip('ED6_DT27/CH03650._CH', 'ED6_DT27/CH03650P._CP', 13)
    LoadChip('ED6_DT26/CH20385._CH', 'ED6_DT26/CH20385P._CP', 14)
    LoadChip('ED6_DT26/CH20397._CH', 'ED6_DT26/CH20397P._CP', 15)
    LoadChip('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP', 16)
    LoadChip('ED6_DT27/CH04540._CH', 'ED6_DT27/CH04540P._CP', 17)
    LoadChip('ED6_DT26/CH20364._CH', 'ED6_DT26/CH20364P._CP', 18)
    LoadChip('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP', 19)
    LoadChip('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP', 20)
    LoadChip('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP', 21)
    LoadChip('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP', 22)
    LoadChip('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP', 23)
    LoadChip('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP', 24)
    LoadChip('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP', 25)
    LoadChip('ED6_DT27/CH04751._CH', 'ED6_DT27/CH04751P._CP', 26)
    LoadChip('ED6_DT27/CH04613._CH', 'ED6_DT27/CH04613P._CP', 27)
    LoadChip('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP', 28)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 29)
    LoadChip('ED6_DT26/CH20386._CH', 'ED6_DT26/CH20386P._CP', 30)

    def _loc_4E2(): pass

    label('loc_4E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 6, 0x1C26)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_500',
    )

    OP_72(0x0006, 0x0004)
    OP_72(0x0006, 0x0020)
    OP_72(0x0006, 0x0008)
    OP_6F(0x0006, 0)

    def _loc_500(): pass

    label('loc_500')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 7, 0x1C27)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_521',
    )

    OP_72(0x0007, 0x0004)
    OP_72(0x0007, 0x0020)
    OP_72(0x0007, 0x0008)
    OP_6F(0x0007, 0)

    Jump('loc_525')

    def _loc_521(): pass

    label('loc_521')

    Call(0, 0x0019)

    def _loc_525(): pass

    label('loc_525')

    OP_71(0x0008, 0x0004)

    Return()

# id: 0x0002 offset: 0x52B
@scena.Code('func_02_52B')
def func_02_52B():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    CameraMove(-31440, 0, -23410, 0)
    OP_67(0, 8400, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(62000, 0)
    OP_6E(445, 0)
    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_057F')
    def lambda_057F():
        CameraMove(-12320, 0, -61450, 15000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_057F)

    @scena.Lambda('lambda_0597')
    def lambda_0597():
        OP_67(0, 28780, -10000, 12000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0597)

    @scena.Lambda('lambda_05AF')
    def lambda_05AF():
        CameraSetDistance(5130, 12000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_05AF)

    @scena.Lambda('lambda_05BF')
    def lambda_05BF():
        OP_6C(61000, 12000)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_05BF)

    OP_6E(600, 12000)
    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C5400._SN', 111, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x5EF
@scena.Code('func_03_5EF')
def func_03_5EF():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    CameraMove(-10950, -35000, -43730, 0)
    OP_67(0, 13010, -10000, 0)
    CameraSetDistance(5540, 0)
    OP_6C(99000, 0)
    OP_6E(1092, 0)
    OP_A1(0x0008, 0x0000)
    OP_A1(0x0009, 0x0001)
    OP_A1(0x000A, 0x0002)
    OP_A1(0x000B, 0x0003)
    OP_A1(0x000C, 0x0004)
    ChrSetPos(0x0008, -10730, -30000, -40850, 0)
    ChrSetPos(0x0009, -10730, -30000, -80850, 0)
    ChrSetPos(0x000A, -10730, -30000, -45850, 0)
    ChrSetPos(0x000B, -7730, -30000, -75850, 0)
    ChrSetPos(0x000C, -7730, -30000, -50850, 0)
    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_06B1')
    def lambda_06B1():
        CameraMove(-12280, -35000, -43960, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_06B1)

    @scena.Lambda('lambda_06C9')
    def lambda_06C9():
        OP_67(0, 6270, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_06C9)

    @scena.Lambda('lambda_06E1')
    def lambda_06E1():
        CameraSetDistance(6200, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_06E1)

    @scena.Lambda('lambda_06F1')
    def lambda_06F1():
        OP_6C(79000, 14000)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_06F1)

    @scena.Lambda('lambda_0701')
    def lambda_0701():
        OP_6E(1092, 10000)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_0701)

    CreateThread(0x0008, 0x01, 0x00, func_05_8E4)
    Sleep(1500)

    CreateThread(0x0009, 0x01, 0x00, func_07_AB5)
    Sleep(2500)

    CreateThread(0x000A, 0x01, 0x00, func_09_C86)
    Sleep(1500)

    CreateThread(0x000B, 0x01, 0x00, func_0B_E57)
    Sleep(2500)

    CreateThread(0x000C, 0x01, 0x00, func_0D_1028)
    WaitForThreadExit(0x000C, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/C5400._SN', 111, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x75F
@scena.Code('func_04_75F')
def func_04_75F():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0000, 0x0004)
    ChrSetPos(0x0000, 0, -70000, -50000, 0)
    CameraMove(5150, -16850, -28970, 0)
    OP_67(0, 20020, -10000, 0)
    CameraSetDistance(3190, 0)
    OP_6C(49000, 0)
    OP_6E(964, 0)
    OP_A1(0x0008, 0x0000)
    OP_A1(0x0009, 0x0001)
    OP_A1(0x000A, 0x0002)
    OP_A1(0x000B, 0x0003)
    OP_A1(0x000C, 0x0004)
    ChrSetPos(0x0008, 0, -30000, -50000, 0)
    ChrSetPos(0x0009, 0, -30000, -50000, 0)
    ChrSetPos(0x000A, 0, -30000, -50000, 0)
    ChrSetPos(0x000B, 0, -30000, -50000, 0)
    ChrSetPos(0x000C, 0, -30000, -50000, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0836')
    def lambda_0836():
        CameraMove(-37950, -32049, -28670, 10000)

        ExitThread()

    DispatchAsync(0x0015, 0x0000, lambda_0836)

    @scena.Lambda('lambda_084E')
    def lambda_084E():
        OP_67(0, 7860, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_084E)

    @scena.Lambda('lambda_0866')
    def lambda_0866():
        CameraSetDistance(4000, 10000)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_0866)

    @scena.Lambda('lambda_0876')
    def lambda_0876():
        OP_6C(49000, 10000)

        ExitThread()

    DispatchAsync(0x0015, 0x0003, lambda_0876)

    @scena.Lambda('lambda_0886')
    def lambda_0886():
        OP_6E(964, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0886)

    CreateThread(0x0008, 0x00, 0x00, func_06_9A2)
    CreateThread(0x0009, 0x00, 0x00, func_08_B73)
    CreateThread(0x000A, 0x00, 0x00, func_0A_D44)
    CreateThread(0x000B, 0x00, 0x00, func_0C_F15)
    CreateThread(0x000C, 0x00, 0x00, func_0E_10E6)
    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/C5400._SN', 111, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x8E4
@scena.Code('func_05_8E4')
def func_05_8E4():
    OP_71(0x0000, 0x0002)
    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0004)
    OP_6F(0x0000, 800)
    ChrMoveTo(0x0008, -10730, -37250, -40850, 10000, 0x00)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 800)
    OP_70(0x0000, 900)
    Sleep(500)

    @scena.Lambda('lambda_092C')
    def lambda_092C():
        OP_D1(0x00FE, 0, 0, 7000, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_092C)

    ChrMoveTo(0x0008, -30710, -35000, -45850, 8000, 0x00)

    @scena.Lambda('lambda_095A')
    def lambda_095A():
        OP_D1(0x00FE, 0, 0, 0, 800)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_095A)

    Sleep(200)

    OP_98(0x00, 0x0008)
    OP_98(0x01, -38130, -27300, -10360)
    OP_98(0x01, -48310, -15150, 20700)
    OP_98(0x02, 0x0008, 25000, 0x06)
    OP_71(0x0000, 0x0004)

    Return()

# id: 0x0006 offset: 0x9A2
@scena.Code('func_06_9A2')
def func_06_9A2():
    Sleep(8000)

    OP_71(0x0000, 0x0002)
    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0004)
    OP_6F(0x0000, 800)
    OP_D1(0x00FE, 10000, 360000, 0, 0)

    @scena.Lambda('lambda_09D6')
    def lambda_09D6():
        OP_D1(0x00FE, 0, 360000, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_09D6)

    @scena.Lambda('lambda_09F0')
    def lambda_09F0():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_09F0)

    Sleep(1100)

    @scena.Lambda('lambda_0A10')
    def lambda_0A10():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0A10)

    Sleep(100)

    @scena.Lambda('lambda_0A30')
    def lambda_0A30():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0A30)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveTo(0x00FE, 0, -70000, -50000, 4000, 0x00)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 800)
    OP_70(0x0000, 900)

    @scena.Lambda('lambda_0A77')
    def lambda_0A77():
        OP_D1(0x00FE, 0, 350000, 10000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_0A77)

    OP_98(0x00, 0x00FE)
    OP_98(0x01, -16000, -70000, 100000)
    OP_98(0x01, -40000, -70000, 200000)
    OP_98(0x02, 0x00FE, 40000, 0x00)

    Return()

# id: 0x0007 offset: 0xAB5
@scena.Code('func_07_AB5')
def func_07_AB5():
    OP_71(0x0001, 0x0002)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0004)
    OP_6F(0x0001, 800)
    ChrMoveTo(0x0009, -10730, -37250, -80850, 10000, 0x00)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 900)
    Sleep(500)

    @scena.Lambda('lambda_0AFD')
    def lambda_0AFD():
        OP_D1(0x00FE, 0, 0, 7000, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0AFD)

    ChrMoveTo(0x0009, -30710, -35000, -85850, 8000, 0x00)

    @scena.Lambda('lambda_0B2B')
    def lambda_0B2B():
        OP_D1(0x00FE, 0, 0, 0, 800)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0B2B)

    Sleep(200)

    OP_98(0x00, 0x0009)
    OP_98(0x01, -40130, -27300, -10360)
    OP_98(0x01, -50310, -15150, 20700)
    OP_98(0x02, 0x0009, 25000, 0x06)
    OP_71(0x0001, 0x0004)

    Return()

# id: 0x0008 offset: 0xB73
@scena.Code('func_08_B73')
def func_08_B73():
    Sleep(10000)

    OP_71(0x0001, 0x0002)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0004)
    OP_6F(0x0001, 800)
    OP_D1(0x00FE, -10000, 360000, 0, 0)

    @scena.Lambda('lambda_0BA7')
    def lambda_0BA7():
        OP_D1(0x00FE, 0, 360000, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_0BA7)

    @scena.Lambda('lambda_0BC1')
    def lambda_0BC1():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0BC1)

    Sleep(1100)

    @scena.Lambda('lambda_0BE1')
    def lambda_0BE1():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0BE1)

    Sleep(100)

    @scena.Lambda('lambda_0C01')
    def lambda_0C01():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0C01)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveTo(0x00FE, 0, -70000, -50000, 4000, 0x00)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 900)

    @scena.Lambda('lambda_0C48')
    def lambda_0C48():
        OP_D1(0x00FE, 0, 340000, 20000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_0C48)

    OP_98(0x00, 0x00FE)
    OP_98(0x01, -24000, -70000, 90000)
    OP_98(0x01, -60000, -70000, 180000)
    OP_98(0x02, 0x00FE, 40000, 0x00)

    Return()

# id: 0x0009 offset: 0xC86
@scena.Code('func_09_C86')
def func_09_C86():
    OP_71(0x0002, 0x0002)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0004)
    OP_6F(0x0002, 800)
    ChrMoveTo(0x000A, -10730, -37250, -45850, 10000, 0x00)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)
    Sleep(500)

    @scena.Lambda('lambda_0CCE')
    def lambda_0CCE():
        OP_D1(0x00FE, 0, 0, 7000, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0CCE)

    ChrMoveTo(0x000A, -30710, -35000, -50850, 8000, 0x00)

    @scena.Lambda('lambda_0CFC')
    def lambda_0CFC():
        OP_D1(0x00FE, 0, 0, 0, 800)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0CFC)

    Sleep(200)

    OP_98(0x00, 0x000A)
    OP_98(0x01, -38130, -30300, -10360)
    OP_98(0x01, -48310, -18150, 20700)
    OP_98(0x02, 0x000A, 25000, 0x06)
    OP_71(0x0002, 0x0004)

    Return()

# id: 0x000A offset: 0xD44
@scena.Code('func_0A_D44')
def func_0A_D44():
    Sleep(12000)

    OP_71(0x0002, 0x0002)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0004)
    OP_6F(0x0002, 800)
    OP_D1(0x00FE, 0, 360000, 10000, 0)

    @scena.Lambda('lambda_0D78')
    def lambda_0D78():
        OP_D1(0x00FE, 0, 360000, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_0D78)

    @scena.Lambda('lambda_0D92')
    def lambda_0D92():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0D92)

    Sleep(1100)

    @scena.Lambda('lambda_0DB2')
    def lambda_0DB2():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0DB2)

    Sleep(100)

    @scena.Lambda('lambda_0DD2')
    def lambda_0DD2():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0DD2)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveTo(0x00FE, 0, -70000, -50000, 4000, 0x00)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)

    @scena.Lambda('lambda_0E19')
    def lambda_0E19():
        OP_D1(0x00FE, 0, 330000, 30000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_0E19)

    OP_98(0x00, 0x00FE)
    OP_98(0x01, -32000, -70000, 80000)
    OP_98(0x01, -80000, -70000, 160000)
    OP_98(0x02, 0x00FE, 40000, 0x00)

    Return()

# id: 0x000B offset: 0xE57
@scena.Code('func_0B_E57')
def func_0B_E57():
    OP_71(0x0003, 0x0002)
    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0004)
    OP_6F(0x0003, 800)
    ChrMoveTo(0x000B, -7730, -37250, -75850, 10000, 0x00)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 800)
    OP_70(0x0003, 900)
    Sleep(500)

    @scena.Lambda('lambda_0E9F')
    def lambda_0E9F():
        OP_D1(0x00FE, 0, 0, 7000, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0E9F)

    ChrMoveTo(0x000B, -27710, -35000, -80850, 8000, 0x00)

    @scena.Lambda('lambda_0ECD')
    def lambda_0ECD():
        OP_D1(0x00FE, 0, 0, 0, 800)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0ECD)

    Sleep(200)

    OP_98(0x00, 0x000B)
    OP_98(0x01, -41130, -27300, -10360)
    OP_98(0x01, -51310, -15150, 20700)
    OP_98(0x02, 0x000B, 25000, 0x06)
    OP_71(0x0003, 0x0004)

    Return()

# id: 0x000C offset: 0xF15
@scena.Code('func_0C_F15')
def func_0C_F15():
    Sleep(14000)

    OP_71(0x0003, 0x0002)
    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0004)
    OP_6F(0x0003, 800)
    OP_D1(0x00FE, 0, 360000, -10000, 0)

    @scena.Lambda('lambda_0F49')
    def lambda_0F49():
        OP_D1(0x00FE, 0, 360000, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_0F49)

    @scena.Lambda('lambda_0F63')
    def lambda_0F63():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0F63)

    Sleep(1100)

    @scena.Lambda('lambda_0F83')
    def lambda_0F83():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0F83)

    Sleep(100)

    @scena.Lambda('lambda_0FA3')
    def lambda_0FA3():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0FA3)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveTo(0x00FE, 0, -70000, -50000, 4000, 0x00)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 800)
    OP_70(0x0003, 900)

    @scena.Lambda('lambda_0FEA')
    def lambda_0FEA():
        OP_D1(0x00FE, 0, 320000, 40000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_0FEA)

    OP_98(0x00, 0x00FE)
    OP_98(0x01, -38000, -70000, 70000)
    OP_98(0x01, -100000, -70000, 140000)
    OP_98(0x02, 0x00FE, 40000, 0x00)

    Return()

# id: 0x000D offset: 0x1028
@scena.Code('func_0D_1028')
def func_0D_1028():
    OP_71(0x0004, 0x0002)
    OP_72(0x0004, 0x0020)
    OP_72(0x0004, 0x0004)
    OP_6F(0x0004, 800)
    ChrMoveTo(0x000C, -7730, -37250, -50850, 10000, 0x00)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 800)
    OP_70(0x0004, 900)
    Sleep(500)

    @scena.Lambda('lambda_1070')
    def lambda_1070():
        OP_D1(0x00FE, 0, 0, 7000, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1070)

    ChrMoveTo(0x000C, -27710, -35000, -55850, 8000, 0x00)

    @scena.Lambda('lambda_109E')
    def lambda_109E():
        OP_D1(0x00FE, 0, 0, 0, 800)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_109E)

    Sleep(200)

    OP_98(0x00, 0x000C)
    OP_98(0x01, -38130, -30300, -10360)
    OP_98(0x01, -48310, -18150, 20700)
    OP_98(0x02, 0x000C, 25000, 0x06)
    OP_71(0x0004, 0x0004)

    Return()

# id: 0x000E offset: 0x10E6
@scena.Code('func_0E_10E6')
def func_0E_10E6():
    Sleep(16000)

    OP_71(0x0004, 0x0002)
    OP_72(0x0004, 0x0020)
    OP_72(0x0004, 0x0004)
    OP_6F(0x0004, 800)
    OP_D1(0x00FE, 0, 360000, -10000, 0)

    @scena.Lambda('lambda_111A')
    def lambda_111A():
        OP_D1(0x00FE, 0, 360000, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_111A)

    @scena.Lambda('lambda_1134')
    def lambda_1134():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1134)

    Sleep(1100)

    @scena.Lambda('lambda_1154')
    def lambda_1154():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1154)

    Sleep(100)

    @scena.Lambda('lambda_1174')
    def lambda_1174():
        ChrMoveTo(0x00FE, 0, -70500, -50000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1174)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveTo(0x00FE, 0, -70000, -50000, 4000, 0x00)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 800)
    OP_70(0x0004, 900)

    @scena.Lambda('lambda_11BB')
    def lambda_11BB():
        OP_D1(0x00FE, 0, 310000, 40000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_11BB)

    OP_98(0x00, 0x00FE)
    OP_98(0x01, -44000, -70000, 60000)
    OP_98(0x01, -120000, -70000, 120000)
    OP_98(0x02, 0x00FE, 40000, 0x00)

    Return()

# id: 0x000F offset: 0x11F9
@scena.Code('func_0F_11F9')
def func_0F_11F9():
    EventBegin(0x00)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetPos(0x0101, 1130, 150, -13000, 180)
    CameraMove(1440, 150, -16820, 0)
    OP_67(0, 5390, -10000, 0)
    CameraSetDistance(3040, 0)
    OP_6C(7000, 0)
    OP_6E(329, 0)
    OP_72(0x0006, 0x0004)

    @scena.Lambda('lambda_125F')
    def lambda_125F():
        CameraSetDistance(2820, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_125F)

    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0006, 0)
    OP_70(0x0006, 230)
    PlaySE(307, 0x00, 0x64)
    OP_73(0x0006)

    @scena.Lambda('lambda_128F')
    def lambda_128F():
        CameraMove(1170, 150, -19540, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_128F)

    @scena.Lambda('lambda_12A7')
    def lambda_12A7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_12A7)

    ChrMoveTo(0x0101, 1020, 0, -20530, 5000, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010330541V#1020F#5P啊啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_12(0x0000F424, 0x000C3500, 0x00001F40)

    @scena.Lambda('lambda_1320')
    def lambda_1320():
        CameraMove(-2500, 0, -43740, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1320)

    @scena.Lambda('lambda_1338')
    def lambda_1338():
        OP_67(0, 26980, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1338)

    @scena.Lambda('lambda_1350')
    def lambda_1350():
        CameraSetDistance(7990, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1350)

    @scena.Lambda('lambda_1360')
    def lambda_1360():
        OP_6C(44000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1360)

    @scena.Lambda('lambda_1370')
    def lambda_1370():
        OP_6E(338, 8000)

        ExitThread()

    DispatchAsync(0x0012, 0x0000, lambda_1370)

    Sleep(4000)

    ChrSetDirection(0x0101, 135, 400)
    ChrWalkTo(0x0101, 11480, 0, -24750, 3000, 0x00)
    ChrSetDirection(0x0101, 90, 400)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    Fade(500)
    OP_12(0x0000F424, 0x0006BC9C, 0x00000000)
    CameraMove(12590, 0, -23580, 0)
    OP_67(0, 5830, -10000, 0)
    CameraSetDistance(3110, 0)
    OP_6C(44000, 0)
    OP_6E(324, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330542V#1007F#6P糟糕了……\n',
            '不知不觉好像跑到甲板上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330543V#1019F话说回来……\n',
            '这里还真是大得离谱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 225, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330544V#1010F#5P看来要想逃出去的话，\n',
            '必须要寻找到降落伞，\n',
            '或者直接夺取飞艇……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330545V#1002F不管了，总之先前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0384, 6, 0x1C26))
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x150C
@scena.Code('func_10_150C')
def func_10_150C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0384, 7, 0x1C27)),
            Expr.Return,
        ),
        'loc_1514',
    )

    Return()

    def _loc_1514(): pass

    label('loc_1514')

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 980, 0, -65550, 180)
    CameraMove(1030, 150, -68450, 0)
    OP_67(0, 8150, -10000, 0)
    CameraSetDistance(3540, 0)
    OP_6C(45000, 0)
    OP_6E(305, 0)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 300)
    OP_0D()
    PlaySE(307, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Sleep(500)

    ChrSetPos(0x000D, 2000, -3900, -76440, 0)
    ChrSetPos(0x000E, -180, -3900, -76440, 0)

    NpcTalk(
        0x000D,
        '男人的声音',
        (
            '#4210330546V#1P在这里了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    @scena.Lambda('lambda_15F5')
    def lambda_15F5():
        ChrMoveTo(0x00FE, 980, 0, -63000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_15F5)

    @scena.Lambda('lambda_1610')
    def lambda_1610():
        CameraMove(1120, 0, -66000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1610)

    @scena.Lambda('lambda_1628')
    def lambda_1628():
        CameraSetDistance(2870, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1628)

    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetSubChip(0x000D, 0)
    ChrSetChipByIndex(0x000D, 8)

    @scena.Lambda('lambda_164C')
    def lambda_164C():
        ChrMoveToRelative(0x00FE, 0, 0, 6000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_164C)

    Sleep(100)

    ChrSetSubChip(0x000E, 0)
    ChrSetChipByIndex(0x000E, 8)

    @scena.Lambda('lambda_1676')
    def lambda_1676():
        ChrMoveToRelative(0x00FE, 0, 0, 6000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1676)

    WaitForThreadExit(0x000D, 0x0001)
    PlaySE(505, 0x00, 0x64)
    ChrSetSubChip(0x000D, 0)
    ChrSetChipByIndex(0x000D, 7)
    WaitForThreadExit(0x000E, 0x0001)
    PlaySE(505, 0x00, 0x64)
    ChrSetSubChip(0x000E, 0)
    ChrSetChipByIndex(0x000E, 7)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010330547V#1020F#5P糟了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000F, 2000, 0, -35250, 180)
    ChrSetPos(0x0010, -180, 0, -35250, 180)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetDirection(0x0101, 0, 600)

    @scena.Lambda('lambda_171B')
    def lambda_171B():
        CameraMove(980, 0, -53000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_171B)

    @scena.Lambda('lambda_1733')
    def lambda_1733():
        OP_67(0, 6000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1733)

    @scena.Lambda('lambda_174B')
    def lambda_174B():
        OP_6E(369, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_174B)

    @scena.Lambda('lambda_175B')
    def lambda_175B():
        CameraSetDistance(2510, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_175B)

    @scena.Lambda('lambda_176B')
    def lambda_176B():
        ChrMoveToRelative(0x00FE, 0, 0, 10000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_176B)

    CreateThread(0x000F, 0x00, 0x00, func_11_25DC)
    Sleep(100)

    CreateThread(0x0010, 0x00, 0x00, func_11_25DC)
    Sleep(300)

    CreateThread(0x000E, 0x00, 0x00, func_12_2605)
    Sleep(100)

    CreateThread(0x000D, 0x00, 0x00, func_12_2605)
    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x000D, 0x0000)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010330548V#1009F#6P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4210330549V#4P呼……\n',
            '看你还能往哪里跑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#4230330550V#5P不愧是Ｓ级游击士、\n',
            '『剑圣』卡西乌斯的女儿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#4230330551V#5P竟然在这种状况下还敢逃走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330552V#1002F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#4220330553V#6P你应该明白才对，\n',
            '徒劳的抵抗是没有用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#4220330554V#6P还是乖乖投降吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0011, 950, 0, -37920, 180)
    ChrClearFlags(0x0011, 0x0080)
    Sleep(500)

    NpcTalk(
        0x0011,
        '青年的声音',
        (
            '#0480330555V#4P哈哈，真是丢脸啊。\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_19AC')
    def lambda_19AC():
        CameraMove(1570, 0, -49360, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_19AC)

    @scena.Lambda('lambda_19C4')
    def lambda_19C4():
        OP_67(0, 5240, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_19C4)

    ChrWalkTo(0x0011, 1060, 0, -46230, 3000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330556V#1026F#4P……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0011,
        '强化猎兵',
        (
            '#0480330557V#5P哼哼，戴上面具\n',
            '就认不出我了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0011,
        '强化猎兵',
        (
            '#0480330558V#5P没办法了。\n',
            '特别优待，让你看看我的真面目吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0011, 1)
    ChrSetSubChip(0x0011, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330559V#1004F#4P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0011,
        '青年',
        (
            '#0480330560V#1226F#5P呵呵……\n',
            '看来总算想起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330561V#1220F做梦也没想到\n',
            '会在这种地方见到我吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

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

    SetMessageWindowPos(-1, 50, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '青年的真正身份是……？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【……您是哪位？】\n'),
            TXT(0x01, '【卡普亚空贼团的次子】\n'),
            TXT(0x02, '【戴尔蒙市长的秘书】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1C2C'),
        (0x00000001, 'loc_1CF7'),
        (0x00000002, 'loc_1DEE'),
        (-1, 'loc_1F05'),
    )

    def _loc_1C2C(): pass

    label('loc_1C2C')

    ChrTalk(
        0x0101,
        (
            '#0010330562V#1025F#4P唔……\n',
            '见好像是见过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330563V#1016F您是……哪位来着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0011,
        '青年',
        (
            '#0480330564V#1225F#5P是戴尔蒙市长的前秘书，\n',
            '基尔巴特！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330565V你自己逮捕过的人\n',
            '好歹也该记清楚吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F05')

    def _loc_1CF7(): pass

    label('loc_1CF7')

    ChrTalk(
        0x0101,
        (
            '#0010330562V#1025F#4P唔……\n',
            '好像是有些眼熟…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330567V#1016F啊！是那个男人婆\n',
            '的二哥吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0011,
        '青年',
        (
            '#0480330568V#1224F#5P那是谁啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330569V#1225F我是戴尔蒙市长的前秘书、基尔巴特！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330565V你自己逮捕过的人\n',
            '好歹也该记清楚吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F05')

    def _loc_1DEE(): pass

    label('loc_1DEE')

    ChrTalk(
        0x0101,
        (
            '#0010330571V#1016F#4P唔……\n',
            '好像是在哪里见过，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330572V#1008F……是不是戴尔蒙市长的\n',
            '那个秘书……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0011,
        '青年',
        (
            '#0480330573V#1224F#5P干嘛那么\n',
            '没自信的样子啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330574V#1225F对，我就是戴尔蒙市长的前秘书，\n',
            '基尔巴特！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330565V你自己逮捕过的人\n',
            '好歹也该记清楚吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F05')

    def _loc_1F05(): pass

    label('loc_1F05')

    ChrTalk(
        0x0101,
        (
            '#0010330576V#1020F#4P因、因为太意外了啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330577V#1019F你不是已经被\n',
            '我们交给王国军关押了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330578V为什么会在这种地方！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0480330579V#1226F#5P哼哼，发生政变事件的时候，\n',
            '我趁乱逃脱了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330580V#1221F之后我被『结社』收留，\n',
            '并发誓从今以后永远效忠于『结社』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330581V#1007F#4P该、该说你执着\n',
            '还是顽固不化呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330582V#1002F看你那身打扮，\n',
            '莫非是想战斗吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0480330583V#1221F#5P我参加战斗很奇怪吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330584V#1226F哼，我虽然是个有文化的才子，\n',
            '但毕竟也是个文武双全的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330585V#1015F#4P但你以前在灯塔被特务兵射中\n',
            '的时候还大声惨叫来着……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330586V所以说，像你这样的人\n',
            '实在不太适合战斗呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '#0480330587V#1225F#5P啰、啰嗦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330588V加入『结社』之后\n',
            '我接受了战斗强化程序！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330589V身体能力被大幅度强化，\n',
            '还学会了最高水平的战斗技术！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330590V区区一个游击士，别妄想打败我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2276')
    def lambda_2276():
        CameraMove(1530, 0, -51170, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2276)

    @scena.Lambda('lambda_228E')
    def lambda_228E():
        OP_6E(450, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_228E)

    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0011, 2)
    ChrSetSubChip(0x0011, 0)
    OP_0D()
    Sleep(300)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000F,
        (
            '#4230330591V#5P哎呀哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#4220330592V#6P没办法了……\n',
            '那就稍微陪你玩一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0480330593V#1221F#5P好了……\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330594V你还是跪下求饶吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330595V那样的话\n',
            '我倒还可以饶过你哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330596V#1007F#4P那可太谢谢了。\n',
            '我高兴得连眼泪都要流出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330597V#1006F不过不好意思，\n',
            '我可是很执着的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 4)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    PlaySE(500, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 5)

    @scena.Lambda('lambda_2439')
    def lambda_2439():
        OP_99(0x0101, 0x00, 0x0C, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2439)

    Sleep(200)

    @scena.Lambda('lambda_244E')
    def lambda_244E():
        CameraMove(1530, 0, -50500, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_244E)

    @scena.Lambda('lambda_2466')
    def lambda_2466():
        OP_6E(400, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2466)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0480330598V#1224F#5P唔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330599V#1022F#4P『执行者』暂且不提，\n',
            '我怎么可能会输给小喽啰嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330600V#1005F好了──\n',
            '放马过来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2517')
    def lambda_2517():
        CameraMove(1170, 0, -52450, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2517)

    @scena.Lambda('lambda_252F')
    def lambda_252F():
        CameraSetDistance(1800, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_252F)

    ChrSetSubChip(0x000F, 0)
    ChrSetChipByIndex(0x000F, 12)
    CreateThread(0x000F, 0x00, 0x00, func_15_2676)
    Sleep(50)

    ChrSetSubChip(0x0010, 0)
    ChrSetChipByIndex(0x0010, 12)
    CreateThread(0x0010, 0x00, 0x00, func_15_2676)
    ChrSetChipByIndex(0x0011, 9)

    @scena.Lambda('lambda_256B')
    def lambda_256B():
        ChrMoveToRelative(0x00FE, 0, 0, -5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_256B)

    Sleep(50)

    ChrSetSubChip(0x000D, 0)
    ChrSetChipByIndex(0x000D, 12)
    CreateThread(0x000D, 0x00, 0x00, func_16_2690)
    Sleep(50)

    ChrSetSubChip(0x000E, 0)
    ChrSetChipByIndex(0x000E, 12)
    CreateThread(0x000E, 0x00, 0x00, func_16_2690)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x000D, 0x00)
    TerminateThread(0x000E, 0x00)
    TerminateThread(0x000F, 0x00)
    TerminateThread(0x0010, 0x00)
    TerminateThread(0x0011, 0x00)
    Battle(0x0000042A, 0x0030000E, 0x00, 0x0000, 0xFF)
    Call(0, 0x0017)

    Return()

# id: 0x0011 offset: 0x25DC
@scena.Code('func_11_25DC')
def func_11_25DC():
    ChrSetChipByIndex(0x00FE, 8)
    ChrMoveToRelative(0x00FE, 0, 0, -13200, 5000, 0x00)
    PlaySE(505, 0x00, 0x64)
    ChrSetChipByIndex(0x00FE, 7)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0012 offset: 0x2605
@scena.Code('func_12_2605')
def func_12_2605():
    ChrSetChipByIndex(0x00FE, 8)
    ChrMoveToRelative(0x00FE, 0, 0, 13200, 5000, 0x00)
    PlaySE(505, 0x00, 0x64)
    ChrSetChipByIndex(0x00FE, 7)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0013 offset: 0x262E
@scena.Code('func_13_262E')
def func_13_262E():
    ChrSetChipByIndex(0x00FE, 8)
    ChrMoveToRelative(0x00FE, 0, 0, -1200, 2000, 0x00)
    ChrSetChipByIndex(0x00FE, 7)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0014 offset: 0x2652
@scena.Code('func_14_2652')
def func_14_2652():
    ChrSetChipByIndex(0x00FE, 8)
    ChrMoveToRelative(0x00FE, 0, 0, 1200, 2000, 0x00)
    ChrSetChipByIndex(0x00FE, 7)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0015 offset: 0x2676
@scena.Code('func_15_2676')
def func_15_2676():
    ChrSetChipByIndex(0x00FE, 8)
    ChrMoveToRelative(0x00FE, 0, 0, -3200, 8000, 0x00)

    Return()

# id: 0x0016 offset: 0x2690
@scena.Code('func_16_2690')
def func_16_2690():
    ChrSetChipByIndex(0x00FE, 8)
    ChrMoveToRelative(0x00FE, 0, 0, 3000, 8000, 0x00)

    Return()

# id: 0x0017 offset: 0x26AA
@scena.Code('func_17_26AA')
def func_17_26AA():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_0D()
    TerminateThread(0x0011, 0x00)
    TerminateThread(0x000D, 0x00)
    TerminateThread(0x000E, 0x00)
    TerminateThread(0x000F, 0x00)
    TerminateThread(0x0010, 0x00)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_26DF'),
        (0x00000007, 'loc_26EC'),
        (0x00000001, 'loc_26F9'),
        (-1, 'loc_2706'),
    )

    def _loc_26DF(): pass

    label('loc_26DF')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2706')

    def _loc_26EC(): pass

    label('loc_26EC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2706')

    def _loc_26F9(): pass

    label('loc_26F9')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2706')

    def _loc_2706(): pass

    label('loc_2706')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2756',
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
        100,
        0,
        (
            TXT(0x00, '【◇胜了】\n'),
            TXT(0x01, '【◇超过数回合】\n'),
            TXT(0x02, '【◇输了】\n'),
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

    def _loc_2756(): pass

    label('loc_2756')

    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2774'),
        (0x00000001, 'loc_2B25'),
        (0x00000002, 'loc_2DB2'),
        (-1, 'loc_2FC0'),
    )

    def _loc_2774(): pass

    label('loc_2774')

    OP_2B(0x0098, 0x0005)
    CameraMove(1360, 0, -52330, 0)
    OP_67(0, 6510, -10000, 0)
    CameraSetDistance(3800, 0)
    OP_6C(45000, 0)
    OP_6E(270, 0)
    CameraMove(1450, 0, -51300, 0)
    OP_67(0, 5350, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(270, 0)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0101, 980, 0, -53200, 0)
    ChrSetPos(0x0011, 980, 0, -48100, 180)
    ChrSetPos(0x000D, 3500, 0, -56070, 315)
    ChrSetPos(0x000E, -1160, 0, -56070, 45)
    ChrSetPos(0x000F, 3300, 0, -50340, 225)
    ChrSetPos(0x0010, -1160, 0, -50440, 135)
    ChrSetChipByIndex(0x0101, 4)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x000D, 9)
    ChrSetSubChip(0x000D, 3)
    ChrSetChipByIndex(0x000E, 9)
    ChrSetSubChip(0x000E, 3)
    ChrSetChipByIndex(0x000F, 9)
    ChrSetSubChip(0x000F, 3)
    ChrSetChipByIndex(0x0010, 9)
    ChrSetSubChip(0x0010, 3)
    ChrSetChipByIndex(0x0011, 2)
    ChrSetSubChip(0x0011, 0)

    @scena.Lambda('lambda_28B4')
    def lambda_28B4():
        CameraSetDistance(3500, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_28B4)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    OP_62(0x0011, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '#0480330601V#1224F#5P不、不可能……\n',
            '面对这么多人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330602V#1005F#4P呼……呼……\n',
            '见识到游击士的力量了吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4210330603V#2P不愧是『剑圣』的女儿……\n',
            '好像有点小看你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#4230330604V#5P……唔。\n',
            '看来有必要解除禁制了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x01, 0x00, func_1E_52C5)
    Sleep(50)

    CreateThread(0x0010, 0x01, 0x00, func_1E_52C5)
    Sleep(100)

    CreateThread(0x000E, 0x01, 0x00, func_1E_52C5)
    Sleep(50)

    CreateThread(0x000F, 0x01, 0x00, func_1E_52C5)
    WaitForThreadExit(0x000F, 0x0001)
    Sleep(100)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0480330605V#1221F#5P哈哈，大吃一惊吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330606V我们都是经由『结社』的技术\n',
            '将身体能力进行了大幅度的强化，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330607V远比一般的人类强韧哟！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x00, 0x00, func_1A_5221)
    Sleep(100)

    CreateThread(0x000E, 0x00, 0x00, func_1B_524A)
    Sleep(100)

    CreateThread(0x000F, 0x00, 0x00, func_1C_5273)
    Sleep(100)

    CreateThread(0x0010, 0x00, 0x00, func_1D_529C)
    WaitForThreadExit(0x0010, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010310610V#1002F#4P可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0099, 0x01, 0x0020)

    Jump('loc_2FC0')

    def _loc_2B25(): pass

    label('loc_2B25')

    OP_2B(0x0098, 0x0002)
    CameraMove(1450, 0, -51300, 0)
    OP_67(0, 5350, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(270, 0)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0101, 980, 0, -53200, 0)
    ChrSetPos(0x0011, 980, 0, -48100, 180)
    ChrSetPos(0x000D, 3500, 0, -56070, 315)
    ChrSetPos(0x000E, -1160, 0, -56070, 45)
    ChrSetPos(0x000F, 3300, 0, -50340, 225)
    ChrSetPos(0x0010, -1160, 0, -50440, 135)
    ChrSetChipByIndex(0x0101, 4)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x000D, 7)
    ChrSetSubChip(0x000D, 0)
    ChrSetChipByIndex(0x000E, 7)
    ChrSetSubChip(0x000E, 0)
    ChrSetChipByIndex(0x000F, 7)
    ChrSetSubChip(0x000F, 0)
    ChrSetChipByIndex(0x0010, 7)
    ChrSetSubChip(0x0010, 0)
    ChrSetChipByIndex(0x0011, 2)
    ChrSetSubChip(0x0011, 0)
    OP_71(0x0007, 0x0004)

    @scena.Lambda('lambda_2C2D')
    def lambda_2C2D():
        CameraSetDistance(3500, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2C2D)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    OP_62(0x0011, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010330609V#1022F#4P呼……呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330610V#1003F真、真是难对付啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0480330611V#1224F#5P好、好顽强的小丫头……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4210330612V#2P不过看起来……\n',
            '你也已经气喘吁吁了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#4230330613V#5P游戏到此为止。\n',
            '现在就要缩小包围圈了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x00, 0x00, func_1A_5221)
    Sleep(100)

    CreateThread(0x000E, 0x00, 0x00, func_1B_524A)
    Sleep(100)

    CreateThread(0x000F, 0x00, 0x00, func_1C_5273)
    Sleep(100)

    CreateThread(0x0010, 0x00, 0x00, func_1D_529C)
    WaitForThreadExit(0x0010, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010330614V#1002F#4P可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0099, 0x01, 0x0040)

    Jump('loc_2FC0')

    def _loc_2DB2(): pass

    label('loc_2DB2')

    CameraMove(1450, 0, -51300, 0)
    OP_67(0, 5350, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(270, 0)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0101, 980, 0, -53200, 0)
    ChrSetPos(0x0011, 980, 0, -48100, 180)
    ChrSetPos(0x000D, 3000, 0, -55570, 315)
    ChrSetPos(0x000E, -660, 0, -55570, 45)
    ChrSetPos(0x000F, 2850, 0, -50940, 225)
    ChrSetPos(0x0010, -660, 0, -50940, 135)
    ChrSetChipByIndex(0x0101, 6)
    ChrSetSubChip(0x0101, 3)
    ChrSetChipByIndex(0x000D, 7)
    ChrSetSubChip(0x000D, 0)
    ChrSetChipByIndex(0x000E, 7)
    ChrSetSubChip(0x000E, 0)
    ChrSetChipByIndex(0x000F, 7)
    ChrSetSubChip(0x000F, 0)
    ChrSetChipByIndex(0x0010, 7)
    ChrSetSubChip(0x0010, 0)
    ChrSetChipByIndex(0x0011, 2)
    ChrSetSubChip(0x0011, 0)

    @scena.Lambda('lambda_2EB0')
    def lambda_2EB0():
        CameraSetDistance(3500, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2EB0)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010330615V#1021F#4P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0480330616V#1226F哼，只会逞口舌之利的小丫头。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330617V虽然我不会杀你，\n',
            '但总要让你稍微吃点苦头。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330618V#1221F哼哼哼……\n',
            '让我高兴一下如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330619V#1002F#4P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0099, 0x01, 0x0080)

    Jump('loc_2FC0')

    def _loc_2FC0(): pass

    label('loc_2FC0')

    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, 1000, 0, -65850, 0)
    Sleep(500)

    NpcTalk(
        0x0012,
        '男人的声音',
        (
            '#0020330620V#1P……我没来晚吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000F, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0010, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0011, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    Fade(500)
    ChrSetFlags(0x0101, 0x0800)
    CameraMove(920, 0, -55380, 0)
    OP_67(0, 3840, -10000, 0)
    CameraSetDistance(3690, 0)
    OP_6C(181000, 0)
    OP_6E(270, 0)

    @scena.Lambda('lambda_30C1')
    def lambda_30C1():
        ChrWalkTo(0x00FE, 1000, 0, -58850, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_30C1)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3103',
    )

    Sleep(100)

    ChrSetFlags(0x0101, 0x0020)
    ChrSetDirection(0x0101, 180, 400)
    ChrClearFlags(0x0101, 0x0020)

    def _loc_3103(): pass

    label('loc_3103')

    WaitForThreadExit(0x0012, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    NpcTalk(
        0x0012,
        '强化猎兵',
        (
            '#0020330621V#5P似乎陷入苦战了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0012,
        '强化猎兵',
        (
            '#0020330622V#5P让我来助你一臂之力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3224',
    )

    ChrTalk(
        0x0011,
        (
            '#0480330623V#1221F#6P哈哈，没那个必要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330624V虽然是个顽强的丫头，\n',
            '但让她彻底屈服也只是时间问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330625V你就待在那里好好看着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_329E')

    def _loc_3224(): pass

    label('loc_3224')

    ChrTalk(
        0x0011,
        (
            '#0480330623V#1221F#6P哈哈，没那个必要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330627V好戏现在才刚刚\n',
            '要开始呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480330625V你就站在那里安静看着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_329E(): pass

    label('loc_329E')

    NpcTalk(
        0x0012,
        '强化猎兵',
        (
            '#0020330629V#5P……我可不是\n',
            '在和你说话哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0480330630V#1224F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0012, 0)
    ChrSetChipByIndex(0x0012, 14)
    OP_0D()
    Sleep(100)

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_338D')
    def lambda_338D():
        ChrTurnDirection(0x00FE, 0x0012, 600)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_338D)

    Sleep(50)

    @scena.Lambda('lambda_33A0')
    def lambda_33A0():
        ChrTurnDirection(0x00FE, 0x0012, 600)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_33A0)

    Sleep(50)

    @scena.Lambda('lambda_33B3')
    def lambda_33B3():
        ChrTurnDirection(0x00FE, 0x0012, 600)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_33B3)

    Sleep(50)

    @scena.Lambda('lambda_33C6')
    def lambda_33C6():
        ChrTurnDirection(0x00FE, 0x0012, 600)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_33C6)

    PlaySE(501, 0x00, 0x64)

    @scena.Lambda('lambda_33D9')
    def lambda_33D9():
        OP_99(0x00FE, 0x01, 0x03, 2500)

        ExitThread()

    DispatchAsync(0x0012, 0x0000, lambda_33D9)

    WaitForThreadExit(0x0012, 0x0000)

    NpcTalk(
        0x0012,
        '强化猎兵',
        (
            '#0020330631V#5P……太慢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    ChrClearFlags(0x0101, 0x0800)
    CameraMove(1070, 0, -54680, 0)
    OP_67(0, 5000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(15000, 0)
    OP_6E(300, 0)
    LoadEffect(0x04, 'Craft\\\\cr161_00.eff')
    MapClearFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_3488')
    def lambda_3488():
        CameraMove(1300, 0, -49560, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3488)

    @scena.Lambda('lambda_34A0')
    def lambda_34A0():
        CameraSetDistance(2800, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_34A0)

    @scena.Lambda('lambda_34B0')
    def lambda_34B0():
        OP_6C(45000, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_34B0)

    ChrSetAfterImage(0x00, 0x0012, 0x0014, 0x01F4)
    CreateThread(0x0012, 0x00, 0x00, func_23_545A)
    Sleep(200)

    OP_7C(0, 200, 3000, 100)
    CreateThread(0x000D, 0x00, 0x00, func_25_54C6)
    Sleep(200)

    OP_7C(0, 200, 3000, 100)
    CreateThread(0x000E, 0x00, 0x00, func_27_55BC)
    Sleep(200)

    OP_7C(0, 200, 3000, 100)
    CreateThread(0x000F, 0x00, 0x00, func_26_5541)
    Sleep(200)

    OP_7C(0, 200, 3000, 100)
    CreateThread(0x0010, 0x00, 0x00, func_28_5637)
    ChrSetPos(0x0012, 1150, 0, -51670, 0)

    @scena.Lambda('lambda_3554')
    def lambda_3554():
        ChrJumpTo(0x00FE, 1050, 0, -49700, 100, 1000)

        ExitThread()

    DispatchAsync(0x0012, 0x0000, lambda_3554)

    @scena.Lambda('lambda_3572')
    def lambda_3572():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 100)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3572)

    PlaySE(155, 0x00, 0x64)
    WaitForThreadExit(0x0012, 0x0000)
    ChrSetAfterImage(0x01, 0x0012, 0x0000, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000010)
    Sleep(1500)

    PlaySE(501, 0x00, 0x64)
    OP_99(0x0012, 0x09, 0x0C, 1500)
    Sleep(500)

    CreateThread(0x000D, 0x00, 0x00, func_1F_52F6)
    Sleep(120)

    CreateThread(0x000E, 0x00, 0x00, func_20_534F)
    Sleep(80)

    CreateThread(0x000F, 0x00, 0x00, func_21_53A8)
    Sleep(120)

    CreateThread(0x0010, 0x00, 0x00, func_22_5401)
    WaitForThreadExit(0x0010, 0x0000)
    ChrJumpTo(0x0011, 980, 0, -48100, 400, 5000)

    @scena.Lambda('lambda_3603')
    def lambda_3603():
        CameraMove(1570, 0, -48000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3603)

    @scena.Lambda('lambda_361B')
    def lambda_361B():
        ChrMoveToRelativeAsync(0x0011, 0, 0, 1000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_361B)

    OP_62(0x0011, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0011,
        (
            '#0480330632V#1224F#5P什、什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_369D',
    )

    ChrSetFlags(0x0101, 0x0020)
    ChrSetDirection(0x0101, 0, 400)
    ChrClearFlags(0x0101, 0x0020)

    Jump('loc_36B1')

    def _loc_369D(): pass

    label('loc_369D')

    OP_99(0x0101, 0x03, 0x00, 1500)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 4)
    OP_0D()

    def _loc_36B1(): pass

    label('loc_36B1')

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330633V#1004F#4P…………咦……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0011,
        (
            '#0480330634V#1224F#5P你、你在干什么！？\n',
            '到底想怎样！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0012,
        '强化猎兵',
        (
            '#0020330635V#4P不好意思……\n',
            '我也认为你并不适合战斗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x02, 'scraft\\\\sc000_11.eff')
    OP_99(0x0012, 0x00, 0x03, 1200)
    ChrSetAfterImage(0x00, 0x0012, 0x0032, 0x01F4)
    CreateThread(0x0012, 0x01, 0x00, func_29_567D)
    Sleep(100)

    @scena.Lambda('lambda_37B0')
    def lambda_37B0():
        CameraMove(2360, 0, -45710, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_37B0)

    @scena.Lambda('lambda_37C8')
    def lambda_37C8():
        CameraSetDistance(3200, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_37C8)

    WaitForThreadExit(0x0012, 0x0001)
    ChrSetAfterImage(0x01, 0x0012, 0x0000, 0x0000)
    OP_7C(0, 200, 3000, 100)
    ChrSetFlags(0x0011, 0x0002)
    ChrSetFlags(0x0011, 0x0020)
    ChrClearFlags(0x0011, 0x0001)
    ChrSetChipByIndex(0x0011, 28)
    ChrSetSubChip(0x0011, 5)
    ChrJumpTo(0x0011, -350, 0, -45820, 400, 10000)

    ChrTalk(
        0x0011,
        (
            '#0480330636V#1227F#5P呜哇！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrSetChipByIndex(0x0011, 10)
    ChrSetSubChip(0x0011, 5)
    ChrJumpTo(0x0011, -1080, 0, -44700, 200, 8000)

    @scena.Lambda('lambda_3868')
    def lambda_3868():
        ChrMoveTo(0x00FE, -1820, 0, -43300, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_3868)

    Sleep(50)

    @scena.Lambda('lambda_3888')
    def lambda_3888():
        ChrMoveTo(0x00FE, -1820, 0, -43300, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_3888)

    Sleep(50)

    @scena.Lambda('lambda_38A8')
    def lambda_38A8():
        ChrMoveTo(0x00FE, -1820, 0, -43300, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_38A8)

    WaitForThreadExit(0x0011, 0x0002)
    Sleep(1000)

    OP_20(0x00000BB8)

    @scena.Lambda('lambda_38D2')
    def lambda_38D2():
        CameraMove(1870, 0, -49200, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38D2)

    @scena.Lambda('lambda_38EA')
    def lambda_38EA():
        OP_6E(308, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_38EA)

    Sleep(200)

    PlaySE(501, 0x00, 0x64)
    OP_99(0x0012, 0x08, 0x0C, 1500)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010330637V#1004F#4P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0012,
        '强化猎兵',
        (
            '#0020330638V#5P……真是的。\n',
            '你到底在想什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    PlayBGM(80)
    Sleep(500)

    Fade(500)
    PlaySE(213, 0x00, 0x64)
    ChrSetFlags(0x0012, 0x0002)
    ChrSetChipByIndex(0x0012, 30)
    ChrSetSubChip(0x0012, 0)
    OP_0D()
    Sleep(500)

    ChrSetFlags(0x0013, 0x0020)
    ChrSetFlags(0x0013, 0x0002)
    ChrSetFlags(0x0013, 0x0004)
    ChrSetFlags(0x0013, 0x0040)
    ChrSetFlags(0x0013, 0x0010)
    ChrSetFlags(0x0013, 0x1000)
    ChrSetChipByIndex(0x0013, 30)
    ChrSetSubChip(0x0013, 16)
    ChrSetPos(0x0013, 1500, 600, -48250, 0)

    @scena.Lambda('lambda_39E4')
    def lambda_39E4():
        CameraSetDistance(2800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_39E4)

    OP_99(0x0012, 0x01, 0x06, 1300)
    CreateThread(0x0013, 0x00, 0x00, func_18_50A4)
    OP_99(0x0012, 0x07, 0x09, 1300)
    WaitForThreadExit(0x0013, 0x0000)
    Sleep(1500)

    NpcTalk(
        0x0012,
        '黑发的少年',
        (
            '#0020330639V#1135F#5P已经当上了正游击士，\n',
            '但还是和从前一样冒失啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0012, 0x0002)
    ChrSetChipByIndex(0x0012, 15)
    ChrSetSubChip(0x0012, 0)
    ChrSetDirection(0x0012, 180, 300)
    Sleep(500)

    NpcTalk(
        0x0012,
        '黑发的少年',
        (
            '#0020330640V#1130F#5P在这种时候\n',
            '有必要如此犯险拼命吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330641V#1025F……啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B1B',
    )

    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    Sleep(500)

    Jump('loc_3B3A')

    def _loc_3B1B(): pass

    label('loc_3B1B')

    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    Sleep(500)

    def _loc_3B3A(): pass

    label('loc_3B3A')

    ChrTalk(
        0x0101,
        (
            '#0010330642V#1016F#4P啊哈哈……是约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330643V#1008F唔……不是在做梦吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330644V#1131F#5P真要是做梦的话\n',
            '那可就轻松多了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330645V#1135F……但现在的情况\n',
            '似乎没有那么乐观啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270406V#1004F#4P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0014, 1190, 0, -36000, 180)
    ChrClearFlags(0x0014, 0x0080)

    NpcTalk(
        0x0014,
        '青年的声音',
        (
            '#0140330647V#4P呵呵……\n',
            '你总算现身了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_3C9A')
    def lambda_3C9A():
        CameraMove(2020, 0, -43560, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3C9A)

    @scena.Lambda('lambda_3CB2')
    def lambda_3CB2():
        OP_67(0, 4000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3CB2)

    @scena.Lambda('lambda_3CCA')
    def lambda_3CCA():
        OP_6E(263, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3CCA)

    @scena.Lambda('lambda_3CDA')
    def lambda_3CDA():
        CameraSetDistance(3200, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3CDA)

    @scena.Lambda('lambda_3CEA')
    def lambda_3CEA():
        ChrWalkTo(0x00FE, 1000, 0, -41240, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_3CEA)

    Sleep(500)

    @scena.Lambda('lambda_3D0A')
    def lambda_3D0A():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3D0A)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0014, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0012,
        (
            '#0020330648V#1131F#4P……好久不见，莱维。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330649V你好像已经预料到\n',
            '我会潜入这里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0140330650V#124F#5P从你的能力特点来考虑，\n',
            '这么做并不奇怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330651V#120F不过你究竟是用什么手段潜入的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330652V#1135F#4P在登上这艘船之前，\n',
            '我就已经潜入到一艘侦察艇了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330653V#1131F由于里面没有『执行者』，\n',
            '我的潜入实在是意外的简单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0140330654V#120F#5P……连教授会动用方舟\n',
            '都被你给预料到了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330655V#124F看来你身为『执行者』的直觉\n',
            '已经完全找回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330656V#1131F#4P托你的福。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330657V其实我一直都很担心，\n',
            '怕突然被莱维或别人发觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0140330658V#124F#5P哼，不用谦虚，\n',
            '没有任何人可以识破你的隐形术。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330659V#123F不过，所谓的隐形术，\n',
            '一旦现形就毫无用处了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0014, 0)
    ChrSetChipByIndex(0x0014, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0014,
        (
            '#0140330660V#120F#5P你已经失去了最大的武器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330661V面对我『剑帝』，\n',
            '你有何打算？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330662V#1130F#4P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330663V#1P慢、慢着……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    ChrSetChipByIndex(0x0101, 29)
    ChrSetFlags(0x0101, 0x1000)

    @scena.Lambda('lambda_40D3')
    def lambda_40D3():
        CameraMove(1760, 0, -43630, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_40D3)

    @scena.Lambda('lambda_40EB')
    def lambda_40EB():
        OP_67(0, 5000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_40EB)

    @scena.Lambda('lambda_4103')
    def lambda_4103():
        CameraSetDistance(3300, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4103)

    ChrMoveTo(0x0101, 60, 0, -49450, 5000, 0x00)
    ChrSetChipByIndex(0x0101, 4)
    WaitForThreadExit(0x0101, 0x0003)
    ChrSetSubChip(0x0101, 0)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010330664V#1005F#6P话说在先！\n',
            '我也可以继续战斗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330665V不管你有多强，\n',
            '也别想轻轻松松就把我们两个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330666V#1135F#2P……退下，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330667V#1133F莱维的实力太强了，\n',
            '即使你我联手也无济于事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330668V#1019F#6P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0140330669V#124F#5P你既然明白这一点，\n',
            '为什么还敢贸然现身？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330670V为了救她的话，倒是可以理解，\n',
            '我也并不想指责你太过天真……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330671V#120F但你如果真的这么在意她，\n',
            '当初为何还要从她的面前消失？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330672V#1133F#2P………唔…………！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330673V#1026F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0140330674V#120F#5P要守护就守护到底，\n',
            '要舍弃就别再回头。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330675V一旦作出选择就要贯彻到底。\n',
            '我不是教过你吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330676V#1131F#2P嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330677V在经过教授的改造之后……\n',
            '第一次的训练时，你就这么教导我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0140330678V#124F#5P如果那女孩真的那么重要，\n',
            '那你无论如何也不该离开她。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330679V即使承受着罪恶感的苛责，\n',
            '也要一直待在她的身边。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330680V#121F你之所以没有这么做，\n',
            '只是因为在逃避，在自我欺瞒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330681V#1135F#2P我明白……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330682V#1137F即使莱维不说\n',
            '我也明白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0140330683V#120F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330684V#1026F#6P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330685V#1133F#2P可是……可是……\n',
            '莱维，你自己又是如何呢……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330686V需要偿还代价的…\n',
            '本应只有我一人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330687V但为什么连你也要加入『结社』，\n',
            '变成了如今的『剑帝』呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0012,
        (
            '#0020330688V#1136F#2P为什么你直到现在…\n',
            '还在协助教授那种人……！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0140330689V#124F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330690V#121F我协助教授…\n',
            '同你完全没有关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330691V纯粹只是我自己的意愿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330692V#1136F#2P莱维的意愿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330693V那么说…果然还是\n',
            '为了给卡琳姐……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0140330694V#124F#5P即使复了仇，\n',
            '卡琳也无法再回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330695V#123F所以我……\n',
            '决定向世界发起试炼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330696V这就是我协助教授的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330697V#1134F#2P向世界发起试炼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0140330698V#124F#5P好了……\n',
            '言尽于此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetFlags(0x0014, 0x0002)
    ChrSetSubChip(0x0014, 5)
    ChrSetChipByIndex(0x0014, 18)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0014,
        (
            '#0140330699V#121F#5P你有三条路可以选择。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330700V#124F和那女孩一起投降。\n',
            '或是保护她，死在我的剑下。\n',
            '再来就是扔下她，自己一个人逃跑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330701V#120F怎样──快点做出选择吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330702V#1026F#6P约、约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330703V#1133F#2P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330704V#1135F不好意思，\n',
            '我要选第四条路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0140330705V#126F#5P什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, func_2A_56DC)
    CreateThread(0x0101, 0x02, 0x00, func_2B_574B)
    Sleep(1000)

    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010330706V#1020F#6P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0140330707V#126F#5P这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330708V#1135F#2P……我在导力引擎上\n',
            '稍微做了点手脚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330709V要是置之不理的话，这艘船\n',
            '就会化为海底的藻屑了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010261088V#1005F#6P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrClearFlags(0x0014, 0x0002)
    ChrSetSubChip(0x0014, 0)
    ChrSetChipByIndex(0x0014, 16)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0014,
        (
            '#0140330711V#121F#5P……真有你的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330712V没想到你竟能入侵\n',
            '需要认证的引擎室……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330713V#1131F#2P现在２２个引擎全部\n',
            '都被我做了不同的设置……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330714V如今教授和玲都不在，\n',
            '能解除的就只有莱维了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0140330715V#124F#5P这是你为了阻止我们的计划\n',
            '而留下来的最后一张底牌吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330716V#123F但你却在这个时候\n',
            '就把它亮了出来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330717V你打算逃避、欺瞒\n',
            '到什么时候？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330718V#1133F#2P………这…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0014, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0014,
        (
            '#0140330719V#125F#5P呵呵，下次再见时\n',
            '准备好答案就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330720V#122F我期待着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4DC3')
    def lambda_4DC3():
        CameraMove(1490, 0, -41340, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4DC3)

    ChrWalkTo(0x0014, 1230, 150, -27200, 3000, 0x00)
    ChrSetFlags(0x0014, 0x0080)
    CameraMove(1160, 0, -47700, 2500)
    Sleep(500)

    ChrTalk(
        0x0012,
        (
            '#0020330721V#1133F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    Sleep(500)

    ChrTurnDirection(0x0101, 0x0012, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330722V#1025F#6P那个、约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330723V#1003F我……我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020330724V#1135F#5P……有什么话稍后再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0012,
        (
            '#0020330725V#1131F#5P我们首先要抢到\n',
            '一架逃脱用的飞艇。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330726V从前面的阶梯下去\n',
            '就可以到达停泊飞艇的机库了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330727V#1026F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330728V#1002F嗯……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    ChrSetStatus(ChrTable['约修亚'], 0x00, 75)
    EquipCmd(ChrTable['约修亚'], 0x0000, 0xFF)
    EquipCmd(ChrTable['约修亚'], ItemTable['折叠刀'], 0xFF)
    EquipCmd(ChrTable['约修亚'], ItemTable['真空防护服'], 0xFF)
    EquipCmd(ChrTable['约修亚'], ItemTable['树脂靴'], 0xFF)
    AddCraft(ChrTable['约修亚'], 0x0000)
    OP_37(0x01, 0x7F, 0x02)
    EquipCmd(ChrTable['约修亚'], ItemTable['行动力４'], 0x00)
    EquipCmd(ChrTable['约修亚'], ItemTable['回避４'], 0x01)
    EquipCmd(ChrTable['约修亚'], ItemTable['省ＥＰ４'], 0x02)
    EquipCmd(ChrTable['约修亚'], ItemTable['驱动２'], 0x03)
    EquipCmd(ChrTable['约修亚'], ItemTable['ＥＰ３'], 0x04)
    EquipCmd(ChrTable['约修亚'], ItemTable['精神３'], 0x05)
    EquipCmd(ChrTable['约修亚'], ItemTable['攻击３'], 0x06)
    OP_71(0x0007, 0x0004)
    ChrSetFlags(0x0013, 0x0080)
    CameraMove(1070, 0, -47920, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF7, 0xFF)
    OP_BB(0x01, 0x00, 0x00200033)
    OP_BB(0x01, 0x01, 0x00000001)
    OP_BD()
    ChrSetFlags(0x0012, 0x0080)
    ChrSetPos(0x0000, 1070, 0, -47920, 180)
    ChrSetPos(0x0001, 1070, 0, -47920, 180)
    OP_69(0x0000, 0)
    SetScenaFlags(ScenaFlag(0x0384, 7, 0x1C27))
    OP_28(0x0099, 0x01, 0x0100)
    OP_28(0x0099, 0x01, 0x0200)
    PlayBGM(113)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0x50A4
@scena.Code('func_18_50A4')
def func_18_50A4():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetSubChip(0x0013, 16)
    ChrWalkTo(0x0013, 1970, 0, -49030, 4000, 0x00)
    PlaySE(177, 0x00, 0x64)

    @scena.Lambda('lambda_50CD')
    def lambda_50CD():
        OP_99(0x00FE, 0x11, 0x13, 1300)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_50CD)

    ChrJumpTo(0x0013, 2530, 0, -49650, 600, 1500)
    WaitForThreadExit(0x0013, 0x0001)

    @scena.Lambda('lambda_50F9')
    def lambda_50F9():
        OP_99(0x00FE, 0x14, 0x17, 1300)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_50F9)

    ChrJumpTo(0x0013, 2980, 0, -50110, 300, 1200)
    WaitForThreadExit(0x0013, 0x0001)

    @scena.Lambda('lambda_5125')
    def lambda_5125():
        OP_99(0x00FE, 0x18, 0x19, 1300)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_5125)

    ChrWalkTo(0x0013, 3000, 0, -50300, 500, 0x00)
    WaitForThreadExit(0x0013, 0x0001)

    Return()

# id: 0x0019 offset: 0x5149
@scena.Code('func_19_5149')
def func_19_5149():
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0002)
    ChrClearFlags(0x000D, 0x0001)
    ChrSetSubChip(0x000D, 13)
    ChrSetChipByIndex(0x000D, 0)
    ChrSetPos(0x000D, 4520, 0, -54070, 180)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0002)
    ChrClearFlags(0x000E, 0x0001)
    ChrSetSubChip(0x000E, 13)
    ChrSetChipByIndex(0x000E, 0)
    ChrSetPos(0x000E, -1990, 0, -54000, 180)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0002)
    ChrClearFlags(0x000F, 0x0001)
    ChrSetSubChip(0x000F, 14)
    ChrSetChipByIndex(0x000F, 0)
    ChrSetPos(0x000F, 4380, 0, -49440, 180)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0002)
    ChrClearFlags(0x0010, 0x0001)
    ChrSetSubChip(0x0010, 12)
    ChrSetChipByIndex(0x0010, 0)
    ChrSetPos(0x0010, -1800, 0, -49280, 180)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0002)
    ChrClearFlags(0x0011, 0x0001)
    ChrSetSubChip(0x0011, 6)
    ChrSetChipByIndex(0x0011, 0)
    ChrSetSubChip(0x0011, 5)
    ChrSetPos(0x0011, -1820, 0, -43300, 180)

    Return()

# id: 0x001A offset: 0x5221
@scena.Code('func_1A_5221')
def func_1A_5221():
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 7)
    ChrWalkTo(0x00FE, 3000, 0, -55570, 500, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 7)

    Return()

# id: 0x001B offset: 0x524A
@scena.Code('func_1B_524A')
def func_1B_524A():
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 7)
    ChrWalkTo(0x00FE, -660, 0, -55570, 500, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 7)

    Return()

# id: 0x001C offset: 0x5273
@scena.Code('func_1C_5273')
def func_1C_5273():
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 7)
    ChrWalkTo(0x00FE, 2850, 0, -50940, 500, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 7)

    Return()

# id: 0x001D offset: 0x529C
@scena.Code('func_1D_529C')
def func_1D_529C():
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 7)
    ChrWalkTo(0x00FE, -660, 0, -50940, 500, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 7)

    Return()

# id: 0x001E offset: 0x52C5
@scena.Code('func_1E_52C5')
def func_1E_52C5():
    OP_9E(0x00FE, 15, 0, 300, 3000)
    Sleep(500)

    OP_99(0x00FE, 0x03, 0x00, 1500)
    PlaySE(505, 0x00, 0x64)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 7)

    Return()

# id: 0x001F offset: 0x52F6
@scena.Code('func_1F_52F6')
def func_1F_52F6():
    ChrClearFlags(0x00FE, 0x0002)
    ChrSetDirection(0x00FE, 180, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 9)
    PlaySE(524, 0x00, 0x64)
    OP_99(0x00FE, 0x00, 0x03, 1500)

    @scena.Lambda('lambda_5320')
    def lambda_5320():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -200, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_5320)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetFlags(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetSubChip(0x00FE, 13)
    ChrSetChipByIndex(0x00FE, 10)

    Return()

# id: 0x0020 offset: 0x534F
@scena.Code('func_20_534F')
def func_20_534F():
    ChrClearFlags(0x00FE, 0x0002)
    ChrSetDirection(0x00FE, 180, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 9)
    PlaySE(524, 0x00, 0x64)
    OP_99(0x00FE, 0x00, 0x03, 1500)

    @scena.Lambda('lambda_5379')
    def lambda_5379():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -200, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_5379)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetFlags(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetSubChip(0x00FE, 13)
    ChrSetChipByIndex(0x00FE, 10)

    Return()

# id: 0x0021 offset: 0x53A8
@scena.Code('func_21_53A8')
def func_21_53A8():
    ChrClearFlags(0x00FE, 0x0002)
    ChrSetDirection(0x00FE, 225, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 9)
    PlaySE(524, 0x00, 0x64)
    OP_99(0x00FE, 0x00, 0x03, 1500)

    @scena.Lambda('lambda_53D2')
    def lambda_53D2():
        ChrMoveToRelativeAsync(0x00FE, -300, 0, -250, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_53D2)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetFlags(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetSubChip(0x00FE, 14)
    ChrSetChipByIndex(0x00FE, 10)

    Return()

# id: 0x0022 offset: 0x5401
@scena.Code('func_22_5401')
def func_22_5401():
    ChrClearFlags(0x00FE, 0x0002)
    ChrSetDirection(0x00FE, 135, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 9)
    PlaySE(524, 0x00, 0x64)
    OP_99(0x00FE, 0x00, 0x03, 1500)

    @scena.Lambda('lambda_542B')
    def lambda_542B():
        ChrMoveToRelativeAsync(0x00FE, 200, 0, -200, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_542B)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetFlags(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetSubChip(0x00FE, 12)
    ChrSetChipByIndex(0x00FE, 10)

    Return()

# id: 0x0023 offset: 0x545A
@scena.Code('func_23_545A')
def func_23_545A():
    ChrSetFlags(0x00FE, 0x1000)

    @scena.Lambda('lambda_5465')
    def lambda_5465():
        OP_99(0x00FE, 0x03, 0x08, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_5465)

    @scena.Lambda('lambda_5475')
    def lambda_5475():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_5475)

    ChrJumpTo(0x00FE, 1190, 0, -54870, 100, 2000)

    Return()

# id: 0x0024 offset: 0x5499
@scena.Code('func_24_5499')
def func_24_5499():
    ChrSetFlags(0x00FE, 0x1000)

    @scena.Lambda('lambda_54A4')
    def lambda_54A4():
        OP_99(0x00FE, 0x03, 0x08, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_54A4)

    ChrJumpTo(0x00FE, 2900, 0, -49510, 100, 22000)

    Return()

# id: 0x0025 offset: 0x54C6
@scena.Code('func_25_54C6')
def func_25_54C6():
    PlayEffect(0x04, 0x00, 0x00FE, 0, 0, 0, 0, 0, 0, 1500, 1100, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetSubChip(0x00FE, 5)
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetFlags(0x00FE, 0x0020)
    ChrMoveToRelativeAsync(0x00FE, 1500, 0, 1500, 10000, 0x00)
    OP_9E(0x00FE, 30, 0, 800, 4000)
    ChrClearFlags(0x00FE, 0x0020)

    Return()

# id: 0x0026 offset: 0x5541
@scena.Code('func_26_5541')
def func_26_5541():
    PlayEffect(0x04, 0x01, 0x00FE, 0, 0, 0, 0, 0, 0, 1000, 1200, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetSubChip(0x00FE, 6)
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetFlags(0x00FE, 0x0020)
    ChrMoveToRelativeAsync(0x00FE, 1500, 0, 1500, 10000, 0x00)
    OP_9E(0x00FE, 30, 0, 800, 4000)
    ChrClearFlags(0x00FE, 0x0020)

    Return()

# id: 0x0027 offset: 0x55BC
@scena.Code('func_27_55BC')
def func_27_55BC():
    PlayEffect(0x04, 0x02, 0x00FE, 0, 0, 0, 0, 0, 0, 1000, 1300, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetSubChip(0x00FE, 5)
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetFlags(0x00FE, 0x0020)
    ChrMoveToRelativeAsync(0x00FE, -1500, 0, 1500, 10000, 0x00)
    OP_9E(0x00FE, 30, 0, 800, 4000)
    ChrClearFlags(0x00FE, 0x0020)

    Return()

# id: 0x0028 offset: 0x5637
@scena.Code('func_28_5637')
def func_28_5637():
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetSubChip(0x00FE, 4)
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetFlags(0x00FE, 0x0020)
    ChrMoveToRelativeAsync(0x00FE, -1500, 0, 1500, 10000, 0x00)
    OP_9E(0x00FE, 30, 0, 800, 4000)
    ChrClearFlags(0x00FE, 0x0020)

    Return()

# id: 0x0029 offset: 0x567D
@scena.Code('func_29_567D')
def func_29_567D():
    @scena.Lambda('lambda_5683')
    def lambda_5683():
        OP_99(0x00FE, 0x03, 0x07, 2500)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_5683)

    ChrWalkTo(0x0012, 1070, 0, -47920, 20000, 0x00)
    PlaySE(521, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0011, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x002A offset: 0x56DC
@scena.Code('func_2A_56DC')
def func_2A_56DC():
    OP_7C(200, 0, 2000, 1000)
    Sleep(1000)

    OP_7C(100, 0, 1000, 1000)
    Sleep(1000)

    OP_7C(50, 0, 500, 1000)
    Sleep(1000)

    OP_7C(25, 0, 250, 1000)
    Sleep(1000)

    OP_7C(12, 0, 125, 1000)
    Sleep(1000)

    Return()

# id: 0x002B offset: 0x574B
@scena.Code('func_2B_574B')
def func_2B_574B():
    PlaySE(133, 0x01, 0x64)
    Sleep(4000)

    OP_24(0x0085, 0x5F)
    Sleep(100)

    OP_24(0x0085, 0x5A)
    Sleep(100)

    OP_24(0x0085, 0x55)
    Sleep(100)

    OP_24(0x0085, 0x50)
    Sleep(100)

    OP_24(0x0085, 0x4B)
    Sleep(100)

    OP_24(0x0085, 0x46)
    Sleep(100)

    OP_24(0x0085, 0x41)
    Sleep(100)

    OP_24(0x0085, 0x32)
    Sleep(100)

    OP_24(0x0085, 0x37)
    Sleep(100)

    OP_24(0x0085, 0x32)
    OP_23(0x0085)

    Return()

# id: 0x002C offset: 0x57AE
@scena.Code('func_2C_57AE')
def func_2C_57AE():
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    OP_A1(0x0008, 0x0008)
    OP_71(0x0008, 0x0002)
    OP_72(0x0008, 0x0004)
    OP_71(0x0008, 0x0020)
    OP_6F(0x0008, 800)
    OP_70(0x0008, 900)
    ChrSetPos(0x0008, -43670, -35000, -67540, 0)
    CameraMove(-5510, 0, -14200, 0)
    OP_67(0, 9720, -10000, 0)
    CameraSetDistance(23040, 0)
    OP_6C(161000, 0)
    OP_6E(270, 0)
    ChrSetFlags(0x000D, 0x0008)
    ChrSetFlags(0x000E, 0x0008)
    ChrSetFlags(0x000F, 0x0008)
    ChrSetFlags(0x0010, 0x0008)
    ChrSetFlags(0x0011, 0x0008)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_5852')
    def lambda_5852():
        OP_67(0, 8070, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5852)

    @scena.Lambda('lambda_586A')
    def lambda_586A():
        OP_6E(245, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_586A)

    OP_98(0x00, 0x0008)
    OP_98(0x01, -40080, 45000, 56000)
    OP_98(0x01, -25540, 190000, 203000)
    OP_98(0x02, 0x0008, 60000, 0x06)
    OP_71(0x0008, 0x0004)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C5406._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x002D offset: 0x58BA
@scena.Code('func_2D_58BA')
def func_2D_58BA():
    EventBegin(0x00)
    OP_11(0xFF, 0xFF, 0xFF, 100000, 1000000, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x000D, 0x0008)
    ChrSetFlags(0x000E, 0x0008)
    ChrSetFlags(0x000F, 0x0008)
    ChrSetFlags(0x0010, 0x0008)
    ChrSetFlags(0x0011, 0x0008)
    OP_E7(0x08, 'l_gun', 0x00, 0x00000001)
    OP_E7(0x08, 'r_gun', 0x00, 0x00000001)
    OP_E7(0x08, 'up_gun', 0x00, 0x00000001)
    OP_E7(0x08, 'l_pad', 0x00, 0x00000001)
    OP_E7(0x08, 'l_pad', 0x00, 0x00000001)
    OP_A1(0x0008, 0x0008)
    OP_71(0x0008, 0x0002)
    OP_72(0x0008, 0x0004)
    OP_71(0x0008, 0x0020)
    OP_6F(0x0008, 800)
    OP_70(0x0008, 900)
    ChrSetPos(0x0008, -15000, -70000, -68000, 0)
    OP_D1(0x0008, -20000, 240000, 20000, 0)
    CameraMove(-79860, -8550, -145600, 0)
    OP_67(0, 6280, -10000, 0)
    CameraSetDistance(14000, 0)
    OP_6C(59000, 0)
    OP_6E(649, 0)
    OP_E5(0x08, 0x00, 0x00)
    PlaySE(121, 0x00, 0x64)
    PlaySE(305, 0x01, 0x46)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_59D1')
    def lambda_59D1():
        CameraMove(-39860, -8550, -145600, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_59D1)

    @scena.Lambda('lambda_59E9')
    def lambda_59E9():
        OP_D1(0x00FE, -20000, 220000, 20000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_59E9)

    OP_98(0x00, 0x0008)
    OP_98(0x01, -124000, 30000, -155000)
    OP_98(0x01, -170000, 74000, -225000)

    @scena.Lambda('lambda_5A23')
    def lambda_5A23():
        OP_98(0x02, 0x00FE, 70000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_5A23)

    Sleep(2000)

    @scena.Lambda('lambda_5A38')
    def lambda_5A38():
        OP_D1(0x00FE, -20000, 210000, -20000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_5A38)

    WaitForThreadExit(0x0008, 0x0000)
    FadeOut(2000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C5406._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x002E offset: 0x5A6E
@scena.Code('func_2E_5A6E')
def func_2E_5A6E():
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    CameraMove(-25640, -21130, -27140, 0)
    OP_67(0, 12400, -10000, 0)
    CameraSetDistance(5680, 0)
    OP_6C(143000, 0)
    OP_6E(803, 0)
    OP_A1(0x0008, 0x0000)
    OP_A1(0x0009, 0x0001)
    OP_A1(0x000A, 0x0002)
    ChrSetPos(0x0008, -10470, -35000, -49220, 0)
    ChrSetPos(0x0009, -12870, -35000, -61390, 0)
    ChrSetPos(0x000A, -12070, -35000, -76540, 0)
    ChrSetFlags(0x000D, 0x0008)
    ChrSetFlags(0x000E, 0x0008)
    ChrSetFlags(0x000F, 0x0008)
    ChrSetFlags(0x0010, 0x0008)
    ChrSetFlags(0x0011, 0x0008)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_5B21')
    def lambda_5B21():
        CameraMove(-25950, -21130, -30440, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5B21)

    @scena.Lambda('lambda_5B39')
    def lambda_5B39():
        OP_6C(111000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5B39)

    CreateThread(0x0008, 0x01, 0x00, func_30_5D40)
    Sleep(1000)

    CreateThread(0x0009, 0x01, 0x00, func_32_5E42)
    Sleep(1000)

    CreateThread(0x000A, 0x01, 0x00, func_34_5F58)
    WaitForThreadExit(0x000A, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    NewScene('ED6_DT21/E0610._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x002F offset: 0x5B7F
@scena.Code('func_2F_5B7F')
def func_2F_5B7F():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_11(0xFF, 0xFF, 0xFF, 100000, 1000000, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x000D, 0x0008)
    ChrSetFlags(0x000E, 0x0008)
    ChrSetFlags(0x000F, 0x0008)
    ChrSetFlags(0x0010, 0x0008)
    ChrSetFlags(0x0011, 0x0008)
    CameraMove(-79860, -8550, -145600, 0)
    OP_67(0, 6280, -10000, 0)
    CameraSetDistance(14000, 0)
    OP_6C(59000, 0)
    OP_6E(649, 0)
    OP_E5(0x08, 0x00, 0x00)
    OP_E5(0x09, 0x00, 0x00)
    OP_E5(0x0A, 0x00, 0x00)
    OP_A1(0x0008, 0x0000)
    OP_A1(0x0009, 0x0001)
    OP_A1(0x000A, 0x0002)
    ChrSetPos(0x0008, -15000, -70000, -68000, 0)
    ChrSetPos(0x0009, -15000, -70000, -38000, 0)
    ChrSetPos(0x000A, -15000, -70000, -8000, 0)
    OP_D1(0x0008, 0, 180000, 0, 0)
    OP_D1(0x0009, 0, 180000, 0, 0)
    OP_D1(0x000A, 0, 180000, 0, 0)
    PlaySE(121, 0x00, 0x64)
    PlaySE(305, 0x01, 0x46)
    OP_71(0x0000, 0x0002)
    OP_72(0x0000, 0x0004)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 800)
    OP_70(0x0000, 900)
    OP_71(0x0001, 0x0002)
    OP_72(0x0001, 0x0004)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 900)
    OP_71(0x0002, 0x0002)
    OP_72(0x0002, 0x0004)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)
    Sleep(2000)

    FadeIn(2000, 0)

    @scena.Lambda('lambda_5CF7')
    def lambda_5CF7():
        CameraMove(-39860, -8550, -145600, 10500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5CF7)

    CreateThread(0x0008, 0x01, 0x00, func_31_5DCE)
    CreateThread(0x0009, 0x01, 0x00, func_33_5ED0)
    CreateThread(0x000A, 0x01, 0x00, func_35_5FE6)
    WaitForThreadExit(0x000A, 0x0001)
    FadeOut(2000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    NewScene('ED6_DT21/E0610._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0030 offset: 0x5D40
@scena.Code('func_30_5D40')
def func_30_5D40():
    OP_71(0x0000, 0x0002)
    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0004)
    OP_6F(0x0000, 800)
    ChrMoveTo(0x0008, -38120, -35000, -55220, 25000, 0x00)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 800)
    OP_70(0x0000, 900)
    ChrMoveTo(0x0008, -40120, -35000, -49220, 40000, 0x00)
    OP_98(0x00, 0x0008)
    OP_98(0x01, -40390, -20000, -30220)
    OP_98(0x01, -37390, 630, -8180)
    OP_98(0x01, -30250, 51560, 47710)
    OP_98(0x02, 0x0008, 55000, 0x06)
    OP_71(0x0000, 0x0004)

    Return()

# id: 0x0031 offset: 0x5DCE
@scena.Code('func_31_5DCE')
def func_31_5DCE():
    @scena.Lambda('lambda_5DD4')
    def lambda_5DD4():
        OP_D1(0x00FE, -20000, 220000, 20000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_5DD4)

    OP_98(0x00, 0x00FE)
    OP_98(0x01, -124000, 30000, -155000)
    OP_98(0x01, -170000, 74000, -225000)

    @scena.Lambda('lambda_5E0E')
    def lambda_5E0E():
        OP_98(0x02, 0x00FE, 70000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_5E0E)

    Sleep(2000)

    @scena.Lambda('lambda_5E23')
    def lambda_5E23():
        OP_D1(0x00FE, -20000, 210000, -20000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_5E23)

    WaitForThreadExit(0x00FE, 0x0000)
    OP_71(0x0000, 0x0004)

    Return()

# id: 0x0032 offset: 0x5E42
@scena.Code('func_32_5E42')
def func_32_5E42():
    OP_71(0x0001, 0x0002)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0004)
    OP_6F(0x0001, 800)
    ChrMoveTo(0x0009, -37900, -35000, -67390, 25000, 0x00)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 900)
    ChrMoveTo(0x0009, -40900, -35000, -61390, 25000, 0x00)
    OP_98(0x00, 0x0009)
    OP_98(0x01, -40390, -20000, -30220)
    OP_98(0x01, -37390, 630, -8180)
    OP_98(0x01, -30250, 51560, 47710)
    OP_98(0x02, 0x0009, 55000, 0x06)
    OP_71(0x0001, 0x0004)

    Return()

# id: 0x0033 offset: 0x5ED0
@scena.Code('func_33_5ED0')
def func_33_5ED0():
    ChrMoveTo(0x00FE, -15000, -70000, -68000, 20000, 0x00)

    @scena.Lambda('lambda_5EEA')
    def lambda_5EEA():
        OP_D1(0x00FE, -20000, 220000, 20000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_5EEA)

    OP_98(0x00, 0x00FE)
    OP_98(0x01, -124000, 30000, -155000)
    OP_98(0x01, -170000, 74000, -225000)

    @scena.Lambda('lambda_5F24')
    def lambda_5F24():
        OP_98(0x02, 0x00FE, 70000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_5F24)

    Sleep(2000)

    @scena.Lambda('lambda_5F39')
    def lambda_5F39():
        OP_D1(0x00FE, -20000, 210000, -20000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_5F39)

    WaitForThreadExit(0x00FE, 0x0000)
    OP_71(0x0001, 0x0004)

    Return()

# id: 0x0034 offset: 0x5F58
@scena.Code('func_34_5F58')
def func_34_5F58():
    OP_71(0x0002, 0x0002)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0004)
    OP_6F(0x0002, 800)
    ChrMoveTo(0x000A, -38100, -35000, -82540, 25000, 0x00)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)
    ChrMoveTo(0x000A, -40900, -35000, -76540, 25000, 0x00)
    OP_98(0x00, 0x000A)
    OP_98(0x01, -40390, -20000, -30220)
    OP_98(0x01, -37390, 630, -8180)
    OP_98(0x01, -30250, 51560, 47710)
    OP_98(0x02, 0x000A, 55000, 0x06)
    OP_71(0x0002, 0x0004)

    Return()

# id: 0x0035 offset: 0x5FE6
@scena.Code('func_35_5FE6')
def func_35_5FE6():
    ChrMoveTo(0x00FE, -15000, -70000, -68000, 20000, 0x00)

    @scena.Lambda('lambda_6000')
    def lambda_6000():
        OP_D1(0x00FE, -20000, 220000, 20000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_6000)

    OP_98(0x00, 0x00FE)
    OP_98(0x01, -124000, 30000, -155000)
    OP_98(0x01, -170000, 74000, -225000)

    @scena.Lambda('lambda_603A')
    def lambda_603A():
        OP_98(0x02, 0x00FE, 70000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_603A)

    Sleep(2000)

    @scena.Lambda('lambda_604F')
    def lambda_604F():
        OP_D1(0x00FE, -20000, 210000, -20000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_604F)

    WaitForThreadExit(0x00FE, 0x0000)
    OP_71(0x0002, 0x0004)

    Return()

# id: 0x0036 offset: 0x606E
@scena.Code('func_36_606E')
def func_36_606E():
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
        (0x00000000, 'loc_60E8'),
        (0x00000001, 'loc_60EE'),
        (-1, 'loc_60F4'),
    )

    def _loc_60E8(): pass

    label('loc_60E8')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_60F4')

    def _loc_60EE(): pass

    label('loc_60EE')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_60F4')

    def _loc_60F4(): pass

    label('loc_60F4')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
