import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0111_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0111_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0111_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    ChrTalk(
        0x000F,
        (
            '#0940470999V#2P唉～～……真伤脑筋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471000V#2P好不容易重新开工的时候\n',
            '那东西却偏偏不见了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471001V#1000F看上去似乎在烦恼什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x000F)
    ChrTurnDirection(0x000F, 0x0101, 400)

    ChrTalk(
        0x000F,
        (
            '#0940471002V#2P喔！是你们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471003V#2P难不成是看了公告板\n',
            '才来我这里的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471004V#1011F啊，嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471005V#022F是不是被偷了什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0103, 400)

    ChrTalk(
        0x000F,
        (
            '#0940471006V#2P啊啊，不知道怎么回事，\n',
            '现在正在发愁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471007V#2P希望能马上开始调查，\n',
            '你们方便吗？',
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

    MenuEnd(0x000D)

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
            (Expr.PushReg, 0xD),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E6',
    )

    Call(1, 0x0002)

    Jump('loc_3E3')

    def _loc_2E6(): pass

    label('loc_2E6')

    ChrTalk(
        0x0101,
        (
            '#0010471008V#1015F抱歉，现在不能\n',
            '马上开始。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471009V我还会回来的，\n',
            '那时再听您说明吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0101, 400)

    ChrTalk(
        0x000F,
        (
            '#0940471010V#2P嗯……看来\n',
            '是忙得很呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471011V#2P唉，没办法了。\n',
            '那下次再麻烦你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471012V#020F嗯，等等再过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0077, 0x01, 0x8000)
    ChrSetDirection(0x000F, 90, 0)

    def _loc_3E3(): pass

    label('loc_3E3')

    Return()

# id: 0x0001 offset: 0x3E4
@scena.Code('func_01_3E4')
def func_01_3E4():
    ChrTurnDirection(0x000F, 0x0101, 400)

    ChrTalk(
        0x000F,
        (
            '#0940471013V#2P哦，是你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471014V#2P如何？\n',
            '可以开始调查了吗？',
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

    MenuEnd(0x000D)

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
            (Expr.PushReg, 0xD),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_492',
    )

    Call(1, 0x0002)

    Jump('loc_51E')

    def _loc_492(): pass

    label('loc_492')

    ChrTalk(
        0x0101,
        (
            '#0010471015V#1007F抱歉，还不行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471016V#2P怎么，你们一直～\n',
            '都这么忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0940471017V唉，没办法。\n',
            '下次再麻烦你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 90, 0)

    def _loc_51E(): pass

    label('loc_51E')

    Return()

# id: 0x0002 offset: 0x51F
@scena.Code('func_02_51F')
def func_02_51F():
    ChrTalk(
        0x0101,
        (
            '#0010471018V#1006F没问题。\n',
            '随时都ＯＫ哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0101, 400)

    ChrTalk(
        0x000F,
        (
            '#0940471019V#2P哦，这可帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471020V#2P那么，在开始关键的\n',
            '说明之前──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x000E, 255)
    ChrTurnDirection(0x000F, 0x000E, 400)

    ChrTalk(
        0x000F,
        (
            '#0940471021V#2P……呼，阿妮娅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    @scena.Lambda('lambda_05F8')
    def lambda_05F8():
        ChrTurnDirection(0x00F9, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_05F8)

    @scena.Lambda('lambda_0606')
    def lambda_0606():
        ChrTurnDirection(0x00F6, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x00F6, 0x0001, lambda_0606)

    Sleep(120)

    @scena.Lambda('lambda_0619')
    def lambda_0619():
        ChrTurnDirection(0x00F7, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0619)

    @scena.Lambda('lambda_0627')
    def lambda_0627():
        ChrTurnDirection(0x00F8, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0627)

    ChrTurnDirection(0x000E, 0x000F, 400)

    ChrTalk(
        0x000E,
        (
            '#3620471022V爸爸，什么事～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471023V#2P爸爸现在\n',
            '有重要的事要谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471024V#2P不好意思，你能去\n',
            '找妈妈念故事书好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3620471025V嗯，明白了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000D, 400)

    ChrTalk(
        0x000E,
        (
            '#3620471026V妈妈～念故事书给我听～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471027V#1001F啊哈哈，原来如此～\n',
            '还有这样那样的准备工作要做啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471028V#525F您费心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    EventBegin(0x00)
    ChrSetPos(0x0101, 1850, 0, 31530, 90)
    ChrSetPos(0x0103, 1160, 0, 32390, 90)
    ChrSetPos(0x00F8, 520, 0, 30850, 90)
    ChrSetPos(0x00F9, 100, 0, 31910, 90)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F7',
    )

    ChrSetPos(0x00F9, 520, 0, 30850, 90)
    ChrSetPos(0x00F8, 100, 0, 31910, 90)

    def _loc_7F7(): pass

    label('loc_7F7')

    ChrSetPos(0x000F, 3600, 0, 31530, 270)
    ChrSetPos(0x000E, -5340, 0, 35800, 0)
    CameraMove(3340, 0, 32130, 0)
    OP_67(0, 4370, -10000, 0)
    CameraSetDistance(2960, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000F,
        (
            '#0940471029V──好了，其他事都解决了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471030V首先，我先说明一下\n',
            '发生了什么事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471031V#1006F#4P嗯，请说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471032V#020F#5P嗯，麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471033V不见了的东西是\n',
            '玛鲁加矿山的管理委任书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471034V这是女王陛下授予的\n',
            '重要的证明书……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471035V里面记载了委任矿山长\n',
            '负责开采管理的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471036V玛鲁加矿山的所有权\n',
            '也是归女王陛下嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471037V要有那个委任书，\n',
            '我们才能采掘矿山。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471038V#1004F#4P是，是这样的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471039V#1015F矿山是女王陛下所有，\n',
            '我以前完全不知道。',
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
        'loc_B1F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471040V#030F实际上虽说是民主国家，\n',
            '但从法律上看这里还是女王的国家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040471041V国家资产的一部分\n',
            '归属于女王是当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C9E')

    def _loc_B1F(): pass

    label('loc_B1F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BA9',
    )

    ChrTalk(
        0x0108,
        (
            '#0080471042V#070F不过，虽说是民主国家，\n',
            '这里也还算是女王的国家嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080471043V矿山是王室的东西\n',
            '一点儿也不奇怪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C9E')

    def _loc_BA9(): pass

    label('loc_BA9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C25',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471044V#040F嗯嗯、王国宪章里\n',
            '是这么规定的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060471045V当然，委任书\n',
            '其实不过是形式上的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C9E')

    def _loc_C25(): pass

    label('loc_C25')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C9E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471046V#050F嗯，这个利贝尔\n',
            '在形式上还是女王的国家嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050471047V王室拥有一两座山\n',
            '也不奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C9E(): pass

    label('loc_C9E')

    ChrTalk(
        0x0103,
        (
            '#0030471048V#020F#5P原来如此，不过因此\n',
            '才有委任书之类的东西吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471049V虽说是形式上，\n',
            '但玛鲁加矿山的确归女王所有……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471050V开采七耀石\n',
            '确实需要一些权限。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471051V嗯，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471052V现在你们明白是\n',
            '多么重要的东西被盗了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471053V#1002F#4P嗯……\n',
            '明白是很重要的东西了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471054V那，关于事件的经过──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471055V委任书不见了\n',
            '是何时发现的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471056V哦，就是今天早上的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471057V发现存放委任书的\n',
            '小箱子开着，就觉得不对劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471058V看看箱子里，\n',
            '果然不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471059V#027F#5P那么，发现出了事\n',
            '还没过多久……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471060V断定是失窃\n',
            '说不定还稍微早了点。',
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
        'loc_F8D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471061V#053F啊啊，我也同意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050471062V#050F也应该考虑一下\n',
            '是不是小孩子的恶作剧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B0')

    def _loc_F8D(): pass

    label('loc_F8D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FE5',
    )

    ChrTalk(
        0x0108,
        (
            '#0080280451V#070F啊啊，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080471064V说不定是孩子的恶作剧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B0')

    def _loc_FE5(): pass

    label('loc_FE5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_104C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471065V#030F呼，我也同意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040471066V孩子们的恶作剧\n',
            '这种情况也应该考虑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B0')

    def _loc_104C(): pass

    label('loc_104C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10B0',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471067V#042F嗯，也可能是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060471068V或许是孩子们\n',
            '弄丢的也说不定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10B0(): pass

    label('loc_10B0')

    ChrTalk(
        0x000F,
        (
            '#0940471069V如果真是这样\n',
            '我也就放心了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471070V可惜不是。\n',
            '这次绝对不会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471071V#1011F#4P啊，为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471072V#022F#5P难不成……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471073V有什么可以证明\n',
            '被盗的线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471074V呼，不愧是专业人员。\n',
            '其实正是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471075V──请看这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS124._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170471076V　美丽的公主及其随从啊。　　\n',
            '　  女王真迹在吾手中。　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170471077V　　   若想取回\n',
            '　就从混沌中寻找真实吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170471078V　　　　　　　　　　　　　　　　\n',
            '　　　 第一把钥匙在市内。 　　　\n',
            '询问『坐在女神旁边的人』。\n',
            '　　　　　　　　　　　　　　　　',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#0940471079V──这张卡片\n',
            '是取而代之放在盒里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471080V怎么看都是盗窃者留下的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x04)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_139B',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_139B(): pass

    label('loc_139B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1425',
    )

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
            TXT(0x00, '【◇查看2章或3章中的布卢布兰任务】\n'),
            TXT(0x01, '【◇没有变更】\n'),
        ),
    )

    MenuEnd(0x000D)

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

    Switch(
        (
            (Expr.PushReg, 0xD),
            Expr.Return,
        ),
        (0x00000000, 'loc_141C'),
        (0x00000001, 'loc_1422'),
        (-1, 'loc_1425'),
    )

    def _loc_141C(): pass

    label('loc_141C')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_1425')

    def _loc_1422(): pass

    label('loc_1422')

    Jump('loc_1425')

    def _loc_1425(): pass

    label('loc_1425')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_1716',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1472',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_146F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471081V#053F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_146F')

    def _loc_146F(): pass

    label('loc_146F')

    Jump('loc_14A0')

    def _loc_1472(): pass

    label('loc_1472')

    ChrTalk(
        0x0103,
        (
            '#0030471082V#025F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_14A0(): pass

    label('loc_14A0')

    ChrTalk(
        0x0101,
        (
            '#0010471083V#1007F#4P啊呼……………………',
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
        'loc_1506',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471084V#047F呼……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1506(): pass

    label('loc_1506')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_153D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471085V#032F唔……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_153D(): pass

    label('loc_153D')

    OP_62(0x000F, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#0940471086V怎、怎么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471087V叹什么气呢。\n',
            '怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_162C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010471088V#1016F#4P唔，没什么，别在意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471089V#1007F#4P『怪盗绅士』布卢布兰……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471090V……真是个烦人的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1713')

    def _loc_162C(): pass

    label('loc_162C')

    ChrTalk(
        0x0101,
        (
            '#0010471091V#1016F#4P不、哪里～只是有点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471092V#025F#5P请别介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471093V唉，不管怎样……\n',
            '这下犯人就有了大致的目标吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471094V#1007F#4P『怪盗绅士』布卢布兰……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471090V……真是烦人的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1713(): pass

    label('loc_1713')

    Jump('loc_1960')

    def _loc_1716(): pass

    label('loc_1716')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_17DA',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1788',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471096V#057F哼、又是卡片谜题啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050471097V前不久不是也\n',
            '见过一样的手法吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17D7')

    def _loc_1788(): pass

    label('loc_1788')

    ChrTalk(
        0x0101,
        (
            '#0010471098V#1007F#4P卡、卡片谜题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471099V这手法好像在哪见过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17D7(): pass

    label('loc_17D7')

    Jump('loc_1835')

    def _loc_17DA(): pass

    label('loc_17DA')

    ChrTalk(
        0x0103,
        (
            '#0030471100V#027F#5P卡片展开的谜题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471101V……好像在哪儿\n',
            '见过类似的手法嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1835(): pass

    label('loc_1835')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1876',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471102V#042F艾丝蒂尔……\n',
            '这难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18E3')

    def _loc_1876(): pass

    label('loc_1876')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18AE',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471103V#032F唔，看来这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18E3')

    def _loc_18AE(): pass

    label('loc_18AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_18E3',
    )

    ChrTalk(
        0x0103,
        (
            '#0030471104V#023F#5P哎呀，有线索吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18E3(): pass

    label('loc_18E3')

    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010471105V#1002F#4P嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471106V『怪盗绅士』布卢布兰……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471107V看来是那家伙\n',
            '干得好事没错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1960(): pass

    label('loc_1960')

    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#0940471108V什、什么啊，\n',
            '那奇怪的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471109V就是偷了\n',
            '委任书的犯人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010471110V#1015F#4P虽然不能断言……\n',
            '我想很有这个可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471111V#1002F嗯，稍后再向您解释吧。\n',
            '不管怎样先开始调查才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471112V#022F#5P嗯，明智的选择……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471113V首先确认一下\n',
            '卡片的内容吧。',
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
        'loc_1B3E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471114V#032F必须要找到的是\n',
            '『坐在女神旁边的人』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040471115V#034F唉、怪盗绅士不知为何\n',
            '好像很喜欢用这手法嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C56')

    def _loc_1B3E(): pass

    label('loc_1B3E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BBB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471116V#050F必须找到的是、\n',
            '『坐在女神旁边的人』……吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050471117V#053F哼、相当\n',
            '夸张的小子嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C56')

    def _loc_1BBB(): pass

    label('loc_1BBB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C0C',
    )

    ChrTalk(
        0x0107,
        (
            '#0070471118V#062F必须找到的是、\n',
            '『坐在女神旁边的人』对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C56')

    def _loc_1C0C(): pass

    label('loc_1C0C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C56',
    )

    ChrTalk(
        0x0108,
        (
            '#0080471119V#072F必须找到的是\n',
            '『坐在女神旁边的人』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C56(): pass

    label('loc_1C56')

    ChrTalk(
        0x0101,
        (
            '#0010471120V#1003F#4P大概这也是什么\n',
            '某种『喻示』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471121V总之只有先在城里\n',
            '试着找找看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471122V看来调查方针\n',
            '也差不多定了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471123V小姑娘啊。\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471124V#1006F#4P嗯！我们会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471125V#020F#5P那么，赶快\n',
            '着手调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471126V哦！无论如何\n',
            '都要找回委任书！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0077, 0x04, 0x04)
    OP_28(0x0077, 0x04, 0x08)
    OP_28(0x0077, 0x01, 0x0001)
    OP_28(0x0077, 0x01, 0x0002)
    OP_28(0x0077, 0x01, 0x0004)
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(1850, 0, 31530, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0000, 1850, 0, 31530, 90)
    ChrSetPos(0x0001, 1850, 0, 31530, 90)
    ChrSetPos(0x0002, 1850, 0, 31530, 90)
    ChrSetPos(0x0003, 1850, 0, 31530, 90)
    ChrSetPos(0x000F, 4600, 0, 31530, 90)
    ChrSetPos(0x000E, 3140, 0, 32100, 180)
    OP_69(0x0000, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    OP_4B(0x000E, 255)
    ChrClearFlags(0x000F, 0x0010)
    EventEnd(0x04)

    Return()

# id: 0x0003 offset: 0x1E93
@scena.Code('func_03_1E93')
def func_03_1E93():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    ChrSetPos(0x000F, 4600, 0, 31530, 90)
    OP_4A(0x000F, 255)
    ChrSetPos(0x0101, 1850, 0, 31530, 90)
    ChrSetPos(0x0103, 1300, 0, 32390, 90)
    ChrSetPos(0x00F8, 520, 0, 30850, 90)
    ChrSetPos(0x00F9, 100, 0, 31910, 90)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F27',
    )

    ChrSetPos(0x00F9, 520, 0, 30850, 90)
    ChrSetPos(0x00F8, 100, 0, 31910, 90)

    def _loc_1F27(): pass

    label('loc_1F27')

    ChrSetPos(0x000E, -5340, 0, 35800, 0)
    OP_4A(0x000E, 255)
    CameraMove(3340, 0, 32130, 0)
    OP_67(0, 4370, -10000, 0)
    CameraSetDistance(2960, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x000F,
        (
            '#0940471241V──这样就放心了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 270, 400)
    ChrWalkTo(0x000F, 3600, 0, 31530, 2000, 0x00)

    ChrTalk(
        0x000F,
        (
            '#0940471242V哎呀～小姑娘……\n',
            '今天真多亏了你们啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471243V没想到这么简单\n',
            '就找回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471244V真不愧是洛连特的骄傲，\n',
            '年轻游击士们的希望啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471245V#1008F#4P啊、啊哈哈……\n',
            '过奖过奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471246V我们只是\n',
            '完成使命罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471247V哈哈哈，很谦虚嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471248V年轻的时候\n',
            '这种态度最重要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471249V哦，此外……\n',
            '忘了问一件重要的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471250V这次偷盗的犯人，\n',
            '已经抓到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471251V#1015F#4P呼……犯人是谁\n',
            '倒是有目标……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471252V#025F#5P但要抓住狐狸尾巴\n',
            '可没那么简单哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说明了犯人名为布卢布兰，\n',
            '以及他个人为了乐趣而犯罪的事实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000F,
        (
            '#0940471253V哦～国际犯罪组织成员啊。\n',
            '相当夸张的家伙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471254V那样的家伙居然特地\n',
            '跑来洛连特找麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471255V这种人脑袋里\n',
            '真不知到底在想些什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471256V#026F#5P唉、这个\n',
            '我们也有同感……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471257V#020F#5P不过，委任书的管理\n',
            '希望以后能更加严格。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471258V这次的事还好，\n',
            '万一被用于恐吓就危险了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471259V哦、是……\n',
            '确实不得不考虑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471260V嗯……但是我家的话，\n',
            '也没什么可以安全保管的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471261V干脆拜托市长\n',
            '放进金库吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471262V#1018F#4P啊，那也不错啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471263V#1016F不，不过，对这个犯人来说\n',
            '也不能说是绝对安全……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471264V（也有过被偷得\n',
            '干干净净的例子……）',
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
        'loc_2544',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471265V#051F但是，还是比这里好点吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050471266V这想法不错呢。\n',
            '应该去请求看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2690')

    def _loc_2544(): pass

    label('loc_2544')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25A9',
    )

    ChrTalk(
        0x0108,
        (
            '#0080471267V#070F话虽如此、\n',
            '一定比这里好些吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080471268V应该去请求看看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2690')

    def _loc_25A9(): pass

    label('loc_25A9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2623',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471269V#031F哈哈，怎么说呢，\n',
            '事件也告一段落了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040471270V你这想法不错呢。\n',
            '应该试试看才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2690')

    def _loc_2623(): pass

    label('loc_2623')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2690',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471271V#040F话虽如此、\n',
            '我想总比这里安全吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060471272V要不就试着\n',
            '去说说看怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2690(): pass

    label('loc_2690')

    ChrTalk(
        0x000F,
        (
            '#0940471273V是啊……\n',
            '过几天就去拜托看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471274V今天马上要去\n',
            '山那边才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471275V#023F#5P哎呀，还真是忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471276V啊啊，一直保持\n',
            '很稳定的出产量呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471277V无论怎么采掘七耀石\n',
            '都不见底哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471278V要使用导力器，\n',
            '七耀石是很重要的，都知道吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471279V#1008F#4P啊哈哈……\n',
            '这当然，我们非常了解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471280V但耀晶片总是不够，\n',
            '去工房都想哭呢。',
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
        'loc_2867',
    )

    ChrTalk(
        0x0107,
        (
            '#0070471281V#067F好的结晶回路\n',
            '成本也高嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_297B')

    def _loc_2867(): pass

    label('loc_2867')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28D6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471282V#034F呼，多么烦恼啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040471283V与我的实力相称的结晶回路\n',
            '总是很难到手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_297B')

    def _loc_28D6(): pass

    label('loc_28D6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2927',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471284V#040F嗯嗯，性能优良的结晶回路\n',
            '总是很难合成呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_297B')

    def _loc_2927(): pass

    label('loc_2927')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_297B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080471285V#070F哈哈，性能好的结晶回路\n',
            '可是相当花费耀晶片的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_297B(): pass

    label('loc_297B')

    ChrTalk(
        0x000F,
        (
            '#0940471286V怎么，原来\n',
            '这么辛苦的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471287V那你们就\n',
            '拿点耀晶片去好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471288V昨天正好拿了\n',
            '几袋回来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010471289V#1004F#4P咦？\n',
            '可，可以给我们些耀晶片吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471290V是啊，没必要\n',
            '那么客气啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471291V进了山里\n',
            '要多少就能挖多少的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471292V要哪个属性的耀晶片？',
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
        -1,
        -1,
        0,
        (
            TXT(0x00, '地之耀晶片×５００\n'),
            TXT(0x01, '水之耀晶片×５００\n'),
            TXT(0x02, '火之耀晶片×５００\n'),
            TXT(0x03, '风之耀晶片×５００\n'),
            TXT(0x04, '时之耀晶片×５００\n'),
            TXT(0x05, '空之耀晶片×５００\n'),
            TXT(0x06, '幻之耀晶片×５００\n'),
        ),
    )

    MenuEnd(0x000D)

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
            (Expr.PushReg, 0xD),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C1C',
    )

    ChrTalk(
        0x000F,
        (
            '#0940471293V哦，琥耀石啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddSepith(0x00, 500)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×５００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_2F6C')

    def _loc_2C1C(): pass

    label('loc_2C1C')

    If(
        (
            (Expr.PushReg, 0xD),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CA7',
    )

    ChrTalk(
        0x000F,
        (
            '#0940471294V哦，苍耀石啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddSepith(0x01, 500)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×５００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_2F6C')

    def _loc_2CA7(): pass

    label('loc_2CA7')

    If(
        (
            (Expr.PushReg, 0xD),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D32',
    )

    ChrTalk(
        0x000F,
        (
            '#0940471295V哦，红耀石啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddSepith(0x02, 500)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×５００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_2F6C')

    def _loc_2D32(): pass

    label('loc_2D32')

    If(
        (
            (Expr.PushReg, 0xD),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DCE',
    )

    ChrTalk(
        0x000F,
        (
            '#0940471296V哦，说到洛连特，\n',
            '还是翠耀石啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddSepith(0x03, 500)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×５００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_2F6C')

    def _loc_2DCE(): pass

    label('loc_2DCE')

    If(
        (
            (Expr.PushReg, 0xD),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E59',
    )

    ChrTalk(
        0x000F,
        (
            '#0940471297V哦，黑耀石啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddSepith(0x04, 500)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×５００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_2F6C')

    def _loc_2E59(): pass

    label('loc_2E59')

    If(
        (
            (Expr.PushReg, 0xD),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EE4',
    )

    ChrTalk(
        0x000F,
        (
            '#0940471298V哦，金耀石啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddSepith(0x05, 500)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×５００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_2F6C')

    def _loc_2EE4(): pass

    label('loc_2EE4')

    If(
        (
            (Expr.PushReg, 0xD),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F6C',
    )

    ChrTalk(
        0x000F,
        (
            '#0940471299V哦，银耀石啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddSepith(0x06, 500)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×５００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_2F6C(): pass

    label('loc_2F6C')

    ChrTalk(
        0x000F,
        (
            '#0940471300V嗯，数量虽然不多，\n',
            '去工房还是够了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471301V努力合成出\n',
            '优良的结晶回路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471302V#1001F#4P嗯、嗯！谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471303V#021F#5P真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471304V那么，我差不多\n',
            '也该去矿山了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471305V小姑娘你们有空\n',
            '也要再回洛连特哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_308B')
    def lambda_308B():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_308B')

    DispatchAsync2(0x0101, 0x0003, lambda_308B)

    @scena.Lambda('lambda_309C')
    def lambda_309C():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_309C')

    DispatchAsync2(0x0103, 0x0003, lambda_309C)

    @scena.Lambda('lambda_30AD')
    def lambda_30AD():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_30AD')

    DispatchAsync2(0x00F8, 0x0003, lambda_30AD)

    @scena.Lambda('lambda_30BE')
    def lambda_30BE():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_30BE')

    DispatchAsync2(0x00F9, 0x0003, lambda_30BE)

    ChrWalkTo(0x000F, 3120, 0, 30480, 2000, 0x00)
    ChrSetDirection(0x000F, 270, 400)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0103, 0x03)
    TerminateThread(0x00F8, 0x03)
    TerminateThread(0x00F9, 0x03)

    ChrTalk(
        0x000F,
        (
            '#0940471306V#2P芙莉莎！阿妮娅！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471307V#2P那么，我走了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3610471308V#4P好……路上小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3167')
    def lambda_3167():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_3167')

    DispatchAsync2(0x000F, 0x0003, lambda_3167)

    ChrTalk(
        0x000E,
        (
            '#3620471309V#4P爸爸～！',
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_3194')
    def lambda_3194():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_3194')

    DispatchAsync2(0x0101, 0x0003, lambda_3194)

    @scena.Lambda('lambda_31A5')
    def lambda_31A5():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_31A5')

    DispatchAsync2(0x0103, 0x0003, lambda_31A5)

    @scena.Lambda('lambda_31B6')
    def lambda_31B6():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_31B6')

    DispatchAsync2(0x00F8, 0x0003, lambda_31B6)

    @scena.Lambda('lambda_31C7')
    def lambda_31C7():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_31C7')

    DispatchAsync2(0x00F9, 0x0003, lambda_31C7)

    ChrWalkTo(0x000E, -4680, 0, 32479, 6000, 0x00)
    ChrWalkTo(0x000E, -240, 0, 29900, 6000, 0x00)
    ChrWalkTo(0x000E, 2200, 0, 30480, 6000, 0x00)
    OP_56(0x00)
    OP_59()
    TerminateThread(0x000F, 0x03)

    ChrTalk(
        0x000E,
        (
            '#3620471310V早点回来哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3620471311V阿妮娅会乖乖\n',
            '等你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471312V#2P哦，我会尽量\n',
            '早点回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940471313V#2P要好好\n',
            '帮妈妈的忙哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3620471314V嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471315V#1016F#1P（唔～多么温馨……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0103, 0x03)
    TerminateThread(0x00F8, 0x03)
    TerminateThread(0x00F9, 0x03)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_334E',
    )

    ChrTalk(
        0x0107,
        (
            '#0070471316V#560F（嘿嘿……\n',
            '真有点令人羡慕呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3392')

    def _loc_334E(): pass

    label('loc_334E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3392',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471317V#048F（嗯嗯……\n',
            '多么幸福的一幕啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3392(): pass

    label('loc_3392')

    ChrTalk(
        0x0103,
        (
            '#0030471318V#021F#5P（呵呵，这下\n',
            '大叔的威严也都没了呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 315, 400)

    ChrTalk(
        0x000F,
        (
            '#0940471319V#2P那，我就此告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3405')
    def lambda_3405():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_3405')

    DispatchAsync2(0x0103, 0x0003, lambda_3405)

    @scena.Lambda('lambda_3416')
    def lambda_3416():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_3416')

    DispatchAsync2(0x00F8, 0x0003, lambda_3416)

    @scena.Lambda('lambda_3427')
    def lambda_3427():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_3427')

    DispatchAsync2(0x00F9, 0x0003, lambda_3427)

    @scena.Lambda('lambda_3438')
    def lambda_3438():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_3438')

    DispatchAsync2(0x000E, 0x0003, lambda_3438)

    ChrTalk(
        0x0103,
        (
            '#0030471320V#525F#5P嗯，工作辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3473')
    def lambda_3473():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_3473')

    DispatchAsync2(0x0101, 0x0003, lambda_3473)

    ChrTalk(
        0x0101,
        (
            '#0010471321V#1001F#2P老大也要多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3620471322V路上小心～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000F, 3120, 0, 28600, 2000, 0x00)

    @scena.Lambda('lambda_34E5')
    def lambda_34E5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_34E5)

    ChrWalkTo(0x000F, 3120, 0, 27500, 2000, 0x00)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0103, 0x03)
    TerminateThread(0x00F8, 0x03)
    TerminateThread(0x00F9, 0x03)
    TerminateThread(0x000E, 0x03)
    OP_28(0x0077, 0x01, 0x0100)
    OP_28(0x0077, 0x04, 0x10)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(23, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【矿山的委任书】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))
    RemoveItem(ItemTable['生锈的钥匙'], 1)
    ChrSetFlags(0x000F, 0x0080)
    EventEnd(0x00)
    OP_4B(0x000E, 255)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
