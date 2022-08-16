import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1121_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1121_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1121_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_B9',
    )

    OP_2A(0x00B5, 0x00B6, 0xFFFF)

    Jump('loc_159')

    def _loc_B9(): pass

    label('loc_B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_D8',
    )

    OP_2A(0x00B1, 0x00B2, 0x00B3, 0x0078, 0x007A, 0x007B, 0x00B4, 0x0079, 0x007C, 0xFFFF)

    Jump('loc_159')

    def _loc_D8(): pass

    label('loc_D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_F3',
    )

    OP_2A(0x00B1, 0x00B2, 0x00B3, 0x0078, 0x007A, 0x007B, 0x00B4, 0xFFFF)

    Jump('loc_159')

    def _loc_F3(): pass

    label('loc_F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_10C',
    )

    OP_2A(0x00B1, 0x00B2, 0x00B3, 0x0078, 0x007A, 0x007B, 0xFFFF)

    Jump('loc_159')

    def _loc_10C(): pass

    label('loc_10C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_125',
    )

    OP_2A(0x00B1, 0x00B2, 0x00B3, 0x0078, 0x007A, 0x007B, 0xFFFF)

    Jump('loc_159')

    def _loc_125(): pass

    label('loc_125')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '没发出什么委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_159(): pass

    label('loc_159')

    TalkEnd(0x00FF)

    Return()

