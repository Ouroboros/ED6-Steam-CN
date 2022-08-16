import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4306_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4306   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4306.x'
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
        ('ED6_DT09/CH11090._CH', 'ED6_DT09/CH11090P._CP'),
        ('ED6_DT09/CH11091._CH', 'ED6_DT09/CH11091P._CP'),
        ('ED6_DT09/CH11100._CH', 'ED6_DT09/CH11100P._CP'),
        ('ED6_DT09/CH11101._CH', 'ED6_DT09/CH11101P._CP'),
        ('ED6_DT09/CH10920._CH', 'ED6_DT09/CH10920P._CP'),
        ('ED6_DT09/CH10921._CH', 'ED6_DT09/CH10921P._CP'),
        ('ED6_DT09/CH10940._CH', 'ED6_DT09/CH10940P._CP'),
        ('ED6_DT09/CH10941._CH', 'ED6_DT09/CH10941P._CP'),
        ('ED6_DT09/CH11000._CH', 'ED6_DT09/CH11000P._CP'),
        ('ED6_DT09/CH11001._CH', 'ED6_DT09/CH11001P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -231330,
            z           = -4000,
            y           = 174900,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -312320,
            z           = -4000,
            y           = 177560,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -114720,
            z           = -4000,
            y           = 169370,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -219720,
            z           = 0,
            y           = -69080,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -227710,
            z           = 0,
            y           = 48930,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -200130,
            z           = -4000,
            y           = -68440,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1E2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -239000,
            y           = -5000,
            z           = 42000,
            range       = 3000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = -376000,
            y           = -1000,
            z           = 55000,
            range       = 3000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -168000,
            y           = -5000,
            z           = 40000,
            range       = 3000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10004 offset: 0x242
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -229350,
            triggerZ            = -4000,
            triggerY            = 41150,
            triggerRange        = 1000,
            actorX              = -230090,
            actorZ              = -4000,
            actorY              = 40900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -156290,
            triggerZ            = -8000,
            triggerY            = 39000,
            triggerRange        = 1000,
            actorX              = -157060,
            actorZ              = -8000,
            actorY              = 38850,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -317160,
            triggerZ            = -4000,
            triggerY            = 256510,
            triggerRange        = 1000,
            actorX              = -317010,
            actorZ              = -4000,
            actorY              = 257160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -368260,
            triggerZ            = -4000,
            triggerY            = 188860,
            triggerRange        = 1000,
            actorX              = -368940,
            actorZ              = -4000,
            actorY              = 188980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -82670,
            triggerZ            = -8000,
            triggerY            = -135220,
            triggerRange        = 1000,
            actorX              = -82050,
            actorZ              = -8000,
            actorY              = -135090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2F6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_304',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_04_44D)

    def _loc_304(): pass

    label('loc_304')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_312',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_06_5A2)

    def _loc_312(): pass

    label('loc_312')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_320',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_08_6F3)

    def _loc_320(): pass

    label('loc_320')

    Return()

# id: 0x0001 offset: 0x321
@scena.Code('func_01_321')
def func_01_321():
    OP_10(0x22, 0x00)
    OP_10(0x23, 0x00)
    OP_10(0x24, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 0, 0x6B8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33C',
    )

    OP_6F(0x0003, 0)

    Jump('loc_343')

    def _loc_33C(): pass

    label('loc_33C')

    OP_6F(0x0003, 60)

    def _loc_343(): pass

    label('loc_343')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 2, 0x6BA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_355',
    )

    OP_6F(0x0006, 0)

    Jump('loc_35C')

    def _loc_355(): pass

    label('loc_355')

    OP_6F(0x0006, 60)

    def _loc_35C(): pass

    label('loc_35C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 4, 0x6BC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36E',
    )

    OP_6F(0x0004, 0)

    Jump('loc_375')

    def _loc_36E(): pass

    label('loc_36E')

    OP_6F(0x0004, 60)

    def _loc_375(): pass

    label('loc_375')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 5, 0x6BD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_387',
    )

    OP_6F(0x0005, 0)

    Jump('loc_38E')

    def _loc_387(): pass

    label('loc_387')

    OP_6F(0x0005, 60)

    def _loc_38E(): pass

    label('loc_38E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 6, 0x6BE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A0',
    )

    OP_6F(0x0007, 0)

    Jump('loc_3A7')

    def _loc_3A0(): pass

    label('loc_3A0')

    OP_6F(0x0007, 60)

    def _loc_3A7(): pass

    label('loc_3A7')

    Return()

# id: 0x0002 offset: 0x3A8
@scena.Code('func_02_3A8')
def func_02_3A8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3BD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_3A8')

    def _loc_3BD(): pass

    label('loc_3BD')

    Return()

