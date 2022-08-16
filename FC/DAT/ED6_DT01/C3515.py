import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3515_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3515   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3515.x'
    header.mapIndex       = 1
    header.bgm            = 33
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
        ('ED6_DT09/CH10710._CH', 'ED6_DT09/CH10710P._CP'),
        ('ED6_DT09/CH10711._CH', 'ED6_DT09/CH10711P._CP'),
        ('ED6_DT09/CH10720._CH', 'ED6_DT09/CH10720P._CP'),
        ('ED6_DT09/CH10721._CH', 'ED6_DT09/CH10721P._CP'),
        ('ED6_DT09/CH10730._CH', 'ED6_DT09/CH10730P._CP'),
        ('ED6_DT09/CH10731._CH', 'ED6_DT09/CH10731P._CP'),
        ('ED6_DT09/CH10740._CH', 'ED6_DT09/CH10740P._CP'),
        ('ED6_DT09/CH10741._CH', 'ED6_DT09/CH10741P._CP'),
    ]

# id: 0x10001 offset: 0xEA
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
    )

# id: 0x10002 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -10,
            z           = 0,
            y           = 20060,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01FD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 3930,
            z           = 0,
            y           = 3980,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01FD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 4000,
            z           = 0,
            y           = -4000,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01FD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -3910,
            z           = 0,
            y           = -4030,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01FD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -4030,
            z           = 0,
            y           = 3990,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01FD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -12470,
            z           = 0,
            y           = -90,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 12450,
            z           = 0,
            y           = -40,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01F6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1CE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1CE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 9470,
            triggerZ            = 0,
            triggerY            = 8330,
            triggerRange        = 1000,
            actorX              = 9000,
            actorZ              = 0,
            actorY              = 8800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 17550,
            triggerZ            = 0,
            triggerY            = -12440,
            triggerRange        = 1000,
            actorX              = 17180,
            actorZ              = 0,
            actorY              = -12940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9430,
            triggerZ            = 0,
            triggerY            = -8330,
            triggerRange        = 1000,
            actorX              = -8980,
            actorZ              = 0,
            actorY              = -8790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -12360,
            triggerZ            = 0,
            triggerY            = -17620,
            triggerRange        = 1000,
            actorX              = -12880,
            actorZ              = 0,
            actorY              = -17210,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9380,
            triggerZ            = 0,
            triggerY            = -8320,
            triggerRange        = 1000,
            actorX              = 8970,
            actorZ              = 0,
            actorY              = -8790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9250,
            triggerZ            = 0,
            triggerY            = 8430,
            triggerRange        = 1000,
            actorX              = -8800,
            actorZ              = 0,
            actorY              = 8880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2A6
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x2A7
@scena.Code('func_01_2A7')
def func_01_2A7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B6, 1, 0x5B1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B9',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2C0')

    def _loc_2B9(): pass

    label('loc_2B9')

    OP_6F(0x0000, 60)

    def _loc_2C0(): pass

    label('loc_2C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B6, 3, 0x5B3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D2',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2D9')

    def _loc_2D2(): pass

    label('loc_2D2')

    OP_6F(0x0001, 60)

    def _loc_2D9(): pass

    label('loc_2D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B6, 5, 0x5B5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EB',
    )

    OP_6F(0x0002, 0)

    Jump('loc_2F2')

    def _loc_2EB(): pass

    label('loc_2EB')

    OP_6F(0x0002, 60)

    def _loc_2F2(): pass

    label('loc_2F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B6, 7, 0x5B7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_304',
    )

    OP_6F(0x0003, 0)

    Jump('loc_30B')

    def _loc_304(): pass

    label('loc_304')

    OP_6F(0x0003, 60)

    def _loc_30B(): pass

    label('loc_30B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B7, 1, 0x5B9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31D',
    )

    OP_6F(0x0004, 0)

    Jump('loc_324')

    def _loc_31D(): pass

    label('loc_31D')

    OP_6F(0x0004, 60)

    def _loc_324(): pass

    label('loc_324')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B7, 2, 0x5BA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_336',
    )

    OP_6F(0x0005, 0)

    Jump('loc_33D')

    def _loc_336(): pass

    label('loc_336')

    OP_6F(0x0005, 60)

    def _loc_33D(): pass

    label('loc_33D')

    Return()

