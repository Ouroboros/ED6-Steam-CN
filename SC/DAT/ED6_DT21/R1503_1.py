import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1503_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1503_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/R1503_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    Fade(1000)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x0008, 255)
    ChrSetPos(0x0101, 1420, -10, 17940, 0)
    ChrSetPos(0x00F7, 2150, 10, 17460, 0)
    ChrSetPos(0x00F8, 1230, -10, 16430, 0)
    ChrSetPos(0x00F9, 2280, 0, 16219, 0)
    CameraMove(2100, 20, 17860, 0)
    OP_67(0, 7330, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#2450490153V#2P少尉……\n',
            '光靠我们对付不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2450490154V#2P我想应该要向\n',
            '师团总部紧急请求增援。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490155V真、真的那么棘手吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2450490156V#2P嗯，因为是\n',
            '没见过的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2450490157V#2P不，根本不知道那\n',
            '能不能称为魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490158V#1011F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490159V请问，出什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(100)

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    @scena.Lambda('lambda_02A0')
    def lambda_02A0():
        ChrSetDirection(0x0008, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_02A0)

    Sleep(100)

    ChrSetDirection(0x0009, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#2440490160V唔……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490161V你、你们……？',
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
        'loc_353',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490162V#551F从外表也应该能\n',
            '看出来的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490163V……我们是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_484')

    def _loc_353(): pass

    label('loc_353')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490164V#027F咦，你们看不见\n',
            '这枚徽章吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490165V……我们是游击士哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_484')

    def _loc_3B8(): pass

    label('loc_3B8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_427',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490166V#070F唔，我以为你们能\n',
            '从这枚徽章上看出来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490167V……我们是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_484')

    def _loc_427(): pass

    label('loc_427')

    ChrTalk(
        0x0101,
        (
            '#0010490168V#1000F我以为你们能\n',
            '从这枚徽章上看出来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490169V……我们是游击士哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_484(): pass

    label('loc_484')

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2440490170V游、游击士！？',
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
        'loc_501',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490171V#030F看起来\n',
            '你们遇到了些麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_604')

    def _loc_501(): pass

    label('loc_501')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_542',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490172V#072F看起来\n',
            '你们遇到了些麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_604')

    def _loc_542(): pass

    label('loc_542')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_583',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490173V#027F看起来\n',
            '你们遇到了些麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_604')

    def _loc_583(): pass

    label('loc_583')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5C6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490174V#052F怎么了？\n',
            '遇到什么麻烦了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_604')

    def _loc_5C6(): pass

    label('loc_5C6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_604',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490175V#1063F你们似乎遇到了些麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_604(): pass

    label('loc_604')

    ChrTalk(
        0x0008,
        (
            '#2440490176V嗯、嗯……是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490177V发生了出乎预料\n',
            '的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490178V#1002F出乎预料的事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490179V嗯，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490180V……废坑内部\n',
            '出现了魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_729',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490181V#1068F这哪里\n',
            '出乎预料了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490182V出现魔兽什么的\n',
            '可是家常便饭哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CA')

    def _loc_729(): pass

    label('loc_729')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_792',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490183V#052F这叫出乎预料的事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490184V出现魔兽之类的\n',
            '不是常有的事情吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CA')

    def _loc_792(): pass

    label('loc_792')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7FB',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490185V#023F这叫出乎预料的事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490186V出现魔兽之类的\n',
            '不是常有的事情吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CA')

    def _loc_7FB(): pass

    label('loc_7FB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_862',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490187V#073F这叫出乎预料的事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490188V出现魔兽之类的\n',
            '是常有的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CA')

    def _loc_862(): pass

    label('loc_862')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8CA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490189V#033F这叫出乎预料的事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490190V出现魔兽之类的\n',
            '应该是常有的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8CA(): pass

    label('loc_8CA')

    ChrTalk(
        0x0008,
        (
            '#2440490191V嗯，说是这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490192V可那种魔兽\n',
            '不是一般的魔兽哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481061V#1002F……什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2450490194V#2P嗯，好像是金属\n',
            '制成的昆虫一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2450490195V#2P它们从废坑各处\n',
            '突然涌现出来……',
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
        'loc_A13',
    )

    ChrTalk(
        0x0107,
        (
            '#0070490196V#065F金属制成的昆虫……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490197V#1002F确实很令人在意呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C02')

    def _loc_A13(): pass

    label('loc_A13')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A5C',
    )

    ChrTalk(
        0x0105,
        (
            '#0060490198V#042F原来如此……\n',
            '确实很令人在意呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C02')

    def _loc_A5C(): pass

    label('loc_A5C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AB6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490199V#035F呼，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490200V确实很令人在意呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C02')

    def _loc_AB6(): pass

    label('loc_AB6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B0E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490201V#072F呼，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490202V确实很令人在意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C02')

    def _loc_B0E(): pass

    label('loc_B0E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B5C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490203V#022F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490204V确实很奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C02')

    def _loc_B5C(): pass

    label('loc_B5C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BB2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490205V#057F呼，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490206V确实很令人在意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C02')

    def _loc_BB2(): pass

    label('loc_BB2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C02',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490207V#1064F啊～原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490208V这确实很古怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C02(): pass

    label('loc_C02')

    ChrTalk(
        0x0008,
        (
            '#2440490209V我们是被派遣过来\n',
            '进行警备的部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490210V很遗憾，我们没有多余的力量\n',
            '去消灭那些不知来历的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490211V但是，这个地方距离\n',
            '拉文努村后方相当近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490212V我们也不能对这种来路不明的\n',
            '魔兽的出现坐视不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490213V#1015F那就是说，\n',
            '我们来得正是时候了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490214V#1007F我、我知道你们\n',
            '很期望我们能够出马。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490215V哎呀，被你看出来了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490216V不过最近我们和协会的\n',
            '关系也在不断改善。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490217V不好意思，\n',
            '能不能帮我们一把？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x007D, 0x04, 0x04)
    OP_28(0x007D, 0x01, 0x0001)
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
        'loc_EAA',
    )

    ChrTalk(
        0x0101,
        (
            '#0010490218V#1006F当然没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490219V这么古怪的事件\n',
            '我们怎么会错过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0002)

    Jump('loc_1083')

    def _loc_EAA(): pass

    label('loc_EAA')

    ChrTalk(
        0x0101,
        (
            '#0010490220V#1015F不，虽然我们很想\n',
            '帮助你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490221V可是很遗憾，\n',
            '现在有点困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490222V是、是这样啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490223V这么唐突的请求。\n',
            '也难怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490224V#1007F对不起啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490225V一旦有空，\n',
            '我们会马上返回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490226V嗯，拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490227V你们要是不行的话，\n',
            '我们只能请求增援了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490228V在事情闹大之前，\n',
            '若是能解决就最好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490229V#1006F嗯，我们会努力的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490230V那么再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_28(0x007D, 0x01, 0x8000)

    def _loc_1083(): pass

    label('loc_1083')

    OP_4B(0x0009, 255)
    OP_4B(0x000A, 255)
    OP_4B(0x0008, 255)
    ChrSetDirection(0x0008, 90, 0)
    ChrSetDirection(0x0009, 270, 0)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x10A0
@scena.Code('func_01_10A0')
def func_01_10A0():
    Fade(1000)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x0008, 255)
    ChrSetPos(0x0101, 1420, -10, 17940, 0)
    ChrSetPos(0x00F7, 2150, 10, 17460, 0)
    ChrSetPos(0x00F8, 1230, -10, 16430, 0)
    ChrSetPos(0x00F9, 2280, 0, 16219, 0)
    CameraMove(2100, 20, 17860, 0)
    OP_67(0, 7330, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetDirection(0x0008, 180, 0)
    ChrSetDirection(0x0009, 180, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_117A',
    )

    ChrTalk(
        0x0008,
        (
            '#2440490231V怎么了？莫非你们能\n',
            '帮忙了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11D8')

    def _loc_117A(): pass

    label('loc_117A')

    ChrTalk(
        0x0008,
        (
            '#2440490232V啊，各位游击士。\n',
            '你们回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490233V那么，怎么样？\n',
            '可以帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11D8(): pass

    label('loc_11D8')

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
        'loc_1283',
    )

    ChrTalk(
        0x0101,
        (
            '#0010490218V#1006F当然没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490219V这么古怪的事件\n',
            '我们怎么能错过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0002)

    Jump('loc_134A')

    def _loc_1283(): pass

    label('loc_1283')

    ChrTalk(
        0x0101,
        (
            '#0010490236V#1007F不，抱歉。\n',
            '现在还是不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490237V唔，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490238V#1002F一旦有空\n',
            '我们会马上返回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490239V嗯，拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490240V那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_134A(): pass

    label('loc_134A')

    OP_4B(0x0009, 255)
    OP_4B(0x000A, 255)
    OP_4B(0x0008, 255)
    ChrSetDirection(0x0008, 90, 0)
    ChrSetDirection(0x0009, 270, 0)
    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0x1367
@scena.Code('func_02_1367')
def func_02_1367():
    ChrTalk(
        0x0008,
        (
            '#2440490241V不好意思，真是感恩不尽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490242V#1010F哪里，情况这么紧急，帮忙是应该的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490243V#1002F好了，那就让我们\n',
            '再重新确认一下任务……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490244V总之只要击退那些\n',
            '怪异的魔兽就行了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490245V嗯，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490246V希望你们能击退所有\n',
            '残留在废坑里的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490247V它们外形特殊，应该很容易\n',
            '跟其他魔兽区分开来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490248V#1002F明白了。',
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
        'loc_1545',
    )

    ChrTalk(
        0x0107,
        (
            '#0070490249V#064F请问还有没有更多\n',
            '关于那种魔兽的情报？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0107, 400)

    Jump('loc_1682')

    def _loc_1545(): pass

    label('loc_1545')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1595',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490250V#072F还有没有更多\n',
            '关于那种魔兽的情报？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0108, 400)

    Jump('loc_1682')

    def _loc_1595(): pass

    label('loc_1595')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15E5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490251V#022F还有没有更多\n',
            '关于那种魔兽的情报？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0103, 400)

    Jump('loc_1682')

    def _loc_15E5(): pass

    label('loc_15E5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1635',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490252V#050F还有没有更多\n',
            '关于那种魔兽的情报？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0106, 400)

    Jump('loc_1682')

    def _loc_1635(): pass

    label('loc_1635')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1682',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490253V#030F还有没有更多\n',
            '关于那种魔兽的情报？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0104, 400)

    def _loc_1682(): pass

    label('loc_1682')

    ChrTalk(
        0x0009,
        (
            '#2450490254V#2P让我想想……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2450490255V#2P单体威力\n',
            '不算很强……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2450490256V#2P不过要特别注意\n',
            '偶尔出现的那些不同颜色的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010490257V#1015F不同颜色的家伙？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2450490258V#2P嗯，它会使用\n',
            '类似魔法的攻击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2450490259V#2P不管怎么说，那是一种\n',
            '从来没见过的魔法……',
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
            '#0010490260V#1020F那、那是什么……',
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
        'loc_1860',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490261V#057F哼，看来还挺难对付……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490262V大家提高警觉\n',
            '开始工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19EE')

    def _loc_1860(): pass

    label('loc_1860')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18BF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490263V#022F确实挺危险的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490264V大家提高警觉\n',
            '开始工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19EE')

    def _loc_18BF(): pass

    label('loc_18BF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1926',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490265V#072F呼，这还真是危险呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490266V大家最好提高警觉\n',
            '开始工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19EE')

    def _loc_1926(): pass

    label('loc_1926')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_198B',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490267V#032F呼，这还真是危险呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490268V大家提高警觉\n',
            '开始工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19EE')

    def _loc_198B(): pass

    label('loc_198B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19EE',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490269V#1068F真的是不知来历呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490270V#1063F我们就\n',
            '提高警觉前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19EE(): pass

    label('loc_19EE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A20',
    )

    ChrTalk(
        0x0105,
        (
            '#0060490271V#042F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AEC')

    def _loc_1A20(): pass

    label('loc_1A20')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A52',
    )

    ChrTalk(
        0x0107,
        (
            '#0070240159V#062F是、是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AEC')

    def _loc_1A52(): pass

    label('loc_1A52')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A86',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490273V#030F呼，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AEC')

    def _loc_1A86(): pass

    label('loc_1A86')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1ABC',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490274V#072F嗯，就这么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AEC')

    def _loc_1ABC(): pass

    label('loc_1ABC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AEC',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490275V#1063F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AEC(): pass

    label('loc_1AEC')

    ChrTalk(
        0x0008,
        (
            '#2440490276V说明也已经很充分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490277V那么，我把门打开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010490278V#1002F嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 0, 400)

    @scena.Lambda('lambda_1B70')
    def lambda_1B70():
        ChrWalkTo(0x0008, 1280, 20, 22700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1B70)

    ChrSetDirection(0x0009, 0, 400)
    Sleep(100)

    @scena.Lambda('lambda_1B97')
    def lambda_1B97():
        ChrWalkTo(0x0009, 2720, 20, 22700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1B97)

    Sleep(500)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    PlaySE(115, 0x00, 0x64)
    Sleep(1000)

    PlaySE(110, 0x00, 0x64)
    Sleep(1000)

    ChrSetPos(0x0008, -107910, 0, 19880, 225)
    ChrSetPos(0x0009, -108310, 10, 21740, 180)
    ChrSetPos(0x000A, -112120, -20, 21740, 180)
    ChrSetPos(0x0101, -110760, -10, 18000, 0)
    ChrSetPos(0x00F7, -109590, 30, 18000, 0)
    ChrSetPos(0x00F8, -110360, -10, 16780, 0)
    ChrSetPos(0x00F9, -109070, -20, 16780, 0)
    CameraMove(-108800, 30, 17820, 0)
    OP_4A(0x000A, 255)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2440490279V诸位请小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490280V如果需要休息\n',
            '就请回到这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490281V请使用王国军设置的\n',
            '回复装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 0)

    ChrTalk(
        0x0101,
        (
            '#0010490282V#1006F谢谢，太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490283V等击退了所有需要消灭的魔兽，\n',
            '我们会回到这里来报告的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490284V嗯，那就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490285V愿女神\n',
            '保佑诸位。',
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
        'loc_1DD2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490286V#050F那我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E73')

    def _loc_1DD2(): pass

    label('loc_1DD2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E06',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490287V#022F那我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E73')

    def _loc_1E06(): pass

    label('loc_1E06')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E3E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490288V#072F嗯，那我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E73')

    def _loc_1E3E(): pass

    label('loc_1E3E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E73',
    )

    ChrTalk(
        0x0104,
        (
            '#0040451169V#035F呼，那我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E73(): pass

    label('loc_1E73')

    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010490290V#1002F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1EA2')
    def lambda_1EA2():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_1EA2')

    DispatchAsync2(0x0008, 0x0001, lambda_1EA2)

    @scena.Lambda('lambda_1EB3')
    def lambda_1EB3():
        CameraMove(-109790, -40, 22610, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1EB3)

    @scena.Lambda('lambda_1ECB')
    def lambda_1ECB():
        ChrWalkTo(0x0101, -110760, -10, 25700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1ECB)

    Sleep(100)

    @scena.Lambda('lambda_1EEB')
    def lambda_1EEB():
        ChrWalkTo(0x00F7, -109590, -10, 25700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1EEB)

    @scena.Lambda('lambda_1F06')
    def lambda_1F06():
        ChrWalkTo(0x00F8, -110360, -10, 24700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1F06)

    Sleep(100)

    @scena.Lambda('lambda_1F26')
    def lambda_1F26():
        ChrWalkTo(0x00F9, -109070, -10, 24700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1F26)

    Sleep(500)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0008, 0x02)
    OP_28(0x007D, 0x04, 0x08)
    OP_28(0x007D, 0x01, 0x0002)
    OP_28(0x007D, 0x01, 0x0004)
    NewScene('ED6_DT21/C1102._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x1F7E
@scena.Code('func_03_1F7E')
def func_03_1F7E():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    ChrSetPos(0x0008, -108020, 30, 18910, 270)
    ChrSetPos(0x0009, -108310, 10, 21740, 180)
    ChrSetPos(0x000A, -112120, -20, 21740, 180)
    CameraMove(-109690, 20, 20450, 0)
    OP_67(0, 7330, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    OP_0D()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_4A(0x0008, 255)
    Sleep(1000)

    ChrSetDirection(0x0008, 0, 400)
    OP_4A(0x0008, 255)
    Sleep(500)

    CameraMove(-109010, 0, 23650, 1500)

    @scena.Lambda('lambda_204E')
    def lambda_204E():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_204E')

    DispatchAsync2(0x0008, 0x0001, lambda_204E)

    Sleep(1000)

    CreateThread(0x0101, 0x00, 0x01, 0x0004)
    Sleep(150)

    CreateThread(0x00F7, 0x00, 0x01, 0x0005)
    Sleep(100)

    CreateThread(0x00F8, 0x00, 0x01, 0x0006)
    Sleep(150)

    CreateThread(0x00F9, 0x00, 0x01, 0x0007)
    CameraMove(-109690, 20, 20450, 2500)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F7, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    TerminateThread(0x0008, 0x01)

    ChrTalk(
        0x0008,
        (
            '#2440490291V啊，情况怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490292V#1006F嗯，需要消灭的魔兽\n',
            '已经被我们全部打倒了。',
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
        'loc_2183',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490293V#051F总之这样一来\n',
            '应该就没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490294V接下来的警戒\n',
            '就交给王国军了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_235A')

    def _loc_2183(): pass

    label('loc_2183')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21F3',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490295V#020F总之这样一来\n',
            '应该就没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490296V接下来的警戒\n',
            '就交给王国军了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_235A')

    def _loc_21F3(): pass

    label('loc_21F3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2267',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490297V#070F总之这样一来\n',
            '应该就没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490298V接下来的警戒\n',
            '就交给你们王国军了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_235A')

    def _loc_2267(): pass

    label('loc_2267')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22DB',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490299V#030F总之这样一来\n',
            '应该就没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490300V接下来的警戒\n',
            '就交给你们王国军了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_235A')

    def _loc_22DB(): pass

    label('loc_22DB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_235A',
    )

    ChrTalk(
        0x0105,
        (
            '#0060490301V#040F嗯，总之这样一来\n',
            '应该就没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060490302V接下来的警戒就要交给\n',
            '边防师团的诸位官兵了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_235A(): pass

    label('loc_235A')

    ChrTalk(
        0x0008,
        (
            '#2440490303V呼，你们搞定了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490304V嗯，这样一来可以暂时放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490305V#1015F嗯，这次的问题\n',
            '的确是解决了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490306V#1003F不过那种魔兽……\n',
            '怎么看都是机械啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490307V莫非这也是\n',
            '结社那帮家伙捣的鬼……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24B1',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490308V#1067F大概没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490309V但可惜的是我们\n',
            '不知道他们的目的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2593')

    def _loc_24B1(): pass

    label('loc_24B1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24F4',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490310V#032F嗯，这么想\n',
            '或许很有道理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2593')

    def _loc_24F4(): pass

    label('loc_24F4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_252A',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490311V#074F嗯，恐怕是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2593')

    def _loc_252A(): pass

    label('loc_252A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2560',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490312V#022F嗯，恐怕是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2593')

    def _loc_2560(): pass

    label('loc_2560')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2593',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490313V#053F嗯，很有可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2593(): pass

    label('loc_2593')

    ChrTalk(
        0x0008,
        (
            '#2440490314V结社就是……\n',
            '那个犯罪组织？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490315V原来如此，就是说也有可能\n',
            '是他们干的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490316V#1002F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490317V我们已经和他们交手多次了，\n',
            '对方并不是等闲之辈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490318V士兵先生们\n',
            '也请多加小心。',
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
        'loc_26F3',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490319V#022F我们游击士\n',
            '也在调查他们的情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490320V要是有什么情况\n',
            '我们也会联络军方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28D1')

    def _loc_26F3(): pass

    label('loc_26F3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_276B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490321V#050F我们游击士\n',
            '也在调查他们的情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490322V要是有什么情况\n',
            '我们也会联络军方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28D1')

    def _loc_276B(): pass

    label('loc_276B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27E3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490323V#072F我们游击士\n',
            '也在调查他们的情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490324V要是有什么情况\n',
            '我们也会联络军方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28D1')

    def _loc_27E3(): pass

    label('loc_27E3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2859',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490325V#032F我们也在\n',
            '全力调查他们的情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490326V要是有什么情况\n',
            '我们也会联络军方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28D1')

    def _loc_2859(): pass

    label('loc_2859')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28D1',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490327V#1063F协会方面正在\n',
            '全力调查他们的情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180490328V如果有所发现，\n',
            '我们也会联络军方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28D1(): pass

    label('loc_28D1')

    ChrTalk(
        0x0008,
        (
            '#2440490329V嗯，那就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490330V关于这一次的事件，\n',
            '我们会从师团总部联络协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490331V你们可以去支部\n',
            '领取我们支付的报酬。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490332V#1006F谢谢，太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490333V那么诸位，\n',
            '回去的路上也请小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490334V我们都不能\n',
            '放松警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490335V因为只有这样才能\n',
            '和看不见的敌人对抗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490336V#1002F嗯，我明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490337V那么，接下来\n',
            '就交给你们负责了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440490338V嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A93')
    def lambda_2A93():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_2A93')

    DispatchAsync2(0x0008, 0x0001, lambda_2A93)

    @scena.Lambda('lambda_2AA4')
    def lambda_2AA4():
        ChrSetDirection(0x0101, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2AA4)

    Sleep(200)

    @scena.Lambda('lambda_2AB7')
    def lambda_2AB7():
        ChrWalkTo(0x0101, -110600, 10, 10000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2AB7)

    @scena.Lambda('lambda_2AD2')
    def lambda_2AD2():
        CameraMove(-110030, 10, 15330, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2AD2)

    Sleep(200)

    @scena.Lambda('lambda_2AEF')
    def lambda_2AEF():
        ChrSetDirection(0x00F7, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_2AEF)

    Sleep(250)

    @scena.Lambda('lambda_2B02')
    def lambda_2B02():
        ChrWalkTo(0x00F7, -110600, 10, 11000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2B02)

    @scena.Lambda('lambda_2B1D')
    def lambda_2B1D():
        ChrSetDirection(0x00F8, 180, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_2B1D)

    Sleep(200)

    @scena.Lambda('lambda_2B30')
    def lambda_2B30():
        ChrWalkTo(0x00F8, -109770, 10, 10000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2B30)

    @scena.Lambda('lambda_2B4B')
    def lambda_2B4B():
        ChrSetDirection(0x00F9, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_2B4B)

    Sleep(200)

    @scena.Lambda('lambda_2B5E')
    def lambda_2B5E():
        ChrWalkTo(0x00F9, -111570, 10, 10000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2B5E)

    Sleep(1400)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0008, 0x00)
    OP_28(0x007D, 0x04, 0x10)
    OP_28(0x007D, 0x01, 0x0010)
    Sleep(2000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(23, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【废坑扫荡战】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)

    OP_20(0x00001388)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C1102._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x2BFF
@scena.Code('func_04_2BFF')
def func_04_2BFF():
    ChrSetPos(0x0101, -109630, -110, 25000, 180)
    ChrWalkTo(0x0101, -109630, 40, 19080, 2000, 0x00)
    ChrSetDirection(0x0101, 90, 400)

    Return()

# id: 0x0005 offset: 0x2C2C
@scena.Code('func_05_2C2C')
def func_05_2C2C():
    ChrSetPos(0x00F7, -110530, -110, 25700, 180)
    ChrWalkTo(0x00F7, -110530, 30, 19700, 2000, 0x00)
    ChrSetDirection(0x00F7, 90, 400)

    Return()

# id: 0x0006 offset: 0x2C59
@scena.Code('func_06_2C59')
def func_06_2C59():
    ChrSetPos(0x00F8, -109640, 30, 26310, 180)
    ChrWalkTo(0x00F8, -109640, 30, 20310, 2000, 0x00)
    ChrSetDirection(0x00F8, 135, 400)

    Return()

# id: 0x0007 offset: 0x2C86
@scena.Code('func_07_2C86')
def func_07_2C86():
    ChrSetPos(0x00F9, -110560, 10, 27530, 180)
    ChrWalkTo(0x00F9, -110560, 10, 21000, 2000, 0x00)
    ChrSetDirection(0x00F9, 135, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
