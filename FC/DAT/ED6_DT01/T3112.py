import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3112_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3112   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3112.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xB7C
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_B4'),
        (-1, 'loc_CD'),
    )

    def _loc_B4(): pass

    label('loc_B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 2, 0x50A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C6',
    )

    SetScenaFlags(ScenaFlag(0x00A1, 2, 0x50A))
    Event(0, 0x0002)

    Jump('loc_CA')

    def _loc_C6(): pass

    label('loc_C6')

    Event(0, 0x0003)

    def _loc_CA(): pass

    label('loc_CA')

    Jump('loc_CD')

    def _loc_CD(): pass

    label('loc_CD')

    Return()

# id: 0x0001 offset: 0xCE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E6',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_113')

    def _loc_E6(): pass

    label('loc_E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_FE',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_113')

    def _loc_FE(): pass

    label('loc_FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_113',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_113(): pass

    label('loc_113')

    Return()

# id: 0x0002 offset: 0x114
@scena.Code('ReInit')
def ReInit():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(1400, 0, 4500, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 1000, 0, 3390, 0)
    SetChrPos(0x0102, -390, 0, 2980, 0)
    SetChrPos(0x0107, 680, 0, 2210, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(800)

    SetChrDirection(0x0101, 270, 400)
    Sleep(200)

    SetChrDirection(0x0101, 0, 400)
    SetChrDirection(0x0101, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010070521V#501F#5P咦，这个房间是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070522V#060F这个是导力梯哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070523V从地下到房顶，\n',
            '这么一跳～就上去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 135, 400)
    SetChrDirection(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070524V#505F#5P嗯……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070525V导力梯不就是\n',
            '矿山里用的那种升降装置吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070526V我哪也没看到导力梯啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070527V#010F不是的，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070528V其实这整个房间就是导力梯了，\n',
            '只不过我们现在看到的这个不同而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070529V#004F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070530V#061F嘿嘿，这可是最新式的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070531V最大载重量５０托里姆……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070532V就算要搬运大型器材，\n',
            '也是轻轻松松的呢⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070533V#506F#5P虽、虽然不大明白……\n',
            '但感觉好像很厉害呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070534V#000F对了，怎么做才能让它动起来呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070535V#560F啊，只要在那边的控制板上\n',
            '选择要去的楼层就ＯＫ了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070536V嗯……\n',
            '是要去城里吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070537V#010F嗯，\n',
            '能带我们去一楼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070538V#061F好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0107, 135, 400)

    @scena.Lambda('lambda_04DE')
    def lambda_04DE():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_04DE')

    DispatchAsync2(0x0101, 0x0001, lambda_04DE)

    @scena.Lambda('lambda_04EF')
    def lambda_04EF():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_04EF')

    DispatchAsync2(0x0102, 0x0001, lambda_04EF)

    ChrWalkTo(0x0107, 1750, 0, 1460, 2000, 0x00)
    SetChrDirection(0x0107, 90, 400)
    Sleep(500)

    PlaySE(103, 0x00, 0x64)
    CameraMove(1400, -500, 4500, 500)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010070539V#004F#10A#1P哇哇……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    FadeOut(1000, 0, -1)
    CameraMove(1400, -12000, 4500, 1500)
    OP_0D()
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    SetMapFlags(0x10000000)
    NewScene('ED6_DT01/T3111._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x59B
@scena.Code('func_03_59B')
def func_03_59B():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetChrPos(0x0000, 1750, 0, 1370, 90)
    SetChrPos(0x0001, 1280, 0, 2600, 180)

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5E1',
    )

    SetChrPos(0x0002, 70, 0, 1470, 180)

    def _loc_5E1(): pass

    label('loc_5E1')

    If(
        (
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5FE',
    )

    SetChrPos(0x0003, -50, 0, 2600, 180)

    def _loc_5FE(): pass

    label('loc_5FE')

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_61B',
    )

    SetChrPos(0x0004, -1380, 0, 1470, 180)

    def _loc_61B(): pass

    label('loc_61B')

    If(
        (
            (Expr.PushValueByIndex, 0xF),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_638',
    )

    SetChrPos(0x0005, -1380, 0, 2600, 180)

    def _loc_638(): pass

    label('loc_638')

    CameraMove(1400, 0, 4500, 0)
    CameraSetDistance(3000, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A8, 0, 0x540)),
            Expr.Return,
        ),
        'loc_6F0',
    )

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '　【 顶楼 】\n'),
            TXT(0x01, '　【 ５层 】\n'),
            TXT(0x02, '　【 ４层 】\n'),
            TXT(0x03, '　【 ３层 】\n'),
            TXT(0x04, '　【 ２层 】\n'),
            TXT(0x05, '　【 １层 】\n'),
            TXT(0x06, '★【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x6),
            (Expr.PushLong, 0x0),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A2F')

    def _loc_6F0(): pass

    label('loc_6F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A8, 1, 0x541)),
            Expr.Return,
        ),
        'loc_77B',
    )

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '　【 顶楼 】\n'),
            TXT(0x01, '　【 ５层 】\n'),
            TXT(0x02, '　【 ４层 】\n'),
            TXT(0x03, '　【 ３层 】\n'),
            TXT(0x04, '　【 ２层 】\n'),
            TXT(0x05, '★【 １层 】\n'),
            TXT(0x06, '　【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A2F')

    def _loc_77B(): pass

    label('loc_77B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A8, 2, 0x542)),
            Expr.Return,
        ),
        'loc_806',
    )

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '　【 顶楼 】\n'),
            TXT(0x01, '　【 ５层 】\n'),
            TXT(0x02, '　【 ４层 】\n'),
            TXT(0x03, '　【 ３层 】\n'),
            TXT(0x04, '★【 ２层 】\n'),
            TXT(0x05, '　【 １层 】\n'),
            TXT(0x06, '　【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A2F')

    def _loc_806(): pass

    label('loc_806')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A8, 3, 0x543)),
            Expr.Return,
        ),
        'loc_891',
    )

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '　【 顶楼 】\n'),
            TXT(0x01, '　【 ５层 】\n'),
            TXT(0x02, '　【 ４层 】\n'),
            TXT(0x03, '★【 ３层 】\n'),
            TXT(0x04, '　【 ２层 】\n'),
            TXT(0x05, '　【 １层 】\n'),
            TXT(0x06, '　【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x6),
            (Expr.PushLong, 0x3),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A2F')

    def _loc_891(): pass

    label('loc_891')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A8, 4, 0x544)),
            Expr.Return,
        ),
        'loc_91C',
    )

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '　【 顶楼 】\n'),
            TXT(0x01, '　【 ５层 】\n'),
            TXT(0x02, '★【 ４层 】\n'),
            TXT(0x03, '　【 ３层 】\n'),
            TXT(0x04, '　【 ２层 】\n'),
            TXT(0x05, '　【 １层 】\n'),
            TXT(0x06, '　【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x6),
            (Expr.PushLong, 0x4),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A2F')

    def _loc_91C(): pass

    label('loc_91C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A8, 5, 0x545)),
            Expr.Return,
        ),
        'loc_9A7',
    )

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '　【 顶楼 】\n'),
            TXT(0x01, '★【 ５层 】\n'),
            TXT(0x02, '　【 ４层 】\n'),
            TXT(0x03, '　【 ３层 】\n'),
            TXT(0x04, '　【 ２层 】\n'),
            TXT(0x05, '　【 １层 】\n'),
            TXT(0x06, '　【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x6),
            (Expr.PushLong, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A2F')

    def _loc_9A7(): pass

    label('loc_9A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A8, 6, 0x546)),
            Expr.Return,
        ),
        'loc_A2F',
    )

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '★【 顶楼 】\n'),
            TXT(0x01, '　【 ５层 】\n'),
            TXT(0x02, '　【 ４层 】\n'),
            TXT(0x03, '　【 ３层 】\n'),
            TXT(0x04, '　【 ２层 】\n'),
            TXT(0x05, '　【 １层 】\n'),
            TXT(0x06, '　【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x6),
            (Expr.PushLong, 0x6),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_A2F(): pass

    label('loc_A2F')

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Gtr,
            Expr.Or,
            Expr.Return,
        ),
        'loc_A5F',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushReg, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_A5F(): pass

    label('loc_A5F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushReg, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_A8D',
    )

    FadeOut(2000, 0, -1)
    PlaySE(103, 0x00, 0x64)
    CameraMove(1400, -11900, 4500, 2000)

    Jump('loc_AB8')

    def _loc_A8D(): pass

    label('loc_A8D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushReg, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_AB8',
    )

    FadeOut(2000, 0, -1)
    PlaySE(103, 0x00, 0x64)
    CameraMove(1400, 11900, 4500, 2000)

    def _loc_AB8(): pass

    label('loc_AB8')

    ClearScenaFlags(ScenaFlag(0x00A8, 0, 0x540))
    ClearScenaFlags(ScenaFlag(0x00A8, 1, 0x541))
    ClearScenaFlags(ScenaFlag(0x00A8, 2, 0x542))
    ClearScenaFlags(ScenaFlag(0x00A8, 3, 0x543))
    ClearScenaFlags(ScenaFlag(0x00A8, 4, 0x544))
    ClearScenaFlags(ScenaFlag(0x00A8, 5, 0x545))
    ClearScenaFlags(ScenaFlag(0x00A8, 6, 0x546))

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000006, 'loc_AF2'),
        (0x00000005, 'loc_B01'),
        (0x00000004, 'loc_B10'),
        (0x00000003, 'loc_B1F'),
        (0x00000002, 'loc_B2E'),
        (0x00000001, 'loc_B3D'),
        (0x00000000, 'loc_B4C'),
        (-1, 'loc_B73'),
    )

    def _loc_AF2(): pass

    label('loc_AF2')

    SetScenaFlags(ScenaFlag(0x00A8, 0, 0x540))
    NewScene('ED6_DT01/T3111._SN', 106, 0, 0)
    IdleLoop()

    Jump('loc_B73')

    def _loc_B01(): pass

    label('loc_B01')

    SetScenaFlags(ScenaFlag(0x00A8, 1, 0x541))
    NewScene('ED6_DT01/T3111._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_B73')

    def _loc_B10(): pass

    label('loc_B10')

    SetScenaFlags(ScenaFlag(0x00A8, 2, 0x542))
    NewScene('ED6_DT01/T3114._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_B73')

    def _loc_B1F(): pass

    label('loc_B1F')

    SetScenaFlags(ScenaFlag(0x00A8, 3, 0x543))
    NewScene('ED6_DT01/T3114._SN', 106, 0, 0)
    IdleLoop()

    Jump('loc_B73')

    def _loc_B2E(): pass

    label('loc_B2E')

    SetScenaFlags(ScenaFlag(0x00A8, 4, 0x544))
    NewScene('ED6_DT01/T3114._SN', 112, 0, 0)
    IdleLoop()

    Jump('loc_B73')

    def _loc_B3D(): pass

    label('loc_B3D')

    SetScenaFlags(ScenaFlag(0x00A8, 5, 0x545))
    NewScene('ED6_DT01/T3119._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_B73')

    def _loc_B4C(): pass

    label('loc_B4C')

    SetScenaFlags(ScenaFlag(0x00A8, 6, 0x546))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B67',
    )

    NewScene('ED6_DT01/T3104._SN', 104, 0, 0)
    IdleLoop()

    Jump('loc_B70')

    def _loc_B67(): pass

    label('loc_B67')

    NewScene('ED6_DT01/T3101._SN', 104, 0, 0)
    IdleLoop()

    def _loc_B70(): pass

    label('loc_B70')

    Jump('loc_B73')

    def _loc_B73(): pass

    label('loc_B73')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