# id: 0x0002 offset: 0x33E
@scena.Code('func_02_33E')
def func_02_33E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_353',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_33E')

    def _loc_353(): pass

    label('loc_353')

    Return()

# id: 0x0003 offset: 0x354
@scena.Code('func_03_354')
def func_03_354():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B6, 1, 0x5B1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F8',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B6, 2, 0x5B2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_430',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, 9000, 2000, 8800, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_03A3')
    def lambda_03A3():
        ChrMoveTo(0x00FE, 9000, 1000, 8800, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_03A3)

    @scena.Lambda('lambda_03BE')
    def lambda_03BE():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_03BE)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x000001F8, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_40B'),
        (0x00000002, 'loc_41D'),
        (0x00000001, 'loc_42D'),
        (-1, 'loc_430'),
    )

    def _loc_40B(): pass

    label('loc_40B')

    SetScenaFlags(ScenaFlag(0x00B6, 2, 0x5B2))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_430')

    def _loc_41D(): pass

    label('loc_41D')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_42D(): pass

    label('loc_42D')

    OP_B4(0x00)

    Return()

    def _loc_430(): pass

    label('loc_430')

    If(
        (
            (Expr.Eval, "AddItem(0x0007, 1)"),
            Expr.Return,
        ),
        'loc_484',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '八角棍',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B6, 1, 0x5B1))

    Jump('loc_4F5')

    def _loc_484(): pass

    label('loc_484')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '八角棍',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '八角棍',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_4F5(): pass

    label('loc_4F5')

    Jump('loc_52E')

    def _loc_4F8(): pass

    label('loc_4F8')

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
    WaitEffect(0x0F, 0x35)
    def _loc_52E(): pass

    label('loc_52E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x53C
@scena.Code('func_04_53C')
def func_04_53C():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B6, 3, 0x5B3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6DA',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B6, 4, 0x5B4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_618',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, 17180, 2000, -12940, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_058B')
    def lambda_058B():
        ChrMoveTo(0x00FE, 17180, 1000, -12940, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_058B)

    @scena.Lambda('lambda_05A6')
    def lambda_05A6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_05A6)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x000001F8, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_5F3'),
        (0x00000002, 'loc_605'),
        (0x00000001, 'loc_615'),
        (-1, 'loc_618'),
    )

    def _loc_5F3(): pass

    label('loc_5F3')

    SetScenaFlags(ScenaFlag(0x00B6, 4, 0x5B4))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_618')

    def _loc_605(): pass

    label('loc_605')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_615(): pass

    label('loc_615')

    OP_B4(0x00)

    Return()

    def _loc_618(): pass

    label('loc_618')

    If(
        (
            (Expr.Eval, "AddItem(0x0028, 1)"),
            Expr.Return,
        ),
        'loc_66A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '隐剑',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B6, 3, 0x5B3))

    Jump('loc_6D7')

    def _loc_66A(): pass

    label('loc_66A')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '隐剑',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '隐剑',
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

    def _loc_6D7(): pass

    label('loc_6D7')

    Jump('loc_710')

    def _loc_6DA(): pass

    label('loc_6DA')

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
    WaitEffect(0x0F, 0x36)
    def _loc_710(): pass

    label('loc_710')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x71E
@scena.Code('func_05_71E')
def func_05_71E():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B6, 5, 0x5B5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B6, 6, 0x5B6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7FA',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, -8980, 2000, -8790, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_076D')
    def lambda_076D():
        ChrMoveTo(0x00FE, -8980, 1000, -8790, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_076D)

    @scena.Lambda('lambda_0788')
    def lambda_0788():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0788)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x000001F8, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_7D5'),
        (0x00000002, 'loc_7E7'),
        (0x00000001, 'loc_7F7'),
        (-1, 'loc_7FA'),
    )

    def _loc_7D5(): pass

    label('loc_7D5')

    SetScenaFlags(ScenaFlag(0x00B6, 6, 0x5B6))
    OP_6F(0x0002, 60)
    Sleep(500)

    Jump('loc_7FA')

    def _loc_7E7(): pass

    label('loc_7E7')

    OP_6F(0x0002, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_7F7(): pass

    label('loc_7F7')

    OP_B4(0x00)

    Return()

    def _loc_7FA(): pass

    label('loc_7FA')

    If(
        (
            (Expr.Eval, "AddItem(0x0260, 1)"),
            Expr.Return,
        ),
        'loc_84E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '攻击３',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B6, 5, 0x5B5))

    Jump('loc_8BF')

    def _loc_84E(): pass

    label('loc_84E')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '攻击３',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '攻击３',
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

    def _loc_8BF(): pass

    label('loc_8BF')

    Jump('loc_8F8')

    def _loc_8C2(): pass

    label('loc_8C2')

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
    WaitEffect(0x0F, 0x37)
    def _loc_8F8(): pass

    label('loc_8F8')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x906
@scena.Code('func_06_906')
def func_06_906():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B6, 7, 0x5B7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AAA',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B7, 0, 0x5B8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9E2',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, -12880, 2000, -17210, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_0955')
    def lambda_0955():
        ChrMoveTo(0x00FE, -12880, 1000, -17210, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0955)

    @scena.Lambda('lambda_0970')
    def lambda_0970():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0970)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x000001F8, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_9BD'),
        (0x00000002, 'loc_9CF'),
        (0x00000001, 'loc_9DF'),
        (-1, 'loc_9E2'),
    )

    def _loc_9BD(): pass

    label('loc_9BD')

    SetScenaFlags(ScenaFlag(0x00B7, 0, 0x5B8))
    OP_6F(0x0003, 60)
    Sleep(500)

    Jump('loc_9E2')

    def _loc_9CF(): pass

    label('loc_9CF')

    OP_6F(0x0003, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_9DF(): pass

    label('loc_9DF')

    OP_B4(0x00)

    Return()

    def _loc_9E2(): pass

    label('loc_9E2')

    If(
        (
            (Expr.Eval, "AddItem(0x009C, 1)"),
            Expr.Return,
        ),
        'loc_A36',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '斩马刀',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B6, 7, 0x5B7))

    Jump('loc_AA7')

    def _loc_A36(): pass

    label('loc_A36')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '斩马刀',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '斩马刀',
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

    def _loc_AA7(): pass

    label('loc_AA7')

    Jump('loc_AE0')

    def _loc_AAA(): pass

    label('loc_AAA')

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
    WaitEffect(0x0F, 0x38)
    def _loc_AE0(): pass

    label('loc_AE0')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xAEE
@scena.Code('func_07_AEE')
def func_07_AEE():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B7, 1, 0x5B9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BDE',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F7, 1)"),
            Expr.Return,
        ),
        'loc_B64',
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
    SetScenaFlags(ScenaFlag(0x00B7, 1, 0x5B9))

    Jump('loc_BDB')

    def _loc_B64(): pass

    label('loc_B64')

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
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_BDB(): pass

    label('loc_BDB')

    Jump('loc_C14')

    def _loc_BDE(): pass

    label('loc_BDE')

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
    WaitEffect(0x0F, 0x39)
    def _loc_C14(): pass

    label('loc_C14')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xC22
@scena.Code('func_08_C22')
def func_08_C22():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B7, 2, 0x5BA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D0C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FD, 1)"),
            Expr.Return,
        ),
        'loc_C96',
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
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B7, 2, 0x5BA))

    Jump('loc_D09')

    def _loc_C96(): pass

    label('loc_C96')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
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

    def _loc_D09(): pass

    label('loc_D09')

    Jump('loc_D42')

    def _loc_D0C(): pass

    label('loc_D0C')

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
    WaitEffect(0x0F, 0x3A)
    def _loc_D42(): pass

    label('loc_D42')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
