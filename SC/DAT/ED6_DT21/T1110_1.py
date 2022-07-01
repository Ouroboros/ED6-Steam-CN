import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1110_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1110_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1110_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x13EB
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
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0011, 17570, 0, 30850, 90)
    SetChrPos(0x0101, 19190, 0, 30760, 270)
    SetChrPos(0x00F7, 20060, 0, 30110, 270)
    SetChrPos(0x00F8, 20850, 0, 31090, 270)
    SetChrPos(0x00F9, 19940, 0, 31760, 270)
    OP_6D(19700, 0, 31270, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010490001V#1000F#1P那个，打扰一下？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490002V请问米拉诺小姐\n',
            '的房间是这里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490003V啊啊，我就是米拉诺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490004V你们\n',
            '是游击士对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_254',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490005V#030F呼，我是协助人员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490006V据说有需要护卫到拉文努村\n',
            '的任务，是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_396')

    def _loc_254(): pass

    label('loc_254')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C1',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490007V#070F啊啊，正是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490008V据说有需要护卫到拉文努村\n',
            '的任务，是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_396')

    def _loc_2C1(): pass

    label('loc_2C1')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490009V#020F嗯，是这样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490010V据说有需要护卫到拉文努村\n',
            '的任务，是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_396')

    def _loc_32C(): pass

    label('loc_32C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_396',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490011V#050F啊啊，正是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490012V据说有需要护卫到拉文努村\n',
            '的任务，是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_396(): pass

    label('loc_396')

    ChrTalk(
        0x0011,
        (
            '#3710490013V啊啊，是这么打算的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490014V打算去看看\n',
            '果园的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490015V不过，还有这么年轻\n',
            '的小姐在啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490016V能不能胜任呢啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010490017V#1009F#1P唔，真、真没礼貌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490018V我也是正游击士哦。\n',
            '麻烦你别小看我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_529',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490019V#057F这家伙的实力我担保。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490020V这样还是不相信的话、\n',
            '不好意思，另请高明吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_697')

    def _loc_529(): pass

    label('loc_529')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5A2',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490021V#026F我可以担保这女孩的实力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490022V这样还是不相信的话、\n',
            '不好意思，另请高明吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_697')

    def _loc_5A2(): pass

    label('loc_5A2')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_617',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490023V#072F我可以担保她的实力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490024V这样还是不相信的话、\n',
            '不好意思，另请高明吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_697')

    def _loc_617(): pass

    label('loc_617')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_697',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490025V#032F我可以担保她的实力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490026V不过，这样还是不相信的话、\n',
            '不好意思，您只能另请高明了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_697(): pass

    label('loc_697')

    ChrTalk(
        0x0011,
        (
            '#3710490027V呼，所谓的\n',
            '人不可貌像呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490028V算了，好罢。\n',
            '姑且相信你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490037V那么，咋办。\n',
            '现在能马上出发吗？',
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
    OP_28(0x007C, 0x01, 0x0001)
    OP_28(0x007C, 0x04, 0x04)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7B1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010490030V#1006F#1P嗯。\n',
            '随时都ＯＫ哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0002)

    Return()

    def _loc_7B1(): pass

    label('loc_7B1')

    ChrTalk(
        0x0101,
        (
            '#0010490031V#1008F#1P啊，抱歉。\n',
            '其实现在有点不方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490032V什么？\n',
            '还有其他事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490033V咳～真没法子。\n',
            '为什么不先办妥了再来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490034V#1007F#1P对，对不起哦。\n',
            '我们马上回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490035V哦，麻烦你喽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)
    OP_28(0x007C, 0x01, 0x8000)
    EventEnd(0x00)
    OP_4B(0x0011, 255)
    TerminateThread(0x0011, 0x00)
    CreateThread(0x0011, 0x00, 0x00, 0x0002)

    Return()

# id: 0x0001 offset: 0x8BC
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    Fade(1000)
    OP_4A(0x0011, 255)
    SetChrPos(0x0011, 17570, 0, 30850, 90)
    SetChrPos(0x0101, 19190, 0, 30760, 270)
    SetChrPos(0x00F7, 20060, 0, 30110, 270)
    SetChrPos(0x00F8, 20850, 0, 31090, 270)
    SetChrPos(0x00F9, 19940, 0, 31760, 270)
    OP_6D(19700, 0, 31270, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_9C2',
    )

    ChrTalk(
        0x0011,
        (
            '#3710490036V啊哟，挺快的嘛。\n',
            '就回来啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490037V那么，咋样。\n',
            '现在能马上出发吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A11')

    def _loc_9C2(): pass

    label('loc_9C2')

    ChrTalk(
        0x0011,
        (
            '#3710490038V呼哟，我等好久了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490039V那，这下总\n',
            '可以出发了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A11(): pass

    label('loc_A11')

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
        'loc_A95',
    )

    ChrTalk(
        0x0101,
        (
            '#0010490040V#1006F#1P啊，嗯。\n',
            'ＯＫ了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0002)

    Return()

    def _loc_A95(): pass

    label('loc_A95')

    ChrTalk(
        0x0101,
        (
            '#0010490041V#1015F#1P唔～其实\n',
            '还是有点不方便呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490042V咳～怎么又来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490043V有事就全部\n',
            '解决之后再来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490044V#1007F#1P抱歉，我去去就来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490045V哦，我就在这等你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)
    OP_4B(0x0011, 255)
    TerminateThread(0x0011, 0x00)
    CreateThread(0x0011, 0x00, 0x00, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0xB80
@scena.Code('ReInit')
def ReInit():
    ChrTalk(
        0x0011,
        (
            '#3710490046V好了！\n',
            '那么，赶快出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490047V#1000F#1P要去拉文努村对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490048V那就是说，要从城西门\n',
            '前往西柏斯街道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C41',
    )

    ChrTalk(
        0x0105,
        (
            '#0060490049V#040F对，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CE2')

    def _loc_C41(): pass

    label('loc_C41')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C79',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490050V#070F啊啊，应该没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CE2')

    def _loc_C79(): pass

    label('loc_C79')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CAF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490051V#020F嗯，是这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CE2')

    def _loc_CAF(): pass

    label('loc_CAF')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CE2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490052V#051F啊啊，没错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CE2(): pass

    label('loc_CE2')

    ChrTalk(
        0x0011,
        (
            '#3710490053V那么，我就先\n',
            '去西门等着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490054V你们应该\n',
            '也需要做些准备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490055V#1018F#1P啊，这样最好不过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490056V那么，稍后再\n',
            '到西门会合吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490057V好，那么出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3710490058V那，等你们喽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0DDC')
    def lambda_0DDC():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_0DDC')

    DispatchAsync2(0x0000, 0x0001, lambda_0DDC)

    @scena.Lambda('lambda_0DED')
    def lambda_0DED():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_0DED')

    DispatchAsync2(0x0001, 0x0001, lambda_0DED)

    @scena.Lambda('lambda_0DFE')
    def lambda_0DFE():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_0DFE')

    DispatchAsync2(0x0002, 0x0001, lambda_0DFE)

    @scena.Lambda('lambda_0E0F')
    def lambda_0E0F():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_0E0F')

    DispatchAsync2(0x0003, 0x0001, lambda_0E0F)

    Sleep(400)

    @scena.Lambda('lambda_0E25')
    def lambda_0E25():
        OP_6D(19700, 0, 39150, 4000)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_0E25)

    OP_8E(0x0011, 19380, 0, 32590, 2000, 0x00)
    OP_8E(0x0011, 19380, 0, 37930, 2000, 0x00)
    OP_8E(0x0011, 18020, 0, 37930, 2000, 0x00)

    @scena.Lambda('lambda_0E79')
    def lambda_0E79():
        OP_9F(0x0011, 0xFF, 0xFF, 0xFF, 0x00, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0E79)

    OP_8E(0x0011, 16620, 0, 37930, 2000, 0x00)
    WaitForThreadExit(0x0011, 0x0001)
    WaitForThreadExit(0x0011, 0x0002)
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)
    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)
    SetChrFlags(0x0011, 0x0080)
    Fade(1000)
    OP_6D(20620, 0, 31160, 0)
    OP_0D()

    @scena.Lambda('lambda_0ED5')
    def lambda_0ED5():
        OP_8C(0x0101, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0ED5)

    Sleep(100)

    @scena.Lambda('lambda_0EE8')
    def lambda_0EE8():
        OP_8C(0x00F7, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0EE8)

    @scena.Lambda('lambda_0EF6')
    def lambda_0EF6():
        OP_8C(0x00F9, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0EF6)

    Sleep(100)

    OP_8C(0x00F8, 270, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010490059V#1006F#1P好了，那么\n',
            '我们也走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F7A',
    )

    ChrTalk(
        0x0109,
        (
            '#0180490060V#1060F噢，城西门是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1059')

    def _loc_F7A(): pass

    label('loc_F7A')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FB2',
    )

    ChrTalk(
        0x0105,
        (
            '#0060490061V#040F好，是城西门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1059')

    def _loc_FB2(): pass

    label('loc_FB2')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FEC',
    )

    ChrTalk(
        0x0107,
        (
            '#0070490062V#060F嗯，是城西门对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1059')

    def _loc_FEC(): pass

    label('loc_FEC')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1024',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490063V#030F啊啊，城西门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1059')

    def _loc_1024(): pass

    label('loc_1024')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1059',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490064V#070F啊啊，城西门啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1059(): pass

    label('loc_1059')

    OP_28(0x007C, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x1062
@scena.Code('func_03_1062')
def func_03_1062():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x381),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_106F',
    )

    Return()

    def _loc_106F(): pass

    label('loc_106F')

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1081',
    )

    Return()

    def _loc_1081(): pass

    label('loc_1081')

    SetMapFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_CD(0x000A)"),
            Expr.Return,
        ),
        'loc_10BC',
    )

    Call(1, 0x0004)

    Jump('loc_117F')

    def _loc_10BC(): pass

    label('loc_10BC')

    If(
        (
            (Expr.Eval, "OP_CD(0x0012)"),
            Expr.Return,
        ),
        'loc_10CB',
    )

    Call(1, 0x0005)

    Jump('loc_117F')

    def _loc_10CB(): pass

    label('loc_10CB')

    If(
        (
            (Expr.Eval, "OP_CD(0x000E)"),
            Expr.Return,
        ),
        'loc_10DA',
    )

    Call(1, 0x0006)

    Jump('loc_117F')

    def _loc_10DA(): pass

    label('loc_10DA')

    If(
        (
            (Expr.Eval, "OP_CD(0x000B)"),
            Expr.Return,
        ),
        'loc_10E9',
    )

    Call(1, 0x0007)

    Jump('loc_117F')

    def _loc_10E9(): pass

    label('loc_10E9')

    If(
        (
            (Expr.Eval, "OP_CD(0x00FF)"),
            Expr.Return,
        ),
        'loc_1141',
    )

    FadeOut(300, 0, 100)
    SetChrName('')

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

    Jump('loc_117F')

    def _loc_1141(): pass

    label('loc_1141')

    FadeOut(300, 0, 100)
    SetChrName('')

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

    def _loc_117F(): pass

    label('loc_117F')

    OP_0D()
    ClearMapFlags(0x00000080)

    Return()

# id: 0x0004 offset: 0x1186
@scena.Code('func_04_1186')
def func_04_1186():
    TalkBegin(0x000A)

    ChrTalk(
        0x000A,
        (
            '#3730490537V唔，１０年前的战役中\n',
            '行踪不明的人吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3730490538V十分遗憾，\n',
            '看来我帮不上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3730490539V请去问问别人看吧。\n',
            '说不定能找到线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0x122A
@scena.Code('func_05_122A')
def func_05_122A():
    TalkBegin(0x0012)

    ChrTalk(
        0x0012,
        (
            '#1290490540V寻找战争孤儿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1290490541V嗨，真令人心痛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1290490542V一回忆起当时的事\n',
            '现在还心如刀绞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0012)

    Return()

# id: 0x0006 offset: 0x12AC
@scena.Code('func_06_12AC')
def func_06_12AC():
    TalkBegin(0x000E)

    ChrTalk(
        0x000E,
        (
            '#1200490543V百日战役的时候许多\n',
            '这样的孩子都成了孤儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1200490544V无论用什么理由开脱，\n',
            '那都是彻头彻尾的错事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1200490545V不管是谁看见这张照片，\n',
            '都应该会注意到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000E)

    Return()

# id: 0x0007 offset: 0x1366
@scena.Code('func_07_1366')
def func_07_1366():
    TalkBegin(0x000B)

    ChrTalk(
        0x000B,
        (
            '#1390490546V那个照片里的孩子\n',
            '竟然是在战争中失踪的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1390490547V真可怕啊……\n',
            '我曾经也有个女儿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
