import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1102_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1102_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1102_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3BF',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480164V#1002F卡片里的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480165V……莫非是指这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480166V#022F嗯，虽然有这可能性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480167V那个事件的调查稍后再进行吧。\n',
            '现在要赶紧前往拉文努村哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480168V#1002F啊，嗯……明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BB')

    def _loc_1AE(): pass

    label('loc_1AE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_260',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480169V#072F嗯，是有很可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480170V不过那个事件的调查稍后再进行吧。\n',
            '现在应该赶紧前往拉文努村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480168V#1002F啊，嗯……明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BB')

    def _loc_260(): pass

    label('loc_260')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_312',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480172V#030F唔，是很有可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480173V不过那个事件的调查稍后再进行吧。\n',
            '现在先赶紧前往拉文努村吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480168V#1002F啊，嗯……明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BB')

    def _loc_312(): pass

    label('loc_312')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BB',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480175V#042F嗯，说不定就是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480176V不过这里迟些再调查吧。\n',
            '现在得赶紧前往拉文努村啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480177V#1002F啊，嗯……说得对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BB(): pass

    label('loc_3BB')

    TalkEnd(0x00FF)

    Return()

    def _loc_3BF(): pass

    label('loc_3BF')

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 23790, -3000, 12560, 135)
    ChrSetPos(0x00F7, 22600, -3000, 12510, 135)
    ChrSetPos(0x00F8, 23080, -3000, 13980, 135)
    ChrSetPos(0x00F9, 21720, -3000, 13710, 135)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_427',
    )

    ChrSetPos(0x0004, 21150, -3000, 12710, 135)

    def _loc_427(): pass

    label('loc_427')

    ChrSetPos(0x0019, 36190, -3000, 13170, 270)
    CameraMove(26500, -3000, 9360, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2950, 0)
    OP_6C(166000, 0)
    OP_6E(262, 0)
    OP_0D()
    CameraMove(23790, -3000, 12560, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010480314V#1011F这就是『被托起的棺材』吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480315V虽然看上去不像是『棺』，\n',
            '不过『被托住』看起来是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_555',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480316V#050F嗯，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480317V好像没发现\n',
            '关键的卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_663')

    def _loc_555(): pass

    label('loc_555')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5AE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480318V#020F嗯，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480319V好像没发现\n',
            '关键的卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_663')

    def _loc_5AE(): pass

    label('loc_5AE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_607',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480320V#070F嗯，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480321V好像没发现\n',
            '关键的卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_663')

    def _loc_607(): pass

    label('loc_607')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_663',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480322V#030F确实如此，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480323V好像没发现\n',
            '关键的卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_663(): pass

    label('loc_663')

    ChrTalk(
        0x0101,
        (
            '#0010480324V#1015F唔，真奇怪～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480325V感觉地方\n',
            '应该没找错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0101, 300, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480326V#1018F啊，莫非！？\n',
            '会不会在货箱底下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_76D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070480327V#063F嗯，有可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070480328V但是，要钻下去调查\n',
            '好像空隙不够呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A9')

    def _loc_76D(): pass

    label('loc_76D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7DA',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480329V#043F嗯，这么想也有道理……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480330V但是，要钻下去调查\n',
            '好像空隙不够。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A9')

    def _loc_7DA(): pass

    label('loc_7DA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_845',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480331V#030F嗯，有这个可能性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480332V但是，要钻下去调查\n',
            '好像空隙不够。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A9')

    def _loc_845(): pass

    label('loc_845')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8A9',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480333V#070F嗯，也有可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480334V但是，要钻下去调查\n',
            '好像空隙不够。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8A9(): pass

    label('loc_8A9')

    ChrTalk(
        0x0101,
        (
            '#0010480335V#1007F确、确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480336V#1003F嗯，可我觉得这个\n',
            '货箱实在很可疑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0019,
        '男人的声音',
        (
            '#3650480337V#2P喂，你们在干吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF6)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_966',
    )

    OP_62(0x00F6, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_9A4')

    def _loc_966(): pass

    label('loc_966')

    If(
        (
            (Expr.Eval, "OP_CB(0xF6)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_98D',
    )

    OP_62(0x00F6, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_9A4')

    def _loc_98D(): pass

    label('loc_98D')

    OP_62(0x00F6, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_9A4(): pass

    label('loc_9A4')

    Sleep(150)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9D0',
    )

    OP_62(0x00F7, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_A0E')

    def _loc_9D0(): pass

    label('loc_9D0')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9F7',
    )

    OP_62(0x00F7, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_A0E')

    def _loc_9F7(): pass

    label('loc_9F7')

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_A0E(): pass

    label('loc_A0E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A35',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_A73')

    def _loc_A35(): pass

    label('loc_A35')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A5C',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_A73')

    def _loc_A5C(): pass

    label('loc_A5C')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_A73(): pass

    label('loc_A73')

    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A9F',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_ADD')

    def _loc_A9F(): pass

    label('loc_A9F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AC6',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_ADD')

    def _loc_AC6(): pass

    label('loc_AC6')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_ADD(): pass

    label('loc_ADD')

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B26',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B0F',
    )

    OP_62(0x0004, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B26')

    def _loc_B0F(): pass

    label('loc_B0F')

    OP_62(0x0004, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B26(): pass

    label('loc_B26')

    Sleep(1000)

    @scena.Lambda('lambda_0B31')
    def lambda_0B31():
        ChrSetDirection(0x0002, 90, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0B31)

    Sleep(100)

    @scena.Lambda('lambda_0B44')
    def lambda_0B44():
        ChrSetDirection(0x0003, 90, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0B44)

    @scena.Lambda('lambda_0B52')
    def lambda_0B52():
        ChrSetDirection(0x0001, 90, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0B52)

    Sleep(100)

    @scena.Lambda('lambda_0B65')
    def lambda_0B65():
        ChrSetDirection(0x0000, 90, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0B65)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B87',
    )

    @scena.Lambda('lambda_0B7F')
    def lambda_0B7F():
        ChrSetDirection(0x0004, 90, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_0B7F)

    def _loc_B87(): pass

    label('loc_B87')

    @scena.Lambda('lambda_0B8D')
    def lambda_0B8D():
        OP_6C(225000, 4000)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0B8D)

    CreateThread(0x0101, 0x02, 0x01, 0x0001)
    ChrWalkTo(0x0019, 25500, -3000, 13090, 3000, 0x00)
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)
    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BD2',
    )

    TerminateThread(0x0004, 0x01)

    def _loc_BD2(): pass

    label('loc_BD2')

    OP_4A(0x0019, 255)

    ChrTalk(
        0x0019,
        (
            '#3650480338V你们是不是在\n',
            '乱动这里的机器？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#3650480339V到底想干什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480340V#1009F我、我们没有乱动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480341V只是有点事情\n',
            '想要调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#3650480342V啊？想要调查事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D12',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480343V#050F嗯，我们的职业是…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '阿加特拿出了游击士的徽章。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_E75')

    def _loc_D12(): pass

    label('loc_D12')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D8E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480344V#020F嗯，我们的职业是…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雪拉扎德拿出了游击士的徽章。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_E75')

    def _loc_D8E(): pass

    label('loc_D8E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E04',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480345V#070F嗯，我们的职业是…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '金拿出了游击士的徽章。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_E75')

    def _loc_E04(): pass

    label('loc_E04')

    ChrTalk(
        0x0101,
        (
            '#0010480346V#1002F嗯，我们\n',
            '的职业其实是…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔拿出了游击士的徽章。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_E75(): pass

    label('loc_E75')

    ChrTalk(
        0x0019,
        (
            '#3650480347V啊，原来是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#3650480348V在调查案件吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480349V#1002F正调查到关键的地方了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480350V#1011F啊，对了。\n',
            '有件事我想问一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480351V大叔你能\n',
            '操纵这部机器吗？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#3650480352V嗯，当然能啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#3650480353V怎么了？你们想让我操纵它？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480354V#1002F嗯，实际上我们\n',
            '必须要调查一下货箱的底部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480355V能不能麻烦你把它提升到\n',
            '能看得到下面的程度？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#3650480356V嗯，这个好办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#3650480357V好，那么你们\n',
            '稍微在那边等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1060')
    def lambda_1060():
        ChrTurnDirection(0x00FE, 0x0019, 400)
        Yield()

        Jump('lambda_1060')

    DispatchAsync2(0x0000, 0x0001, lambda_1060)

    @scena.Lambda('lambda_1071')
    def lambda_1071():
        ChrTurnDirection(0x00FE, 0x0019, 400)
        Yield()

        Jump('lambda_1071')

    DispatchAsync2(0x0001, 0x0001, lambda_1071)

    @scena.Lambda('lambda_1082')
    def lambda_1082():
        ChrTurnDirection(0x00FE, 0x0019, 400)
        Yield()

        Jump('lambda_1082')

    DispatchAsync2(0x0002, 0x0001, lambda_1082)

    @scena.Lambda('lambda_1093')
    def lambda_1093():
        ChrTurnDirection(0x00FE, 0x0019, 400)
        Yield()

        Jump('lambda_1093')

    DispatchAsync2(0x0003, 0x0001, lambda_1093)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10BB',
    )

    @scena.Lambda('lambda_10B0')
    def lambda_10B0():
        ChrTurnDirection(0x00FE, 0x0019, 400)
        Yield()

        Jump('lambda_10B0')

    DispatchAsync2(0x0004, 0x0001, lambda_10B0)

    def _loc_10BB(): pass

    label('loc_10BB')

    @scena.Lambda('lambda_10C1')
    def lambda_10C1():
        OP_6C(155000, 4000)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_10C1)

    @scena.Lambda('lambda_10D1')
    def lambda_10D1():
        CameraMove(26860, -3000, 9620, 4000)

        ExitThread()

    DispatchAsync(0x002A, 0x0002, lambda_10D1)

    ChrSetDirection(0x0019, 135, 400)
    ChrWalkTo(0x0019, 27980, -3000, 10790, 2000, 0x00)
    ChrSetDirection(0x0019, 225, 400)
    ChrWalkTo(0x0019, 27670, -3000, 10480, 1000, 0x00)
    ChrSetFlags(0x0019, 0x0040)
    ChrSetFlags(0x0019, 0x0004)
    ChrSetFlags(0x0019, 0x0010)
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)
    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)
    ChrWalkTo(0x0019, 27240, -2400, 9370, 1000, 0x00)
    ChrSetDirection(0x0019, 315, 400)
    ChrWalkTo(0x0019, 26930, -2600, 9650, 1000, 0x00)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1177',
    )

    TerminateThread(0x0004, 0x01)

    def _loc_1177(): pass

    label('loc_1177')

    Sleep(1000)

    Sleep(100)

    PlaySE(157, 0x00, 0x64)
    Sleep(400)

    PlaySE(207, 0x01, 0x55)

    ChrTalk(
        0x0019,
        (
            '#3650480358V好，那么我要开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_24(0x00CF, 0x64)
    OP_B0(0x000D, 0x0A)
    OP_70(0x000D, 30)
    OP_73(0x000D)
    PlaySE(154, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0019,
        (
            '#3650480359V嗯～已经固定好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#3650480360V你们可以到\n',
            '货箱下面去调查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480361V#1006F#1P嗯，明白了。\n',
            '我们马上调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 25100, -3000, 10990, 2000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0101, 270, 400)
    Sleep(200)

    ChrSetDirection(0x0101, 90, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 120, 400)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '调查了货箱底部，\n',
            '发现贴着卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010480362V#1006F#1P好，有了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 23790, -3000, 12560, 2000, 0x00)
    ChrSetDirection(0x0101, 120, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480363V#1018F#1P谢谢你，大叔。\n',
            '已经好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#3650480364V嗯，那么我要放下\n',
            '货箱了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_B0(0x000D, 0x0A)
    OP_6F(0x000D, 30)
    OP_70(0x000D, 0)
    OP_73(0x000D)
    PlaySE(154, 0x00, 0x64)
    OP_23(0x009D)
    OP_23(0x00CF)
    Sleep(400)

    Fade(1000)
    OP_6C(225000, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2950, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0019, 27780, -3000, 10390, 30)
    ChrSetFlags(0x0019, 0x0040)
    ChrSetFlags(0x0019, 0x0004)
    ChrSetFlags(0x0019, 0x0010)

    @scena.Lambda('lambda_1416')
    def lambda_1416():
        ChrTurnDirection(0x00FE, 0x0019, 400)
        Yield()

        Jump('lambda_1416')

    DispatchAsync2(0x0000, 0x0001, lambda_1416)

    @scena.Lambda('lambda_1427')
    def lambda_1427():
        ChrTurnDirection(0x00FE, 0x0019, 400)
        Yield()

        Jump('lambda_1427')

    DispatchAsync2(0x0001, 0x0001, lambda_1427)

    @scena.Lambda('lambda_1438')
    def lambda_1438():
        ChrTurnDirection(0x00FE, 0x0019, 400)
        Yield()

        Jump('lambda_1438')

    DispatchAsync2(0x0002, 0x0001, lambda_1438)

    @scena.Lambda('lambda_1449')
    def lambda_1449():
        ChrTurnDirection(0x00FE, 0x0019, 400)
        Yield()

        Jump('lambda_1449')

    DispatchAsync2(0x0003, 0x0001, lambda_1449)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1471',
    )

    @scena.Lambda('lambda_1466')
    def lambda_1466():
        ChrTurnDirection(0x00FE, 0x0019, 400)
        Yield()

        Jump('lambda_1466')

    DispatchAsync2(0x0004, 0x0001, lambda_1466)

    def _loc_1471(): pass

    label('loc_1471')

    @scena.Lambda('lambda_1477')
    def lambda_1477():
        CameraMove(23760, -3000, 13010, 3000)

        ExitThread()

    DispatchAsync(0x002A, 0x0002, lambda_1477)

    ChrWalkTo(0x0019, 27180, -3000, 11640, 2000, 0x00)
    ChrWalkTo(0x0019, 25500, -3000, 13090, 2000, 0x00)
    ChrTurnDirection(0x0019, 0x0101, 400)
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)
    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14D8',
    )

    TerminateThread(0x0004, 0x01)

    def _loc_14D8(): pass

    label('loc_14D8')

    WaitForThreadExit(0x002A, 0x0001)
    WaitForThreadExit(0x002A, 0x0002)

    ChrTalk(
        0x0019,
        (
            '#3650480365V看来你们已经\n',
            '找到了要找的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1549',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480366V#030F多谢您的帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E6')

    def _loc_1549(): pass

    label('loc_1549')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_157F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480367V#070F谢谢您的帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E6')

    def _loc_157F(): pass

    label('loc_157F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15B5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480368V#525F谢谢您的帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E6')

    def _loc_15B5(): pass

    label('loc_15B5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15E6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480369V#051F谢谢您帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15E6(): pass

    label('loc_15E6')

    ChrTalk(
        0x0019,
        (
            '#3650480370V哈哈，不用介意。\n',
            '我也没做什么了不得的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#3650480371V虽然不知道你们在调查什么，\n',
            '总之好好地解决掉它吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#3650480372V那我就回去工作啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480373V#1001F嗯，谢谢您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x02, 0x01, 0x0002)
    ChrWalkTo(0x0019, 36190, -3000, 13170, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010480374V#1011F呼，想不到在这时候\n',
            '出现了一个帮手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_174C',
    )

    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080480375V#070F嗯，那么\n',
            '我们就继续工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1827')

    def _loc_174C(): pass

    label('loc_174C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1796',
    )

    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050480376V#050F嗯，那么\n',
            '我们就继续工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1827')

    def _loc_1796(): pass

    label('loc_1796')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17E0',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030480377V#020F嗯，那么\n',
            '我们就继续工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1827')

    def _loc_17E0(): pass

    label('loc_17E0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1827',
    )

    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040480378V#030F嗯，那么\n',
            '我们就继续工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1827(): pass

    label('loc_1827')

    @scena.Lambda('lambda_182D')
    def lambda_182D():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_182D)

    @scena.Lambda('lambda_183B')
    def lambda_183B():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_183B)

    @scena.Lambda('lambda_1849')
    def lambda_1849():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1849)

    @scena.Lambda('lambda_1857')
    def lambda_1857():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1857)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1879',
    )

    @scena.Lambda('lambda_1871')
    def lambda_1871():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_1871)

    def _loc_1879(): pass

    label('loc_1879')

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_189E',
    )

    WaitForThreadExit(0x0004, 0x0001)

    def _loc_189E(): pass

    label('loc_189E')

    ChrTalk(
        0x0101,
        (
            '#0010480379V#1000F#1P嗯，赶快确认\n',
            '卡片内容吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)
    Fade(500)
    ChrSetChipByIndex(0x0101, 32)
    OP_0D()
    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS124._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170480380V　　 门已经被打开了。 　 　\n',
            '　　　寻求虚荣之证　　　\n',
            '　就在『女神的话语』中。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010480381V#1000F#1P…………就这些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480382V#1000F看来只差最后一步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A58',
    )

    ChrTalk(
        0x0107,
        (
            '#0070480383V#060F嗯，好像是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070480384V接下来的提示是\n',
            '『女神的话语』啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B8A')

    def _loc_1A58(): pass

    label('loc_1A58')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1ABF',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480385V#040F嗯，好像是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480386V接下来的提示是\n',
            '『女神的话语』啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B8A')

    def _loc_1ABF(): pass

    label('loc_1ABF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B26',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480387V#030F嗯，好像是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480388V接下来的提示是\n',
            '『女神的话语』啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B8A')

    def _loc_1B26(): pass

    label('loc_1B26')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B8A',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480389V#070F嗯，好像是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480390V接下来的提示是\n',
            '『女神的话语』啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B8A(): pass

    label('loc_1B8A')

    ChrTalk(
        0x0101,
        (
            '#0010480391V#1015F#1P说起城里的『女神』的话\n',
            '就只有那一个地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C2E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480392V#050F确实如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480393V马上去那里\n',
            '调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    Jump('loc_1D49')

    def _loc_1C2E(): pass

    label('loc_1C2E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C8C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480394V#020F确实如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480395V马上去那里\n',
            '调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    Jump('loc_1D49')

    def _loc_1C8C(): pass

    label('loc_1C8C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CEA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480396V#070F确实如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480397V马上去那里\n',
            '调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    Jump('loc_1D49')

    def _loc_1CEA(): pass

    label('loc_1CEA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D49',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480398V#030F嗯，确实如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480399V马上去那里\n',
            '调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    def _loc_1D49(): pass

    label('loc_1D49')

    ChrTalk(
        0x0101,
        (
            '#0010480400V#1006F#1P嗯，就这么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0019, 255)
    ChrClearFlags(0x0019, 0x0010)
    ChrSetPos(0x0019, 27300, -10000, 26800, 315)
    OP_28(0x0078, 0x01, 0x0040)
    OP_28(0x0078, 0x01, 0x0080)
    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))
    OP_64(0x01, 0x0001)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x1DA2
@scena.Code('func_01_1DA2')
def func_01_1DA2():
    CameraMove(23760, -3000, 13010, 2000)

    Return()

# id: 0x0002 offset: 0x1DB4
@scena.Code('func_02_1DB4')
def func_02_1DB4():
    CameraMove(27220, -3000, 13160, 2000)
    Sleep(1000)

    CameraMove(22860, -3000, 13110, 2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
