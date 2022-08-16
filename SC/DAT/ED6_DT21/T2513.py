import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2513_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2513   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2513.x'
    header.mapIndex       = 1
    header.bgm            = 14
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
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xBA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xBA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xBA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xBA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x69),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CF',
    )

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x5F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CF(): pass

    label('loc_CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_E5',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_08_1A97)

    Jump('loc_110')

    def _loc_E5(): pass

    label('loc_E5')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006C, 'loc_FD'),
        (0x0000006D, 'loc_FD'),
        (0x00000070, 'loc_FD'),
        (0x00000071, 'loc_FD'),
        (-1, 'loc_110'),
    )

    def _loc_FD(): pass

    label('loc_FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 0, 0x1220)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10D',
    )

    Event(0, func_02_16A)

    def _loc_10D(): pass

    label('loc_10D')

    Jump('loc_110')

    def _loc_110(): pass

    label('loc_110')

    Return()

# id: 0x0001 offset: 0x111
@scena.Code('func_01_111')
def func_01_111():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_129',
    )

    OP_B1('t2513_y')

    Jump('loc_132')

    def _loc_129(): pass

    label('loc_129')

    OP_B1('t2513_n')

    def _loc_132(): pass

    label('loc_132')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_13C',
    )

    Jump('loc_169')

    def _loc_13C(): pass

    label('loc_13C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Return,
        ),
        'loc_154',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)

    Jump('loc_169')

    def _loc_154(): pass

    label('loc_154')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Return,
        ),
        'loc_169',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)

    def _loc_169(): pass

    label('loc_169')

    Return()

