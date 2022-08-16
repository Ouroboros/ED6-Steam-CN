import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0702_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0702   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0702.x'
    header.mapIndex       = 1
    header.bgm            = 60
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
        ('ED6_DT29/CH12590._CH', 'ED6_DT29/CH12590P._CP'),
        ('ED6_DT29/CH12591._CH', 'ED6_DT29/CH12591P._CP'),
        ('ED6_DT29/CH12600._CH', 'ED6_DT29/CH12600P._CP'),
        ('ED6_DT29/CH12601._CH', 'ED6_DT29/CH12601P._CP'),
        ('ED6_DT29/CH12610._CH', 'ED6_DT29/CH12610P._CP'),
        ('ED6_DT29/CH12611._CH', 'ED6_DT29/CH12611P._CP'),
        ('ED6_DT29/CH12620._CH', 'ED6_DT29/CH12620P._CP'),
        ('ED6_DT29/CH12621._CH', 'ED6_DT29/CH12621P._CP'),
        ('ED6_DT29/CH12630._CH', 'ED6_DT29/CH12630P._CP'),
        ('ED6_DT29/CH12631._CH', 'ED6_DT29/CH12631P._CP'),
        ('ED6_DT29/CH12640._CH', 'ED6_DT29/CH12640P._CP'),
        ('ED6_DT29/CH12641._CH', 'ED6_DT29/CH12641P._CP'),
        ('ED6_DT29/CH12651._CH', 'ED6_DT29/CH12651P._CP'),
        ('ED6_DT29/CH12651._CH', 'ED6_DT29/CH12651P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 0,
            z                   = 8170,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
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
            x           = -5920,
            z           = 400,
            y           = -46200,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E8,
            word_18     = 0x1FCD,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 6500,
            z           = 400,
            y           = -46310,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E9,
            word_18     = 0x1FCE,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -41540,
            z           = -3600,
            y           = -16470,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EA,
            word_18     = 0x1FCF,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 31300,
            z           = 400,
            y           = -14460,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EA,
            word_18     = 0x1FD0,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 43860,
            z           = 400,
            y           = -14570,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E9,
            word_18     = 0x1FD1,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -5320,
            z           = 4000,
            y           = 40390,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E8,
            word_18     = 0x1FD2,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 5600,
            z           = 4000,
            y           = 51500,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EA,
            word_18     = 0x1FD3,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1FE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1FE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 100,
            triggerZ            = 7170,
            triggerY            = -670,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 7170,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 3600,
            triggerY            = 45490,
            triggerRange        = 1000,
            actorX              = 90,
            actorZ              = 3600,
            actorY              = 46140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x246
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_25E'),
        (0x00000065, 'loc_265'),
        (0x00000066, 'loc_26C'),
        (0x00000067, 'loc_273'),
        (-1, 'loc_27A'),
    )

    def _loc_25E(): pass

    label('loc_25E')

    Event(0, func_05_666)

    Jump('loc_27A')

    def _loc_265(): pass

    label('loc_265')

    Event(0, func_07_7F9)

    Jump('loc_27A')

    def _loc_26C(): pass

    label('loc_26C')

    Event(0, func_09_97C)

    Jump('loc_27A')

    def _loc_273(): pass

    label('loc_273')

    Event(0, func_0B_B08)

    Jump('loc_27A')

    def _loc_27A(): pass

    label('loc_27A')

    Return()

