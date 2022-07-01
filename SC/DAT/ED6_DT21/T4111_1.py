import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4111_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4111_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4111.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T4111_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5D6
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
    Fade(500)
    OP_6D(1120, 0, 63720, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 1620, 0, 63260, 0)
    SetChrPos(0x0105, 3140, 0, 62800, 315)
    SetChrPos(0x0104, 2160, 0, 61840, 0)
    SetChrPos(0x0108, 700, 0, 61860, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010460323V#1015F嗯～说到老将\n',
            '还是指摩尔根将军吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460324V也就是说，这个就是\n',
            '『时间的旁观者』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460325V#042F嗯嗯……\n',
            '我想这个可能性很高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040460326V#030F呼，看来有必要\n',
            '调查一下里面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们和家里的人商量\n',
            '让他们确认了钟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_6D(-4940, 0, 64160, 0)
    OP_67(0, 5460, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)
    SetChrPos(0x000D, -1600, 0, 64260, 90)
    SetChrPos(0x000E, -2180, 0, 63520, 90)
    SetChrPos(0x000F, -1600, 0, 64800, 90)
    SetChrPos(0x0101, 1660, 0, 62460, 0)
    SetChrPos(0x0105, -560, 0, 62280, 45)
    SetChrPos(0x0104, -240, 0, 61160, 45)
    SetChrPos(0x0108, -1620, 0, 61240, 45)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0321')
    def lambda_0321():
        OP_6D(-940, 0, 64160, 3000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0321)

    Sleep(1200)

    OP_8E(0x0101, 1660, 0, 63660, 1000, 0x00)
    WaitForThreadExit(0x000D, 0x0001)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x0101, 8)
    SetChrSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '调查钟里面，\n',
            '发现里盖上贴着卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    OP_AD(0x00240093, 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170460327V　　　第二把钥匙在市内。　　　\n',
            '寻找『留在地上的象征』。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0108,
        (
            '#0080460328V#074F唔，和猜想的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3270460329V啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3280460330V没想到家里\n',
            '竟然被放了这种东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x0101, 65535)
    OP_0D()
    OP_8C(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010460331V#1016F不过，应该不是\n',
            '针对这个家恶意所为\n',
            '我想不用担心的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460332V#1000F不过保险起见，晚上\n',
            '还是请锁好门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3270460333V是，是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3280460334V嗯嗯，会小心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040460335V#030F唔，那么\n',
            '去下一处看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C4, 0x01, 0x0004)
    OP_28(0x00C4, 0x01, 0x0008)
    OP_64(0x00, 0x0001)
    OP_4B(0x000D, 255)
    OP_4B(0x000E, 255)
    OP_4B(0x000F, 255)
    CreateThread(0x000F, 0x00, 0x06, 0x0002)
    SetChrPos(0x000F, -1460, 0, 64920, 180)
    OP_A2(0x0002)
    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
