import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1700_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1700   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1700.x'
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
        ('ED6_DT29/CH12800._CH', 'ED6_DT29/CH12800P._CP'),
        ('ED6_DT29/CH12801._CH', 'ED6_DT29/CH12801P._CP'),
        ('ED6_DT29/CH12810._CH', 'ED6_DT29/CH12810P._CP'),
        ('ED6_DT29/CH12811._CH', 'ED6_DT29/CH12811P._CP'),
        ('ED6_DT29/CH12820._CH', 'ED6_DT29/CH12820P._CP'),
        ('ED6_DT29/CH12821._CH', 'ED6_DT29/CH12821P._CP'),
        ('ED6_DT29/CH12830._CH', 'ED6_DT29/CH12830P._CP'),
        ('ED6_DT29/CH12831._CH', 'ED6_DT29/CH12831P._CP'),
        ('ED6_DT29/CH12840._CH', 'ED6_DT29/CH12840P._CP'),
        ('ED6_DT29/CH12841._CH', 'ED6_DT29/CH12841P._CP'),
        ('ED6_DT29/CH12850._CH', 'ED6_DT29/CH12850P._CP'),
        ('ED6_DT29/CH12851._CH', 'ED6_DT29/CH12851P._CP'),
        ('ED6_DT29/CH12860._CH', 'ED6_DT29/CH12860P._CP'),
        ('ED6_DT29/CH12861._CH', 'ED6_DT29/CH12861P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 0,
            z           = -7650,
            y           = 0,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F9,
            word_18     = 0x1FDE,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x136
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x136
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -7530,
            triggerZ            = 400,
            triggerY            = 83790,
            triggerRange        = 1000,
            actorX              = -7520,
            actorZ              = 400,
            actorY              = 84450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7490,
            triggerZ            = 400,
            triggerY            = 83790,
            triggerRange        = 1000,
            actorX              = 7500,
            actorZ              = 400,
            actorY              = 84450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x17E
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_18E'),
        (0x00000065, 'loc_195'),
        (-1, 'loc_19C'),
    )

    def _loc_18E(): pass

    label('loc_18E')

    Event(0, func_04_446)

    Jump('loc_19C')

    def _loc_195(): pass

    label('loc_195')

    Event(0, func_0E_ACC)

    Jump('loc_19C')

    def _loc_19C(): pass

    label('loc_19C')

    Return()

# id: 0x0001 offset: 0x19D
@scena.Code('func_01_19D')
def func_01_19D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F2, 0, 0x1F90)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AF',
    )

    OP_6F(0x0001, 0)

    Jump('loc_1B6')

    def _loc_1AF(): pass

    label('loc_1AF')

    OP_6F(0x0001, 60)

    def _loc_1B6(): pass

    label('loc_1B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F2, 1, 0x1F91)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C8',
    )

    OP_6F(0x0002, 0)

    Jump('loc_1CF')

    def _loc_1C8(): pass

    label('loc_1C8')

    OP_6F(0x0002, 60)

    def _loc_1CF(): pass

    label('loc_1CF')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')
    OP_1B(0x00, 0x00, 0x0009)
    OP_1B(0x01, 0x00, 0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FB, 6, 0x1FDE)),
            Expr.Return,
        ),
        'loc_20D',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_20D(): pass

    label('loc_20D')

    Return()

