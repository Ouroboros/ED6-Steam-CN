import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C4303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4303   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '凯文神父'),
    TXT(0x02, '尤莉亚上尉'),
    TXT(0x03, '幻想乐曲'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4303.x'
    header.mapIndex       = 216
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xE26
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
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP'),
        (None, 'ED6_DT27/CH03090P._CP'),
    ]

# id: 0x10002 offset: 0xBE
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
        ScenaNpcData(
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x11E
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x11E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x11E
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x11E
@scena.Code('PreInit')
def PreInit():
    Event(0, 0x0002)

    Return()

# id: 0x0001 offset: 0x123
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x124
@scena.Code('ReInit')
def ReInit():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    SetChrFlags(0x0101, 0x0008)
    SetChrFlags(0x010A, 0x0008)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, 800, 0, -15000, 0)
    SetChrPos(0x0009, -800, 0, -16000, 0)
    SetChrFlags(0x0008, 0x0040)
    OP_6D(2460, 0, -21910, 0)
    OP_67(0, 10420, -10000, 0)
    OP_6B(4190, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_A1(0x000A, 0x0009)
    SetChrPos(0x000A, 4030, 0, 6430, 63)
    OP_72(0x0009, 0x0020)
    OP_72(0x0009, 0x0004)
    OP_72(0x0009, 0x0002)
    OP_6F(0x0009, 843)
    OP_70(0x0009, 0x0000034B)
    OP_72(0x0006, 0x0020)
    OP_6F(0x0006, 240)
    OP_72(0x0005, 0x0020)
    OP_71(0x0005, 0x0004)
    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0000, 3260)
    OP_6F(0x0001, 3260)
    OP_6F(0x0002, 3260)
    OP_6F(0x0003, 3260)

    @scena.Lambda('lambda_0227')
    def lambda_0227():
        OP_6D(1480, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0227)

    @scena.Lambda('lambda_023F')
    def lambda_023F():
        OP_67(0, 10420, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_023F)

    @scena.Lambda('lambda_0257')
    def lambda_0257():
        OP_8E(0x0009, -800, 0, -10, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0257)

    @scena.Lambda('lambda_0272')
    def lambda_0272():
        OP_8E(0x0008, 800, 0, 90, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0272)

    FadeIn(2000, 0)
    WaitForThreadExit(0x0101, 0x0000)
    Fade(500)
    OP_6B(3200, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0008)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0180200019V#1063F#5P这可真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100200020V#6P#178F七耀教会对于如何\n',
            '处置这东西也会略感为难吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100200021V毕竟称得上是无畏级的\n',
            '古代遗物吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0180200022V#1067F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 265, 500)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0180200023V#1060F#5P……可以\n',
            '让我稍微检查一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 90, 500)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#0100200024V#6P#178F当然。\n',
            '陛下也给予了许可。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100200025V希望能借助\n',
            '你的智慧来帮助我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 0, 500)
    OP_8C(0x0008, 45, 500)

    @scena.Lambda('lambda_045F')
    def lambda_045F():
        OP_6D(3630, 0, 4360, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_045F)

    @scena.Lambda('lambda_0477')
    def lambda_0477():
        OP_67(0, 7000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0477)

    @scena.Lambda('lambda_048F')
    def lambda_048F():
        OP_8E(0x0008, 2510, 0, 3180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_048F)

    OP_8C(0x0009, 37, 500)
    WaitForThreadExit(0x0101, 0x0001)
    OP_8C(0x0008, 339, 1000)
    Sleep(1000)

    OP_8C(0x0008, 48, 1000)
    Sleep(1000)

    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0180200026V#1063F这就是报告书里的\n',
            '『环之守护者』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200027V和卡尔瓦德出土的\n',
            '巨像感觉相似……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200028V#1067F嗯～真想亲眼确认\n',
            '这东西活动的样子啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 0, 500)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0180200029V#1063F还有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05A2')
    def lambda_05A2():
        OP_8E(0x0008, -710, 0, 6860, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05A2)

    Sleep(1000)

    OP_8C(0x0009, 0, 500)

    @scena.Lambda('lambda_05C9')
    def lambda_05C9():
        OP_6D(390, 600, 19290, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_05C9)

    @scena.Lambda('lambda_05E1')
    def lambda_05E1():
        OP_67(0, 9500, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_05E1)

    @scena.Lambda('lambda_05F9')
    def lambda_05F9():
        OP_6B(4200, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_05F9)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_060E')
    def lambda_060E():
        OP_8E(0x0008, 240, 600, 17900, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_060E)

    Sleep(500)

    @scena.Lambda('lambda_062E')
    def lambda_062E():
        OP_8E(0x0009, -570, 0, 10830, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_062E)

    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0009, 0x0008, 500)
    WaitForThreadExit(0x0009, 0x0000)
    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0180200030V#1063F古代塞姆利亚文明末期……\n',
            '１２００年前的东西是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200031V虽然不清楚这个装置的机能，\n',
            '但好像是整个遗迹的中枢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0100200032V#5P#178F对古代遗物的分析……\n',
            '以现代的技术来说几乎是不可能的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100200033V虽然同样由导力驱动，\n',
            '但却是和导力器相异的机械体系……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100200034V拉赛尔博士是这么说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 500)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0180200035V#1060F#5P『女神为时过早的赠物』\n',
            '——教会是这样定义的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 225, 500)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0180200036V#1063F#5P那些东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_082F')
    def lambda_082F():
        OP_8E(0x0008, -6470, 0, 13730, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_082F)

    Sleep(1000)

    @scena.Lambda('lambda_084F')
    def lambda_084F():
        OP_6D(-6050, 0, 13970, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_084F)

    @scena.Lambda('lambda_0867')
    def lambda_0867():
        OP_67(0, 9500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0867)

    OP_8C(0x0009, 225, 500)
    Sleep(1000)

    @scena.Lambda('lambda_088B')
    def lambda_088B():
        OP_8E(0x0009, -5910, 0, 10330, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_088B)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0009, 0x0000)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0009, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0180200037V#5P#1063F当使用了一种叫作『福音』的\n',
            '漆黑的导力器之后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200038V这些巨大的柱子\n',
            '似乎就陷入地下了是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100200039V#4P#178F#2P是的，大厅里的\n',
            '四根柱子都陷进去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100200040V但是，过了将近两个月，\n',
            '还是没能找到当中的玄机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0180200041V#5P#1065F被封印的『辉之环』……\n',
            '还有被使用过的漆黑的『福音』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200042V装置所说的第二结界和\n',
            '设备塔的启动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200043V#1067F原来如此……\n',
            '我明白它们之间微妙的联系了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(800)

    ChrTurnDirection(0x0009, 0x0008, 500)

    ChrTalk(
        0x0009,
        (
            '#0100200044V#4P#173F微妙的联系……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100200045V那、那到底是怎么回事……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 500)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0180200046V#5P#1060F呀～是某种\n',
            '类似直觉的感觉啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200047V我想这地方\n',
            '会不会就是『门』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100200048V#4P#178F『门』……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0180200049V#5P#1060F嗯嗯，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200050V#1065F在通向女神至宝\n',
            '的『路』上堵塞着巨大的『门』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200051V想打开它的话，就需要\n',
            '被称为『福音』的漆黑钥匙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200052V#1063F这样想的话，这里没有\n',
            '关键的『辉之环』也可以理解了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100200053V#4P#178F但、但要说是『路』的话，\n',
            '这里已经是遗迹的最下层了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100200054V博士调查后也确定\n',
            '这里不存在其它的区域……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0180200055V#5P#1060F大概这条『路』不是\n',
            '用通常的方法可以看到的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('凯文神父')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0180200056V是地下流动的七耀脉……\n',
            '或是其它更不同的路径……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200057V或许在越过那里之后，\n',
            '应该就能找到有关『环』的线索了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_DB()
    Sleep(2000)

    Sleep(1000)

    OP_AD(0x002400A4, 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_20(0x00000BB8)
    OP_AE(0x000000C8)
    Sleep(2000)

    OP_21()
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    OP_DC()
    NewScene('ED6_DT21/T4105._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