# id: 0x0001 offset: 0x27B
@scena.Code('func_01_27B')
def func_01_27B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E0, 7, 0x1F07)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28D',
    )

    OP_6F(0x0000, 0)

    Jump('loc_294')

    def _loc_28D(): pass

    label('loc_28D')

    OP_6F(0x0000, 60)

    def _loc_294(): pass

    label('loc_294')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E1, 1, 0x1F09)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A6',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2AD')

    def _loc_2A6(): pass

    label('loc_2A6')

    OP_6F(0x0001, 60)

    def _loc_2AD(): pass

    label('loc_2AD')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F9, 5, 0x1FCD)),
            Expr.Return,
        ),
        'loc_2E1',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_2E1(): pass

    label('loc_2E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F9, 6, 0x1FCE)),
            Expr.Return,
        ),
        'loc_2ED',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_2ED(): pass

    label('loc_2ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F9, 7, 0x1FCF)),
            Expr.Return,
        ),
        'loc_2F9',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_2F9(): pass

    label('loc_2F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FA, 0, 0x1FD0)),
            Expr.Return,
        ),
        'loc_305',
    )

    ChrSetFlags(0x000C, 0x0080)

    def _loc_305(): pass

    label('loc_305')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FA, 1, 0x1FD1)),
            Expr.Return,
        ),
        'loc_311',
    )

    ChrSetFlags(0x000D, 0x0080)

    def _loc_311(): pass

    label('loc_311')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FA, 2, 0x1FD2)),
            Expr.Return,
        ),
        'loc_31D',
    )

    ChrSetFlags(0x000E, 0x0080)

    def _loc_31D(): pass

    label('loc_31D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FA, 3, 0x1FD3)),
            Expr.Return,
        ),
        'loc_329',
    )

    ChrSetFlags(0x000F, 0x0080)

    def _loc_329(): pass

    label('loc_329')

    ExecExpressionWithValue(
        0x000B,
        0x24,
        (
            (Expr.PushLong, 0xCF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x24,
        (
            (Expr.PushLong, 0xCF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x24,
        (
            (Expr.PushLong, 0xCF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_1B(0x00, 0x00, 0x0006)
    OP_1B(0x01, 0x00, 0x0008)
    OP_1B(0x02, 0x00, 0x000A)
    OP_1B(0x03, 0x00, 0x000C)

    Return()

# id: 0x0002 offset: 0x35F
@scena.Code('func_02_35F')
def func_02_35F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_374',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_35F')

    def _loc_374(): pass

    label('loc_374')

    Return()

# id: 0x0003 offset: 0x375
@scena.Code('func_03_375')
def func_03_375():
    UnlockAchievement(0x02, 0x0200, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E0, 7, 0x1F07)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E1, 0, 0x1F08)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_459',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_03CC')
    def lambda_03CC():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_03CC)

    @scena.Lambda('lambda_03E7')
    def lambda_03E7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_03E7)

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
    Battle(0x000003F0, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_434'),
        (0x00000002, 'loc_446'),
        (0x00000001, 'loc_456'),
        (-1, 'loc_459'),
    )

    def _loc_434(): pass

    label('loc_434')

    SetScenaFlags(ScenaFlag(0x03E1, 0, 0x1F08))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_459')

    def _loc_446(): pass

    label('loc_446')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_456(): pass

    label('loc_456')

    OP_B4(0x00)

    Return()

    def _loc_459(): pass

    label('loc_459')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['太极服'], 1)"),
            Expr.Return,
        ),
        'loc_4A8',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['太极服']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03E0, 7, 0x1F07))

    Jump('loc_50A')

    def _loc_4A8(): pass

    label('loc_4A8')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['太极服']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['太极服']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_50A(): pass

    label('loc_50A')

    Jump('loc_53C')

    def _loc_50D(): pass

    label('loc_50D')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_53C(): pass

    label('loc_53C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x54A
@scena.Code('func_04_54A')
def func_04_54A():
    UnlockAchievement(0x02, 0x0019, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E1, 1, 0x1F09)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_627',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['Ｓ－药片'], 1)"),
            Expr.Return,
        ),
        'loc_5BE',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03E1, 1, 0x1F09))

    Jump('loc_624')

    def _loc_5BE(): pass

    label('loc_5BE')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_624(): pass

    label('loc_624')

    Jump('loc_658')

    def _loc_627(): pass

    label('loc_627')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_658(): pass

    label('loc_658')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x666
@scena.Code('func_05_666')
def func_05_666():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, 250, -80830, 0)
    OP_6C(225000, 0)
    ChrSetPos(0x0101, -500, 250, -80330, 0)
    ChrSetPos(0x0102, 500, 250, -80330, 0)
    ChrSetPos(0x00F8, -500, 250, -81330, 0)
    ChrSetPos(0x00F9, 500, 250, -81330, 0)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x000D)
    Call(0, 0x000F)
    Fade(500)
    CameraMove(70, -50, -76860, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0000, 70, -50, -76860, 0)
    ChrSetPos(0x0001, 70, -50, -76860, 0)
    ChrSetPos(0x0002, 70, -50, -76860, 0)
    ChrSetPos(0x0003, 70, -50, -76860, 0)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0006 offset: 0x778
