import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4307_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4307   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4307.x'
    header.mapIndex       = 1
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
        ('ED6_DT09/CH10940._CH', 'ED6_DT09/CH10940P._CP'),
        ('ED6_DT09/CH10941._CH', 'ED6_DT09/CH10941P._CP'),
        ('ED6_DT09/CH11000._CH', 'ED6_DT09/CH11000P._CP'),
        ('ED6_DT09/CH11001._CH', 'ED6_DT09/CH11001P._CP'),
        ('ED6_DT09/CH10920._CH', 'ED6_DT09/CH10920P._CP'),
        ('ED6_DT09/CH10921._CH', 'ED6_DT09/CH10921P._CP'),
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
            dword_10            = 4,
            chipIndex           = 4,
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
            dword_10            = 6,
            chipIndex           = 6,
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
            x           = -1320,
            z           = -8000,
            y           = -82980,
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
            x           = 84650,
            z           = -8000,
            y           = 22370,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x172
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -3000,
            y           = -9000,
            z           = 124000,
            range       = 3000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10004 offset: 0x192
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -40770,
            triggerZ            = -8000,
            triggerY            = -12300,
            triggerRange        = 1000,
            actorX              = -41050,
            actorZ              = -8000,
            actorY              = -13100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 15250,
            triggerZ            = -8000,
            triggerY            = -12250,
            triggerRange        = 1000,
            actorX              = 14900,
            actorZ              = -8000,
            actorY              = -12990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 43320,
            triggerZ            = -8000,
            triggerY            = 38970,
            triggerRange        = 1000,
            actorX              = 44000,
            actorZ              = -8000,
            actorY              = 38940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -3160,
            triggerZ            = -8000,
            triggerY            = 131230,
            triggerRange        = 1000,
            actorX              = -3090,
            actorZ              = -8000,
            actorY              = 131910,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x222
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_230',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_04_33A)

    def _loc_230(): pass

    label('loc_230')

    Return()

# id: 0x0001 offset: 0x231
@scena.Code('func_01_231')
def func_01_231():
    OP_10(0x10, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D6, 1, 0x6B1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_246',
    )

    OP_6F(0x0001, 0)

    Jump('loc_24D')

    def _loc_246(): pass

    label('loc_246')

    OP_6F(0x0001, 60)

    def _loc_24D(): pass

    label('loc_24D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D6, 3, 0x6B3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25F',
    )

    OP_6F(0x0002, 0)

    Jump('loc_266')

    def _loc_25F(): pass

    label('loc_25F')

    OP_6F(0x0002, 60)

    def _loc_266(): pass

    label('loc_266')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D6, 5, 0x6B5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_278',
    )

    OP_6F(0x0003, 0)

    Jump('loc_27F')

    def _loc_278(): pass

    label('loc_278')

    OP_6F(0x0003, 60)

    def _loc_27F(): pass

    label('loc_27F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D6, 7, 0x6B7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_291',
    )

    OP_6F(0x0004, 0)

    Jump('loc_298')

    def _loc_291(): pass

    label('loc_291')

    OP_6F(0x0004, 60)

    def _loc_298(): pass

    label('loc_298')

    Return()

# id: 0x0002 offset: 0x299
@scena.Code('func_02_299')
def func_02_299():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2AE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_299')

    def _loc_2AE(): pass

    label('loc_2AE')

    Return()

# id: 0x0003 offset: 0x2AF
@scena.Code('func_03_2AF')
def func_03_2AF():
    EventBegin(0x00)
    Fade(1000)
    OP_89(0x0000, -2200, 20000, 124800, 0)
    OP_89(0x0001, -3800, 20000, 124800, 0)
    OP_89(0x0002, -3800, 20000, 123200, 0)
    OP_89(0x0003, -2200, 20000, 123200, 0)
    CameraMove(-3000, -8000, 124000, 1500)
    Sleep(100)

    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 300)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4308._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x33A
@scena.Code('func_04_33A')
def func_04_33A():
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

    OP_6F(0x0000, 150)
    OP_70(0x0000, 0)
    Yield()
    OP_89(0x0000, -2200, 20000, 124800, 0)
    OP_89(0x0001, -3800, 20000, 124800, 0)
    OP_89(0x0002, -3800, 20000, 123200, 0)
    OP_89(0x0003, -2200, 20000, 123200, 0)
    CameraMove(-3000, -8000, 124000, 0)
    OP_73(0x0000)
    Sleep(100)

    Fade(1000)
    OP_89(0x0000, 480, -8000, 124010, 90)
    OP_89(0x0001, 480, -8000, 124010, 90)
    OP_89(0x0002, 480, -8000, 124010, 90)
    OP_89(0x0003, 480, -8000, 124010, 90)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x400