# id: 0x0002 offset: 0x20E
@scena.Code('func_02_20E')
def func_02_20E():
    UnlockAchievement(0x02, 0x0067, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F2, 0, 0x1F90)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EB',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅲ'], 1)"),
            Expr.Return,
        ),
        'loc_282',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅲ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03F2, 0, 0x1F90))

    Jump('loc_2E8')

    def _loc_282(): pass

    label('loc_282')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅲ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅲ']),
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

    def _loc_2E8(): pass

    label('loc_2E8')

    Jump('loc_31C')

    def _loc_2EB(): pass

    label('loc_2EB')

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
    def _loc_31C(): pass

    label('loc_31C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x32A
@scena.Code('func_03_32A')
def func_03_32A():
    UnlockAchievement(0x02, 0x0068, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F2, 1, 0x1F91)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_407',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_39E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03F2, 1, 0x1F91))

    Jump('loc_404')

    def _loc_39E(): pass

    label('loc_39E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_404(): pass

    label('loc_404')

    Jump('loc_438')

    def _loc_407(): pass

    label('loc_407')

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
    def _loc_438(): pass

    label('loc_438')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x446
@scena.Code('func_04_446')
def func_04_446():
    EventBegin(0x00)
    CameraMove(680, 750, -84120, 0)
    OP_67(0, 8500, -10000, 0)
    CameraSetDistance(3460, 0)
    OP_6C(140000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 0, 1050, -83970, 0)
    ChrSetPos(0x0102, 0, 1050, -83970, 0)
    ChrSetPos(0x00F8, 0, 1050, -83970, 0)
    ChrSetPos(0x00F9, 0, 1050, -83970, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x00F8, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x00F9, 255, 255, 255, 0, 0)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x00F8, 0x0004)
    ChrSetFlags(0x00F9, 0x0004)
    ChrClearFlags(0x0101, 0x0001)
    ChrClearFlags(0x0102, 0x0001)
    ChrClearFlags(0x00F8, 0x0001)
    ChrClearFlags(0x00F9, 0x0001)
    OP_C8(0x0200, 0x0046, 'C_PLAC23._CH', 0x00, 0x01F4)
    ShowPlaceName('琥珀之塔')
    FadeIn(1000, 0)
    CreateThread(0x0101, 0x00, 0x00, func_05_626)
    Sleep(800)

    @scena.Lambda('lambda_0557')
    def lambda_0557():
        CameraMove(140, 600, -78810, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0557)

    CreateThread(0x0102, 0x00, 0x00, func_06_691)
    Sleep(800)

    CreateThread(0x00F8, 0x00, 0x00, func_07_6FC)
    Sleep(800)

    CreateThread(0x00F9, 0x00, 0x00, func_08_767)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    Fade(500)
    CameraMove(610, 600, -77870, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 610, 600, -77870, 0)
    ChrSetPos(0x0001, 610, 600, -77870, 0)
    ChrSetPos(0x0002, 610, 600, -77870, 0)
    ChrSetPos(0x0003, 610, 600, -77870, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x626
@scena.Code('func_05_626')
def func_05_626():
    @scena.Lambda('lambda_062C')
    def lambda_062C():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_062C)

    @scena.Lambda('lambda_0646')
    def lambda_0646():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0646)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    PlaySE(153, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrClearFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_0671')
    def lambda_0671():
        ChrMoveTo(0x00FE, 610, 600, -77870, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0671)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0006 offset: 0x691
@scena.Code('func_06_691')
def func_06_691():
    @scena.Lambda('lambda_0697')
    def lambda_0697():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0697)

    @scena.Lambda('lambda_06B1')
    def lambda_06B1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_06B1)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    PlaySE(153, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrClearFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_06DC')
    def lambda_06DC():
        ChrMoveTo(0x00FE, -470, 600, -78090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_06DC)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0007 offset: 0x6FC
@scena.Code('func_07_6FC')
def func_07_6FC():
    @scena.Lambda('lambda_0702')
    def lambda_0702():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0702)

    @scena.Lambda('lambda_071C')
    def lambda_071C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_071C)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    PlaySE(153, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrClearFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_0747')
    def lambda_0747():
        ChrMoveTo(0x00FE, 630, 750, -79310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0747)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0008 offset: 0x767
@scena.Code('func_08_767')
def func_08_767():
    @scena.Lambda('lambda_076D')
    def lambda_076D():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_076D)

    @scena.Lambda('lambda_0787')
    def lambda_0787():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0787)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    PlaySE(153, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrClearFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_07B2')
    def lambda_07B2():
        ChrMoveTo(0x00FE, -540, 750, -79320, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_07B2)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0009 offset: 0x7D2
@scena.Code('func_09_7D2')
def func_09_7D2():
    EventBegin(0x00)
    Fade(500)
    MapClearFlags(0x00000001)
    CameraMove(680, 750, -84120, 0)
    OP_67(0, 8500, -10000, 0)
    CameraSetDistance(3460, 0)
    OP_6C(140000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 680, 700, -81310, 180)
    ChrSetPos(0x0102, -330, 700, -81100, 180)
    ChrSetPos(0x00F8, 910, 750, -79600, 180)
    ChrSetPos(0x00F9, -270, 750, -79450, 180)
    CreateThread(0x0101, 0x00, 0x00, func_0A_8B8)
    Sleep(300)

    CreateThread(0x0102, 0x00, 0x00, func_0B_93D)
    Sleep(300)

    CreateThread(0x00F8, 0x00, 0x00, func_0C_9C2)
    Sleep(300)

    CreateThread(0x00F9, 0x00, 0x00, func_0D_A47)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    FadeOut(1000, 0, -1)
    OP_0D()
    MapClearFlags(0x02000000)
    NewScene('ED6_DT21/R1402._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x8B8
@scena.Code('func_0A_8B8')
def func_0A_8B8():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -2000, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_08FD')
    def lambda_08FD():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_08FD)

    @scena.Lambda('lambda_0917')
    def lambda_0917():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0917)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000B offset: 0x93D