# id: 0x0003 offset: 0x3BE
@scena.Code('func_03_3BE')
def func_03_3BE():
    EventBegin(0x00)
    Fade(1000)
    OP_89(0x0000, -238200, 20000, 42800, 0)
    OP_89(0x0001, -240000, 20000, 42800, 0)
    OP_89(0x0002, -240000, 20000, 41200, 0)
    OP_89(0x0003, -238200, 20000, 41200, 0)
    CameraMove(-239000, -4000, 42000, 1500)
    Sleep(100)

    OP_B0(0x0000, 0x5A)
    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0000, 1600)
    OP_70(0x0000, 1000)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4305._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x44D
@scena.Code('func_04_44D')
def func_04_44D():
    EventBegin(0x00)
    OP_13(0x00DF)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0000, 1300)
    OP_70(0x0000, 1600)
    Yield()
    OP_89(0x0000, -238200, 20000, 42800, 0)
    OP_89(0x0001, -238200, 20000, 41200, 0)
    OP_89(0x0002, -239800, 20000, 42800, 0)
    OP_89(0x0003, -239800, 20000, 41200, 0)
    CameraMove(-239000, -4000, 42000, 0)
    OP_73(0x0000)
    Sleep(100)

    Fade(1000)
    OP_89(0x0000, -238960, -4000, 45410, 0)
    OP_89(0x0001, -238960, -4000, 45410, 0)
    OP_89(0x0002, -238960, -4000, 45410, 0)
    OP_89(0x0003, -238960, -4000, 45410, 0)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x513
@scena.Code('func_05_513')
def func_05_513():
    EventBegin(0x00)
    Fade(1000)
    OP_89(0x0000, -375200, 20000, 55800, 0)
    OP_89(0x0001, -376800, 20000, 55800, 0)
    OP_89(0x0002, -376800, 20000, 54200, 0)
    OP_89(0x0003, -375200, 20000, 54200, 0)
    CameraMove(-376000, 0, 55000, 1500)
    Sleep(100)

    OP_B0(0x0001, 0x5A)
    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0001, 1600)
    OP_70(0x0001, 1000)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C4305._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x5A2
@scena.Code('func_06_5A2')
def func_06_5A2():
    EventBegin(0x00)
    OP_13(0x00DF)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0001, 1300)
    OP_70(0x0001, 1600)
    Yield()
    OP_89(0x0000, -375200, 20000, 55800, 0)
    OP_89(0x0001, -376800, 20000, 55800, 0)
    OP_89(0x0002, -376800, 20000, 54200, 0)
    OP_89(0x0003, -375200, 20000, 54200, 0)
    CameraMove(-376000, 0, 55000, 0)
    OP_73(0x0001)
    Sleep(100)

    Fade(1000)
    OP_89(0x0000, -372650, 0, 55060, 90)
    OP_89(0x0001, -372650, 0, 55060, 90)
    OP_89(0x0002, -372650, 0, 55060, 90)
    OP_89(0x0003, -372650, 0, 55060, 90)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x668
@scena.Code('func_07_668')
def func_07_668():
    EventBegin(0x00)
    Fade(1000)
    OP_89(0x0000, -167200, 20000, 40800, 0)
    OP_89(0x0001, -168800, 20000, 40800, 0)
    OP_89(0x0002, -168800, 20000, 39200, 0)
    OP_89(0x0003, -167200, 20000, 39200, 0)
    CameraMove(-168000, -4000, 40000, 1500)
    Sleep(100)

    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 300)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C4308._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x6F3
@scena.Code('func_08_6F3')
def func_08_6F3():
    EventBegin(0x00)
    OP_13(0x00DF)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0002, 150)
    OP_70(0x0002, 0)
    Yield()
    OP_89(0x0000, -167200, 20000, 40800, 0)
    OP_89(0x0001, -168800, 20000, 40800, 0)
    OP_89(0x0002, -168800, 20000, 39200, 0)
    OP_89(0x0003, -167200, 20000, 39200, 0)
    CameraMove(-168000, -4000, 40000, 0)
    OP_73(0x0002)
    Sleep(100)

    Fade(1000)
    OP_89(0x0000, -171410, -4000, 39970, 270)
    OP_89(0x0001, -171410, -4000, 39970, 270)
    OP_89(0x0002, -171410, -4000, 39970, 270)
    OP_89(0x0003, -171410, -4000, 39970, 270)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x7B9
