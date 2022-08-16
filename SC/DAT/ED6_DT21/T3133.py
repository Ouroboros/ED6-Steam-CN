import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3133_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3133   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3133.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T3133._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00065._CH', 'ED6_DT07/CH00065P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT07/CH02023._CH', 'ED6_DT07/CH02023P._CP'),
        ('ED6_DT27/CH03670._CH', 'ED6_DT27/CH03670P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20140._CH', 'ED6_DT06/CH20140P._CP'),
        ('ED6_DT06/CH20141._CH', 'ED6_DT06/CH20141P._CP'),
        ('ED6_DT07/CH00061._CH', 'ED6_DT07/CH00061P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT26/CH20278._CH', 'ED6_DT26/CH20278P._CP'),
    ]

# id: 0x10001 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '拉赛尔博士',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卡西乌斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '福音',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 917515,
            chipIndex           = 11,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '重剑用零件',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '提妲的报告书',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 131088,
            chipIndex           = 16,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '莱恩',
            x                   = 32950,
            z                   = -1000,
            y                   = 10430,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
    )

# id: 0x10002 offset: 0x212
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x212
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x212
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x212
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_236',
    )

    ChrClearFlags(0x000E, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_236',
    )

    ChrSetPos(0x000E, 34650, -1000, 2160, 90)

    def _loc_236(): pass

    label('loc_236')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_255',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x22),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_08_396F)

    Jump('loc_281')

    def _loc_255(): pass

    label('loc_255')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x68),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_270',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26D',
    )

    Event(0, func_04_A70)

    def _loc_26D(): pass

    label('loc_26D')

    Jump('loc_281')

    def _loc_270(): pass

    label('loc_270')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 1, 0x1409)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_281',
    )

    MapSetFlags(0x10000000)
    Event(0, func_03_6BE)

    def _loc_281(): pass

    label('loc_281')

    Return()

# id: 0x0001 offset: 0x282
@scena.Code('func_01_282')
def func_01_282():
    Return()