# id: 0x0001 offset: 0x15D
@scena.Code('func_01_15D')
def func_01_15D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_476',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480164V#1002F卡片里说的地方……',
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
        'loc_265',
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

    Jump('loc_472')

    def _loc_265(): pass

    label('loc_265')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_317',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480169V#072F嗯，是有这可能……',
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

    Jump('loc_472')

    def _loc_317(): pass

    label('loc_317')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C9',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480172V#030F唔，是有这可能……',
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

    Jump('loc_472')

    def _loc_3C9(): pass

    label('loc_3C9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_472',
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

    def _loc_472(): pass

    label('loc_472')

    TalkEnd(0x00FF)

    Return()

    def _loc_476(): pass

    label('loc_476')

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 27040, 0, 22430, 270)
    ChrSetPos(0x00F7, 28320, 0, 22190, 270)
    ChrSetPos(0x00F8, 29010, 0, 21500, 270)
    ChrSetPos(0x00F9, 27620, 0, 24010, 220)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4DE',
    )

    ChrSetPos(0x0004, 29870, 0, 22190, 270)

    def _loc_4DE(): pass

    label('loc_4DE')

    CameraMove(28000, 0, 23000, 0)
    OP_67(0, 4340, -10000, 0)
    CameraSetDistance(2790, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '调查书本\n',
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
            '#0010480243V#1002F好，找到喽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480244V#1015F嗯……写着什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0101, 17)
    OP_0D()
    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS124._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170480245V　想找到第三把钥匙，\n',
            '就去检查『被托起的棺材』吧。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480246V#1007F呼，看来\n',
            '是答对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_703',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480247V#047F将『ＦＴＨＫＣ２Ｅ』\n',
            '各推进一个字的话，\n',
            '『ＧＵＩＬＤ３Ｆ』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480248V#040F也就是说\n',
            '在协会３楼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B8')

    def _loc_703(): pass

    label('loc_703')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_794',
    )

    ChrTalk(
        0x0107,
        (
            '#0070480249V#060F将『ＦＴＨＫＣ２Ｅ』\n',
            '各推进一个字的话，\n',
            '『ＧＵＩＬＤ３Ｆ』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070480250V也就是在\n',
            '协会３楼的意思了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B8')

    def _loc_794(): pass

    label('loc_794')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_82A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480251V#035F将『ＦＴＨＫＣ２Ｅ』\n',
            '各推进一个字的话，\n',
            '『ＧＵＩＬＤ３Ｆ』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480252V#030F也就是在\n',
            '协会３楼的意思了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B8')

    def _loc_82A(): pass

    label('loc_82A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8B8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480253V#020F将『ＦＴＨＫＣ２Ｅ』\n',
            '各推进一个字的话，\n',
            '『ＧＵＩＬＤ３Ｆ』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480254V也就是在\n',
            '协会３楼的意思了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8B8(): pass

    label('loc_8B8')

    ChrTalk(
        0x0101,
        (
            '#0010480255V#1015F唔，虽说解开谜题了\n',
            '是很好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480256V#1007F但没、没想到居然\n',
            '在协会里做了手脚呢。',
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
        'loc_99F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480257V#057F哼，真是\n',
            '太目中无人了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480258V下次碰到那家伙，\n',
            '可要好好回敬一番。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    Jump('loc_B08')

    def _loc_99F(): pass

    label('loc_99F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A1B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480259V#075F啊啊，真是\n',
            '被藐视了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480260V#072F下次碰上那家伙，\n',
            '可得好好回敬一番。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    Jump('loc_B08')

    def _loc_A1B(): pass

    label('loc_A1B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A90',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480261V#025F咳，真是\n',
            '被小看了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480262V下次碰上那家伙，\n',
            '好好回敬他一番吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    Jump('loc_B08')

    def _loc_A90(): pass

    label('loc_A90')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B08',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480263V#031F呼，真是\n',
            '被小瞧了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480264V下次碰上那家伙，\n',
            '必须好好地回敬他一番呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    def _loc_B08(): pass

    label('loc_B08')

    ChrTalk(
        0x0101,
        (
            '#0010480265V#1002F嗯，那可不是。',
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
        'loc_BAB',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480266V#030F那，下一条线索是\n',
            '『被托起的棺材』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480267V可能这也是\n',
            '某种『比喻』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    Jump('loc_D19')

    def _loc_BAB(): pass

    label('loc_BAB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C26',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480268V#022F那，下一条线索\n',
            '『被托起的棺材』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480269V我想大概\n',
            '是某种『比喻』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    Jump('loc_D19')

    def _loc_C26(): pass

    label('loc_C26')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C9F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070480270V#062F下一条线索是\n',
            '『被托起的棺材』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070480271V我想大概\n',
            '是某种『比喻』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    Jump('loc_D19')

    def _loc_C9F(): pass

    label('loc_C9F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D19',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480272V#042F那么，下一条线索是\n',
            '『被托起的棺材』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480273V恐怕是\n',
            '某种『比喻』吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    def _loc_D19(): pass

    label('loc_D19')

    ChrTalk(
        0x0101,
        (
            '#0010480274V#1002F这么想没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480275V因为真正的『棺材』之类的\n',
            '东西哪可能在这附近随便乱放。',
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
        'loc_DFB',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480276V#073F噢，相当\n',
            '敏锐的洞察力啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480277V#070F那么就尽快去确认那个\n',
            '『棺材』的原形吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F61')

    def _loc_DFB(): pass

    label('loc_DFB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E77',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480278V#051F呵，看来已经\n',
            '看破对方的手法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480279V那么就立刻去确认那个\n',
            '『棺材』的原形吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F61')

    def _loc_E77(): pass

    label('loc_E77')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EEC',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480280V#020F哎呀，洞察力挺敏锐的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480281V那么就尽快去确认那个\n',
            '『棺材』的原形吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F61')

    def _loc_EEC(): pass

    label('loc_EEC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F61',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480282V#030F呼，观察力\n',
            '也敏锐起来了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480283V那么就尽快去确认那个\n',
            '『棺材』的原形吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F61(): pass

    label('loc_F61')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_28(0x0078, 0x01, 0x0010)
    OP_28(0x0078, 0x01, 0x0020)
    OP_64(0x03, 0x0001)

    @scena.Lambda('lambda_0F7D')
    def lambda_0F7D():
        ChrWalkTo(0x0000, 27700, 0, 22200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0F7D)

    @scena.Lambda('lambda_0F98')
    def lambda_0F98():
        ChrWalkTo(0x0001, 27700, 0, 22200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_0F98)

    @scena.Lambda('lambda_0FB3')
    def lambda_0FB3():
        ChrWalkTo(0x0002, 27700, 0, 22200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_0FB3)

    @scena.Lambda('lambda_0FCE')
    def lambda_0FCE():
        ChrWalkTo(0x0003, 27700, 0, 22200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_0FCE)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_100A',
    )

    @scena.Lambda('lambda_0FF5')
    def lambda_0FF5():
        ChrWalkTo(0x0004, 27700, 0, 22200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0004, 0x0000, lambda_0FF5)

    def _loc_100A(): pass

    label('loc_100A')

    CameraMove(27700, 0, 22200, 1000)
    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0001, 0x0000)
    WaitForThreadExit(0x0002, 0x0000)
    WaitForThreadExit(0x0003, 0x0000)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1040',
    )

    WaitForThreadExit(0x0004, 0x0000)

    def _loc_1040(): pass

    label('loc_1040')

    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0x1043
@scena.Code('func_02_1043')
def func_02_1043():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x381),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1050',
    )

    Return()

    def _loc_1050(): pass

    label('loc_1050')

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1062',
    )

    Return()

    def _loc_1062(): pass

    label('loc_1062')

    MapSetFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_CD(0x0008)"),
            Expr.Return,
        ),
        'loc_109D',
    )

    Call(1, 0x0003)

    Jump('loc_1142')

    def _loc_109D(): pass

    label('loc_109D')

    If(
        (
            (Expr.Eval, "OP_CD(0x03E8)"),
            Expr.Return,
        ),
        'loc_10AC',
    )

    Call(1, 0x0003)

    Jump('loc_1142')

    def _loc_10AC(): pass

    label('loc_10AC')

    If(
        (
            (Expr.Eval, "OP_CD(0x00FF)"),
            Expr.Return,
        ),
        'loc_1104',
    )

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '试着出示了照片，\n',
            '但似乎没有见过的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_1142')

    def _loc_1104(): pass

    label('loc_1104')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '附近没有人可以确认照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_1142(): pass

    label('loc_1142')

    OP_0D()
    MapClearFlags(0x00000080)

    Return()

# id: 0x0003 offset: 0x1149
@scena.Code('func_03_1149')
def func_03_1149():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1211',
    )

    ChrTalk(
        0x0008,
        (
            '#0380490554V#632F原来如此，在做公告板上\n',
            '找人的委托啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380490555V我想这工作大概不轻松，\n',
            '尽量想办法找吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380490556V因为来委托工作的女人\n',
            '除了我们以外\n',
            '已经没有别人可依靠了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1288')

    def _loc_1211(): pass

    label('loc_1211')

    ChrTalk(
        0x0008,
        (
            '#0380490557V#632F因为来委托工作的女人\n',
            '已经没有别人可依靠了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380490558V我想这工作大概不轻松，\n',
            '尽量想办法找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1288(): pass

    label('loc_1288')

    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
