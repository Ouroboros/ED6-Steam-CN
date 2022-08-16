import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3301   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3301.x'
    header.mapIndex       = 1
    header.bgm            = 32
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
        ('ED6_DT09/CH10630._CH', 'ED6_DT09/CH10630P._CP'),
        ('ED6_DT09/CH10631._CH', 'ED6_DT09/CH10631P._CP'),
        ('ED6_DT09/CH10640._CH', 'ED6_DT09/CH10640P._CP'),
        ('ED6_DT09/CH10641._CH', 'ED6_DT09/CH10641P._CP'),
        ('ED6_DT09/CH10650._CH', 'ED6_DT09/CH10650P._CP'),
        ('ED6_DT09/CH10651._CH', 'ED6_DT09/CH10651P._CP'),
        ('ED6_DT09/CH10660._CH', 'ED6_DT09/CH10660P._CP'),
        ('ED6_DT09/CH10661._CH', 'ED6_DT09/CH10661P._CP'),
        ('ED6_DT09/CH10670._CH', 'ED6_DT09/CH10670P._CP'),
        ('ED6_DT09/CH10671._CH', 'ED6_DT09/CH10671P._CP'),
        ('ED6_DT09/CH10680._CH', 'ED6_DT09/CH10680P._CP'),
        ('ED6_DT09/CH10681._CH', 'ED6_DT09/CH10681P._CP'),
        ('ED6_DT09/CH10690._CH', 'ED6_DT09/CH10690P._CP'),
        ('ED6_DT09/CH10691._CH', 'ED6_DT09/CH10691P._CP'),
    ]

