import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3303   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '巨大企鹅'),
    TXT(0x02, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3303.x'
    header.mapIndex       = 1
    header.bgm            = 32
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xBBD
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00002EE0,
            dword_04        = 0x00000000,
            dword_08        = 0x0001A1F8,
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
        ('ED6_DT09/CH10700._CH', 'ED6_DT09/CH10700P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
    ]

# id: 0x10002 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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
    )

# id: 0x10003 offset: 0x112
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x112
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x112
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 12720,
            triggerZ            = 160,
            triggerY            = 113900,
            triggerRange        = 1200,
            actorX              = 12720,
            actorZ              = 160,
            actorY              = 113900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x136
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_142'),
        (-1, 'loc_158'),
    )

    def _loc_142(): pass

    label('loc_142')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 4, 0x554)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 3, 0x553)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_155',
    )

    SetScenaFlags(ScenaFlag(0x00AA, 4, 0x554))
    Event(0, 0x0002)

    def _loc_155(): pass

    label('loc_155')

    Jump('loc_158')

    def _loc_158(): pass

    label('loc_158')

    Return()

# id: 0x0001 offset: 0x159
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 6, 0x556)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 2, 0x552)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_169',
    )

    OP_64(0x00, 0x0001)

    def _loc_169(): pass

    label('loc_169')

    PlaySE(461, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x16F
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    FadeIn(2000, 0)
    OP_28(0x0042, 0x01, 0x0040)
    CameraMove(12310, -50, 109720, 0)
    OP_67(0, 4019, -10000, 0)
    CameraSetDistance(7650, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_12(0x00000064, 0x0003D090, 0x00000000)
    SetChrPos(0x0101, 12570, 10, 89500, 0)
    SetChrPos(0x0102, 13320, -60, 88210, 0)
    SetChrPos(0x0107, 11270, 0, 87840, 0)
    SetChrPos(0x0108, 12570, -60, 87040, 0)

    @scena.Lambda('lambda_0214')
    def lambda_0214():
        OP_6C(8000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0214)

    Sleep(5000)

    OP_12(0x00000000, 0x00000000, 0x00000BB8)

    @scena.Lambda('lambda_0236')
    def lambda_0236():
        CameraMove(13110, 20, 92050, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0236)

    @scena.Lambda('lambda_024E')
    def lambda_024E():
        CameraSetDistance(3850, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_024E)

    Sleep(3000)

    ChrTalk(
        0x0101,
        (
            '#0010081526V#004F唔哇～……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081527V#560F好漂亮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080081528V#071F呵呵……\n',
            '真是不错的景观啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081529V#001F嗯嗯！\n',
            '想象不出我们就在洞窟里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081530V#010F这里应该就是洞窟湖了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081531V『塞姆里亚苔藓』\n',
            '也许就生长在这附近的石笋上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081532V#006FＯＫ！\n',
            '继续进行地毯式搜索！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x387
@scena.Code('func_03_387')
def func_03_387():
    SetScenaFlags(ScenaFlag(0x00AA, 5, 0x555))
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 12730, 160, 113310, 0)
    SetChrPos(0x0102, 11580, -30, 112670, 0)
    SetChrPos(0x0107, 13950, -30, 112810, 0)
    SetChrPos(0x0108, 12450, -50, 111850, 0)
    CameraMove(12600, 160, 114570, 1000)
    OP_0D()
    SetChrPos(0x0008, 8000, -3500, 119800, 0)

    ChrTalk(
        0x0107,
        (
            '#0070081533V#560F啊，这是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080081534V#073F看来这就是我们要找的\n',
            '『塞姆里亚苔藓』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081535V#008F哇～闪闪亮的……\n',
            '真没想到竟然是这么漂亮的苔藓呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081536V为什么会发光呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081537V#010F也许是因为苔藓里面\n',
            '含有大量的七耀石成分吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081538V马上采集好，\n',
            '然后赶快返回蔡斯吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '采集到了',
            (TxtCtl.SetColor, 0x2),
            '塞姆里亚苔藓',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x0365, 1)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010081539V#006F好，任务完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081540V#010F那么，我们马上回去，\n',
            '然后把这药料交给教区长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_64(0x00, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010081541V#001F嗯，就这样做吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0108,
        (
            '#0080081542V#072F……慢着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0008, 400)
    Fade(250)
    SetChrPos(0x0108, 12550, -50, 111760, 315)
    PlaySE(143, 0x00, 0x64)
    SetChrChipByIndex(0x0108, 7)
    OP_0D()

    @scena.Lambda('lambda_0662')
    def lambda_0662():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0662)

    @scena.Lambda('lambda_0670')
    def lambda_0670():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0670)

    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010081543V#004F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081544V#016F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 800)
    Fade(500)
    PlaySE(501, 0x00, 0x64)
    SetChrChipByIndex(0x0102, 3)
    OP_0D()
    Sleep(250)

    @scena.Lambda('lambda_06D5')
    def lambda_06D5():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_06D5)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0108,
        (
            '#0080081545V#076F小心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0702')
    def lambda_0702():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0702')

    DispatchAsync2(0x0107, 0x0001, lambda_0702)

    @scena.Lambda('lambda_0713')
    def lambda_0713():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0713')

    DispatchAsync2(0x0101, 0x0001, lambda_0713)

    @scena.Lambda('lambda_0724')
    def lambda_0724():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0724')

    DispatchAsync2(0x0102, 0x0001, lambda_0724)

    @scena.Lambda('lambda_0735')
    def lambda_0735():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0735')

    DispatchAsync2(0x0108, 0x0001, lambda_0735)

    @scena.Lambda('lambda_0746')
    def lambda_0746():
        CameraMove(8400, -50, 117630, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0746)

    @scena.Lambda('lambda_075E')
    def lambda_075E():
        CameraSetDistance(2480, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_075E)

    @scena.Lambda('lambda_076E')
    def lambda_076E():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_076E)

    Sleep(2000)

    PlaySE(227, 0x00, 0x64)
    Sleep(1000)

    SetChrDirection(0x0008, 160, 0)

    @scena.Lambda('lambda_0794')
    def lambda_0794():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0794')

    DispatchAsync2(0x0008, 0x0003, lambda_0794)

    SetChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x0008, 0x0080)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_07BC')
    def lambda_07BC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_07BC)

    @scena.Lambda('lambda_07CE')
    def lambda_07CE():
        OP_67(0, 5840, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_07CE)

    @scena.Lambda('lambda_07E6')
    def lambda_07E6():
        CameraMove(9140, 60, 113530, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_07E6)

    @scena.Lambda('lambda_07FE')
    def lambda_07FE():
        CameraSetDistance(3140, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_07FE)

    @scena.Lambda('lambda_080E')
    def lambda_080E():
        OP_6C(334000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_080E)

    LoadEffect(0x00, 'map\\\\mp012_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 8000, -1500, 119800, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(228, 0x00, 0x64)

    @scena.Lambda('lambda_086C')
    def lambda_086C():
        ChrJumpTo(0x00FE, 8610, 50, 113340, 8000, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_086C)

    Sleep(500)

    SetChrDirection(0x0008, 120, 0)
    WaitForThreadExit(0x0008, 0x0000)
    PlaySE(229, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)
    SetChrChipByIndex(0x0101, 1)
    SetChrChipByIndex(0x0107, 5)
    WaitForThreadExit(0x0101, 0x0002)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010081546V#509F这、这是什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081547V#065F哇哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080081548V#070F呼呼……\n',
            '看来它就是这洞窟湖的主人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081549V#012F这下……\n',
            '看来不得不战斗了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0107, 0xFF)
    Battle(0x00000398, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_9AC'),
        (-1, 'loc_9AF'),
    )

    def _loc_9AC(): pass

    label('loc_9AC')

    OP_B4(0x00)

    Return()

    def _loc_9AF(): pass

    label('loc_9AF')

    EventBegin(0x00)
    SetChrPos(0x0101, 7630, 40, 114200, 0)
    SetChrPos(0x0102, 8980, 30, 114440, 0)
    SetChrPos(0x0108, 8950, 50, 113270, 0)
    SetChrPos(0x0107, 7380, -40, 112770, 0)
    CameraMove(8280, 40, 113660, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0107, 65535)
    SetChrChipByIndex(0x0108, 65535)
    SetChrFlags(0x0008, 0x0080)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010081550V#007F吓、吓了一大跳～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081551V#067F虽、虽然挺可爱的，\n',
            '不过还是有点可怕呢～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081552V#017F呼……\n',
            '总算是把魔兽击退了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081553V#012F不过，再磨磨蹭蹭的话，\n',
            '恐怕我们又会遭到袭击的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080081554V#070F嗯，没错。\n',
            '尽快回城镇比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081555V只要把刚才采到的药料\n',
            '拿到城镇里的教会就行了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081556V#006F嗯，快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00AA, 6, 0x556))
    OP_28(0x0042, 0x01, 0x0080)
    OP_64(0x00, 0x0001)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
