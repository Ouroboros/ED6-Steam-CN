import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0136_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0136_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0136_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
    EventBegin(0x00)
    ChrSetDirection(0x000B, 270, 0)
    Fade(1000)
    ChrSetPos(0x0101, -84710, 0, 119250, 270)
    ChrSetPos(0x0103, -85200, 0, 120650, 225)
    ChrSetPos(0x00F8, -83460, 0, 119250, 270)
    ChrSetPos(0x00F9, -83730, 0, 120510, 225)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_129',
    )

    ChrSetPos(0x00F9, -83460, 0, 119250, 270)
    ChrSetPos(0x00F8, -83730, 0, 120510, 225)

    def _loc_129(): pass

    label('loc_129')

    CameraMove(-85090, 0, 119630, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_174',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_174(): pass

    label('loc_174')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F4',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇完成过【小猫的搜索】】\n'),
            TXT(0x01, '【◇没完成过【小猫的搜索】】\n'),
        ),
    )

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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1E8'),
        (0x00000001, 'loc_1EE'),
        (-1, 'loc_1F4'),
    )

    def _loc_1E8(): pass

    label('loc_1E8')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_1F4')

    def _loc_1EE(): pass

    label('loc_1EE')

    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_1F4')

    def _loc_1F4(): pass

    label('loc_1F4')

    ChrTalk(
        0x000B,
        (
            '#1090460987V真是的～\n',
            '怎么办～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x000B)
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#1090460988V……咦～～？\n',
            '你们是～～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2B3',
    )

    ChrTalk(
        0x0101,
        (
            '#0010460989V#1006F好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460990V是看了公告板而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_303')

    def _loc_2B3(): pass

    label('loc_2B3')

    ChrTalk(
        0x0101,
        (
            '#0010460991V#1000F嗯，我们是看了告示板来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460992V您就是伊娜女士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_303(): pass

    label('loc_303')

    ChrTalk(
        0x000B,
        (
            '#1090460993V哎呀，麻烦你们了，\n',
            '这么晚还过来～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090460994V开门见山～～\n',
            '能不能帮我寻找安莉尔～～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3FA',
    )

    ChrTalk(
        0x0101,
        (
            '#0010460995V#1004F安、安莉尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460996V#1016F那只猫……\n',
            '又走失了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090460997V怎么样～～？\n',
            '你们愿意帮忙吗～～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FA(): pass

    label('loc_3FA')

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_452',
    )

    Call(1, 0x0002)

    Jump('loc_56E')

    def _loc_452(): pass

    label('loc_452')

    ChrTalk(
        0x0101,
        (
            '#0010460998V#1015F抱歉啊，现在不行。\n',
            '手头还有点事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090460999V哎呀，这就不好办了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461000V可是可是，这是你们的工作，\n',
            '也没办法哦～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461001V#020F多谢您的理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461002V#1000F不过有空了\n',
            '我们马上就会回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461003V嗯，拜托了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0074, 0x01, 0x8000)

    def _loc_56E(): pass

    label('loc_56E')

    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x571
@scena.Code('func_01_571')
def func_01_571():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -84710, 0, 119250, 270)
    ChrSetPos(0x0103, -85200, 0, 120650, 225)
    ChrSetPos(0x00F8, -83460, 0, 119250, 270)
    ChrSetPos(0x00F9, -83730, 0, 120510, 225)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5EB',
    )

    ChrSetPos(0x00F9, -83460, 0, 119250, 270)
    ChrSetPos(0x00F8, -83730, 0, 120510, 225)

    def _loc_5EB(): pass

    label('loc_5EB')

    ChrTurnDirection(0x000B, 0x0101, 0)
    CameraMove(-85090, 0, 119630, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#1090461004V哎呀～～游击士小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461005V愿意帮我寻找\n',
            '安莉尔了吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6DB',
    )

    Call(1, 0x0002)

    Jump('loc_78D')

    def _loc_6DB(): pass

    label('loc_6DB')

    ChrTalk(
        0x0101,
        (
            '#0010461006V#1015F抱歉啊，现在不行。\n',
            '还有点事情…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461007V哎呀～～是吗～～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461008V#1000F有了时间的话\n',
            '我们马上就会回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461003V嗯，拜托了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_78D(): pass

    label('loc_78D')

    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0x790
@scena.Code('func_02_790')
def func_02_790():
    ChrTalk(
        0x0101,
        (
            '#0010461010V#1000F嗯……现在算是ＯＫ了哟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461011V#1015F虽然对现在来做这件事\n',
            '合不合适有些疑惑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030461012V#026F不过处理细小事件\n',
            '也是游击士的重要责任啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461013V#027F我们会尽力帮助你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461014V嗯～这就足够了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x000B, 400)

    ChrTalk(
        0x0103,
        (
            '#0030461015V#020F那就请你重新说明\n',
            '一下委托的内容吧。',
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
        'loc_940',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461016V#050F你好像在\n',
            '寻找一只猫呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050461017V就是刚才提到的\n',
            '那只名叫安莉尔的猫吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A95')

    def _loc_940(): pass

    label('loc_940')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9B2',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461018V#070F你好像在\n',
            '寻找一只猫呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080461019V就是刚才提到的\n',
            '那只名叫安莉尔的猫吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A95')

    def _loc_9B2(): pass

    label('loc_9B2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A26',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461020V#030F你好像在寻找\n',
            '一只猫呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040461021V就是刚才提到的\n',
            '那只名叫安莉尔的猫吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A95')

    def _loc_A26(): pass

    label('loc_A26')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A95',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461022V#040F你好像在\n',
            '寻找一只猫呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060461023V就是刚才提到的\n',
            '那只名叫安莉尔的猫吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A95(): pass

    label('loc_A95')

    ChrTalk(
        0x000B,
        (
            '#1090461024V嗯，是啊～～\n',
            '就是在找安莉尔～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461025V我只是稍微午睡了一会儿。\n',
            '它就不见了～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_B52',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010461026V#1007F（完、完全和上次一样啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B52(): pass

    label('loc_B52')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BCD',
    )

    ChrTalk(
        0x0107,
        (
            '#0070461027V#064F就是说从中午以后\n',
            '就一直没回来过？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070461028V#063F那、那倒是\n',
            '让人有点担心了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D03')

    def _loc_BCD(): pass

    label('loc_BCD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C34',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461029V#043F就是说已经\n',
            '半天没回来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060461030V那倒是让人挺担心的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D03')

    def _loc_C34(): pass

    label('loc_C34')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C9E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461031V#032F就是说……\n',
            '已经失踪半天了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040461032V嗯，那倒是挺\n',
            '让人担心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D03')

    def _loc_C9E(): pass

    label('loc_C9E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D03',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461033V#074F就是说已经\n',
            '失踪半天了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080461034V嗯，那倒是挺\n',
            '有点令人担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D03(): pass

    label('loc_D03')

    ChrTalk(
        0x0103,
        (
            '#0030461035V#022F您觉得它\n',
            '会去哪里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461036V能不能告诉我们它\n',
            '平时经常去的地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0103, 400)

    ChrTalk(
        0x000B,
        (
            '#1090461037V嗯～～不知道能不能算是线索～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461038V根据阿姨我的直觉\n',
            '飞船坪好像很可疑～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461039V#1011F飞船坪！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#1090461040V听整备人员说\n',
            '好像有人看到了猫～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461041V而且还是褐色的，\n',
            '一定是安莉尔～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461042V#1002F是、是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461043V#1015F呜…猫的毛色\n',
            '记在手册上。',
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
        'loc_F13',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461044V#070F嗯，这可是条有用的线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080461045V先从这条线\n',
            '开始调查怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_103D')

    def _loc_F13(): pass

    label('loc_F13')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F78',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461046V#051F这可是条有用的线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050461047V先从这条线\n',
            '开始调查也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_103D')

    def _loc_F78(): pass

    label('loc_F78')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FDF',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461048V#030F啊，这可是条有用的线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040461049V先从这条线\n',
            '开始查怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_103D')

    def _loc_FDF(): pass

    label('loc_FDF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_103D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461050V#040F……很有用的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060461051V那就先从这一点\n',
            '开始调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_103D(): pass

    label('loc_103D')

    ChrTalk(
        0x0103,
        (
            '#0030461052V#020F嗯，这线索有调查的价值。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461053V总之我们先\n',
            '去飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010461054V#1006F嗯……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461055V看来我的说明\n',
            '已经足够了～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461056V那么，阿姨我\n',
            '就在这里等着～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461057V游击士们，\n',
            '接下来就拜托你们了～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010461058V#1006F找到了我们会来报告的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461059V#020F嗯，那就先这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0074, 0x01, 0x0001)
    OP_28(0x0074, 0x01, 0x0002)
    OP_28(0x0074, 0x01, 0x0004)
    OP_28(0x0074, 0x04, 0x04)
    OP_28(0x0074, 0x04, 0x08)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

# id: 0x0003 offset: 0x11C9
@scena.Code('func_03_11C9')
def func_03_11C9():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetFlags(0x000F, 0x0004)
    ChrSetPos(0x000B, -85600, 0, 119540, 90)
    ChrSetPos(0x000C, -85720, 0, 120310, 90)
    ChrSetPos(0x000F, -84190, 0, 123070, 330)
    ChrSetPos(0x000E, -83500, 580, 117300, 270)
    ChrSetPos(0x000D, -83030, 580, 116830, 315)
    CreateThread(0x000F, 0x01, 0x00, 0x0002)
    CreateThread(0x000E, 0x01, 0x00, 0x0003)
    CreateThread(0x000D, 0x01, 0x00, 0x0003)
    OP_4A(0x000B, 255)
    ChrSetPos(0x0101, -83980, 0, 119500, 270)
    ChrSetPos(0x0103, -83580, 0, 120500, 273)
    ChrSetPos(0x00F8, -82420, 0, 119000, 270)
    ChrSetPos(0x00F9, -82100, 0, 120000, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12DE',
    )

    ChrSetPos(0x00F9, -82420, 0, 119000, 270)
    ChrSetPos(0x00F8, -82100, 0, 120000, 270)

    def _loc_12DE(): pass

    label('loc_12DE')

    CameraMove(-85080, 0, 120200, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#1090461333V真是的～～\n',
            '阿姨我可吓了一跳～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461334V我家的安莉尔竟然\n',
            '做了妈妈回来了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461335V#1016F#3P我们才\n',
            '大吃一惊呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461336V没想到会\n',
            '变成这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461337V#020F#2P总之肯定是\n',
            '母子都平安了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461338V今后也请好好\n',
            '养育它们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461339V那是当然～～\n',
            '因为它们是我重要的家人～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461340V可是可是～～\n',
            '今后也不容易啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461341V为小猫们起名字\n',
            '也是一项工作～～',
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
        'loc_150C',
    )

    ChrTalk(
        0x0107,
        (
            '#0070461342V#560F请给它们起几个\n',
            '可爱的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E0')

    def _loc_150C(): pass

    label('loc_150C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1553',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461343V#040F嗯，请给它们起几个\n',
            '可爱的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E0')

    def _loc_1553(): pass

    label('loc_1553')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15A0',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461344V#030F呵呵，期待你给它们起几个\n',
            '好听的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E0')

    def _loc_15A0(): pass

    label('loc_15A0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15E0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461345V#070F嗯，请给它们起几个\n',
            '好名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15E0(): pass

    label('loc_15E0')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_15ED',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_15ED(): pass

    label('loc_15ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_166D',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇完成过【小猫的搜索】】\n'),
            TXT(0x01, '【◇没完成过【小猫的搜索】】\n'),
        ),
    )

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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1661'),
        (0x00000001, 'loc_1667'),
        (-1, 'loc_166D'),
    )

    def _loc_1661(): pass

    label('loc_1661')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_166D')

    def _loc_1667(): pass

    label('loc_1667')

    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_166D')

    def _loc_166D(): pass

    label('loc_166D')

    ChrTalk(
        0x000B,
        (
            '#1090461346V嗯，交给我吧～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_18B2',
    )

    ChrTalk(
        0x000B,
        (
            '#1090461347V啊～不过各位。\n',
            '请稍微等一下再回去～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461348V还有事要\n',
            '跟你们说～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010461349V#1015F#3P请问还有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461350V嗯～因为这已经是第二次\n',
            '受到游击士的帮助了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461351V是的～请你们收下这个㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['祭师之豆']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['祭师之豆'], 1)

    ChrTalk(
        0x000B,
        (
            '#1090461352V这是阿姨做礼拜时\n',
            '喜欢用的物品～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1090461353V能让人心情平静下来，\n',
            '所以请你们一定要用用看㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461354V#1011F#3P呵呵～是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461355V#1000F嗯，谢谢。\n',
            '那我们就不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18B2(): pass

    label('loc_18B2')

    ChrTalk(
        0x000B,
        (
            '#1090461356V那么，各位路上\n',
            '也请小心～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x000C, 255)
    ChrTurnDirection(0x000C, 0x0101, 400)
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x000C,
        (
            '#1100461357V喵～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x000D, 255)
    ChrTurnDirection(0x000D, 0x0101, 400)
    PlaySE(348, 0x00, 0x64)

    ChrTalk(
        0x000D,
        (
            '#3450461358V咪～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/T0101._SN', 116, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