# id: 0x10001 offset: 0x11A
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
            dword_10            = 10,
            chipIndex           = 10,
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
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x15A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 151480,
            z           = 10,
            y           = -36090,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E9,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 173520,
            z           = -30,
            y           = -9860,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01EB,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 145980,
            z           = 0,
            y           = -16110,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01ED,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 133740,
            z           = -10,
            y           = -17360,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01EF,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 100000,
            z           = 40,
            y           = -11970,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 103250,
            z           = 60,
            y           = -23320,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 86210,
            z           = -10,
            y           = -27450,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 68170,
            z           = 20,
            y           = -25410,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01EA,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x23A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x23A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 158010,
            triggerZ            = 30,
            triggerY            = -64629,
            triggerRange        = 1000,
            actorX              = 157660,
            actorZ              = 1530,
            actorY              = -65230,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 140470,
            triggerZ            = -30,
            triggerY            = -11410,
            triggerRange        = 1000,
            actorX              = 140500,
            actorZ              = 1470,
            actorY              = -10700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 90610,
            triggerZ            = 50,
            triggerY            = -19930,
            triggerRange        = 1000,
            actorX              = 91210,
            actorZ              = 1550,
            actorY              = -19850,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 97500,
            triggerZ            = -20,
            triggerY            = -18130,
            triggerRange        = 1000,
            actorX              = 96830,
            actorZ              = 1480,
            actorY              = -18060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2CA
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x2CB
@scena.Code('func_01_2CB')
def func_01_2CB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B8, 1, 0x5C1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DD',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2E4')

    def _loc_2DD(): pass

    label('loc_2DD')

    OP_6F(0x0000, 60)

    def _loc_2E4(): pass

    label('loc_2E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B8, 2, 0x5C2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F6',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2FD')

    def _loc_2F6(): pass

    label('loc_2F6')

    OP_6F(0x0001, 60)

    def _loc_2FD(): pass

    label('loc_2FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B8, 3, 0x5C3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30F',
    )

    OP_6F(0x0002, 0)

    Jump('loc_316')

    def _loc_30F(): pass

    label('loc_30F')

    OP_6F(0x0002, 60)

    def _loc_316(): pass

    label('loc_316')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B8, 4, 0x5C4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_328',
    )

    OP_6F(0x0003, 0)

    Jump('loc_32F')

    def _loc_328(): pass

    label('loc_328')

    OP_6F(0x0003, 60)

    def _loc_32F(): pass

    label('loc_32F')

    PlaySE(461, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x335
@scena.Code('func_02_335')
def func_02_335():
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

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_3ED')

    def _loc_35A(): pass

    label('loc_35A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_373',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_3ED')

    def _loc_373(): pass

    label('loc_373')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_38C',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_3ED')

    def _loc_38C(): pass

    label('loc_38C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A5',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_3ED')

    def _loc_3A5(): pass

    label('loc_3A5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BE',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_3ED')

    def _loc_3BE(): pass

    label('loc_3BE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D7',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_3ED')

    def _loc_3D7(): pass

    label('loc_3D7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3ED',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    def _loc_3ED(): pass

    label('loc_3ED')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_402',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_3ED')

    def _loc_402(): pass

    label('loc_402')

    Return()

# id: 0x0003 offset: 0x403
@scena.Code('func_03_403')
def func_03_403():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B8, 1, 0x5C1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F3',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_479',
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
    SetScenaFlags(ScenaFlag(0x00B8, 1, 0x5C1))

    Jump('loc_4F0')

    def _loc_479(): pass

    label('loc_479')

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
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_4F0(): pass

    label('loc_4F0')

    Jump('loc_529')

    def _loc_4F3(): pass

    label('loc_4F3')

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
    WaitEffect(0x0F, 0x26)
    def _loc_529(): pass

    label('loc_529')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x537
@scena.Code('func_04_537')
def func_04_537():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B8, 2, 0x5C2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6DB',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B8, 7, 0x5C7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_613',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, 140500, 2970, -10700, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_0586')
    def lambda_0586():
        ChrMoveTo(0x00FE, 140500, 1470, -10700, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0586)

    @scena.Lambda('lambda_05A1')
    def lambda_05A1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_05A1)

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
    Battle(0x000001F2, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_5EE'),
        (0x00000002, 'loc_600'),
        (0x00000001, 'loc_610'),
        (-1, 'loc_613'),
    )

    def _loc_5EE(): pass

    label('loc_5EE')

    SetScenaFlags(ScenaFlag(0x00B8, 7, 0x5C7))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_613')

    def _loc_600(): pass

    label('loc_600')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_610(): pass

    label('loc_610')

    OP_B4(0x00)

    Return()

    def _loc_613(): pass

    label('loc_613')

    If(
        (
            (Expr.Eval, "AddItem(0x025D, 1)"),
            Expr.Return,
        ),
        'loc_667',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ３',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B8, 2, 0x5C2))

    Jump('loc_6D8')

    def _loc_667(): pass

    label('loc_667')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ３',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ３',
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

    def _loc_6D8(): pass

    label('loc_6D8')

    Jump('loc_711')

    def _loc_6DB(): pass

    label('loc_6DB')

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
    WaitEffect(0x0F, 0x27)
    def _loc_711(): pass

    label('loc_711')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x71F
@scena.Code('func_05_71F')
def func_05_71F():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B8, 3, 0x5C3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8CF',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B9, 0, 0x5C8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7FB',
    )

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetPos(0x0009, 91210, 3050, -19850, 320)
    ChrTurnDirection(0x0009, 0x0000, 0)

    @scena.Lambda('lambda_076E')
    def lambda_076E():
        ChrMoveTo(0x00FE, 91210, 1550, -19850, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_076E)

    @scena.Lambda('lambda_0789')
    def lambda_0789():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0789)

    ChrClearFlags(0x0009, 0x0080)

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
    Battle(0x000001F2, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0009, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_7D6'),
        (0x00000002, 'loc_7E8'),
        (0x00000001, 'loc_7F8'),
        (-1, 'loc_7FB'),
    )

    def _loc_7D6(): pass

    label('loc_7D6')

    SetScenaFlags(ScenaFlag(0x00B9, 0, 0x5C8))
    OP_6F(0x0002, 60)
    Sleep(500)

    Jump('loc_7FB')

    def _loc_7E8(): pass

    label('loc_7E8')

    OP_6F(0x0002, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_7F8(): pass

    label('loc_7F8')

    OP_B4(0x00)

    Return()

    def _loc_7FB(): pass

    label('loc_7FB')

    If(
        (
            (Expr.Eval, "AddItem(0x00B9, 1)"),
            Expr.Return,
        ),
        'loc_853',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            'Ｇ－冲击炮',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B8, 3, 0x5C3))

    Jump('loc_8CC')

    def _loc_853(): pass

    label('loc_853')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            'Ｇ－冲击炮',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            'Ｇ－冲击炮',
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

    def _loc_8CC(): pass

    label('loc_8CC')

    Jump('loc_905')

    def _loc_8CF(): pass

    label('loc_8CF')

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
    WaitEffect(0x0F, 0x28)
    def _loc_905(): pass

    label('loc_905')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x913
@scena.Code('func_06_913')
def func_06_913():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B8, 4, 0x5C4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A03',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_989',
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
    SetScenaFlags(ScenaFlag(0x00B8, 4, 0x5C4))

    Jump('loc_A00')

    def _loc_989(): pass

    label('loc_989')

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
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_A00(): pass

    label('loc_A00')

    Jump('loc_A39')

    def _loc_A03(): pass

    label('loc_A03')

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
    WaitEffect(0x0F, 0x29)
    def _loc_A39(): pass

    label('loc_A39')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
