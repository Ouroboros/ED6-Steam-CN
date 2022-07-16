import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R0302_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0302_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

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

# id: 0xFFFF offset: 0x124D
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_403',
    )

    SetMapFlags(0x08000000)
    EventBegin(0x01)

    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_187',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_129',
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

    Jump('loc_184')

    def _loc_129(): pass

    label('loc_129')

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

    def _loc_184(): pass

    label('loc_184')

    Jump('loc_3E0')

    def _loc_187(): pass

    label('loc_187')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F2',
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

    Jump('loc_369')

    def _loc_2F2(): pass

    label('loc_2F2')

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

    def _loc_369(): pass

    label('loc_369')

    Jump('loc_3E0')

    def _loc_36C(): pass

    label('loc_36C')

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
    def _loc_3E0(): pass

    label('loc_3E0')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    ClearMapFlags(0x08000000)

    Jump('loc_403')

    def _loc_403(): pass

    label('loc_403')

    Return()

# id: 0x0001 offset: 0x404
@scena.Code('Init')
def Init():
    SetMapFlags(0x08000000)
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -113140, 5930, 66530, 208)
    SetChrPos(0x0102, -113990, 5950, 67470, 179)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_462',
    )

    SetChrPos(0x0002, -112370, 5890, 67560, 236)
    SetChrPos(0x0003, -112920, 5990, 68310, 224)

    def _loc_462(): pass

    label('loc_462')

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
    SetChrDirection(0x0101, 180, 400)

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
        'loc_798',
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

    def _loc_798(): pass

    label('loc_798')

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
    SetChrDirection(0x0101, 180, 400)

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
        'loc_904',
    )

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    SetChrDirection(0x0102, 180, 400)
    OP_62(0x010F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0110, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_08F2')
    def lambda_08F2():
        SetChrDirection(0x010F, 180, 400)

        ExitThread()

    DispatchAsync(0x010F, 0x0001, lambda_08F2)

    SetChrDirection(0x0110, 180, 400)

    Jump('loc_922')

    def _loc_904(): pass

    label('loc_904')

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    SetChrDirection(0x0102, 180, 400)

    def _loc_922(): pass

    label('loc_922')

    Sleep(400)

    Fade(1000)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, -113010, 5920, 53930, 130)
    SetChrPos(0x0009, -113010, 5920, 53930, 130)
    SetChrPos(0x000A, -113010, 5920, 53930, 130)
    SetChrChipByIndex(0x0008, 1)
    SetChrChipByIndex(0x0009, 1)
    SetChrChipByIndex(0x000A, 1)
    CameraSetDistance(3300, 0)
    CameraMove(-115560, 6020, 58870, 0)
    OP_6C(270000, 0)
    SetChrDirection(0x0101, 225, 0)
    SetChrDirection(0x0102, 225, 0)
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
        'loc_9CF',
    )

    SetChrDirection(0x0002, 225, 0)
    SetChrDirection(0x0003, 225, 0)

    def _loc_9CF(): pass

    label('loc_9CF')

    @scena.Lambda('lambda_09D5')
    def lambda_09D5():
        CameraMove(-114970, 6000, 64120, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_09D5)

    @scena.Lambda('lambda_09ED')
    def lambda_09ED():
        OP_6C(315000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_09ED)

    OP_0D()

    @scena.Lambda('lambda_09FE')
    def lambda_09FE():
        OP_97(0x0008, -111730, 61810, 75000, 5000, 0x0000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_09FE)

    @scena.Lambda('lambda_0A1A')
    def lambda_0A1A():
        ChrTurnDirection(0x0008, 0x0101, 0)
        Yield()

        Jump('lambda_0A1A')

    DispatchAsync2(0x0008, 0x0002, lambda_0A1A)

    Sleep(400)

    @scena.Lambda('lambda_0A30')
    def lambda_0A30():
        OP_97(0x0009, -111730, 61810, 65000, 5000, 0x0000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A30)

    @scena.Lambda('lambda_0A4C')
    def lambda_0A4C():
        ChrTurnDirection(0x0009, 0x0101, 0)
        Yield()

        Jump('lambda_0A4C')

    DispatchAsync2(0x0009, 0x0002, lambda_0A4C)

    Sleep(400)

    @scena.Lambda('lambda_0A62')
    def lambda_0A62():
        OP_97(0x000A, -111730, 61810, 55000, 5000, 0x0000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A62)

    @scena.Lambda('lambda_0A7E')
    def lambda_0A7E():
        ChrTurnDirection(0x000A, 0x0101, 0)
        Yield()

        Jump('lambda_0A7E')

    DispatchAsync2(0x000A, 0x0002, lambda_0A7E)

    WaitForThreadExit(0x000A, 0x0001)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    SetChrChipByIndex(0x000A, 0)
    WaitForThreadExit(0x0008, 0x0001)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    SetChrChipByIndex(0x0008, 0)
    Sleep(100)

    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    SetChrChipByIndex(0x0009, 0)
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
    SetChrChipByIndex(0x0102, 3)
    ChrTurnDirection(0x0102, 0x0008, 0)

    ChrTalk(
        0x0102,
        (
            '#0020150198V#016F艾丝蒂尔，迎战！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 2)
    ChrTurnDirection(0x0101, 0x0008, 0)

    @scena.Lambda('lambda_0B4B')
    def lambda_0B4B():
        ChrTurnDirection(0x0101, 0x0008, 0)
        Yield()

        Jump('lambda_0B4B')

    DispatchAsync2(0x0101, 0x0001, lambda_0B4B)

    @scena.Lambda('lambda_0B5C')
    def lambda_0B5C():
        ChrTurnDirection(0x0102, 0x0008, 0)
        Yield()

        Jump('lambda_0B5C')

    DispatchAsync2(0x0102, 0x0001, lambda_0B5C)

    TerminateThread(0x000A, 0x00)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x0008, 0x00)

    @scena.Lambda('lambda_0B79')
    def lambda_0B79():
        CameraMove(-113290, 5960, 66180, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0B79)

    @scena.Lambda('lambda_0B91')
    def lambda_0B91():
        CameraSetDistance(2800, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0B91)

    SetChrChipByIndex(0x0008, 1)

    @scena.Lambda('lambda_0BA6')
    def lambda_0BA6():
        OP_97(0x0008, -117750, 66100, -100000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0BA6)

    Sleep(100)

    SetChrChipByIndex(0x0009, 1)

    @scena.Lambda('lambda_0BCC')
    def lambda_0BCC():
        OP_97(0x0009, -117750, 66100, -80000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0BCC)

    Sleep(100)

    SetChrChipByIndex(0x000A, 1)

    @scena.Lambda('lambda_0BF2')
    def lambda_0BF2():
        OP_97(0x000A, -117750, 66100, -60000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BF2)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C70',
    )

    OP_62(0x010F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0110, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_0C40')
    def lambda_0C40():
        ChrWalkTo(0x010F, -114550, 5960, 68280, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010F, 0x0001, lambda_0C40)

    @scena.Lambda('lambda_0C5B')
    def lambda_0C5B():
        ChrWalkTo(0x0110, -115730, 5970, 68140, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0110, 0x0001, lambda_0C5B)

    def _loc_C70(): pass

    label('loc_C70')

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
        'loc_C9F',
    )

    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)

    def _loc_C9F(): pass

    label('loc_C9F')

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
        (0x00000001, 'loc_CC1'),
        (-1, 'loc_CC4'),
    )

    def _loc_CC1(): pass

    label('loc_CC1')

    OP_B4(0x00)

    Return()

    def _loc_CC4(): pass

    label('loc_CC4')

    EventBegin(0x00)
    SetChrPos(0x0101, -113140, 5930, 66530, 208)
    SetChrPos(0x0102, -113990, 5950, 67470, 179)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D18',
    )

    SetChrPos(0x0002, -112370, 5890, 67560, 236)
    SetChrPos(0x0003, -112920, 5990, 68310, 224)

    def _loc_D18(): pass

    label('loc_D18')

    CameraMove(-112920, 5990, 68310, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    OP_64(0x01, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D6A',
    )

    SetChrDirection(0x0002, 180, 0)
    SetChrDirection(0x0003, 180, 0)

    def _loc_D6A(): pass

    label('loc_D6A')

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
    SetChrChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150200V#012F那个荧光菇还完好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 65535)
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
        'loc_EF8',
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

    Jump('loc_F5F')

    def _loc_EF8(): pass

    label('loc_EF8')

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

    def _loc_F5F(): pass

    label('loc_F5F')

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
        'loc_10B5',
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

    Jump('loc_111A')

    def _loc_10B5(): pass

    label('loc_10B5')

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

    def _loc_111A(): pass

    label('loc_111A')

    EventEnd(0x00)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0002 offset: 0x1122
@scena.Code('ReInit')
def ReInit():
    OP_A6(0x0000)
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -118000, 6000, 57600, 3000, 0x00)
    CreateThread(0x00FE, 0x02, 0x00, 0x0002)
    SetChrDirection(0x00FE, 315, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    ChrWalkTo(0x00FE, -118900, 6000, 60000, 7000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0003 offset: 0x116A
@scena.Code('func_03_116A')
def func_03_116A():
    OP_A6(0x0002)
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -116200, 6000, 58000, 3000, 0x00)
    CreateThread(0x00FE, 0x02, 0x00, 0x0002)
    SetChrDirection(0x00FE, 315, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_A6(0x0002)
    ChrWalkTo(0x00FE, -117500, 6000, 60200, 7000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x0004 offset: 0x11B2
@scena.Code('func_04_11B2')
def func_04_11B2():
    OP_A6(0x0001)
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -114600, 6000, 59300, 3000, 0x00)
    CreateThread(0x00FE, 0x02, 0x00, 0x0002)
    SetChrDirection(0x00FE, 315, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    ChrWalkTo(0x00FE, -116800, 6000, 61400, 7000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0005 offset: 0x11FA
@scena.Code('func_05_11FA')
def func_05_11FA():
    OP_A6(0x0004)
    Sleep(200)

    SetChrDirection(0x0102, 225, 0)
    Sleep(400)

    ChrWalkTo(0x0102, -119100, 5900, 63150, 3000, 0x00)
    SetChrDirection(0x0102, 225, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Return()

# id: 0x0006 offset: 0x122D
@scena.Code('func_06_122D')
def func_06_122D():
    CameraMove(-120100, 5900, 62700, 800)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