@scena.Code('func_0B_93D')
def func_0B_93D():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -2000, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0982')
    def lambda_0982():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0982)

    @scena.Lambda('lambda_099C')
    def lambda_099C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_099C)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000C offset: 0x9C2
@scena.Code('func_0C_9C2')
def func_0C_9C2():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -3000, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0A07')
    def lambda_0A07():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0A07)

    @scena.Lambda('lambda_0A21')
    def lambda_0A21():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0A21)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000D offset: 0xA47
@scena.Code('func_0D_A47')
def func_0D_A47():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -3000, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0A8C')
    def lambda_0A8C():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0A8C)

    @scena.Lambda('lambda_0AA6')
    def lambda_0AA6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0AA6)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000E offset: 0xACC
@scena.Code('func_0E_ACC')
def func_0E_ACC():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, 250, 84500, 0)
    ChrSetPos(0x0101, 500, 250, 84000, 180)
    ChrSetPos(0x0102, -500, 250, 84000, 180)
    ChrSetPos(0x00F8, 500, 250, 85000, 180)
    ChrSetPos(0x00F9, -500, 250, 85000, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0011)
    Call(0, 0x0012)
    Fade(500)
    CameraMove(50, 250, 82510, 0)
    ChrSetPos(0x0000, 50, 250, 82510, 180)
    ChrSetPos(0x0001, 50, 250, 82510, 180)
    ChrSetPos(0x0002, 50, 250, 82510, 180)
    ChrSetPos(0x0003, 50, 250, 82510, 180)
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0xBC7
@scena.Code('func_0F_BC7')
def func_0F_BC7():
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
    CameraMove(0, 250, 84500, 0)
    ChrSetPos(0x0101, -500, 250, 85000, 0)
    ChrSetPos(0x0102, 500, 250, 85000, 0)
    ChrSetPos(0x00F8, -500, 250, 84000, 0)
    ChrSetPos(0x00F9, 500, 250, 84000, 0)
    OP_0D()
    Call(0, 0x0011)
    Call(0, 0x0013)
    NewScene('ED6_DT21/C1701._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0xC3F
@scena.Code('func_10_C3F')
def func_10_C3F():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x0011 offset: 0xD1E
@scena.Code('func_11_D1E')
def func_11_D1E():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x0012 offset: 0xDFD
@scena.Code('func_12_DFD')
def func_12_DFD():
    @scena.Lambda('lambda_0E03')
    def lambda_0E03():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0E03)

    @scena.Lambda('lambda_0E15')
    def lambda_0E15():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0E15)

    @scena.Lambda('lambda_0E27')
    def lambda_0E27():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0E27)

    @scena.Lambda('lambda_0E39')
    def lambda_0E39():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0E39)

    Sleep(2500)

    Return()

# id: 0x0013 offset: 0xE4B
@scena.Code('func_13_E4B')
def func_13_E4B():
    @scena.Lambda('lambda_0E51')
    def lambda_0E51():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0E51)

    @scena.Lambda('lambda_0E63')
    def lambda_0E63():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0E63)

    @scena.Lambda('lambda_0E75')
    def lambda_0E75():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0E75)

    @scena.Lambda('lambda_0E87')
    def lambda_0E87():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0E87)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