# id: 0x0002 offset: 0x16A
@scena.Code('func_02_16A')
def func_02_16A():
    EventBegin(0x00)
    MapClearFlags(0x00000001)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006C, 'loc_189'),
        (0x0000006D, 'loc_1AE'),
        (0x00000070, 'loc_1D3'),
        (0x00000071, 'loc_1F8'),
        (-1, 'loc_21D'),
    )

    def _loc_189(): pass

    label('loc_189')

    ChrSetPos(0x0101, 56060, 1000, 17010, 126)
    ChrSetPos(0x0105, 55790, 1000, 15650, 126)

    Jump('loc_21D')

    def _loc_1AE(): pass

    label('loc_1AE')

    ChrSetPos(0x0101, 63650, 1000, 17010, 206)
    ChrSetPos(0x0105, 63920, 1000, 15650, 206)

    Jump('loc_21D')

    def _loc_1D3(): pass

    label('loc_1D3')

    ChrSetPos(0x0101, 56840, 1000, 12230, 52)
    ChrSetPos(0x0105, 55920, 1000, 12290, 52)

    Jump('loc_21D')

    def _loc_1F8(): pass

    label('loc_1F8')

    ChrSetPos(0x0101, 63220, 1000, 12000, 325)
    ChrSetPos(0x0105, 64230, 1000, 11610, 325)

    Jump('loc_21D')

    def _loc_21D(): pass

    label('loc_21D')

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010210161V#1026F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    @scena.Lambda('lambda_024E')
    def lambda_024E():
        CameraMove(58730, 2850, 2760, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_024E)

    @scena.Lambda('lambda_0266')
    def lambda_0266():
        OP_6C(18000, 4000)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_0266)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006C, 'loc_288'),
        (0x0000006D, 'loc_29E'),
        (0x00000070, 'loc_2B4'),
        (0x00000071, 'loc_2CA'),
        (-1, 'loc_2E0'),
    )

    def _loc_288(): pass

    label('loc_288')

    CreateThread(0x0101, 0x01, 0x00, func_03_1A0B)
    Sleep(800)

    CreateThread(0x0105, 0x01, 0x00, func_04_1A27)

    Jump('loc_2E0')

    def _loc_29E(): pass

    label('loc_29E')

    CreateThread(0x0101, 0x01, 0x00, func_03_1A0B)
    Sleep(800)

    CreateThread(0x0105, 0x01, 0x00, func_05_1A43)

    Jump('loc_2E0')

    def _loc_2B4(): pass

    label('loc_2B4')

    CreateThread(0x0101, 0x01, 0x00, func_03_1A0B)
    Sleep(800)

    CreateThread(0x0105, 0x01, 0x00, func_06_1A5F)

    Jump('loc_2E0')

    def _loc_2CA(): pass

    label('loc_2CA')

    CreateThread(0x0101, 0x01, 0x00, func_03_1A0B)
    Sleep(800)

    CreateThread(0x0105, 0x01, 0x00, func_07_1A7B)

    Jump('loc_2E0')

    def _loc_2E0(): pass

    label('loc_2E0')

    WaitForThreadExit(0x0105, 0x0001)
    WaitForThreadExit(0x0105, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010211040V#1025F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211041V#542F#7P……好奇妙的感觉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211042V虽然只是几个月前的事，\n',
            '但却觉得非常怀念呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211043V#1025F#5P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD('ED6_DT24/C_VIS169._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    Sleep(2000)

    OP_AE(0x000001F4)
    Sleep(1000)

    @scena.Lambda('lambda_03CC')
    def lambda_03CC():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_03CC')

    DispatchAsync2(0x0105, 0x0001, lambda_03CC)

    @scena.Lambda('lambda_03DD')
    def lambda_03DD():
        ChrWalkTo(0x00FE, 60140, 1000, 11500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03DD)

    @scena.Lambda('lambda_03F8')
    def lambda_03F8():
        CameraMove(60140, 700, 12000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_03F8)

    @scena.Lambda('lambda_0410')
    def lambda_0410():
        OP_6C(0, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0410)

    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0105, 0x01)
    WaitForThreadExit(0x0101, 0x0002)
    ChrSetFlags(0x0101, 0x0004)
    ChrJumpTo(0x0101, 60140, 700, 10970, 200, 4000)
    ChrSetChipByIndex(0x0101, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211044V#1025F#5P自那之后，\n',
            '真的是发生了太多的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211045V只是温柔美丽的约修亚\n',
            '公主已经不在了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211046V现在，只有我们两个人\n',
            '坐在这个舞台上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211047V#1016F感觉真是不可思议啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211048V#047F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211049V#040F嗯…艾丝蒂尔。\n',
            '能让我坦白一件事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0101, 0x0010)
    ChrTurnDirection(0x0101, 0x0105, 0)

    If(
        (
            (Expr.GetChrWork, 0x101, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_597',
    )

    ChrSetSubChip(0x0101, 2)

    Jump('loc_5B2')

    def _loc_597(): pass

    label('loc_597')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_5AD',
    )

    ChrSetSubChip(0x0101, 2)

    Jump('loc_5B2')

    def _loc_5AD(): pass

    label('loc_5AD')

    ChrSetSubChip(0x0101, 1)

    def _loc_5B2(): pass

    label('loc_5B2')

    ChrSetDirection(0x0101, 180, 0)
    ChrSetFlags(0x0101, 0x0010)

    ChrTalk(
        0x0101,
        (
            '#0010211050V#1004F#5P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006C, 'loc_5FE'),
        (0x0000006D, 'loc_63B'),
        (0x00000070, 'loc_678'),
        (0x00000071, 'loc_6B5'),
        (-1, 'loc_6F2'),
    )

    def _loc_5FE(): pass

    label('loc_5FE')

    ChrWalkTo(0x0105, 59270, 0, 11500, 2000, 0x00)
    ChrSetFlags(0x0105, 0x0004)
    ChrJumpTo(0x0105, 59270, 700, 10970, 200, 4000)
    ChrSetChipByIndex(0x0105, 1)
    Sleep(500)

    Jump('loc_6F2')

    def _loc_63B(): pass

    label('loc_63B')

    ChrWalkTo(0x0105, 61070, 0, 11500, 2000, 0x00)
    ChrSetFlags(0x0105, 0x0004)
    ChrJumpTo(0x0105, 61070, 700, 10970, 200, 4000)
    ChrSetChipByIndex(0x0105, 1)
    Sleep(500)

    Jump('loc_6F2')

    def _loc_678(): pass

    label('loc_678')

    ChrWalkTo(0x0105, 59270, 0, 11500, 2000, 0x00)
    ChrSetFlags(0x0105, 0x0004)
    ChrJumpTo(0x0105, 59270, 700, 10970, 200, 4000)
    ChrSetChipByIndex(0x0105, 1)
    Sleep(500)

    Jump('loc_6F2')

    def _loc_6B5(): pass

    label('loc_6B5')

    ChrWalkTo(0x0105, 61070, 0, 11500, 2000, 0x00)
    ChrSetFlags(0x0105, 0x0004)
    ChrJumpTo(0x0105, 61070, 700, 10970, 500, 4000)
    ChrSetChipByIndex(0x0105, 1)
    Sleep(500)

    Jump('loc_6F2')

    def _loc_6F2(): pass

    label('loc_6F2')

    OP_21()
    PlayBGM(118)
    Sleep(500)

    ChrTalk(
        0x0105,
        (
            '#0060211051V#540F我……\n',
            '我很喜欢约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211052V在第一次见面时，就感觉到他的身上\n',
            '有一种奇妙的魅力，\n',
            '把我深深地吸引住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211053V#1004F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211054V#1025F……是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211055V#1016F啊哈哈…果然是这样吗。\n',
            '虽然我以前就有这种感觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0105, 0x0010)
    ChrTurnDirection(0x0105, 0x0101, 0)

    If(
        (
            (Expr.GetChrWork, 0x105, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_836',
    )

    ChrSetSubChip(0x0105, 2)

    Jump('loc_851')

    def _loc_836(): pass

    label('loc_836')

    If(
        (
            (Expr.GetChrWork, 0x105, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_84C',
    )

    ChrSetSubChip(0x0105, 2)

    Jump('loc_851')

    def _loc_84C(): pass

    label('loc_84C')

    ChrSetSubChip(0x0105, 1)

    def _loc_851(): pass

    label('loc_851')

    ChrSetDirection(0x0105, 180, 0)
    ChrSetFlags(0x0105, 0x0010)

    ChrTalk(
        0x0105,
        (
            '#0060211056V#542F在舞台剧最后一幕的吻戏时，\n',
            '我的心跳得好快。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211057V虽然觉得有些\n',
            '对不起艾丝蒂尔，\n',
            '但我根本没办法不投入到剧情中……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211058V#045F当时完全没有感觉是在演戏，\n',
            '就好像自己的吻真的被他夺去一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211059V#1013F#5P是、是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211060V科洛丝你…\n',
            '还真是大胆啊……好意外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211061V#542F呵呵，其实平时的我\n',
            '就是这样的啦，尤莉亚小姐也\n',
            '对我很头疼呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211062V#047F不过那个时候……\n',
            '当戴尔蒙市长用枪口\n',
            '对准你的时候……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211063V约修亚他……\n',
            '约修亚他的眼神真的好可怕……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211064V在那时我才感受到，\n',
            '你在他的心中是多么重要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211065V#542F也终于明白…\n',
            '你们之间根本就没有我介入的余地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211066V#1015F#5P嗯、嗯嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211067V也许我说这种话有些不太合适，不过… \n',
            '你现在就放弃的话未免有点早吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211068V#1007F说实话，科洛丝要和我竞争的话…\n',
            '胜负还很难预料呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211069V#048F真是的～艾丝蒂尔\n',
            '你实在太不了解自己了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211070V竟然完全都不清楚\n',
            '自己有多大的魅力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211071V#1019F#5P呜……\n',
            '换句话说就是我太笨了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211072V#045F呵呵，才没有那种事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211073V#542F我最喜欢艾丝蒂尔你\n',
            '这种可爱和率直……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211074V我想约修亚也一定\n',
            '和我一样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211075V所以从某种意义上说，\n',
            '我和约修亚可以算是知音了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211076V#1004F#5P啊……说起来的话\n',
            '我也有这种感觉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211077V#1015F你们都是那种头脑聪明、\n',
            '举止端正、外表清秀的类型……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211078V所以当时我还说你们很般配，\n',
            '挑唆约修亚和你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211079V#049F我在认识特蕾莎院长之前\n',
            '每天都过着孤独的生活。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211080V约修亚在遇到\n',
            '艾丝蒂尔之前\n',
            '大概也是如此吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211081V#047F但我和他之间有一点不同，\n',
            '……那就是他比我坚强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211082V#1004F#5P坚强？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0105, 0)
    Sleep(500)

    ChrTalk(
        0x0105,
        (
            '#0060211083V#043F祖母大人指名让我担当\n',
            '下一任的女王。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211084V以现在的状况来考虑，\n',
            '也许这种决定很正确……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211085V#047F但我一旦当上了女王……\n',
            '就再也无法做回『科洛丝』的身份了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211086V只能以肩负重大权利和责任的\n',
            '科洛蒂娅·冯·奥赛雷丝的\n',
            '身份过完一生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211087V那样的话，就再也不能和朋友轻松交谈，\n',
            '不能和院长撒娇，也不能和那些可爱的\n',
            '孩子们拥抱玩耍……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211088V#049F每当想起这些的时候我就好害怕……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211089V害怕自己再次回到那种孤独的生活，\n',
            '但同时我也对自己的懦弱感到羞愧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211090V至今也还没能给祖母\n',
            '一个明确的答复……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211091V#1026F#5P科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211092V#542F从这一点上看，约修亚\n',
            '实在比我坚强太多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211093V虽然他深深地爱着你，十分不愿意\n',
            '从你身边离开……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211094V但为了避免你被牵连\n',
            '到自己的事情中，他还是\n',
            '毅然选择了离开……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211095V#1003F#5P……嗯，约修亚确实很坚强。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211096V#1010F但是……\n',
            '我认为他的坚强用错了地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.GetChrWork, 0x105, 0x1),
            (Expr.PushLong, 0xEAEC),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1258',
    )

    ChrSetSubChip(0x0105, 1)

    Jump('loc_125D')

    def _loc_1258(): pass

    label('loc_1258')

    ChrSetSubChip(0x0105, 2)

    def _loc_125D(): pass

    label('loc_125D')

    Sleep(500)

    ChrTalk(
        0x0105,
        (
            '#0060211097V#044F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211098V#1025F#5P科洛丝毕竟是要担任治理整个国家的\n',
            '女王，有这种烦恼也是理所当然的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211099V感到不安是再正常不过的，\n',
            '如果没有这种感觉那才奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211100V即便是如此这般的烦恼，都无法\n',
            '阻止你去追寻正确的答案，这样的科洛丝\n',
            '一定能成为一个称职的好女王。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211101V#542F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211102V#1002F#5P但是约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211103V约修亚他…根本就没有烦恼过！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211104V他根本就没有留恋和犹豫，\n',
            '那么坚决地就从我们身边离去……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211105V#1003F这一点……\n',
            '才是我最不能原谅他的地方！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211106V#043F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211107V#047F……嗯，说的对。\n',
            '确实不能原谅他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211108V#042F他完全都没有考虑过\n',
            '女孩子的心情啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0105, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0101)
    OP_63(0x0105)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006C, 'loc_1554'),
        (0x00000070, 'loc_1554'),
        (0x0000006D, 'loc_15A4'),
        (0x00000071, 'loc_15A4'),
        (-1, 'loc_15F1'),
    )

    def _loc_1554(): pass

    label('loc_1554')

    ChrTalk(
        0x0101,
        (
            '#0010211111V#1016F#5P#1K扑哧……',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0105,
        (
            '#0060211112V#045F#1K哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_15F1')

    def _loc_15A4(): pass

    label('loc_15A4')

    ChrTalk(
        0x0101,
        (
            '#0010211111V#1016F#5P#1K扑哧……',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0105,
        (
            '#0060211112V#045F#1K哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_15F1')

    def _loc_15F1(): pass

    label('loc_15F1')

    Sleep(1000)

    OP_56(0x01)
    OP_59()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010211113V#1017F#5P能和科洛丝成为朋友\n',
            '真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211114V能让我这么痛快地倾诉\n',
            '心里话的对象实在太少了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211115V#041F呵呵，我也是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211116V#542F刚才说了好多\n',
            '难为情的话，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211117V嗯…请不要误解啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211118V我现在对约修亚已经\n',
            '不再有那种想法了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211119V#1016F#5P啊啊～没关系的没关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211120V#1017F喜欢就是喜欢，\n',
            '没必要刻意去抑制。\n',
            '我已经完全明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211121V有什么感觉就要坦率地表达出来，\n',
            '这才是青春呢，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211122V#045F艾丝蒂尔～你真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211123V#540F嗯…如果说我对他一点感觉都没有了，\n',
            '那肯定是假话，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211124V我现在更大的愿望是帮助\n',
            '你们两个重新……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211125V#1012F#5P嗯嗯！我明白的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211126V#1006F……好了。\n',
            '这次聊得真是太尽兴了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211127V咱们还是继续去调查学生们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211128V#045F啊～说的对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211129V在太阳落山之前\n',
            '我们还是抓紧时间调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_20(0x000007D0)
    OP_0D()
    CameraMove(60140, 1000, 12380, 0)
    OP_67(0, 2930, -10000, 0)
    CameraSetDistance(1420, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0105, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0105, 65535)
    ChrSetPos(0x0101, 60140, 1000, 12380, 180)
    ChrSetPos(0x0105, 60140, 1000, 12380, 180)
    Sleep(500)

    OP_21()
    PlayBGM(14)
    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x0244, 0, 0x1220))
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x1A0B
@scena.Code('func_03_1A0B')
def func_03_1A0B():
    ChrWalkTo(0x00FE, 60140, 0, 14620, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0004 offset: 0x1A27
@scena.Code('func_04_1A27')
def func_04_1A27():
    ChrWalkTo(0x00FE, 59270, 0, 15500, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0005 offset: 0x1A43
@scena.Code('func_05_1A43')
def func_05_1A43():
    ChrWalkTo(0x00FE, 61070, 0, 15500, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0006 offset: 0x1A5F
@scena.Code('func_06_1A5F')
def func_06_1A5F():
    ChrWalkTo(0x00FE, 59270, 0, 13860, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0007 offset: 0x1A7B
@scena.Code('func_07_1A7B')
def func_07_1A7B():
    ChrWalkTo(0x00FE, 61070, 0, 13860, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0008 offset: 0x1A97
@scena.Code('func_08_1A97')
def func_08_1A97():
    EventBegin(0x00)
    ChrSetFlags(0x0102, 0x0080)
    CameraMove(1070, -250, -3000, 0)
    OP_67(0, 5920, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)

    @scena.Lambda('lambda_1AE1')
    def lambda_1AE1():
        CameraMove(1580, -250, 13840, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1AE1)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0102, 0x0001)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
    NewScene('ED6_DT21/T2500._SN', 125, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
