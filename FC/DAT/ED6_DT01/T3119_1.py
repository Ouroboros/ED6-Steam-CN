import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3119_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3119_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3119.x'
    header.mapIndex       = 1
    header.bgm            = 10
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
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('func_01_A9')
def func_01_A9():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('func_02_AA')
def func_02_AA():
    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_24A',
    )

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0100)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AC',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181057V#010F刚才已经问过话了，\n',
            '可是安东尼一点反应也没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181058V我们在工房里面再调查一下吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181059V照米妮亚姆医生说的，\n',
            '在某个地方也许会有线索的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181060V#003F唔……也只有这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_241')

    def _loc_1AC(): pass

    label('loc_1AC')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C2',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_1C9')

    def _loc_1C2(): pass

    label('loc_1C2')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_1C9(): pass

    label('loc_1C9')

    ChrTalk(
        0x0102,
        (
            '#0020181057V#010F刚才已经问过话了，\n',
            '安东尼一点反应也没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181067V我们还是去二楼\n',
            '工房长的房间调查看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_241(): pass

    label('loc_241')

    TalkEnd(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)

    Return()

    def _loc_24A(): pass

    label('loc_24A')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_710',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_2AF',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#1960181045V哦，怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181046V我的嫌疑洗清了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

    def _loc_2AF(): pass

    label('loc_2AF')

    EventBegin(0x00)
    Fade(1000)
    CameraMove(400, 0, 9640, 0)
    ChrSetPos(0x0101, 450, 0, 9220, 358)
    ChrSetPos(0x0102, 1650, 0, 9460, 322)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_308',
    )

    ChrSetPos(0x0107, 1160, 0, 8750, 357)

    def _loc_308(): pass

    label('loc_308')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_327',
    )

    ChrSetPos(0x0106, -720, 0, 8630, 37)

    def _loc_327(): pass

    label('loc_327')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_346',
    )

    ChrSetPos(0x013C, -590, 0, 9610, 42)

    def _loc_346(): pass

    label('loc_346')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_360',
    )

    @scena.Lambda('lambda_0358')
    def lambda_0358():
        ChrTurnDirection(0x0000, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0358)

    def _loc_360(): pass

    label('loc_360')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_37A',
    )

    @scena.Lambda('lambda_0372')
    def lambda_0372():
        ChrTurnDirection(0x0001, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0372)

    def _loc_37A(): pass

    label('loc_37A')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_394',
    )

    @scena.Lambda('lambda_038C')
    def lambda_038C():
        ChrTurnDirection(0x0002, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_038C)

    def _loc_394(): pass

    label('loc_394')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3AE',
    )

    @scena.Lambda('lambda_03A6')
    def lambda_03A6():
        ChrTurnDirection(0x0003, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_03A6)

    def _loc_3AE(): pass

    label('loc_3AE')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3C8',
    )

    @scena.Lambda('lambda_03C0')
    def lambda_03C0():
        ChrTurnDirection(0x0004, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_03C0)

    def _loc_3C8(): pass

    label('loc_3C8')

    ChrTurnDirection(0x0008, 0x0101, 0)
    OP_4A(0x00FE, 255)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#1960181006V哟，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181007V你们要找的东西找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181008V#000F啊，嗯。\n',
            '虽说已经找到了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181009V但是还需要找另外一件东西。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1960181010V另外一件东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181011V#010F嗯，\n',
            '我们还要寻找被人从医务室里\n',
            '拿出来的烟草。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1960181012V哦哦……\n',
            '是这件事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181013V哎呀～\n',
            '你们也真是很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181014V#010F特莱斯主任您今天去过医务室吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181015V没有，没有去过。\n',
            '我今天一直都在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181016V如果不相信的话，\n',
            '可以对这间屋子进行搜查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181017V#505F唔唔～\n',
            '好像没什么可怀疑的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181018V#017F是啊，白忙一场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181019V怎么样？我的嫌疑洗清了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181020V#010F非常抱歉，\n',
            '在您百忙之中前来打扰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181021V可以的话，\n',
            '今后还要请您协助调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181022V啊，当然没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 400)
    OP_4B(0x00FE, 255)
    OP_28(0x002C, 0x01, 0x0020)

    Jump('loc_1191')

    def _loc_710(): pass

    label('loc_710')

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_A2C',
    )

    EventBegin(0x00)
    OP_4A(0x00FE, 255)
    Fade(1000)
    CameraMove(400, 0, 9640, 0)
    ChrSetPos(0x0101, 450, 0, 9220, 358)
    ChrSetPos(0x0102, 1650, 0, 9460, 322)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_778',
    )

    ChrSetPos(0x0107, 1160, 0, 8750, 357)

    def _loc_778(): pass

    label('loc_778')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_797',
    )

    ChrSetPos(0x0106, -720, 0, 8630, 37)

    def _loc_797(): pass

    label('loc_797')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7B6',
    )

    ChrSetPos(0x013C, -590, 0, 9610, 42)

    def _loc_7B6(): pass

    label('loc_7B6')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_7D0',
    )

    @scena.Lambda('lambda_07C8')
    def lambda_07C8():
        ChrTurnDirection(0x0000, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_07C8)

    def _loc_7D0(): pass

    label('loc_7D0')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_7EA',
    )

    @scena.Lambda('lambda_07E2')
    def lambda_07E2():
        ChrTurnDirection(0x0001, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_07E2)

    def _loc_7EA(): pass

    label('loc_7EA')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_804',
    )

    @scena.Lambda('lambda_07FC')
    def lambda_07FC():
        ChrTurnDirection(0x0002, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_07FC)

    def _loc_804(): pass

    label('loc_804')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_81E',
    )

    @scena.Lambda('lambda_0816')
    def lambda_0816():
        ChrTurnDirection(0x0003, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0816)

    def _loc_81E(): pass

    label('loc_81E')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_838',
    )

    @scena.Lambda('lambda_0830')
    def lambda_0830():
        ChrTurnDirection(0x0004, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_0830)

    def _loc_838(): pass

    label('loc_838')

    ChrTurnDirection(0x0008, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#1960181045V哦，怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181046V我的嫌疑洗清了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181049V#000F不好意思。\n',
            '很快就会结束的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08BC')
    def lambda_08BC():
        ChrTurnDirection(0x0102, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_08BC)

    @scena.Lambda('lambda_08CA')
    def lambda_08CA():
        ChrTurnDirection(0x0107, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_08CA)

    ChrTurnDirection(0x0101, 0x013C, 400)

    ChrTalk(
        0x013C,
        (
            '#2030181038V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTurnDirection(0x013C, 0x0101, 400)

    ChrTalk(
        0x013C,
        (
            '#2030181039V………………喵噢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070181040V#063F没有反应呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181053V#010F抱歉打扰了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181054V谢谢您配合我们工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09A4')
    def lambda_09A4():
        ChrTurnDirection(0x0107, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_09A4)

    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010181055V#000F那么再见了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1960181056V到、到底怎么回事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 400)
    OP_4B(0x00FE, 255)
    OP_28(0x002C, 0x01, 0x0040)

    Jump('loc_FB0')

    def _loc_A2C(): pass

    label('loc_A2C')

    EventBegin(0x00)
    OP_4A(0x00FE, 255)
    Fade(1000)
    CameraMove(400, 0, 9640, 0)
    ChrSetPos(0x0101, 450, 0, 9220, 358)
    ChrSetPos(0x0102, 1650, 0, 9460, 322)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A89',
    )

    ChrSetPos(0x0107, 1160, 0, 8750, 357)

    def _loc_A89(): pass

    label('loc_A89')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AA8',
    )

    ChrSetPos(0x0106, -720, 0, 8630, 37)

    def _loc_AA8(): pass

    label('loc_AA8')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AC7',
    )

    ChrSetPos(0x013C, -590, 0, 9610, 42)

    def _loc_AC7(): pass

    label('loc_AC7')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_AE1',
    )

    @scena.Lambda('lambda_0AD9')
    def lambda_0AD9():
        ChrTurnDirection(0x0000, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0AD9)

    def _loc_AE1(): pass

    label('loc_AE1')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_AFB',
    )

    @scena.Lambda('lambda_0AF3')
    def lambda_0AF3():
        ChrTurnDirection(0x0001, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0AF3)

    def _loc_AFB(): pass

    label('loc_AFB')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_B15',
    )

    @scena.Lambda('lambda_0B0D')
    def lambda_0B0D():
        ChrTurnDirection(0x0002, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0B0D)

    def _loc_B15(): pass

    label('loc_B15')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_B2F',
    )

    @scena.Lambda('lambda_0B27')
    def lambda_0B27():
        ChrTurnDirection(0x0003, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0B27)

    def _loc_B2F(): pass

    label('loc_B2F')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_B49',
    )

    @scena.Lambda('lambda_0B41')
    def lambda_0B41():
        ChrTurnDirection(0x0004, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_0B41)

    def _loc_B49(): pass

    label('loc_B49')

    ChrTurnDirection(0x0008, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#1960181006V哟，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181007V你们要找的东西找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181008V#000F啊，嗯。\n',
            '虽说已经找到了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181009V但是还需要找另外一件东西。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1960181010V另外一件东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181011V#010F嗯，\n',
            '我们还要寻找被人从医务室里\n',
            '拿出来的烟草。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1960181012V哦哦……\n',
            '是这件事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181013V哎呀～\n',
            '你们也真是很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181014V#010F特莱斯主任您今天去过医务室吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181015V没有，没有去过。\n',
            '我今天一直都在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181016V如果不相信的话，\n',
            '可以对这间屋子进行搜查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181017V#505F唔唔～\n',
            '好像没什么可怀疑的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181018V#017F是啊，白忙一场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181019V怎么样？我的嫌疑洗清了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181037V#004F啊，对了。\n',
            '安东尼，如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E26')
    def lambda_0E26():
        ChrTurnDirection(0x0102, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0E26)

    @scena.Lambda('lambda_0E34')
    def lambda_0E34():
        ChrTurnDirection(0x0107, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0E34)

    ChrTurnDirection(0x0101, 0x013C, 400)

    ChrTalk(
        0x013C,
        (
            '#2030181038V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTurnDirection(0x013C, 0x0101, 400)

    ChrTalk(
        0x013C,
        (
            '#2030181039V………………喵噢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070181040V#063F没有反应呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181041V#000F哎呀，\n',
            '这么说来果真是预料落空了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181020V#010F非常抱歉，\n',
            '在您百忙之中前来打扰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181021V可以的话，\n',
            '今后还要请您协助调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F68')
    def lambda_0F68():
        ChrTurnDirection(0x0107, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0F68)

    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x00FE,
        (
            '#1960181022V啊，当然没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 400)
    OP_4B(0x00FE, 255)
    OP_28(0x002C, 0x01, 0x0020)
    OP_28(0x002C, 0x01, 0x0040)
    def _loc_FB0(): pass

    label('loc_FB0')

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_1191',
    )

    @scena.Lambda('lambda_0FC1')
    def lambda_0FC1():
        ChrTurnDirection(0x0102, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0FC1)

    ChrTurnDirection(0x0101, 0x0102, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_1094',
    )

    ChrTalk(
        0x0101,
        (
            '#0010181068V#505F唔～对两个人都没有反应呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181069V还是去刚才安东尼\n',
            '有反应的地方调查一下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181070V#010F是二楼工房长的房间对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181071V我们赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_118B')

    def _loc_1094(): pass

    label('loc_1094')

    ChrTalk(
        0x0101,
        (
            '#0010181061V#505F唔～\n',
            '对两个人都没有反应呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181062V#013F也就是说没有线索了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181063V#010F我们到工房里面再调查一下吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181059V照米妮亚姆医生说的，\n',
            '在某个地方也许会有线索的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181060V#003F唔……也只有这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_118B(): pass

    label('loc_118B')

    OP_28(0x002C, 0x01, 0x0080)

    def _loc_1191(): pass

    label('loc_1191')

    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
