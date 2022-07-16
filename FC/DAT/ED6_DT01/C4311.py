import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4311_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4311   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4311.x'
    header.mapIndex       = 1
    header.bgm            = 35
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xADA
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
        ('ED6_DT09/CH11090._CH', 'ED6_DT09/CH11090P._CP'),
        ('ED6_DT09/CH11091._CH', 'ED6_DT09/CH11091P._CP'),
        ('ED6_DT09/CH11100._CH', 'ED6_DT09/CH11100P._CP'),
        ('ED6_DT09/CH11101._CH', 'ED6_DT09/CH11101P._CP'),
        ('ED6_DT09/CH10920._CH', 'ED6_DT09/CH10920P._CP'),
        ('ED6_DT09/CH10921._CH', 'ED6_DT09/CH10921P._CP'),
        ('ED6_DT09/CH10940._CH', 'ED6_DT09/CH10940P._CP'),
        ('ED6_DT09/CH10941._CH', 'ED6_DT09/CH10941P._CP'),
        ('ED6_DT09/CH10950._CH', 'ED6_DT09/CH10950P._CP'),
        ('ED6_DT09/CH10951._CH', 'ED6_DT09/CH10951P._CP'),
        ('ED6_DT09/CH10990._CH', 'ED6_DT09/CH10990P._CP'),
        ('ED6_DT09/CH10991._CH', 'ED6_DT09/CH10991P._CP'),
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
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x14A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -205700,
            z           = 0,
            y           = -291370,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0291,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -110910,
            z           = -4000,
            y           = -303160,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x030D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 6950,
            z           = -4000,
            y           = -349460,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0291,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -32200,
            z           = -8000,
            y           = -171090,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x030D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -58060,
            z           = 0,
            y           = -104990,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x030D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1D6
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -60000,
            y           = -1000,
            z           = -32000,
            range       = 3000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x1F6
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -261269,
            triggerZ            = -4000,
            triggerY            = -297640,
            triggerRange        = 1000,
            actorX              = -261100,
            actorZ              = -4000,
            actorY              = -296970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 17060,
            triggerZ            = -4000,
            triggerY            = -165400,
            triggerRange        = 1000,
            actorX              = 17040,
            actorZ              = -4000,
            actorY              = -164810,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -204610,
            triggerZ            = -4000,
            triggerY            = -359520,
            triggerRange        = 1000,
            actorX              = -204860,
            actorZ              = -4000,
            actorY              = -360270,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 16350,
            triggerZ            = -8000,
            triggerY            = -118970,
            triggerRange        = 1000,
            actorX              = 16920,
            actorZ              = -8000,
            actorY              = -119010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x286
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_294',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0004)

    def _loc_294(): pass

    label('loc_294')

    Return()

# id: 0x0001 offset: 0x295
@scena.Code('Init')
def Init():
    OP_10(0x17, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D2, 7, 0x697)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AA',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2B1')

    def _loc_2AA(): pass

    label('loc_2AA')

    OP_6F(0x0001, 60)

    def _loc_2B1(): pass

    label('loc_2B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D3, 1, 0x699)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C3',
    )

    OP_6F(0x0003, 0)

    Jump('loc_2CA')

    def _loc_2C3(): pass

    label('loc_2C3')

    OP_6F(0x0003, 60)

    def _loc_2CA(): pass

    label('loc_2CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D3, 3, 0x69B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DC',
    )

    OP_6F(0x0002, 0)

    Jump('loc_2E3')

    def _loc_2DC(): pass

    label('loc_2DC')

    OP_6F(0x0002, 60)

    def _loc_2E3(): pass

    label('loc_2E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D3, 4, 0x69C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F5',
    )

    OP_6F(0x0004, 0)

    Jump('loc_2FC')

    def _loc_2F5(): pass

    label('loc_2F5')

    OP_6F(0x0004, 60)

    def _loc_2FC(): pass

    label('loc_2FC')

    Return()

# id: 0x0002 offset: 0x2FD
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_312',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_312(): pass

    label('loc_312')

    Return()

# id: 0x0003 offset: 0x313
@scena.Code('func_03_313')
def func_03_313():
    EventBegin(0x00)
    Fade(1000)
    OP_89(0x0000, -59200, 20000, -32800, 0)
    OP_89(0x0001, -60800, 20000, -32800, 0)
    OP_89(0x0002, -60800, 20000, -31200, 0)
    OP_89(0x0003, -59200, 20000, -31200, 0)
    CameraMove(-60000, 0, -32000, 1500)
    Sleep(100)

    SetMapFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 300)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4302._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x39E