@scena.Code('func_09_7B9')
def func_09_7B9():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 0, 0x6B8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_973',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 1, 0x6B9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_899',
    )

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetPos(0x0009, -230090, -1500, 40900, 320)
    ChrTurnDirection(0x0009, 0x0000, 0)

    @scena.Lambda('lambda_0808')
    def lambda_0808():
        ChrMoveTo(0x00FE, -230090, -3000, 40900, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0808)

    @scena.Lambda('lambda_0823')
    def lambda_0823():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0823)

    ChrClearFlags(0x0009, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '机械人形出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x0000030F, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0009, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_874'),
        (0x00000002, 'loc_886'),
        (0x00000001, 'loc_896'),
        (-1, 'loc_899'),
    )

    def _loc_874(): pass

    label('loc_874')

    SetScenaFlags(ScenaFlag(0x00D7, 1, 0x6B9))
    OP_6F(0x0003, 60)
    Sleep(500)

    Jump('loc_899')

    def _loc_886(): pass

    label('loc_886')

    OP_6F(0x0003, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_896(): pass

    label('loc_896')

    OP_B4(0x00)

    Return()

    def _loc_899(): pass

    label('loc_899')

    If(
        (
            (Expr.Eval, "AddItem(0x00BB, 1)"),
            Expr.Return,
        ),
        'loc_8F3',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '高能量粒子炮',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D7, 0, 0x6B8))

    Jump('loc_970')

    def _loc_8F3(): pass

    label('loc_8F3')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '高能量粒子炮',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '高能量粒子炮',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_970(): pass

    label('loc_970')

    Jump('loc_9A9')

    def _loc_973(): pass

    label('loc_973')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x59)
    def _loc_9A9(): pass

    label('loc_9A9')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000A offset: 0x9B7
@scena.Code('func_0A_9B7')
def func_0A_9B7():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 2, 0x6BA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B65',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 3, 0x6BB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A97',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, -157060, -5500, 38850, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_0A06')
    def lambda_0A06():
        ChrMoveTo(0x00FE, -157060, -7000, 38850, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0A06)

    @scena.Lambda('lambda_0A21')
    def lambda_0A21():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0A21)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '机械人形出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000311, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_A72'),
        (0x00000002, 'loc_A84'),
        (0x00000001, 'loc_A94'),
        (-1, 'loc_A97'),
    )

    def _loc_A72(): pass

    label('loc_A72')

    SetScenaFlags(ScenaFlag(0x00D7, 3, 0x6BB))
    OP_6F(0x0006, 60)
    Sleep(500)

    Jump('loc_A97')

    def _loc_A84(): pass

    label('loc_A84')

    OP_6F(0x0006, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_A94(): pass

    label('loc_A94')

    OP_B4(0x00)

    Return()

    def _loc_A97(): pass

    label('loc_A97')

    If(
        (
            (Expr.Eval, "AddItem(0x0119, 1)"),
            Expr.Return,
        ),
        'loc_AED',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '天神之靴',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D7, 2, 0x6BA))

    Jump('loc_B62')

    def _loc_AED(): pass

    label('loc_AED')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '天神之靴',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '天神之靴',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)

    def _loc_B62(): pass

    label('loc_B62')

    Jump('loc_B9B')

    def _loc_B65(): pass

    label('loc_B65')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x5A)
    def _loc_B9B(): pass

    label('loc_B9B')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000B offset: 0xBA9
@scena.Code('func_0B_BA9')
def func_0B_BA9():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 4, 0x6BC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C99',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_C1F',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D7, 4, 0x6BC))

    Jump('loc_C96')

    def _loc_C1F(): pass

    label('loc_C1F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_C96(): pass

    label('loc_C96')

    Jump('loc_CCF')

    def _loc_C99(): pass

    label('loc_C99')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x5B)
    def _loc_CCF(): pass

    label('loc_CCF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000C offset: 0xCDD
@scena.Code('func_0C_CDD')
def func_0C_CDD():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 5, 0x6BD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DCD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_D53',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D7, 5, 0x6BD))

    Jump('loc_DCA')

    def _loc_D53(): pass

    label('loc_D53')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_DCA(): pass

    label('loc_DCA')

    Jump('loc_E03')

    def _loc_DCD(): pass

    label('loc_DCD')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x5C)
    def _loc_E03(): pass

    label('loc_E03')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000D offset: 0xE11
@scena.Code('func_0D_E11')
def func_0D_E11():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 6, 0x6BE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F01',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F7, 1)"),
            Expr.Return,
        ),
        'loc_E87',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D7, 6, 0x6BE))

    Jump('loc_EFE')

    def _loc_E87(): pass

    label('loc_E87')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)

    def _loc_EFE(): pass

    label('loc_EFE')

    Jump('loc_F37')

    def _loc_F01(): pass

    label('loc_F01')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x5D)
    def _loc_F37(): pass

    label('loc_F37')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