# id: 0x0002 offset: 0x283
@scena.Code('func_02_283')
def func_02_283():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_6BA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0417, 7, 0x20BF)),
            Expr.Ez,
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_427',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '呜哇……！？\n',
            '是、是谁！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#064F啊……？\n',
            '是……莱恩先生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，啊啊……\n',
            '什么啊，原来是提妲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉啊。\n',
            '随随便便就进来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在正在检查\n',
            '市内的导力器……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看起来这里的器材\n',
            '也全部瘫痪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#063F嗯……\n',
            '嗯～好像确实是这样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以请暂时\n',
            '不要打扰我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用不了多久就可以完工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F啊、是的，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0417, 7, 0x20BF))

    Jump('loc_6BA')

    def _loc_427(): pass

    label('loc_427')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_5B3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_490',
    )

    ChrTalk(
        0x00FE,
        (
            '看起来这里的器材\n',
            '全部都无法运转了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这样的状态下\n',
            '要重新开始研究太勉强了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B0')

    def _loc_490(): pass

    label('loc_490')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_558',
    )

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士\n',
            '好像接受军队的求援，前去援助了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说由博士挑选的研究员\n',
            '也一起同行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也就是说，王国未来的命运\n',
            '就全要托付给他们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身为中央工房的一员，\n',
            '我也感到自豪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_5B0')

    def _loc_558(): pass

    label('loc_558')

    ChrTalk(
        0x00FE,
        (
            '王国未来的命运\n',
            '就全靠博士他们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身为中央工房的一员，\n',
            '我也替他们感到自豪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B0(): pass

    label('loc_5B0')

    Jump('loc_6BA')

    def _loc_5B3(): pass

    label('loc_5B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_662',
    )

    ChrTalk(
        0x00FE,
        (
            '根据工房长的指示，\n',
            '要对市内的全部导力器\n',
            '进行检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然，这里的机械\n',
            '也全部都无法运转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～在这种状况下，要怎样\n',
            '才能重新展开研究呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_6BA')

    def _loc_662(): pass

    label('loc_662')

    ChrTalk(
        0x00FE,
        (
            '看起来这里的器材\n',
            '全部都无法运转了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这样的状态下\n',
            '要重新开始研究太勉强了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6BA(): pass

    label('loc_6BA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x6BE
@scena.Code('func_03_6BE')
def func_03_6BE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6D8',
    )

    Call(0, 0x0009)
    FadeIn(0, 0)

    def _loc_6D8(): pass

    label('loc_6D8')

    EventBegin(0x00)
    ChrSetPos(0x0101, -1220, 0, -2240, 0)
    ChrSetPos(0x00F7, -2340, 0, -2240, 0)
    ChrSetPos(0x0105, -1220, 0, -3260, 0)
    ChrSetPos(0x0104, -2340, 0, -3260, 0)
    CameraMove(-960, 0, 4280, 0)
    OP_67(0, 6650, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_C8(0x0200, 0x0046, 'C_PLAC08._CH', 0x01, 0x03E8)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_077F')
    def lambda_077F():
        OP_67(0, 6150, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_077F)

    CameraMove(-490, 0, -1760, 2500)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010220529V#1015F#4P嗯……\n',
            '不知道博士和提妲在不在家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_820',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220530V#051F#6P也没准是去了\n',
            '中央工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_855')

    def _loc_820(): pass

    label('loc_820')

    ChrTalk(
        0x0103,
        (
            '#0030220531V#027F#6P也有可能是去了\n',
            '中央工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_855(): pass

    label('loc_855')

    ChrSetPos(0x0008, 3920, 0, -830, 270)

    NpcTalk(
        0x0008,
        '女孩子的声音',
        (
            '#0540220532V#1S#5P爷爷～\n',
            '2楼已经整理好啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08A9')
    def lambda_08A9():
        CameraMove(1720, 0, -1220, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_08A9)

    Sleep(100)

    @scena.Lambda('lambda_08C6')
    def lambda_08C6():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_08C6)

    Sleep(100)

    @scena.Lambda('lambda_08D9')
    def lambda_08D9():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_08D9)

    Sleep(100)

    @scena.Lambda('lambda_08EC')
    def lambda_08EC():
        ChrSetDirection(0x00FE, 88, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_08EC)

    Sleep(100)

    @scena.Lambda('lambda_08FF')
    def lambda_08FF():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_08FF)

    WaitForThreadExit(0x0101, 0x0002)

    NpcTalk(
        0x0008,
        '老人的声音',
        (
            '#0540220533V#1S#1P喔，辛苦你啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '老人的声音',
        (
            '#0540220534V#1S#1P接着帮我把那里的零件\n',
            '也收拾一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女孩子的声音',
        (
            '#0540220535V#1S#5P好的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09B4')
    def lambda_09B4():
        CameraMove(-490, 0, -1760, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_09B4)

    WaitForThreadExit(0x0104, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010220536V#1017F#6P呵呵，两个人\n',
            '好像都在研究室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A3C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220537V#051F#6P嗯，过去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A6A')

    def _loc_A3C(): pass

    label('loc_A3C')

    ChrTalk(
        0x0103,
        (
            '#0030220538V#021F#6P嗯，那就过去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A6A(): pass

    label('loc_A6A')

    SetScenaFlags(ScenaFlag(0x0281, 1, 0x1409))
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0xA70
@scena.Code('func_04_A70')
def func_04_A70():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A8A',
    )

    Call(0, 0x0009)
    FadeIn(0, 0)

    def _loc_A8A(): pass

    label('loc_A8A')

    EventBegin(0x00)
    FadeOut(0, 0, -1)
    CameraMove(35500, -1000, 10320, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(1900, 0)
    OP_6C(45000, 0)
    OP_6E(503, 0)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 2)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, 34400, -1000, 8900, 0)
    ChrSetPos(0x0009, 34650, -1000, 2190, 90)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0B18')
    def lambda_0B18():
        CameraMove(36140, -1000, 7440, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B18)

    @scena.Lambda('lambda_0B30')
    def lambda_0B30():
        OP_67(0, 6000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B30)

    Sleep(1000)

    ChrSetChipByIndex(0x0009, 1)
    OP_0D()
    Sleep(500)

    ChrWalkTo(0x0009, 34560, -1000, 4350, 2000, 0x00)
    ChrSetDirection(0x0009, 90, 400)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 2)
    Sleep(1000)

    ChrSetChipByIndex(0x0009, 1)
    OP_0D()
    Sleep(500)

    ChrWalkTo(0x0009, 34650, -1000, 2190, 2000, 0x00)
    ChrSetDirection(0x0009, 90, 400)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 2)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0070220539V#5P嘿咻、嘿咻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_E46',
    )

    ChrSetPos(0x0106, 25790, 0, -130, 90)

    ChrTalk(
        0x0106,
        (
            '#0050220540V#2P哟！打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_0C3C')
    def lambda_0C3C():
        CameraMove(34640, -1000, 5940, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0C3C)

    @scena.Lambda('lambda_0C54')
    def lambda_0C54():
        ChrWalkTo(0x0106, 32500, -1000, 1760, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0C54)

    ChrSetChipByIndex(0x0009, 1)
    ChrTurnDirection(0x0009, 0x0106, 400)
    Sleep(500)

    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0008, 0x0106, 400)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#0070220541V#560F#2P啊、阿加特哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0CCD')
    def lambda_0CCD():
        ChrWalkTo(0x0008, 32500, -1000, 3360, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0CCD)

    @scena.Lambda('lambda_0CE8')
    def lambda_0CE8():
        ChrMoveTo(0x0009, 33500, -1000, 1760, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0CE8)

    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0070220542V#061F#2P嘿嘿、欢迎！\n',
            '今天有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0540220543V#100F#5P哎呀。\n',
            '是不良青年来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0008, 400)

    ChrTalk(
        0x0106,
        (
            '#0050220544V#551F来的好像不是时候啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220545V#051F话说回来，这里一点都没变，\n',
            '还是这么乱七八糟的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220546V刚才的地震\n',
            '把东西都震倒了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070220547V#067F#2P嘿嘿嘿……\n',
            '就是那样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_107E')

    def _loc_E46(): pass

    label('loc_E46')

    ChrSetPos(0x0103, 25790, 0, -130, 90)

    ChrTalk(
        0x0103,
        (
            '#0030220548V#2P呵呵呵，早啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_0EA9')
    def lambda_0EA9():
        CameraMove(34640, -1000, 5940, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0EA9)

    @scena.Lambda('lambda_0EC1')
    def lambda_0EC1():
        ChrWalkTo(0x0103, 32500, -1000, 1760, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0EC1)

    ChrSetChipByIndex(0x0009, 1)
    ChrTurnDirection(0x0009, 0x0103, 400)
    Sleep(500)

    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0008, 0x0103, 400)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#0070220549V#064F#2P啊！雪拉姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F36')
    def lambda_0F36():
        ChrWalkTo(0x0008, 32500, -1000, 3360, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F36)

    @scena.Lambda('lambda_0F51')
    def lambda_0F51():
        ChrMoveTo(0x0009, 33500, -1000, 1760, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0F51)

    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0070220550V#061F#2P好久不见了啊。\n',
            '今天有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0540220551V#103F#5P噢噢，卡西乌斯的弟子吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0008, 400)

    ChrTalk(
        0x0103,
        (
            '#0030220552V#021F好久不见了啊，二位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220553V#027F屋子里真是一片狼籍啊，\n',
            '是因为刚才的地震吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070220554V#067F#2P啊，是的。\n',
            '确实是那样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_107E(): pass

    label('loc_107E')

    ChrSetPos(0x0101, 25230, 0, -750, 90)
    ChrSetPos(0x0105, 24390, 0, 660, 90)
    ChrSetPos(0x0104, 23490, 0, -870, 90)

    ChrTalk(
        0x0101,
        (
            '#0010220555V#2P好久不见了啊，二位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0070220556V#064F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)

    @scena.Lambda('lambda_113A')
    def lambda_113A():
        ChrTurnDirection(0x0008, 0x0101, 400)
        Yield()

        Jump('lambda_113A')

    DispatchAsync2(0x0008, 0x0002, lambda_113A)

    @scena.Lambda('lambda_114B')
    def lambda_114B():
        CameraMove(33140, -1000, 3940, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_114B)

    @scena.Lambda('lambda_1163')
    def lambda_1163():
        ChrWalkTo(0x00FE, 29610, -1000, 320, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1163)

    Sleep(500)

    @scena.Lambda('lambda_1183')
    def lambda_1183():
        ChrWalkTo(0x00FE, 30060, -1000, 980, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1183)

    Sleep(200)

    @scena.Lambda('lambda_11A3')
    def lambda_11A3():
        ChrWalkTo(0x00FE, 30260, -1000, -40, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_11A3)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_11C3')
    def lambda_11C3():
        ChrWalkTo(0x00FE, 31830, -1000, 1670, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11C3)

    ChrSetDirection(0x00F7, 180, 400)

    @scena.Lambda('lambda_11E5')
    def lambda_11E5():
        ChrWalkTo(0x00FE, 32299, -1000, 400, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_11E5)

    WaitForThreadExit(0x00F7, 0x0001)

    @scena.Lambda('lambda_1205')
    def lambda_1205():
        ChrTurnDirection(0x00F7, 0x0101, 400)
        Yield()

        Jump('lambda_1205')

    DispatchAsync2(0x00F7, 0x0002, lambda_1205)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010220557V#1016F#6P嘿嘿……\n',
            '久疏问候了，真是抱歉啊。',
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0104, 0x0001)
    ChrTurnDirection(0x0104, 0x0009, 400)
    TerminateThread(0x00F7, 0x02)
    TerminateThread(0x0008, 0x02)
    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540220558V#103F#5P喔喔！！艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070220559V#065F#2P姐、姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0070220560V#068F#2P#3S艾丝蒂尔姐姐！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrSetFlags(0x0009, 0x0040)

    @scena.Lambda('lambda_130A')
    def lambda_130A():
        CameraMove(32640, -1000, 3440, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_130A)

    @scena.Lambda('lambda_1322')
    def lambda_1322():
        CameraSetDistance(1770, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1322)

    @scena.Lambda('lambda_1332')
    def lambda_1332():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_1332')

    DispatchAsync2(0x0008, 0x0001, lambda_1332)

    ChrSetChipByIndex(0x0009, 14)
    OP_92(0x0009, 0x0101, 400, 5000, 0x00)

    @scena.Lambda('lambda_1356')
    def lambda_1356():
        OP_94(0x01, 0x0009, 0x0000, 0x000000C8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1356)

    Yield()
    ChrSetDirection(0x0009, 270, 0)
    ChrSetFlags(0x0009, 0x0020)
    ChrSetChipByIndex(0x0009, 13)
    ChrSetSubChip(0x0009, 0)
    ChrSetDirection(0x0101, 90, 0)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x000007D0, 0x00)
    WaitForThreadExit(0x0009, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010220561V#1004F#6P哇哇～提妲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070220562V#069F#2P艾丝蒂尔姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070220563V太好了……\n',
            '真的是姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220564V#1016F#6P怎、怎么了提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070220565V#069F#2P我、我听说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070220566V约修亚哥哥他\n',
            '不见了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070220567V连艾丝蒂尔姐姐\n',
            '也去了国外……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070220568V#562F我还以为以后再也见不到你们了！\n',
            '一直……都好难过的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220569V#1025F#6P是嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220570V对不起……\n',
            '对不起…没和你打招呼就去了那么远的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0x01)

    ChrTalk(
        0x0008,
        (
            '#0540220571V#100F#5P嗯，你是去了列曼自治州\n',
            '的训练场对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220572V是什么时候回国的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0009, 1)
    ChrSetSubChip(0x0009, 0)
    ChrSetPos(0x0009, 32350, -1000, 1670, 270)
    OP_0D()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010220573V#1017F#6P回来还没多久呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220574V做完了卢安的工作之后\n',
            '刚刚才到了蔡斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540220575V#101F#5P是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0104, 400)

    ChrTalk(
        0x0008,
        (
            '#0540220576V#103F#5P啊，你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0008, 400)

    ChrTalk(
        0x0105,
        (
            '#0060220577V#048F好久不见了，\n',
            '博士，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220578V#031F#4P呼～打扰啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0104, 400)

    ChrTalk(
        0x0009,
        (
            '#0070220579V#560F#2P科洛丝姐姐……\n',
            '还有奥利维尔先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010220580V#1006F#6P他们两个都在\n',
            '协助我进行调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220581V在卢安可是发生了不少事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540220582V#104F#5P嗯，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220583V#100F别一直在这里站着说话，\n',
            '大家都去客厅坐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x1833
@scena.Code('func_05_1833')
def func_05_1833():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_184D',
    )

    Call(0, 0x0009)
    FadeIn(0, 0)

    def _loc_184D(): pass

    label('loc_184D')

    CameraMove(-860, 0, 1560, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(40000, 0)
    OP_6E(280, 0)
    ChrSetFlags(0x0000, 0x0004)
    ChrSetFlags(0x0001, 0x0004)
    ChrSetFlags(0x0002, 0x0004)
    ChrSetFlags(0x0003, 0x0004)
    ChrSetPos(0x0101, -2270, 200, 480, 90)
    ChrSetPos(0x00F7, -2270, 200, 1700, 90)
    ChrSetPos(0x0008, 270, 200, 1700, 270)
    ChrSetPos(0x0009, 250, 200, 480, 270)
    ChrSetPos(0x0105, -1100, 200, -800, 0)
    ChrSetPos(0x0104, -1100, 200, 2650, 180)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1913',
    )

    ChrSetChipByIndex(0x00F7, 4)

    Jump('loc_1918')

    def _loc_1913(): pass

    label('loc_1913')

    ChrSetChipByIndex(0x00F7, 5)

    def _loc_1918(): pass

    label('loc_1918')

    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0105, 6)
    ChrSetChipByIndex(0x0104, 7)
    ChrSetChipByIndex(0x0009, 8)
    ChrSetChipByIndex(0x0008, 9)
    OP_72(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0540220584V#104F政变的幕后黑手\n',
            '已经开始行动了吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220585V#102F而且再次动用到『福音』\n',
            '的力量……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070220586V#065F将空间投影装置生出的影像\n',
            '传送到远方的座标……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070220587V那、那种事…\n',
            '到底是怎么做到的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 1)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0540220588V#100F#5P空间投影装置并不是\n',
            '什么难以实现的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220589V只要时间充足的话\n',
            '我也可以造出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220590V#104F只是把生出的影像\n',
            '传送到远处……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220591V#102F嗯嗯……\n',
            '这现象就难以解释了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220592V#1007F#6P那个戴面具的男子说是在进行\n',
            '『新型福音』的试验。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220593V#1015F那个新型福音…虽然体积比原来大了一圈，\n',
            '但并没有引发导力停止现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1C1B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220594V#050F对了，在政变时出现的那个\n',
            '『福音』现在怎样了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220595V对它的研究有没有什么进展？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C7F')

    def _loc_1C1B(): pass

    label('loc_1C1B')

    ChrTalk(
        0x0103,
        (
            '#0030220596V#020F说起来，在政变时使用过的那个\n',
            '『福音』怎么样了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220597V还在继续解析吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C7F(): pass

    label('loc_1C7F')

    ChrSetSubChip(0x0008, 0)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0540220598V#104F嗯……那个啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220599V随着解析工作的深入，\n',
            '一个奇妙的现象就显现出来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010220600V#1004F#6P奇妙的现象？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540220601V#102F嗯，从结论开始讲吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220602V那个『福音』本身\n',
            '似乎并没有引起『导力停止现象』\n',
            '的功效。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220603V#1020F#6P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220604V#043F可、可是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220605V可是、那个黑色导力器\n',
            '确实引起了导力停止现象啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 1)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0540220606V#104F#5P喔，这只是表面现象而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220607V#102F正如我刚才所说的，\n',
            '随着我对它内部结晶回路的不断分析，\n',
            '更加可以确定它没有那种功效。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220608V只是它可以引起\n',
            '『导力场扭曲』的现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220609V#042F『导力场扭曲』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070220610V#560F那个，所谓的『导力场』\n',
            '就是由导力能源在周围产生\n',
            '出的干涉区域。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070220611V一般都可以根据特定的规则\n',
            '将它的作用线路描绘出来，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070220612V根据爷爷解析出的结果来看，\n',
            '『福音』产生的导力场\n',
            '却违背了这个规则……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220613V#034F#5P唔唔、话题怎么开始\n',
            '转为专业性的学术讨论了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010220614V#1007F#6P我也是听得脑袋都大了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 0)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0540220615V#100F啊，简单来说，\n',
            '就是产生了违背现有法则\n',
            '的导力场扭曲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220616V#104F不过，导力场必须\n',
            '存在于一定的时间和空间内，\n',
            '不然也无法产生导力能源。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220617V如果没有赋予具体的方向命令，\n',
            '是肯定不会出现\n',
            '『导力停止』这种现象的…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220618V#100F总之研究确实是进入瓶颈了啊，\n',
            '但听了你们在卢安遇到的事件之后\n',
            '可能会有什么新转机也说不定啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220619V#101F总之先谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220620V#1016F#6P啊哈哈……\n',
            '还是不能理解…\n',
            '我是不大懂啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2300',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220621V#051F有关敌人使用的投影装置，\n',
            '王国军应该已经开始调查了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220622V有兴趣的话就和他们联络一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2370')

    def _loc_2300(): pass

    label('loc_2300')

    ChrTalk(
        0x0103,
        (
            '#0030220623V#020F王国军应该已经开始调查\n',
            '敌人使用的投影装置了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220624V有兴趣的话就和他们联络一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2370(): pass

    label('loc_2370')

    ChrTalk(
        0x0008,
        (
            '#0540220625V#104F嗯……\n',
            '那就联络看看好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220626V#100F对了，你们现在\n',
            '有什么打算？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220627V打算继续在\n',
            '蔡斯工作一阵吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220628V#1006F#6P啊、这个嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将协会的要求，以及地震的调查情况\n',
            '向博士做了汇报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0540220629V#103F喔……\n',
            '刚才的地震吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220630V#102F利贝尔确实是\n',
            '很少发生地震的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220631V而且三天前在沃尔费堡垒\n',
            '也发生过同样的地震呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070220632V#064F三天前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070220633V#063F嗯～但在蔡斯市内\n',
            '却感觉不到一点摇动，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070220634V确实有些奇怪啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220635V#1006F#6P现在还无法判明到底是\n',
            '自然现象还是『结社』搞的鬼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220636V但既然开始调查了，就好好调查一下吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540220637V#104F嗯，地震吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220638V也许可以用上\n',
            '那东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220639V#1004F#6P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_26C1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220640V#552F啊～又有什么可以派上用场\n',
            '的发明品了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26FF')

    def _loc_26C1(): pass

    label('loc_26C1')

    ChrTalk(
        0x0103,
        (
            '#0030220641V#526F哎呀～您又要拿出什么\n',
            '有用的发明品了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26FF(): pass

    label('loc_26FF')

    ChrTalk(
        0x0008,
        (
            '#0540220642V#102F嗯，这是我在数年前\n',
            '制造的装置……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220643V如果给它装上传送器\n',
            '然后用『卡佩尔』解析的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220644V#101F嗯嗯……也许能行！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220645V#1016F#6P好啦～博士。\n',
            '别再吊大家胃口了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540220646V#100F嗯，我已经想出一个可以\n',
            '协助你们调查的好主意了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220647V你们现在就去沃尔费堡垒\n',
            '好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220648V在这段时间我会把『好东西』造好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220649V#1025F#6P那、那样当然是好，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220650V『好东西』究竟是指什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540220651V#101F呵呵。\n',
            '那个以后再告诉你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540220652V那么我这就要去\n',
            '中央工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 1)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0540220653V#100F#5P提妲，你也来帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2C4C',
    )

    ChrSetSubChip(0x0009, 2)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0070220654V#560F啊，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 0)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0070220655V#561F对不起了。\n',
            '姐姐、阿加特哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070220656V才刚见面就…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220657V#1016F#6P啊哈哈，没关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220658V#1017F能看见提妲\n',
            '我就已经很开心啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070220659V#066F艾丝蒂尔姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050220660V#051F而且我们这段时间\n',
            '都会待在蔡斯，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220661V见面的机会还有的是呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070220662V#067F嘿嘿嘿～是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetPos(0x0008, 360, 0, 2530, 225)
    ChrSetFlags(0x0008, 0x0004)
    OP_0D()
    ChrSetSubChip(0x0009, 0)
    Sleep(100)

    ChrSetChipByIndex(0x0009, 1)

    @scena.Lambda('lambda_2B2D')
    def lambda_2B2D():
        ChrJumpTo(0x00FE, 380, 0, -200, 500, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2B2D)

    ChrSetDirection(0x0009, 180, 1000)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetSubChip(0x0105, 2)
    Sleep(500)

    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#0070220663V#560F#2P那个那个…招待不周，\n',
            '对不住大家啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220664V#048F#6P呵呵，没有的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220665V#031F#5P嘿～有机会的话\n',
            '我还会再来拜访的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220666V下次再见的时候小提妲你一定要\n',
            '叫人家『大哥哥』才行呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F14')

    def _loc_2C4C(): pass

    label('loc_2C4C')

    ChrSetSubChip(0x0009, 2)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0070220654V#560F啊，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 0)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0070220668V#561F对不起了。\n',
            '艾丝蒂尔姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070220656V才刚见面就…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220657V#1016F#6P啊哈哈，没关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220671V#1017F能看见提妲\n',
            '我就已经很开心啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220672V我们这段时间都会待在蔡斯，\n',
            '见面的机会还有的是啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070220673V#560F艾丝蒂尔姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070220674V#067F嘿嘿～说的也对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetPos(0x0008, 360, 0, 2530, 225)
    ChrSetFlags(0x0008, 0x0004)
    OP_0D()
    ChrSetSubChip(0x0009, 0)
    Sleep(100)

    ChrSetChipByIndex(0x0009, 1)

    @scena.Lambda('lambda_2DEF')
    def lambda_2DEF():
        ChrJumpTo(0x00FE, 380, 0, -200, 600, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2DEF)

    ChrSetDirection(0x0009, 180, 1000)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetSubChip(0x0105, 2)
    Sleep(500)

    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#0070220663V#560F#2P那个那个…招待不周，\n',
            '对不住大家啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220664V#048F#6P呵呵，没有的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030220677V#021F嘿～有机会的话\n',
            '我还会再来拜访的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220678V#031F#5P下次再见的时候小提妲你一定要\n',
            '叫人家『大哥哥』才行呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F14(): pass

    label('loc_2F14')

    ChrSetSubChip(0x0101, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010220679V#1019F#6P好啦～你给我适可而止！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070220680V#067F#2P啊、啊哈哈……\n',
            '那就一会见啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540220681V#101F我们准备好以后\n',
            '会去协会和你们联络的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2FC8')
    def lambda_2FC8():
        CameraMove(-980, 0, -50, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2FC8)

    CreateThread(0x0009, 0x01, 0x00, func_06_3878)
    CreateThread(0x0008, 0x01, 0x00, func_07_38E2)
    ChrSetSubChip(0x0101, 0)
    Sleep(50)

    ChrSetSubChip(0x00F7, 2)
    Sleep(50)

    ChrSetSubChip(0x0101, 2)
    WaitForThreadExit(0x0008, 0x0001)
    CameraMove(-860, 0, 1560, 1000)
    ChrSetSubChip(0x0105, 0)
    Sleep(100)

    ChrSetSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010220682V#1016F#6P嗯～……\n',
            '那２个人真是一点也没有变啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_343D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220683V#551F#1P不过，那么小的年龄\n',
            '就这么专注于机械的世界……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220684V总让人有些不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 0)
    Sleep(75)

    ChrSetSubChip(0x0101, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010220685V#1015F#6P嗯，确实啊，小孩子\n',
            '还是应该拥有小孩子的生活。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220686V#1006F不过如果是提妲的话\n',
            '我们就没有必要担心了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050220687V#552F#1P哼……真正应该担心\n',
            '这些的应该是她的父母。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220688V但人在国外就没办法了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220689V下次有机会的话\n',
            '要让她爷爷注意一下这个问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0104, 2)
    Sleep(300)

    ChrTalk(
        0x0104,
        (
            '#0040220690V#031F#5P哎呀～阿加特兄。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220691V真是标准的大哥哥式\n',
            '发言啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0106, 0)
    Sleep(75)

    ChrSetSubChip(0x0106, 1)
    Sleep(300)

    ChrTalk(
        0x0106,
        (
            '#0050220692V#055F#6P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220693V#035F#5P又或者是父亲式的发言……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220694V#037F呵呵呵～要是被别的男人们听见的话，\n',
            '他们一定会羡慕死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050220695V#555F#6P听不懂你在说什么……\n',
            '难道是想打架吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220696V#031F#5P啊哈哈～没有的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220697V只是看那孩子对你这么信赖，\n',
            '实在是让人有些妒嫉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220698V#041F呵呵，我有点理解\n',
            '奥利维尔的心情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220699V#048F我也很想和提妲\n',
            '成为更好的朋友呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3611')

    def _loc_343D(): pass

    label('loc_343D')

    ChrTalk(
        0x0103,
        (
            '#0030220700V#021F#1P哈～小提妲还是\n',
            '那么可爱啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220701V真想紧紧地\n',
            '抱住她不放。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0104, 2)
    Sleep(300)

    ChrTalk(
        0x0104,
        (
            '#0040220702V#035F#5P呼……我也是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220703V那散发着牛奶香味，\n',
            '像小猫一样柔弱幼嫩的身体……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220704V#037F光是想象一下\n',
            '我就快要受不了了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 0)
    Sleep(75)

    ChrSetSubChip(0x0101, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010220705V#1019F#6P雪拉姐也就算了……\n',
            '你那可是犯罪行为啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220706V#041F呵呵……\n',
            '雪拉扎德小姐的心情，\n',
            '我也能够明白一些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220699V#048F其实我也很想和提妲\n',
            '成为更好的朋友呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3611(): pass

    label('loc_3611')

    ChrSetSubChip(0x0101, 0)
    Sleep(75)

    ChrSetSubChip(0x0101, 2)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010220708V#1016F#6P真是的，连科洛丝也……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220709V#1006F不用担心啦，\n',
            '除了奥利维尔之外，\n',
            '大家一定都能很快和提妲成为好朋友的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220710V#036F#5P艾丝蒂尔～你好过分啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_376D',
    )

    ChrSetSubChip(0x0106, 0)
    Sleep(75)

    ChrSetSubChip(0x0106, 2)
    Sleep(300)

    ChrTalk(
        0x0106,
        (
            '#0050220711V#551F#1P真是的……\n',
            '让人头疼的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220712V#555F好了，现在马上\n',
            '开始处理协会交付的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37C0')

    def _loc_376D(): pass

    label('loc_376D')

    ChrTalk(
        0x0103,
        (
            '#0030220713V#020F#1P呵呵，接下来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220714V赶快开始协会交付\n',
            '的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37C0(): pass

    label('loc_37C0')

    ChrSetSubChip(0x0101, 0)
    Sleep(75)

    ChrSetSubChip(0x0101, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010220715V#1006F#6P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220716V在工作时顺便去\n',
            '沃尔费堡垒调查一下吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetChipByIndex(0x0105, 65535)
    ChrSetChipByIndex(0x0104, 65535)
    ChrClearFlags(0x0000, 0x0004)
    ChrClearFlags(0x0001, 0x0004)
    ChrClearFlags(0x0002, 0x0004)
    ChrClearFlags(0x0003, 0x0004)
    SetScenaFlags(ScenaFlag(0x0281, 2, 0x140A))
    OP_28(0x0085, 0x01, 0x0002)
    OP_28(0x0085, 0x01, 0x0004)
    NewScene('ED6_DT21/T3100._SN', 118, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x3878
@scena.Code('func_06_3878')
def func_06_3878():
    ChrClearFlags(0x00FE, 0x0020)
    ChrWalkTo(0x00FE, 50, 0, -1490, 2000, 0x00)
    ChrWalkTo(0x00FE, -2130, 0, -3910, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    PlaySE(6, 0x00, 0x64)
    Sleep(300)

    @scena.Lambda('lambda_38BC')
    def lambda_38BC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_38BC)

    ChrWalkTo(0x00FE, -2150, -500, -6340, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0007 offset: 0x38E2
@scena.Code('func_07_38E2')
def func_07_38E2():
    ChrSetDirection(0x00FE, 90, 400)
    ChrWalkTo(0x00FE, 1180, 0, 2440, 2500, 0x00)
    ChrWalkTo(0x00FE, 1330, 0, -190, 2500, 0x00)
    ChrWalkTo(0x00FE, -2090, 0, -3900, 2500, 0x00)
    ChrWalkTo(0x00FE, -2009, -500, -4550, 2500, 0x00)
    ChrSetFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_3944')
    def lambda_3944():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3944)

    ChrWalkTo(0x00FE, -2150, -500, -6340, 2500, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    PlaySE(7, 0x00, 0x64)

    Return()

# id: 0x0008 offset: 0x396F
@scena.Code('func_08_396F')
def func_08_396F():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(30650, -1000, 330, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(33000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0008, 29950, -1000, 8750, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x000B, 34450, -350, 10510, 0)
    ChrSetPos(0x000C, 28600, -850, 7700, 0)
    ChrSetPos(0x000D, 28750, -900, 8450, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)

    @scena.Lambda('lambda_3A20')
    def lambda_3A20():
        CameraMove(29210, 0, 8080, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3A20)

    @scena.Lambda('lambda_3A38')
    def lambda_3A38():
        OP_67(0, 6000, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3A38)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0540300159V#102F#5P原来如此，这次的『福音』\n',
            '已经可以干涉到人的精神吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300160V而且以雾的粒子作为媒介，\n',
            '进行广范围的掌握和控制。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300161V#104F嗯……看来只有这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000A, 22550, 0, 0, 45)
    ChrClearFlags(0x000A, 0x0080)

    NpcTalk(
        0x000A,
        '男性的声音',
        (
            '#0160300162V#2P博士，打扰啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_3B80')
    def lambda_3B80():
        CameraMove(26250, 0, 4030, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3B80)

    @scena.Lambda('lambda_3B98')
    def lambda_3B98():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3B98)

    CameraSetDistance(3000, 2500)

    ChrTalk(
        0x0008,
        (
            '#0540300163V#103F#6P喔喔！卡西乌斯。\n',
            '有1个月没见了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300164V是从雷斯顿要塞来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160300165V#1120F#5P嗯，工作总算是\n',
            '暂时告一段落了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160300166V就来探望您一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3C67')
    def lambda_3C67():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_3C67')

    DispatchAsync2(0x0008, 0x0001, lambda_3C67)

    @scena.Lambda('lambda_3C78')
    def lambda_3C78():
        CameraMove(30720, -1000, 7630, 6500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C78)

    @scena.Lambda('lambda_3C90')
    def lambda_3C90():
        CameraSetDistance(2750, 6500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3C90)

    ChrWalkTo(0x000A, 30620, -1000, 810, 2500, 0x00)
    ChrWalkTo(0x000A, 30620, -1000, 5470, 2500, 0x00)
    ChrTurnDirection(0x000A, 0x0008, 400)
    Sleep(1000)

    TerminateThread(0x0008, 0x01)

    @scena.Lambda('lambda_3CD8')
    def lambda_3CD8():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_3CD8')

    DispatchAsync2(0x000A, 0x0001, lambda_3CD8)

    ChrTalk(
        0x000A,
        (
            '#0160300167V#1120F那个是……\n',
            '您孙女的报告吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540300168V#101F#5P嗯，今天早上\n',
            '才从洛连特送来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300169V#100F通过这份报告\n',
            '我更加确信了自己的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160300170V#1122F是关于『福音』的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540300171V#104F#5P嗯，其实只能算是个假想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300172V#102F不过这也是通过上千次思考试验和\n',
            '『卡佩尔』演算所得到的结果。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300173V要听听吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160300174V#1125F当然，洗耳恭听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540300175V#101F#5P嗯，那么──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)
    ChrWalkTo(0x0008, 32950, -1000, 10370, 2000, 0x00)
    ChrTurnDirection(0x0008, 0x000B, 400)
    Sleep(500)

    PlaySE(130, 0x00, 0x64)
    ChrSetFlags(0x000B, 0x0800)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x8000)
    Sleep(500)

    ChrSetDirection(0x0008, 180, 400)
    ChrSetDirection(0x0008, 270, 400)
    ChrWalkTo(0x0008, 29950, -1000, 8750, 2000, 0x00)
    ChrSetPos(0x000B, 29260, -400, 8750, 0)
    ChrTurnDirection(0x0008, 0x000B, 400)
    Sleep(500)

    ChrClearFlags(0x000B, 0x0080)
    PlaySE(130, 0x00, 0x64)
    TerminateThread(0x000A, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0540300176V#104F#5P有关这个『福音』引起的\n',
            '『导力停止现象』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000A, 400)

    ChrTalk(
        0x0008,
        (
            '#0540300177V#100F#5P按照你的理解，\n',
            '是怎么一回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160300178V#1122F『福音』可以让周围的\n',
            '导力器产生连锁的\n',
            '机能停止反应……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160300179V大概就是这样了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540300180V#100F#5P半对半错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300181V#104F你所说的这种现象\n',
            '和导力魔法中的\n',
            '『反魔法领域』类似。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300182V让内部结晶回路瘫痪，\n',
            '从而使导力器暂时\n',
            '无法运转。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300183V#102F但是『福音』引起的现象\n',
            '和那个却有着本质上的区别……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300184V它是直接将导力器中产生出的导力\n',
            '彻底夺走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160300185V#1122F也就是说，不是『导力停止』，\n',
            '而是『导力吸收』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540300186V#100F嗯，用内燃引擎来做个比喻的话，\n',
            '就是汽油被抽干了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160300187V#1128F嗯，如果是那样的话，\n',
            '确实是和『反魔法领域』\n',
            '有着本质上的区别啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160300188V#1122F啊……等等。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160300189V那么被抽走的导力\n',
            '难道是储存在『福音』中了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540300190V#101F#5P嗯，你终于发现关键问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300191V#100F但从结论上来看，\n',
            '被夺走的导力并没有\n',
            '被储存在『福音』中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300192V甚至连１ＥＰ都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160300193V#1122F有没有可能是扩散到周围了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540300194V#104F#5P绝无可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300195V是完全彻底地\n',
            '消失在某个地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160300196V#1128F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540300197V#100F#5P而且，艾丝蒂尔她们遇到\n',
            '的那一连串『新型福音』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300198V引发出了一系列连最新导力技术\n',
            '也无法解释的『不可能发生的现象』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300199V#104F那些现象的发生原因\n',
            '现在虽然还无法探明……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300200V但有一点我可以确定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160300201V#1124F那是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540300202V#102F#5P发生装置实在太小了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300203V那种超大规模异常现象的\n',
            '发生装置竟然是那种手掌大的小东西，\n',
            '从物理角度上来看无论如何也是不可能的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300204V就算『结社』拥有比我们\n',
            '先进很多的技术力也是一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160300205V#1123F原来如此……\n',
            '看来总算是抓住关键了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160300206V#1120F也就是说，这『福音』\n',
            '只是『终端』设备而已，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540300207V#101F嗯……正是如此！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300208V#100F『福音』拥有\n',
            '能发生异常的\n',
            '导力场扭曲效能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300209V而这种扭曲会和周围导力器产生共鸣，\n',
            '将导力器的导力夺走。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300210V而被夺走的导力\n',
            '都会被吸入扭曲的源头而消失。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300211V#104F啊，正确的说并不是消失。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300212V#102F而是被送到了另一个空间内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160300213V#1125F而在那个空间中应该\n',
            '就存在着引发这些奇异现象\n',
            '的关键物体……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160300214V#1122F大概就是这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540300215V#102F嗯，应该没错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300216V结社大概是通过『福音』\n',
            '将那神秘物体的力量引发出来\n',
            '并加以利用了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300217V#104F唉，『福音』\n',
            '确实是个了不起的东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160300218V#1128F……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160300219V这样的话……\n',
            '我对那个『神秘物体』开始感兴趣了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160300220V那是用超先进的技术制造出的\n',
            '导力器吗，又或是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540300221V#104F#5P这就不知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300222V虽然存在着各种的可能性，\n',
            '但我现在无法再进一步推断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300223V#100F那么，卡西乌斯──\n',
            '我仍然要问你这个同１０年前一样的问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300224V在如今这种状况，\n',
            '你希望我接下来怎么做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160300225V#1120F哈哈，在警备飞艇完成时\n',
            '您也是这么问我的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160300226V#1125F唔，这样的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160300227V……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 90, 400)
    Sleep(1200)

    ChrMoveToRelative(0x000A, 600, 0, 0, 1000, 0x00)
    Sleep(800)

    ChrSetDirection(0x000A, 270, 400)
    Sleep(1000)

    ChrMoveToRelative(0x000A, -1200, 0, 0, 1000, 0x00)
    Sleep(1500)

    ChrTurnDirection(0x000A, 0x0008, 400)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0160300228V#1122F『福音』可以产生出\n',
            '让导力场扭曲的共鸣现象──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160300229V您能否开发出防止这种\n',
            '共鸣现象的东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540300230V#101F#5P呵呵，我就知道你会这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300231V#100F现在我手上的发明\n',
            '马上就要完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540300232V把这个结束之后\n',
            '我就马上开始研究你说的那个东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/E0001._SN', 110, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x4C6A
@scena.Code('func_09_4C6A')
def func_09_4C6A():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
        (0x00000000, 'loc_4CE4'),
        (0x00000001, 'loc_4CEA'),
        (-1, 'loc_4CF0'),
    )

    def _loc_4CE4(): pass

    label('loc_4CE4')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_4CF0')

    def _loc_4CEA(): pass

    label('loc_4CEA')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_4CF0')

    def _loc_4CF0(): pass

    label('loc_4CF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4CFE',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_4D02')

    def _loc_4CFE(): pass

    label('loc_4CFE')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_4D02(): pass

    label('loc_4D02')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
