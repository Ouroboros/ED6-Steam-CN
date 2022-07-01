import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1100_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1100_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1100_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x13A7
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
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480164V#1002F那卡片里写的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480165V……莫非是指这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B6',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480166V#022F嗯，虽然有这可能性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480167V不过那个事件的调查稍后再进行吧。\n',
            '现在要赶紧赶去拉文努村哦。',
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

    Jump('loc_3C1')

    def _loc_1B6(): pass

    label('loc_1B6')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_268',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480169V#072F嗯，是有这可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480170V不过那个事件的调查稍后再进行吧。\n',
            '现在应该赶紧赶去拉文努村。',
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

    Jump('loc_3C1')

    def _loc_268(): pass

    label('loc_268')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_318',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480172V#030F唔，是有这可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480173V不过那个事件的调查稍后再进行吧。\n',
            '现在先赶紧去拉文努村吧。',
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

    Jump('loc_3C1')

    def _loc_318(): pass

    label('loc_318')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C1',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480175V#042F嗯，说不定就是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480176V不过这里迟些再调查吧。\n',
            '现在得赶紧赶去拉文努村啊……',
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

    def _loc_3C1(): pass

    label('loc_3C1')

    TalkEnd(0x00FF)

    Return()

    def _loc_3C5(): pass

    label('loc_3C5')

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 65390, 3000, 33170, 0)
    SetChrPos(0x00F7, 65090, 3000, 31150, 0)
    SetChrPos(0x00F8, 66060, 3000, 31080, 0)
    SetChrPos(0x00F9, 65600, 3000, 30290, 0)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42D',
    )

    SetChrPos(0x0004, 64830, 3000, 29670, 0)

    def _loc_42D(): pass

    label('loc_42D')

    OP_6D(65390, 3000, 32689, 0)
    OP_67(0, 7650, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4EB',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480178V#042F卡片上的提示是\n',
            '『ＲＩＣＵＬ』和『花的后面』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480179V还有写着\n',
            '『结束就是开端』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_668')

    def _loc_4EB(): pass

    label('loc_4EB')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070480180V#062F卡片上的提示是\n',
            '『ＲＩＣＵＬ』和『花的后面』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070480181V还有写着\n',
            '『结束就是开端』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_668')

    def _loc_56B(): pass

    label('loc_56B')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5EB',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480182V#035F卡片上的提示是\n',
            '『ＲＩＣＵＬ』和『花的后面』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480183V而且写着\n',
            '『结束就是开端』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_668')

    def _loc_5EB(): pass

    label('loc_5EB')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_668',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480184V#026F卡片上的提示是\n',
            '『ＲＩＣＵＬ』和『花的后面』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480185V还有写着\n',
            '『结束就是开端』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_668(): pass

    label('loc_668')

    OP_8C(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480186V#1015F#2P大概是要我们\n',
            '倒过来念吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480187V如果从背后开始读的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480188V就是『调查ＬＵＣＩＲ\n',
            '背后的花』',
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
        'loc_76B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480189V#051F呼，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480190V在柏斯名字叫ＬＵＣＩＲ的，\n',
            '只有这间鲁希尔工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D8')

    def _loc_76B(): pass

    label('loc_76B')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7E3',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480191V#021F呵呵，看来就是这儿了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480192V在柏斯名字叫LUCIR的，\n',
            '只有这间鲁希尔工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D8')

    def _loc_7E3(): pass

    label('loc_7E3')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_866',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480193V#070F嗯，看来就是这儿了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480194V在这座城市里名字叫ＬＵＣＩＲ的\n',
            '看来只有这间鲁希尔工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D8')

    def _loc_866(): pass

    label('loc_866')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8D8',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480195V#030F嗯，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480196V在柏斯名字叫ＬＵＣＩＲ的，\n',
            '只有这间鲁希尔工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D8(): pass

    label('loc_8D8')

    OP_8C(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480197V#1006F#2P嗯，而且和卡片上所写的一样，\n',
            '这里也有『花』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480198V不管怎样，先调查看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0953')
    def lambda_0953():
        ChrTurnDirection(0x00F7, 0x0101, 400)
        Yield()

        Jump('lambda_0953')

    DispatchAsync2(0x00F7, 0x0001, lambda_0953)

    @scena.Lambda('lambda_0964')
    def lambda_0964():
        ChrTurnDirection(0x00F8, 0x0101, 400)
        Yield()

        Jump('lambda_0964')

    DispatchAsync2(0x00F8, 0x0001, lambda_0964)

    @scena.Lambda('lambda_0975')
    def lambda_0975():
        ChrTurnDirection(0x00F9, 0x0101, 400)
        Yield()

        Jump('lambda_0975')

    DispatchAsync2(0x00F9, 0x0001, lambda_0975)

    @scena.Lambda('lambda_0986')
    def lambda_0986():
        OP_6D(65470, 3000, 35800, 2000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_0986)

    OP_8E(0x0101, 65390, 3000, 35740, 2000, 0x00)
    Sleep(1000)

    WaitForThreadExit(0x00F7, 0x0002)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '调查了盆栽，\n',
            '发现贴着卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010480199V#1018F#2P好！找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(600)

    OP_8C(0x0101, 180, 400)

    @scena.Lambda('lambda_0A41')
    def lambda_0A41():
        OP_6D(65470, 3000, 32689, 2000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_0A41)

    OP_8E(0x0101, 65390, 3000, 33170, 2000, 0x00)
    WaitForThreadExit(0x00F7, 0x0002)

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AAC',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480200V#031F看来我们找到正确答案了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B69')

    def _loc_AAC(): pass

    label('loc_AAC')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AEC',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480201V#070F看来我们找到正确答案了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B69')

    def _loc_AEC(): pass

    label('loc_AEC')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B2C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480202V#020F看来我们找到正确答案了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B69')

    def _loc_B2C(): pass

    label('loc_B2C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B69',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480203V#051F看来我们找到正确答案了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B69(): pass

    label('loc_B69')

    ChrTalk(
        0x0101,
        (
            '#0010480204V#1006F嗯，快点看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x0101, 8)
    OP_0D()
    FadeOut(300, 0, 100)
    OP_AD(0x00240093, 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170480205V　　第二把钥匙是如下的咒语──\n',
            '　　　　ＦＴＨＫＣ２Ｅ \n',
            '　　　  看那打开着的书。　　　　　　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170480206V　　  绝不要忘记一个道理。　　　　\n',
            '    辨清真相的人总抢先一步。',
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
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010480207V#1019F#2P唔、唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480208V接下来的提示\n',
            '『ＦＴＨＫＣ２Ｅ』是？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480209V真的搞不懂是什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DC7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480210V#047F大概跟前面一样，\n',
            '也有某种念法吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480211V#042F我觉得『总抢先一步』\n',
            '应该是一条线索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F44')

    def _loc_DC7(): pass

    label('loc_DC7')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E47',
    )

    ChrTalk(
        0x0107,
        (
            '#0070480212V#064F这应该跟前面一样，\n',
            '也有某种念法吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070480213V我觉得『总抢先一步』\n',
            '应该是一条线索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F44')

    def _loc_E47(): pass

    label('loc_E47')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EC7',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480214V#030F这应该跟前面一样，\n',
            '也有某种念法吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480215V我觉得『总抢先一步』\n',
            '恐怕是一条线索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F44')

    def _loc_EC7(): pass

    label('loc_EC7')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F44',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480216V#027F这应该跟前面一样，\n',
            '也有某种念法吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480217V我觉得『总抢先一步』\n',
            '一定是一条线索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F44(): pass

    label('loc_F44')

    OP_59()
    Fade(500)
    SetChrChipByIndex(0x0101, 65535)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010480218V#1015F#2P总之只能先\n',
            '在城里再调查一下了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480219V那样的话有可能会\n',
            '发现一点什么。',
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
        'loc_1018',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480220V#050F嗯，呆坐着瞎想也\n',
            '没什么用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480221V赶快开始调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_115D')

    def _loc_1018(): pass

    label('loc_1018')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1079',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480222V#020F嗯，呆坐着瞎想也\n',
            '没什么用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480223V赶快开始调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_115D')

    def _loc_1079(): pass

    label('loc_1079')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10E6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480224V#070F嗯，在外面走的时候\n',
            '思路也会更清晰一些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480225V好，那么出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_115D')

    def _loc_10E6(): pass

    label('loc_10E6')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_115D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480226V#030F嗯，边走边想的话\n',
            '常会有好的想法浮现呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480227V既然决定了，\n',
            '赶快开始调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_115D(): pass

    label('loc_115D')

    ChrTalk(
        0x0101,
        (
            '#0010480228V#1000F#2P是啊，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0078, 0x01, 0x0004)
    OP_28(0x0078, 0x01, 0x0008)
    OP_64(0x00, 0x0001)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x1197
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x381),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11A4',
    )

    Return()

    def _loc_11A4(): pass

    label('loc_11A4')

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_11B6',
    )

    Return()

    def _loc_11B6(): pass

    label('loc_11B6')

    SetMapFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_CD(0x000F)"),
            Expr.Return,
        ),
        'loc_11F1',
    )

    Call(1, 0x0002)

    Jump('loc_1296')

    def _loc_11F1(): pass

    label('loc_11F1')

    If(
        (
            (Expr.Eval, "OP_CD(0x000E)"),
            Expr.Return,
        ),
        'loc_1200',
    )

    Call(1, 0x0003)

    Jump('loc_1296')

    def _loc_1200(): pass

    label('loc_1200')

    If(
        (
            (Expr.Eval, "OP_CD(0x00FF)"),
            Expr.Return,
        ),
        'loc_1258',
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

    Jump('loc_1296')

    def _loc_1258(): pass

    label('loc_1258')

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

    def _loc_1296(): pass

    label('loc_1296')

    OP_0D()
    ClearMapFlags(0x00000080)

    Return()

# id: 0x0002 offset: 0x129D
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x000F)

    ChrTalk(
        0x000F,
        (
            '#3750490533V哎呀，好可爱的小姑娘啊。\n',
            '不过不巧，我没印象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3750490534V要寻问的话，去比南街区\n',
            '人多的北街区看看怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000F)

    Return()

# id: 0x0003 offset: 0x1326
@scena.Code('func_03_1326')
def func_03_1326():
    TalkBegin(0x000E)

    ChrTalk(
        0x000E,
        (
            '#3740490535V啊，是在『百日战役』中\n',
            '成为孤儿的……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3740490536V……真可怜。\n',
            '我对帮不了你们感到很遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000E)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