@scena.Code('func_06_778')
def func_06_778():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    CameraMove(0, 250, -80830, 0)
    OP_6C(225000, 0)
    ChrSetPos(0x0101, -500, 250, -81330, 180)
    ChrSetPos(0x0102, 500, 250, -81330, 180)
    ChrSetPos(0x00F8, -500, 250, -80330, 180)
    ChrSetPos(0x00F9, 500, 250, -80330, 180)
    OP_0D()
    Call(0, 0x000D)
    Call(0, 0x0010)
    NewScene('ED6_DT21/C0701._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x7F9
@scena.Code('func_07_7F9')
def func_07_7F9():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(50, 3850, 80830, 0)
    ChrSetPos(0x0101, 500, 3850, 80330, 180)
    ChrSetPos(0x0102, -500, 3850, 80330, 180)
    ChrSetPos(0x00F8, 500, 3850, 81330, 180)
    ChrSetPos(0x00F9, -500, 3850, 81330, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x000E)
    Call(0, 0x000F)
    Fade(500)
    CameraMove(20, 3870, 78170, 0)
    ChrSetPos(0x0000, 20, 3870, 78170, 180)
    ChrSetPos(0x0001, 20, 3870, 78170, 180)
    ChrSetPos(0x0002, 20, 3870, 78170, 180)
    ChrSetPos(0x0003, 20, 3870, 78170, 180)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0008 offset: 0x8F9
@scena.Code('func_08_8F9')
def func_08_8F9():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    CameraMove(50, 3850, 80830, 0)
    ChrSetPos(0x0101, -500, 3850, 81330, 0)
    ChrSetPos(0x0102, 500, 3850, 81330, 0)
    ChrSetPos(0x00F8, -500, 3850, 80330, 0)
    ChrSetPos(0x00F9, 500, 3850, 80330, 0)
    OP_0D()
    Call(0, 0x000E)
    Call(0, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    NewScene('ED6_DT21/C0703._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x97C
@scena.Code('func_09_97C')
def func_09_97C():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(15500, 4250, 16000, 0)
    ChrSetPos(0x0101, 16000, 4250, 16500, 90)
    ChrSetPos(0x0102, 16000, 4250, 15500, 90)
    ChrSetPos(0x00F8, 15000, 4250, 16500, 90)
    ChrSetPos(0x00F9, 15000, 4250, 15500, 90)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x000E)
    Call(0, 0x000F)
    Fade(500)
    CameraMove(18560, 4300, 16090, 0)
    ChrSetPos(0x0000, 18560, 4300, 16090, 90)
    ChrSetPos(0x0001, 18560, 4300, 16090, 90)
    ChrSetPos(0x0002, 18560, 4300, 16090, 90)
    ChrSetPos(0x0003, 18560, 4300, 16090, 90)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x12E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000A offset: 0xA85
@scena.Code('func_0A_A85')
def func_0A_A85():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    CameraMove(15500, 4250, 16000, 0)
    ChrSetPos(0x0101, 15000, 4250, 15500, 270)
    ChrSetPos(0x0102, 15000, 4250, 16500, 270)
    ChrSetPos(0x00F8, 16000, 4250, 15500, 270)
    ChrSetPos(0x00F9, 16000, 4250, 16500, 270)
    OP_0D()
    Call(0, 0x000E)
    Call(0, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    NewScene('ED6_DT21/C0703._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0xB08
@scena.Code('func_0B_B08')
def func_0B_B08():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-19500, -7350, -16000, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0101, -20000, -7350, -16500, 270)
    ChrSetPos(0x0102, -20000, -7350, -15500, 270)
    ChrSetPos(0x00F8, -19000, -7350, -16500, 270)
    ChrSetPos(0x00F9, -19000, -7350, -15500, 270)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x000E)
    Call(0, 0x000F)
    Fade(500)
    CameraMove(-22350, -7300, -16129, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0000, -22350, -7300, -16129, 270)
    ChrSetPos(0x0001, -22350, -7300, -16129, 270)
    ChrSetPos(0x0002, -22350, -7300, -16129, 270)
    ChrSetPos(0x0003, -22350, -7300, -16129, 270)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000C offset: 0xC1A
@scena.Code('func_0C_C1A')
def func_0C_C1A():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    CameraMove(-19500, -7350, -16000, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0101, -19000, -7350, -15500, 90)
    ChrSetPos(0x0102, -19000, -7350, -16500, 90)
    ChrSetPos(0x00F8, -20000, -7350, -15500, 90)
    ChrSetPos(0x00F9, -20000, -7350, -16500, 90)
    OP_0D()
    Call(0, 0x000E)
    Call(0, 0x0010)
    NewScene('ED6_DT21/C0703._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0xC9B
@scena.Code('func_0D_C9B')
def func_0D_C9B():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x000E offset: 0xD7A
@scena.Code('func_0E_D7A')
def func_0E_D7A():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x000F offset: 0xE59
@scena.Code('func_0F_E59')
def func_0F_E59():
    @scena.Lambda('lambda_0E5F')
    def lambda_0E5F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0E5F)

    @scena.Lambda('lambda_0E71')
    def lambda_0E71():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0E71)

    @scena.Lambda('lambda_0E83')
    def lambda_0E83():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0E83)

    @scena.Lambda('lambda_0E95')
    def lambda_0E95():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0E95)

    Sleep(2500)

    Return()

# id: 0x0010 offset: 0xEA7
@scena.Code('func_10_EA7')
def func_10_EA7():
    @scena.Lambda('lambda_0EAD')
    def lambda_0EAD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0EAD)

    @scena.Lambda('lambda_0EBF')
    def lambda_0EBF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0EBF)

    @scena.Lambda('lambda_0ED1')
    def lambda_0ED1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0ED1)

    @scena.Lambda('lambda_0EE3')
    def lambda_0EE3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0EE3)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