@scena.Code('func_04_39E')
def func_04_39E():
    EventBegin(0x00)
    OP_13(0x00E1)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xE1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0000, 150)
    OP_70(0x0000, 0)
    Yield()
    OP_89(0x0000, -59200, 20000, -32800, 0)
    OP_89(0x0001, -60800, 20000, -32800, 0)
    OP_89(0x0002, -60800, 20000, -31200, 0)
    OP_89(0x0003, -59200, 20000, -31200, 0)
    CameraMove(-60000, 0, -32000, 0)
    OP_73(0x0000)
    Sleep(100)

    Fade(1000)
    OP_89(0x0000, -60000, 0, -35200, 180)
    OP_89(0x0001, -60000, 0, -35200, 180)
    OP_89(0x0002, -60000, 0, -35200, 180)
    OP_89(0x0003, -60000, 0, -35200, 180)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x464
@scena.Code('func_05_464')
def func_05_464():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D2, 7, 0x697)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_612',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D3, 0, 0x698)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_544',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    SetChrPos(0x0008, -261100, -1500, -296970, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_04B3')
    def lambda_04B3():
        ChrMoveTo(0x00FE, -261100, -3000, -296970, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_04B3)

    @scena.Lambda('lambda_04CE')
    def lambda_04CE():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_04CE)

    ClearChrFlags(0x0008, 0x0080)

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
    Battle(0x00000312, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_51F'),
        (0x00000002, 'loc_531'),
        (0x00000001, 'loc_541'),
        (-1, 'loc_544'),
    )

    def _loc_51F(): pass

    label('loc_51F')

    SetScenaFlags(ScenaFlag(0x00D3, 0, 0x698))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_544')

    def _loc_531(): pass

    label('loc_531')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_541(): pass

    label('loc_541')

    OP_B4(0x00)

    Return()

    def _loc_544(): pass

    label('loc_544')

    If(
        (
            (Expr.Eval, "AddItem(0x0029, 1)"),
            Expr.Return,
        ),
        'loc_59A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '合金乌剑',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D2, 7, 0x697))

    Jump('loc_60F')

    def _loc_59A(): pass

    label('loc_59A')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '合金乌剑',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '合金乌剑',
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

    def _loc_60F(): pass

    label('loc_60F')

    Jump('loc_648')

    def _loc_612(): pass

    label('loc_612')

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
    WaitEffect(0x0F, 0x72)
    def _loc_648(): pass

    label('loc_648')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x656
@scena.Code('func_06_656')
def func_06_656():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D3, 1, 0x699)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_80A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D3, 2, 0x69A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_736',
    )

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    SetChrPos(0x0009, 17040, -1500, -164810, 320)
    ChrTurnDirection(0x0009, 0x0000, 0)

    @scena.Lambda('lambda_06A5')
    def lambda_06A5():
        ChrMoveTo(0x00FE, 17040, -3000, -164810, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_06A5)

    @scena.Lambda('lambda_06C0')
    def lambda_06C0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_06C0)

    ClearChrFlags(0x0009, 0x0080)

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
    Battle(0x00000313, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0009, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_711'),
        (0x00000002, 'loc_723'),
        (0x00000001, 'loc_733'),
        (-1, 'loc_736'),
    )

    def _loc_711(): pass

    label('loc_711')

    SetScenaFlags(ScenaFlag(0x00D3, 2, 0x69A))
    OP_6F(0x0003, 60)
    Sleep(500)

    Jump('loc_736')

    def _loc_723(): pass

    label('loc_723')

    OP_6F(0x0003, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_733(): pass

    label('loc_733')

    OP_B4(0x00)

    Return()

    def _loc_736(): pass

    label('loc_736')

    If(
        (
            (Expr.Eval, "AddItem(0x00FE, 1)"),
            Expr.Return,
        ),
        'loc_78E',
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
    SetScenaFlags(ScenaFlag(0x00D3, 1, 0x699))

    Jump('loc_807')

    def _loc_78E(): pass

    label('loc_78E')

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

    def _loc_807(): pass

    label('loc_807')

    Jump('loc_840')

    def _loc_80A(): pass

    label('loc_80A')

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
    WaitEffect(0x0F, 0x73)
    def _loc_840(): pass

    label('loc_840')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x84E
@scena.Code('func_07_84E')
def func_07_84E():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D3, 3, 0x69B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_950',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FF, 1)"),
            Expr.Return,
        ),
        'loc_8CA',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D3, 3, 0x69B))

    Jump('loc_94D')

    def _loc_8CA(): pass

    label('loc_8CA')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
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

    def _loc_94D(): pass

    label('loc_94D')

    Jump('loc_986')

    def _loc_950(): pass

    label('loc_950')

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
    WaitEffect(0x0F, 0x74)
    def _loc_986(): pass

    label('loc_986')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x994
@scena.Code('func_08_994')
def func_08_994():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D3, 4, 0x69C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A84',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F7, 1)"),
            Expr.Return,
        ),
        'loc_A0A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    SetScenaFlags(ScenaFlag(0x00D3, 4, 0x69C))

    Jump('loc_A81')

    def _loc_A0A(): pass

    label('loc_A0A')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_A81(): pass

    label('loc_A81')

    Jump('loc_ABA')

    def _loc_A84(): pass

    label('loc_A84')

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
    WaitEffect(0x0F, 0x75)
    def _loc_ABA(): pass

    label('loc_ABA')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
