import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R0302_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0302_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'rolent'
    header.mapModel       = 'R0302.x'
    header.mapIndex       = 21
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10000 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_453',
    )

    MapSetFlags(0x08000000)
    EventBegin(0x01)

    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_1A0',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_138',
    )

    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#0020150570V#014F艾丝蒂尔，\n',
            '那边是玛鲁加矿山啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150571V#014F我们先去佛莱迪先生那里汇报一下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 0)

    ChrTalk(
        0x0101,
        (
            '#0010150572V#000F啊，说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19D')

    def _loc_138(): pass

    label('loc_138')

    ChrTalk(
        0x0102,
        (
            '#0020150573V#010F这边是玛鲁加矿山啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150574V#010F还是先回佛莱迪先生那里汇报一下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19D(): pass

    label('loc_19D')

    Jump('loc_430')

    def _loc_1A0(): pass

    label('loc_1A0')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#0020150570V#014F艾丝蒂尔，\n',
            '那边是玛鲁加矿山啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150576V#014F我觉得还是应该先去西边的米尔西街道\n',
            '把导力灯的更换工作做完比较好吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150577V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150578V#018F难道……你已经忘了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010150579V#008F真、真讨厌，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150580V我怎么可能把委托给忘了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150581V#017F……这样就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AF')

    def _loc_32E(): pass

    label('loc_32E')

    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#0020150582V#014F这边是玛鲁加矿山。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150583V#014F还是应该先去西边的米尔西街道\n',
            '把导力灯的更换工作做完比较好。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AF(): pass

    label('loc_3AF')

    Jump('loc_430')

    def _loc_3B2(): pass

    label('loc_3B2')

    ChrTalk(
        0x0102,
        (
            '#0020150573V#010F这边是玛鲁加矿山啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150585V#010F还是应该先去西边的米尔西街道\n',
            '把导力灯的更换工作做完比较好。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_430(): pass

    label('loc_430')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapClearFlags(0x08000000)

    Jump('loc_453')

    def _loc_453(): pass

    label('loc_453')

    Return()

# id: 0x0001 offset: 0x454
@scena.Code('func_01_454')
def func_01_454():
    MapSetFlags(0x08000000)
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -113140, 5930, 66530, 208)
    ChrSetPos(0x0102, -113990, 5950, 67470, 179)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4B2',
    )

    ChrSetPos(0x0002, -112370, 5890, 67560, 236)
    ChrSetPos(0x0003, -112920, 5990, 68310, 224)

    def _loc_4B2(): pass

    label('loc_4B2')

    CameraMove(-112920, 5990, 68310, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010150179V#004F啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#0020150180V#014F怎么了？\n',
            '突然叫那么大声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150181V#502F哼哼哼哼，找到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150182V#001F真有成就感呢～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0384, 1)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '荧光菇',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrTurnDirection(0x0102, 0x0101, 400)
    LoadEffect(0x00, 'map\\\\evsepith.eff')
    PlayEffect(0x00, 0x00, 0x0101, 0, 1000, 250, 0, 0, 0, 300, 300, 300, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(
        0x0102,
        (
            '#0020150183V#014F啊，这个蘑菇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150184V#508F怎么样？就是它没错了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150185V生长在这样的地方，\n',
            '还依稀发出淡绿色的光～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150186V#001F肯定就是刚才\n',
            '那个什么大叔说的『荧光菇』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150187V#017F委托人叫奥维德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150188V#000F啊，对，奥维德先生。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150189V#000F虽然感觉有点怪怪的，\n',
            '不过还真是漂亮的蘑菇呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150190V#000F和七耀石一样的光芒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_829',
    )

    ChrTurnDirection(0x0110, 0x0101, 400)

    ChrTalk(
        0x0110,
        (
            '#0280150191V#151F嗯嗯～真的呢～\n',
            '看起来就是那种光呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_829(): pass

    label('loc_829')

    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020150192V#014F……七耀石？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150193V#501F嗯？\n',
            '怎么了，约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150194V#012F也许是我有些多虑了，艾丝蒂尔，\n',
            '快把那个蘑菇放进包里去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150195V#004F……啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9A9',
    )

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrSetDirection(0x0102, 180, 400)
    OP_62(0x010F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0110, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0997')
    def lambda_0997():
        ChrSetDirection(0x010F, 180, 400)

        ExitThread()

    DispatchAsync(0x010F, 0x0001, lambda_0997)

    ChrSetDirection(0x0110, 180, 400)

    Jump('loc_9C7')

    def _loc_9A9(): pass

    label('loc_9A9')

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrSetDirection(0x0102, 180, 400)

    def _loc_9C7(): pass

    label('loc_9C7')

    Sleep(400)

    Fade(1000)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, -113010, 5920, 53930, 130)
    ChrSetPos(0x0009, -113010, 5920, 53930, 130)
    ChrSetPos(0x000A, -113010, 5920, 53930, 130)
    ChrSetChipByIndex(0x0008, 1)
    ChrSetChipByIndex(0x0009, 1)
    ChrSetChipByIndex(0x000A, 1)
    CameraSetDistance(3300, 0)
    CameraMove(-115560, 6020, 58870, 0)
    OP_6C(270000, 0)
    ChrSetDirection(0x0101, 225, 0)
    ChrSetDirection(0x0102, 225, 0)
    StopEffect(0x00, 0x00)
    OP_84(0x00)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A74',
    )

    ChrSetDirection(0x0002, 225, 0)
    ChrSetDirection(0x0003, 225, 0)

    def _loc_A74(): pass

    label('loc_A74')

    @scena.Lambda('lambda_0A7A')
    def lambda_0A7A():
        CameraMove(-114970, 6000, 64120, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0A7A)

    @scena.Lambda('lambda_0A92')
    def lambda_0A92():
        OP_6C(315000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0A92)

    OP_0D()

    @scena.Lambda('lambda_0AA3')
    def lambda_0AA3():
        OP_97(0x0008, -111730, 61810, 75000, 5000, 0x0000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0AA3)

    @scena.Lambda('lambda_0ABF')
    def lambda_0ABF():
        ChrTurnDirection(0x0008, 0x0101, 0)
        Yield()

        Jump('lambda_0ABF')

    DispatchAsync2(0x0008, 0x0002, lambda_0ABF)

    Sleep(400)

    @scena.Lambda('lambda_0AD5')
    def lambda_0AD5():
        OP_97(0x0009, -111730, 61810, 65000, 5000, 0x0000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0AD5)

    @scena.Lambda('lambda_0AF1')
    def lambda_0AF1():
        ChrTurnDirection(0x0009, 0x0101, 0)
        Yield()

        Jump('lambda_0AF1')

    DispatchAsync2(0x0009, 0x0002, lambda_0AF1)

    Sleep(400)

    @scena.Lambda('lambda_0B07')
    def lambda_0B07():
        OP_97(0x000A, -111730, 61810, 55000, 5000, 0x0000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0B07)

    @scena.Lambda('lambda_0B23')
    def lambda_0B23():
        ChrTurnDirection(0x000A, 0x0101, 0)
        Yield()

        Jump('lambda_0B23')

    DispatchAsync2(0x000A, 0x0002, lambda_0B23)

    WaitForThreadExit(0x000A, 0x0001)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    ChrSetChipByIndex(0x000A, 0)
    WaitForThreadExit(0x0008, 0x0001)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    ChrSetChipByIndex(0x0008, 0)
    Sleep(100)

    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    ChrSetChipByIndex(0x0009, 0)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020150196V#012F果然不出所料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150197V#004F难道是这个蘑菇引来的？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0102, 3)
    ChrTurnDirection(0x0102, 0x0008, 0)

    ChrTalk(
        0x0102,
        (
            '#0020150198V#016F艾丝蒂尔，迎战！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 2)
    ChrTurnDirection(0x0101, 0x0008, 0)

    @scena.Lambda('lambda_0BFF')
    def lambda_0BFF():
        ChrTurnDirection(0x0101, 0x0008, 0)
        Yield()

        Jump('lambda_0BFF')

    DispatchAsync2(0x0101, 0x0001, lambda_0BFF)

    @scena.Lambda('lambda_0C10')
    def lambda_0C10():
        ChrTurnDirection(0x0102, 0x0008, 0)
        Yield()

        Jump('lambda_0C10')

    DispatchAsync2(0x0102, 0x0001, lambda_0C10)

    TerminateThread(0x000A, 0x00)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x0008, 0x00)

    @scena.Lambda('lambda_0C2D')
    def lambda_0C2D():
        CameraMove(-113290, 5960, 66180, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0C2D)

    @scena.Lambda('lambda_0C45')
    def lambda_0C45():
        CameraSetDistance(2800, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0C45)

    ChrSetChipByIndex(0x0008, 1)

    @scena.Lambda('lambda_0C5A')
    def lambda_0C5A():
        OP_97(0x0008, -117750, 66100, -100000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C5A)

    Sleep(100)

    ChrSetChipByIndex(0x0009, 1)

    @scena.Lambda('lambda_0C80')
    def lambda_0C80():
        OP_97(0x0009, -117750, 66100, -80000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0C80)

    Sleep(100)

    ChrSetChipByIndex(0x000A, 1)

    @scena.Lambda('lambda_0CA6')
    def lambda_0CA6():
        OP_97(0x000A, -117750, 66100, -60000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0CA6)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D24',
    )

    OP_62(0x010F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0110, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_0CF4')
    def lambda_0CF4():
        ChrWalkTo(0x010F, -114550, 5960, 68280, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010F, 0x0001, lambda_0CF4)

    @scena.Lambda('lambda_0D0F')
    def lambda_0D0F():
        ChrWalkTo(0x0110, -115730, 5970, 68140, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0110, 0x0001, lambda_0D0F)

    def _loc_D24(): pass

    label('loc_D24')

    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D53',
    )

    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)

    def _loc_D53(): pass

    label('loc_D53')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x000003EA, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_D75'),
        (-1, 'loc_D78'),
    )

    def _loc_D75(): pass

    label('loc_D75')

    OP_B4(0x00)

    Return()

    def _loc_D78(): pass

    label('loc_D78')

    EventBegin(0x00)
    ChrSetPos(0x0101, -113140, 5930, 66530, 208)
    ChrSetPos(0x0102, -113990, 5950, 67470, 179)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DCC',
    )

    ChrSetPos(0x0002, -112370, 5890, 67560, 236)
    ChrSetPos(0x0003, -112920, 5990, 68310, 224)

    def _loc_DCC(): pass

    label('loc_DCC')

    CameraMove(-112920, 5990, 68310, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    OP_64(0x01, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E1E',
    )

    ChrSetDirection(0x0002, 180, 0)
    ChrSetDirection(0x0003, 180, 0)

    def _loc_E1E(): pass

    label('loc_E1E')

    OP_0D()
    OP_28(0x0005, 0x01, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010150199V#007F呼～吓我一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150200V#012F那个荧光菇还完好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150201V#006F嗯，还是好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FD4',
    )

    ChrTurnDirection(0x010F, 0x0102, 400)

    ChrTalk(
        0x010F,
        (
            '#0270150207V#143F怎、怎么回事啊刚才。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270150208V为什么会突然有魔兽袭击过来呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x010F, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150202V#012F七耀石的原石发出的光可以吸引魔兽……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150203V而那个蘑菇发出的光\n',
            '似乎也有相同的效果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0110, 0x0102, 400)

    ChrTalk(
        0x0110,
        (
            '#0280150209V#153F哇～～真是厉害的蘑菇呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1045')

    def _loc_FD4(): pass

    label('loc_FD4')

    ChrTalk(
        0x0102,
        (
            '#0020150202V#012F七耀石的原石发出的光可以吸引魔兽……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150211V那个蘑菇发出的光\n',
            '似乎也有相同的效果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1045(): pass

    label('loc_1045')

    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010150212V#009F那个狡猾的大叔～～～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150213V#009F对于会发生这种情况的可能性只字不提。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11B9',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150214V#017F我想如果我们提高警惕的话，\n',
            '拿着回去也应该没什么问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150215V回到城里之后，\n',
            '就立刻把蘑菇交给委托人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0270150216V#142F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270150217V……一定不要出什么差错啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_122D')

    def _loc_11B9(): pass

    label('loc_11B9')

    ChrTalk(
        0x0102,
        (
            '#0020150204V#012F总之，现在还是先回城里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150205V#005F好！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150206V#005F奸商，\n',
            '给我等着瞧～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_122D(): pass

    label('loc_122D')

    EventEnd(0x00)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0002 offset: 0x1235
@scena.Code('func_02_1235')
def func_02_1235():
    OP_A6(0x0000)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -118000, 6000, 57600, 3000, 0x00)
    CreateThread(0x00FE, 0x02, 0x00, 0x0002)
    ChrSetDirection(0x00FE, 315, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    ChrWalkTo(0x00FE, -118900, 6000, 60000, 7000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0003 offset: 0x127D
@scena.Code('func_03_127D')
def func_03_127D():
    OP_A6(0x0002)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -116200, 6000, 58000, 3000, 0x00)
    CreateThread(0x00FE, 0x02, 0x00, 0x0002)
    ChrSetDirection(0x00FE, 315, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_A6(0x0002)
    ChrWalkTo(0x00FE, -117500, 6000, 60200, 7000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x0004 offset: 0x12C5
@scena.Code('func_04_12C5')
def func_04_12C5():
    OP_A6(0x0001)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -114600, 6000, 59300, 3000, 0x00)
    CreateThread(0x00FE, 0x02, 0x00, 0x0002)
    ChrSetDirection(0x00FE, 315, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    ChrWalkTo(0x00FE, -116800, 6000, 61400, 7000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0005 offset: 0x130D
@scena.Code('func_05_130D')
def func_05_130D():
    OP_A6(0x0004)
    Sleep(200)

    ChrSetDirection(0x0102, 225, 0)
    Sleep(400)

    ChrWalkTo(0x0102, -119100, 5900, 63150, 3000, 0x00)
    ChrSetDirection(0x0102, 225, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Return()

# id: 0x0006 offset: 0x1340
@scena.Code('func_06_1340')
def func_06_1340():
    CameraMove(-120100, 5900, 62700, 800)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