@scena.Code('func_05_400')
def func_05_400():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D6, 1, 0x6B1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5AE',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D6, 2, 0x6B2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E0',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, -41050, -5500, -13100, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_044F')
    def lambda_044F():
        ChrMoveTo(0x00FE, -41050, -7000, -13100, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_044F)

    @scena.Lambda('lambda_046A')
    def lambda_046A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_046A)

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
        (0x00000000, 'loc_4BB'),
        (0x00000002, 'loc_4CD'),
        (0x00000001, 'loc_4DD'),
        (-1, 'loc_4E0'),
    )

    def _loc_4BB(): pass

    label('loc_4BB')

    SetScenaFlags(ScenaFlag(0x00D6, 2, 0x6B2))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_4E0')

    def _loc_4CD(): pass

    label('loc_4CD')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_4DD(): pass

    label('loc_4DD')

    OP_B4(0x00)

    Return()

    def _loc_4E0(): pass

    label('loc_4E0')

    If(
        (
            (Expr.Eval, "AddItem(0x011A, 1)"),
            Expr.Return,
        ),
        'loc_536',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '风神之靴',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D6, 1, 0x6B1))

    Jump('loc_5AB')

    def _loc_536(): pass

    label('loc_536')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '风神之靴',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '风神之靴',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_5AB(): pass

    label('loc_5AB')

    Jump('loc_5E4')

    def _loc_5AE(): pass

    label('loc_5AE')

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
    WaitEffect(0x0F, 0x5E)
    def _loc_5E4(): pass

    label('loc_5E4')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x5F2
@scena.Code('func_06_5F2')
def func_06_5F2():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D6, 3, 0x6B3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_79A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D6, 4, 0x6B4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6D2',
    )

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetPos(0x0009, 14900, -5500, -12990, 320)
    ChrTurnDirection(0x0009, 0x0000, 0)

    @scena.Lambda('lambda_0641')
    def lambda_0641():
        ChrMoveTo(0x00FE, 14900, -7000, -12990, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0641)

    @scena.Lambda('lambda_065C')
    def lambda_065C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_065C)

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
        (0x00000000, 'loc_6AD'),
        (0x00000002, 'loc_6BF'),
        (0x00000001, 'loc_6CF'),
        (-1, 'loc_6D2'),
    )

    def _loc_6AD(): pass

    label('loc_6AD')

    SetScenaFlags(ScenaFlag(0x00D6, 4, 0x6B4))
    OP_6F(0x0002, 60)
    Sleep(500)

    Jump('loc_6D2')

    def _loc_6BF(): pass

    label('loc_6BF')

    OP_6F(0x0002, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_6CF(): pass

    label('loc_6CF')

    OP_B4(0x00)

    Return()

    def _loc_6D2(): pass

    label('loc_6D2')

    If(
        (
            (Expr.Eval, "AddItem(0x0080, 1)"),
            Expr.Return,
        ),
        'loc_726',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '水晶剑',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D6, 3, 0x6B3))

    Jump('loc_797')

    def _loc_726(): pass

    label('loc_726')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '水晶剑',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '水晶剑',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_797(): pass

    label('loc_797')

    Jump('loc_7D0')

    def _loc_79A(): pass

    label('loc_79A')

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
    WaitEffect(0x0F, 0x5F)
    def _loc_7D0(): pass

    label('loc_7D0')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x7DE
@scena.Code('func_07_7DE')
def func_07_7DE():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D6, 5, 0x6B5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_992',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D6, 6, 0x6B6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8BE',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, 44000, -5500, 38940, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_082D')
    def lambda_082D():
        ChrMoveTo(0x00FE, 44000, -7000, 38940, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_082D)

    @scena.Lambda('lambda_0848')
    def lambda_0848():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0848)

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
        (0x00000000, 'loc_899'),
        (0x00000002, 'loc_8AB'),
        (0x00000001, 'loc_8BB'),
        (-1, 'loc_8BE'),
    )

    def _loc_899(): pass

    label('loc_899')

    SetScenaFlags(ScenaFlag(0x00D6, 6, 0x6B6))
    OP_6F(0x0003, 60)
    Sleep(500)

    Jump('loc_8BE')

    def _loc_8AB(): pass

    label('loc_8AB')

    OP_6F(0x0003, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_8BB(): pass

    label('loc_8BB')

    OP_B4(0x00)

    Return()

    def _loc_8BE(): pass

    label('loc_8BE')

    If(
        (
            (Expr.Eval, "AddItem(0x00FE, 1)"),
            Expr.Return,
        ),
        'loc_916',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '女武神战甲',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D6, 5, 0x6B5))

    Jump('loc_98F')

    def _loc_916(): pass

    label('loc_916')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '女武神战甲',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '女武神战甲',
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

    def _loc_98F(): pass

    label('loc_98F')

    Jump('loc_9C8')

    def _loc_992(): pass

    label('loc_992')

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
    WaitEffect(0x0F, 0x60)
    def _loc_9C8(): pass

    label('loc_9C8')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x9D6
@scena.Code('func_08_9D6')
def func_08_9D6():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D6, 7, 0x6B7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AC6',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_A4C',
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
    SetScenaFlags(ScenaFlag(0x00D6, 7, 0x6B7))

    Jump('loc_AC3')

    def _loc_A4C(): pass

    label('loc_A4C')

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

    def _loc_AC3(): pass

    label('loc_AC3')

    Jump('loc_AFC')

    def _loc_AC6(): pass

    label('loc_AC6')

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
    WaitEffect(0x0F, 0x61)
    def _loc_AFC(): pass

    label('loc_AFC')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
