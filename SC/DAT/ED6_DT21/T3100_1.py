import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3100_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3100_1 ._SN')

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
    header.importTable    = ['ED6_DT21/T3100._SN', 'ED6_DT21/T3100_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450798V#1004F啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450799V这、这是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_139',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450800V#052F发现什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E')

    def _loc_139(): pass

    label('loc_139')

    ChrTalk(
        0x0103,
        (
            '#0030450801V#023F发现什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15E(): pass

    label('loc_15E')

    ChrTalk(
        0x0101,
        (
            '#0010441823V#1002F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44E')

    def _loc_17F(): pass

    label('loc_17F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_212',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450805V#052F嗯！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450806V这是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450807V#1002F发现什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050450808V#050F嗯，来看看这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44E')

    def _loc_212(): pass

    label('loc_212')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030450809V#023F哎呀！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450810V这莫非是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450807V#1002F发现什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030450812V#027F艾丝蒂尔……\n',
            '来看看这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44E')

    def _loc_2B0(): pass

    label('loc_2B0')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_324',
    )

    ChrTalk(
        0x0105,
        (
            '#0060450813V#044F……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450814V艾丝蒂尔，这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450815V#1002F发现什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44E')

    def _loc_324(): pass

    label('loc_324')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A9',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450816V#033F呀…！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450817V#1002F奥利维尔，发现什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450818V#035F嗯，来看看这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44E')

    def _loc_3A9(): pass

    label('loc_3A9')

    ChrTalk(
        0x0107,
        (
            '#0070450819V#064F咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070450820V这、这是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450807V#1002F发现什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070450822V#062F嗯、嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070450823V姐姐，看看这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44E(): pass

    label('loc_44E')

    OP_59()
    Fade(1000)
    EventBegin(0x00)
    CameraMove(35000, 500, 87940, 0)
    OP_67(0, 8109, -10000, 0)
    CameraSetDistance(2770, 0)
    OP_6C(143000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 36310, 0, 87490, 280)
    ChrSetPos(0x00F7, 35950, 0, 86340, 310)
    ChrSetPos(0x00F8, 37540, 0, 85600, 329)
    ChrSetPos(0x00F9, 37230, 0, 84600, 328)
    OP_0D()
    Sleep(400)

    ChrWalkTo(0x0101, 35010, 500, 87990, 1000, 0x00)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_543',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450803V#1002F#7P……没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450804V是那家伙的卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5AE')

    def _loc_543(): pass

    label('loc_543')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010450824V#1002F#7P这、这张卡片……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450825V肯定是那家伙的东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5AE(): pass

    label('loc_5AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5E3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450826V#050F那么，上面写着什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_613')

    def _loc_5E3(): pass

    label('loc_5E3')

    ChrTalk(
        0x0103,
        (
            '#0030450827V#022F那么……\n',
            '上面写着些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_613(): pass

    label('loc_613')

    ChrTalk(
        0x0101,
        (
            '#0010450828V#1002F#7P嗯、嗯……\n',
            '等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Sleep(400)

    Fade(1000)
    CameraMove(36720, 0, 87530, 0)
    OP_67(0, 6900, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(309000, 0)
    OP_6E(262, 0)
    OP_71(0x0016, 0x0004)
    ChrSetPos(0x0101, 35000, 500, 87760, 270)
    ChrSetPos(0x00F8, 37880, 0, 87320, 270)
    ChrSetPos(0x00F7, 37790, 0, 86040, 315)
    ChrSetPos(0x00F9, 39170, 0, 86460, 270)
    OP_0D()
    Sleep(400)

    ChrSetDirection(0x0101, 90, 400)
    ChrMoveTo(0x0101, 36350, 0, 87180, 2000, 0x00)
    Fade(1000)
    ChrSetChipByIndex(0x0101, 11)
    OP_0D()
    Sleep(1000)

    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS124._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170450829V　　美丽的公主及其随从啊　　\n',
            '　　汝等所寻之物尚在远处',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170450830V　　第二把钥匙在中央工房 　　\n',
            '　　调查『最聪明者』吧',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    Fade(1000)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010450831V#1002F#5P──看来以上就是接下来的提示了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_860',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450832V#051F#3P原来如此……\n',
            '就是说接下来是中央工房啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A1')

    def _loc_860(): pass

    label('loc_860')

    ChrTalk(
        0x0103,
        (
            '#0030450833V#020F#3P原来如此……\n',
            '就是说接下来是中央工房啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8A1(): pass

    label('loc_8A1')

    ChrTalk(
        0x0101,
        (
            '#0010450834V#1002F#5P嗯，场所倒是知道了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450835V这个『最聪明者』到底\n',
            '是谁呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450836V#1007F不会是\n',
            '拉赛尔博士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_985',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450837V#050F#3P总之那个东西在\n',
            '中央工房就是了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450838V去调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9E4')

    def _loc_985(): pass

    label('loc_985')

    ChrTalk(
        0x0103,
        (
            '#0030450839V#020F#3P总之那个东西在\n',
            '中央工房就是了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450840V那我们就快去参观参观吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9E4(): pass

    label('loc_9E4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A19',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450841V#031F嗯，那么出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A19(): pass

    label('loc_A19')

    ChrTalk(
        0x0101,
        (
            '#0010450842V#1006F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_64(0x03, 0x0001)

    @scena.Lambda('lambda_0A45')
    def lambda_0A45():
        ChrWalkTo(0x0000, 39170, 0, 86460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0A45)

    @scena.Lambda('lambda_0A60')
    def lambda_0A60():
        ChrWalkTo(0x0001, 39170, 0, 86460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0A60)

    @scena.Lambda('lambda_0A7B')
    def lambda_0A7B():
        ChrWalkTo(0x0002, 39170, 0, 86460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0A7B)

    @scena.Lambda('lambda_0A96')
    def lambda_0A96():
        ChrWalkTo(0x0003, 39170, 0, 86460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0A96)

    OP_69(0x00F9, 1000)
    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)
    OP_6A(0x00FF)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0xACC
@scena.Code('func_01_ACC')
def func_01_ACC():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 58240, 0, 48320, 270)
    ChrSetPos(0x00F7, 59110, 0, 47500, 270)
    ChrSetPos(0x00F8, 59440, 0, 48970, 270)
    ChrSetPos(0x00F9, 60100, 0, 48320, 270)
    CameraMove(56710, 0, 46620, 0)
    OP_67(0, 7560, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010450870V#1011F#5P３根高低不同的烟囱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450871V#1015F我说，你们不觉得『尖帽子三兄弟』\n',
            '就是指这里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0BCF')
    def lambda_0BCF():
        CameraMove(52980, 0, 43380, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0BCF)

    OP_67(0, 10800, -10000, 2000)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C6F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070450872V#060F#2P这里烟囱的高度\n',
            '呈逐渐变化之势。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070450873V#061F嘿嘿，感觉真的像\n',
            '兄弟一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD4')

    def _loc_C6F(): pass

    label('loc_C6F')

    ChrTalk(
        0x0105,
        (
            '#0060450874V#040F#2P３根的高度都有所不同呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450875V原来如此……\n',
            '兄弟有可能指的就是这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CD4(): pass

    label('loc_CD4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_D46',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450876V#050F#1P有３根烟囱的建筑物\n',
            '好像只此一家呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450877V有可能就是这儿。\n',
            '调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB4')

    def _loc_D46(): pass

    label('loc_D46')

    ChrTalk(
        0x0103,
        (
            '#0030450878V#020F#1P有３根烟囱的建筑物\n',
            '好像只此一家呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450879V我想有可能就是这儿。\n',
            '快调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DB4(): pass

    label('loc_DB4')

    OP_59()

    @scena.Lambda('lambda_0DBB')
    def lambda_0DBB():
        CameraMove(56710, 0, 46620, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0DBB)

    @scena.Lambda('lambda_0DD3')
    def lambda_0DD3():
        ChrWalkTo(0x0101, 56880, 0, 48320, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DD3)

    CameraMove(59550, 0, 47740, 2000)
    WaitForThreadExit(0x0101, 0x0001)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在烟囱的管子下\n',
            '发现贴着卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010450880V#1018F#5P好，找到了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    @scena.Lambda('lambda_0E6D')
    def lambda_0E6D():
        CameraMove(59080, 0, 48310, 2000)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_0E6D)

    @scena.Lambda('lambda_0E85')
    def lambda_0E85():
        OP_67(0, 7560, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_0E85)

    @scena.Lambda('lambda_0E9D')
    def lambda_0E9D():
        CameraSetDistance(2800, 2000)

        ExitThread()

    DispatchAsync(0x0013, 0x0003, lambda_0E9D)

    ChrSetDirection(0x0101, 90, 400)
    ChrWalkTo(0x0101, 58240, 0, 48320, 2000, 0x00)

    @scena.Lambda('lambda_0EC8')
    def lambda_0EC8():
        ChrTurnDirection(0x00F7, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0EC8)

    @scena.Lambda('lambda_0ED6')
    def lambda_0ED6():
        ChrTurnDirection(0x00F8, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0ED6)

    @scena.Lambda('lambda_0EE4')
    def lambda_0EE4():
        ChrTurnDirection(0x00F9, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0EE4)

    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0013, 0x0001)
    WaitForThreadExit(0x0013, 0x0002)
    WaitForThreadExit(0x0013, 0x0003)
    Fade(1000)
    ChrSetChipByIndex(0x0101, 11)
    OP_0D()
    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS124._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170450881V　　 　门已经被打开了　　\n',
            '　勇士们的灵魂眠于安静的地下',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170450882V　　 高声献唱给女神吧　　\n',
            '　　『Ｃ－２６Ｄ－Ｅ』！　　',
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
    Fade(1000)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010450883V#1007F#5P呼～看来\n',
            '接下来就是最后一步了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450884V#1015F不过，『安静的地下』和\n',
            '『献唱给女神』……',
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
        'loc_1104',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450885V#032F唔，『安静的地下』\n',
            '应该就是如字面意思的地方吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450886V问题是『女神』和后面的\n',
            '意义不明的文字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_118B')

    def _loc_1104(): pass

    label('loc_1104')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_118B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060450887V#042F『安静的地下』\n',
            '应该就是如字面意思的地方吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450888V问题是『女神』和后面的\n',
            '意义不明的文字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_118B(): pass

    label('loc_118B')

    ChrTalk(
        0x0101,
        (
            '#0010450889V#1006F#5P总之，我们还是先去\n',
            '『地下』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450890V蔡斯的地下的话，\n',
            '就只有那里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1224',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450891V#051F#1P嗯，快点去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_124C')

    def _loc_1224(): pass

    label('loc_1224')

    ChrTalk(
        0x0103,
        (
            '#0030450892V#020F#1P嗯，快点去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_124C(): pass

    label('loc_124C')

    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0x124F
@scena.Code('func_02_124F')
def func_02_124F():
    EventBegin(0x00)
    ChrSetPos(0x000F, 28770, 0, 61520, 71)
    ChrSetPos(0x0101, 27390, 0, 60100, 71)
    ChrSetPos(0x00F7, 26830, 0, 61050, 61)
    ChrSetPos(0x00F8, 27120, 0, 59000, 71)
    ChrSetPos(0x00F9, 26310, 0, 59830, 71)
    ChrClearFlags(0x000F, 0x0080)
    OP_4A(0x0009, 255)
    ChrSetFlags(0x0010, 0x0008)
    OP_72(0x0001, 0x0004)
    OP_71(0x0015, 0x0004)
    OP_64(0x02, 0x0001)
    CameraMove(29300, 10850, 62850, 0)
    OP_67(0, 5320, -10000, 0)
    CameraSetDistance(3700, 0)
    OP_6C(330000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_1305')
    def lambda_1305():
        CameraMove(29300, 1900, 63800, 6000)

        ExitThread()

    DispatchAsync(0x0013, 0x0000, lambda_1305)

    @scena.Lambda('lambda_131D')
    def lambda_131D():
        OP_67(0, 5320, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_131D)

    @scena.Lambda('lambda_1335')
    def lambda_1335():
        CameraSetDistance(2800, 6000)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_1335)

    @scena.Lambda('lambda_1345')
    def lambda_1345():
        OP_6C(296000, 6000)

        ExitThread()

    DispatchAsync(0x0013, 0x0003, lambda_1345)

    OP_0D()
    Sleep(2000)

    WaitForThreadExit(0x0013, 0x0003)
    Sleep(2000)

    @scena.Lambda('lambda_1365')
    def lambda_1365():
        CameraMove(26280, 0, 60230, 3000)

        ExitThread()

    DispatchAsync(0x0013, 0x0000, lambda_1365)

    @scena.Lambda('lambda_137D')
    def lambda_137D():
        OP_6C(283000, 3000)

        ExitThread()

    DispatchAsync(0x0013, 0x0003, lambda_137D)

    @scena.Lambda('lambda_138D')
    def lambda_138D():
        ChrSetDirection(0x00F7, 61, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_138D)

    ChrSetDirection(0x000F, 250, 400)
    WaitForThreadExit(0x0013, 0x0003)

    ChrTalk(
        0x000F,
        (
            '#0580450963V#791F顺利地取回了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450964V我就知道你们\n',
            '能做到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450965V#1006F能够不负你的期待真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450966V#1007F不过这次又被\n',
            '怪盗Ｂ给大大地耍了一把。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_14CD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450967V#053F#2P嗯，感觉又一次\n',
            '了解到他的厉害了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450968V#050F说不定……\n',
            '这才是他的目标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1536')

    def _loc_14CD(): pass

    label('loc_14CD')

    ChrTalk(
        0x0103,
        (
            '#0030450969V#026F#2P嗯，感觉又一次\n',
            '了解到他的厉害了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450970V#022F说不定……\n',
            '这才是他的目标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1536(): pass

    label('loc_1536')

    ChrSetDirection(0x0101, 307, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450971V#1002F通过让我们见识他的实力\n',
            '来威胁我们？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450972V#1015F不，我不认为他\n',
            '考虑得这么深。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0580450973V#792F不管怎么说\n',
            '敌人都不简单。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450974V#790F今后也要\n',
            '谨慎行动。',
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
        'loc_163A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450975V#030F#1P嗯，这样比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_166A')

    def _loc_163A(): pass

    label('loc_163A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_166A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070450976V#062F#1P嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_166A(): pass

    label('loc_166A')

    ChrSetDirection(0x0101, 71, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010450977V#1002F嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0580450978V#791F好，这样一来这件委托就完成了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450979V你们就继续去忙\n',
            '你们本来的任务吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1730',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450980V#050F#2P嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1756')

    def _loc_1730(): pass

    label('loc_1730')

    ChrTalk(
        0x0103,
        (
            '#0030450981V#020F#2P嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1756(): pass

    label('loc_1756')

    ChrTalk(
        0x000F,
        (
            '#0580450982V#790F那我就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1783')
    def lambda_1783():
        ChrTurnDirection(0x0000, 0x000F, 0)
        Yield()

        Jump('lambda_1783')

    DispatchAsync2(0x0000, 0x0001, lambda_1783)

    @scena.Lambda('lambda_1794')
    def lambda_1794():
        ChrTurnDirection(0x0001, 0x000F, 0)
        Yield()

        Jump('lambda_1794')

    DispatchAsync2(0x0001, 0x0001, lambda_1794)

    @scena.Lambda('lambda_17A5')
    def lambda_17A5():
        ChrTurnDirection(0x0002, 0x000F, 0)
        Yield()

        Jump('lambda_17A5')

    DispatchAsync2(0x0002, 0x0001, lambda_17A5)

    @scena.Lambda('lambda_17B6')
    def lambda_17B6():
        ChrTurnDirection(0x0003, 0x000F, 0)
        Yield()

        Jump('lambda_17B6')

    DispatchAsync2(0x0003, 0x0001, lambda_17B6)

    ChrWalkTo(0x000F, 26930, 0, 63270, 2000, 0x00)
    ChrSetDirection(0x000F, 0, 400)
    OP_70(0x000C, 29)
    OP_73(0x000C)
    ChrWalkTo(0x000F, 26930, 0, 64830, 2000, 0x00)
    OP_72(0x000C, 0x0800)
    OP_6F(0x000C, 29)
    OP_70(0x000C, 0)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x000C)
    OP_71(0x000C, 0x0800)
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)
    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【被盗的招牌板】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrSetFlags(0x000F, 0x0080)
    OP_4B(0x0009, 255)
    ChrSetPos(0x0010, 13900, 0, 58910, 227)
    ChrClearFlags(0x0010, 0x0008)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
